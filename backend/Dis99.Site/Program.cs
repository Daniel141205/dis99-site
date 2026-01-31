using MailKit.Net.Smtp;
using MailKit.Security;
using Microsoft.AspNetCore.Http.HttpResults;
using MimeKit;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

static string? Env(string key) => Environment.GetEnvironmentVariable(key);

static SecureSocketOptions GetSocketOptions(string? v)
{
    // Default safe for ABV: 465 implicit TLS
    if (string.IsNullOrWhiteSpace(v)) return SecureSocketOptions.SslOnConnect;

    return v.Trim().ToLowerInvariant() switch
    {
        "sslonconnect" or "ssl" or "true" => SecureSocketOptions.SslOnConnect,
        "starttls" => SecureSocketOptions.StartTls,
        "starttlswhenavailable" => SecureSocketOptions.StartTlsWhenAvailable,
        "none" or "false" => SecureSocketOptions.None,
        _ => SecureSocketOptions.SslOnConnect
    };
}

app.MapGet("/api/debug/env", () =>
{
    var host = Env("SMTP_HOST");
    var port = Env("SMTP_PORT");
    var user = Env("SMTP_USER");
    var pass = Env("SMTP_PASS");

    return Results.Json(new
    {
        host,
        port,
        user,
        passPresent = !string.IsNullOrWhiteSpace(pass),
        passLength = pass?.Length ?? 0,
        ssl = Env("SMTP_SSL"),
        mailTo = Env("MAIL_TO"),
        mailFrom = Env("MAIL_FROM")
    });
});

app.MapPost("/api/contact", async (HttpRequest request, ILogger<Program> log) =>
{
    try
    {
        if (!request.HasFormContentType)
        {
            return Results.BadRequest(new
            {
                ok = false,
                error = "Incorrect Content-Type. Use application/x-www-form-urlencoded or multipart/form-data."
            });
        }

        var form = await request.ReadFormAsync();

        // Honeypot
        var website = form["website"].ToString();
        if (!string.IsNullOrWhiteSpace(website))
            return Results.Ok(new { ok = true });

        var name = form["name"].ToString().Trim();
        var email = form["email"].ToString().Trim();
        var topic = form["topic"].ToString().Trim();
        var message = form["message"].ToString().Trim();
        var company = form["company"].ToString().Trim();
        var phone = form["phone"].ToString().Trim();
        var consent = form.ContainsKey("consent");

        if (string.IsNullOrWhiteSpace(name) ||
            string.IsNullOrWhiteSpace(email) ||
            string.IsNullOrWhiteSpace(topic) ||
            string.IsNullOrWhiteSpace(message) ||
            !consent)
        {
            return Results.BadRequest(new
            {
                ok = false,
                error = "Моля попълнете задължителните полета и съгласие."
            });
        }

        // Read SMTP config from env
        var smtpHost = Env("SMTP_HOST") ?? "";
        var smtpPortStr = Env("SMTP_PORT") ?? "465";
        var smtpUser = Env("SMTP_USER") ?? "";
        var smtpPass = Env("SMTP_PASS") ?? "";
        var smtpSsl = Env("SMTP_SSL");

        var mailTo = Env("MAIL_TO") ?? smtpUser;
        var mailFrom = Env("MAIL_FROM") ?? smtpUser;

        if (string.IsNullOrWhiteSpace(smtpHost) ||
            string.IsNullOrWhiteSpace(smtpUser) ||
            string.IsNullOrWhiteSpace(smtpPass) ||
            string.IsNullOrWhiteSpace(mailTo) ||
            string.IsNullOrWhiteSpace(mailFrom))
        {
            log.LogError("SMTP env missing. host/user/pass/to/from must be set.");
            return Results.Json(new { ok = false, error = "Сървърна конфигурационна грешка." }, statusCode: 500);
        }

        if (!int.TryParse(smtpPortStr, out var smtpPort))
            smtpPort = 465;

        var socketOptions = GetSocketOptions(smtpSsl);

        // Build email
        var subject = $"DIS 99 – Контакт форма: {topic}";
        var body =
$@"Ново запитване от сайта:

Име: {name}
Email: {email}
Фирма: {(string.IsNullOrWhiteSpace(company) ? "-" : company)}
Телефон: {(string.IsNullOrWhiteSpace(phone) ? "-" : phone)}
Тема: {topic}

Съобщение:
{message}
";

        var msg = new MimeMessage();

        // ✅ Реалният подател (вашия акаунт)
        msg.From.Add(new MailboxAddress("DIS 99 (форма)", mailFrom));

        // ✅ До вас (Inbox)
        msg.To.Add(MailboxAddress.Parse(mailTo));

        // ✅ Reply-To = клиентът (ТОВА е важното)
        msg.ReplyTo.Add(new MailboxAddress(name, email));

        msg.Subject = subject;
        msg.Body = new TextPart("plain") { Text = body };

        // Send
        using var client = new SmtpClient();

        // Optional: avoid OAuth2 auto mechanism noise
        client.AuthenticationMechanisms.Remove("XOAUTH2");

        await client.ConnectAsync(smtpHost, smtpPort, socketOptions);
        await client.AuthenticateAsync(smtpUser, smtpPass);
        await client.SendAsync(msg);
        await client.DisconnectAsync(true);

        log.LogInformation("Contact email sent. From={From} To={To} Topic={Topic}", email, mailTo, topic);

        return Results.Ok(new { ok = true });
    }
    catch (Exception ex)
    {
        log.LogError(ex, "Failed to send contact email.");
        return Results.Json(new { ok = false, error = "Грешка при изпращане. Моля опитайте отново." }, statusCode: 500);
    }
});

app.Run();
