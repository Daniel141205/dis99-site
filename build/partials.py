# -*- coding: utf-8 -*-
"""Shared header/footer/document builders for the ДИС 99 site.
Uses relative asset prefixes so pages work at any depth and on any host."""

NAV = {
    "bg": [("services", "Услуги"), ("pricing", "Цени"), ("about", "За нас"),
           ("faq", "Въпроси"), ("contact", "Контакт")],
    "en": [("services", "Services"), ("pricing", "Pricing"), ("about", "About"),
           ("faq", "FAQ"), ("contact", "Contact")],
}
SUB = {"bg": "Счетоводна къща", "en": "Accounting Firm"}
CTA = {"bg": "Заяви консултация", "en": "Book a consultation"}
HOME_LABEL = {"bg": "Начало", "en": "Home"}
SKIP = {"bg": "Към съдържанието", "en": "Skip to content"}
FOOT_ABOUT = {
    "bg": "Счетоводно обслужване за малък и среден бизнес в Пловдив и дистанционно в цялата страна — от 2008 г.",
    "en": "Accounting services for small and medium businesses in Plovdiv and remotely across Bulgaria — since 2008.",
}
FOOT_SVC = {"bg": "Услуги", "en": "Services"}
FOOT_FIRM = {"bg": "Фирмата", "en": "Company"}
FOOT_CONTACT = {"bg": "Контакт", "en": "Contact"}
HOURS = {"bg": "Пн–Пт · 09:00–17:00", "en": "Mon–Fri · 09:00–17:00"}
ADDR = {"bg": "Пловдив, бул. Цариградско шосе 112", "en": "Plovdiv, 112 Tsarigradsko shose Blvd"}
RIGHTS = {"bg": "Всички права запазени.", "en": "All rights reserved."}
PRIVACY_L = {"bg": "Поверителност", "en": "Privacy"}
COOKIES_L = {"bg": "Бисквитки", "en": "Cookies"}
SVC_LINKS = {
    "bg": ["Текущо счетоводство", "ДДС и VIES", "ГФО", "ТРЗ и заплати", "Данъчна защита"],
    "en": ["Bookkeeping", "VAT & VIES", "Annual accounts", "Payroll", "Tax defense"],
}
FIRM_LINKS = {
    "bg": [("about", "За нас"), ("pricing", "Цени"), ("faq", "Въпроси"),
           ("contact", "Контакт"), ("privacy", "Поверителност")],
    "en": [("about", "About"), ("pricing", "Pricing"), ("faq", "FAQ"),
           ("contact", "Contact"), ("privacy", "Privacy")],
}

ICON_PHONE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92"/></svg>'
ICON_MAIL = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>'
ICON_PIN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0"/><circle cx="12" cy="10" r="3"/></svg>'
ICON_CLOCK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
SOCIAL = ('<div class="footer-social">'
  '<a href="#" aria-label="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3l.5-3H14V4.5c0-.8.3-1.5 1.5-1.5H18V.2C17.6.1 16.4 0 15.3 0 12.8 0 11 1.5 11 4.3V6H8v3h3v9h3z"/></svg></a>'
  '<a href="#" aria-label="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>'
  '<a href="#" aria-label="LinkedIn"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 1 0 3.5a2.5 2.5 0 0 1 4.98 0M.5 8h4V24h-4zM8 8h3.8v2.2h.05c.53-1 1.83-2.2 3.77-2.2 4.03 0 4.78 2.65 4.78 6.1V24h-4v-6.9c0-1.64-.03-3.75-2.28-3.75-2.29 0-2.64 1.79-2.64 3.63V24H8z"/></svg></a>'
  '</div>')


def paths(lang, key):
    """Return (asset_prefix, page_prefix, other_lang_href) for a page.
    asset_prefix: prefix to reach site root assets (css/js/img/fonts).
    page_prefix: prefix to reach sibling pages within same lang.
    """
    is_home = key == "index"
    if lang == "bg":
        if is_home:
            return "", "", "en/index.html"
        return "../", "", "../en/pages/%s.html" % key
    else:  # en
        if is_home:
            return "../", "/en", "../index.html"
        return "../../", "", "../../pages/%s.html" % key


def header(lang, active):
    ap, _, other = paths(lang, active)
    nav = NAV[lang]
    # Within a language dir: index lives at the root, pages live in /pages/.
    lp = "pages/" if active == "index" else ""           # link prefix to reach pages
    home = "index.html" if active == "index" else "../index.html"
    items = ""
    for k, label in nav:
        cur = ' aria-current="page"' if k == active else ""
        items += '<li><a href="%s%s.html"%s>%s</a></li>' % (lp, k, cur, label)
    # language switch: self in current lang, equivalent URL in the other lang
    self_link = "index.html" if active == "index" else "%s.html" % active
    if lang == "bg":
        bg_link, en_link = self_link, other
    else:
        en_link, bg_link = self_link, other
    cta_href = "pages/contact.html" if active == "index" else "contact.html"
    return ("""    <header class="site-header" id="header">
      <div class="container header-row">
        <a class="brand" href="{home}" aria-label="ДИС 99 — {homelabel}">
          <img class="brand-mark" src="{ap}img/logo-mark.svg" width="48" height="48" alt="" aria-hidden="true" />
          <span class="brand-text">
            <span class="brand-name">ДИС&nbsp;<span class="nines">99</span></span>
            <span class="brand-sub">{sub}</span>
          </span>
        </a>
        <button class="nav-toggle" aria-expanded="false" aria-controls="nav-collapse" aria-label="Menu"><span></span></button>
        <div class="nav-collapse" id="nav-collapse">
          <nav aria-label="{homelabel}">
            <ul class="nav-menu">{items}</ul>
          </nav>
          <div class="header-actions">
            <div class="lang-switch" aria-label="Language">
              <a href="{bg_link}"{bg_cur}>BG</a>
              <a href="{en_link}"{en_cur}>EN</a>
            </div>
            <a class="btn btn-primary" href="{cta_href}">{cta}</a>
          </div>
        </div>
      </div>
    </header>""").format(
        home=home, homelabel=HOME_LABEL[lang], ap=ap, sub=SUB[lang], items=items,
        bg_link=bg_link, en_link=en_link,
        bg_cur=' aria-current="true"' if lang == "bg" else "",
        en_cur=' aria-current="true"' if lang == "en" else "",
        cta_href=cta_href, cta=CTA[lang])


def footer(lang, active):
    ap, _, _ = paths(lang, active)
    lp = "pages/" if active == "index" else ""
    svc = "".join('<li><a href="%sservices.html">%s</a></li>' % (lp, s) for s in SVC_LINKS[lang])
    firm = "".join('<li><a href="%s%s.html">%s</a></li>' % (lp, k, l) for k, l in FIRM_LINKS[lang])
    home = "index.html" if active == "index" else "../index.html"
    return ("""    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a class="brand" href="{home}" aria-label="ДИС 99">
              <img class="brand-mark" src="{ap}img/logo-mark.svg" width="48" height="48" alt="" aria-hidden="true" />
              <span class="brand-text"><span class="brand-name">ДИС&nbsp;<span class="nines">99</span></span><span class="brand-sub">{sub}</span></span>
            </a>
            <p class="footer-about">{about}</p>
            {social}
          </div>
          <div class="footer-col">
            <h4>{svc_h}</h4>
            <ul>{svc}</ul>
          </div>
          <div class="footer-col">
            <h4>{firm_h}</h4>
            <ul>{firm}</ul>
          </div>
          <div class="footer-col">
            <h4>{contact_h}</h4>
            <ul class="footer-contact">
              <li>{ic_phone}<a href="tel:+359885738666">0885 738 666</a></li>
              <li>{ic_mail}<a href="mailto:dis99@abv.bg">dis99@abv.bg</a></li>
              <li>{ic_pin}<span>{addr}</span></li>
              <li>{ic_clock}<span>{hours}</span></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <span>© <span id="year">2026</span> Счетоводна къща ДИС 99. {rights}</span>
          <span><a href="{lp}privacy.html">{priv}</a> · <a href="{lp}cookies.html">{cook}</a></span>
        </div>
      </div>
    </footer>""").format(
        home=home, ap=ap, sub=SUB[lang], about=FOOT_ABOUT[lang], social=SOCIAL,
        svc_h=FOOT_SVC[lang], svc=svc, firm_h=FOOT_FIRM[lang], firm=firm,
        contact_h=FOOT_CONTACT[lang], ic_phone=ICON_PHONE, ic_mail=ICON_MAIL,
        ic_pin=ICON_PIN, ic_clock=ICON_CLOCK, addr=ADDR[lang], hours=HOURS[lang],
        rights=RIGHTS[lang], priv=PRIVACY_L[lang], cook=COOKIES_L[lang], lp=lp)


def document(lang, key, title, desc, main, head_extra=""):
    ap, _, other = paths(lang, key)
    if lang == "bg":
        canon = "https://dis99.bg/" + ("" if key == "index" else "pages/%s.html" % key)
        alt_bg = canon
        alt_en = "https://dis99.bg/en/" + ("" if key == "index" else "pages/%s.html" % key)
    else:
        canon = "https://dis99.bg/en/" + ("" if key == "index" else "pages/%s.html" % key)
        alt_en = canon
        alt_bg = "https://dis99.bg/" + ("" if key == "index" else "pages/%s.html" % key)
    locale = "bg_BG" if lang == "bg" else "en_US"
    return ("""<!doctype html>
<html lang="{lang}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <meta name="theme-color" content="#0f1d31" />
    <link rel="icon" href="{ap}img/logo-mark.svg" type="image/svg+xml" />
    <link rel="canonical" href="{canon}" />
    <link rel="alternate" hreflang="bg" href="{alt_bg}" />
    <link rel="alternate" hreflang="en" href="{alt_en}" />
    <link rel="alternate" hreflang="x-default" href="{alt_bg}" />
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="{locale}" />
    <meta property="og:site_name" content="ДИС 99" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:url" content="{canon}" />
    <meta property="og:image" content="https://dis99.bg/img/og-cover.jpg" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preload" href="{ap}fonts/Inter-600-cyrillic.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="preload" href="{ap}fonts/PlayfairDisplay-700-cyrillic.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="stylesheet" href="{ap}css/style.css" />
{head_extra}  </head>
  <body>
    <a class="skip-link" href="#main">{skip}</a>
{header}

    <main id="main">
{main}
    </main>

{footer}

    <script src="{ap}js/main.js" defer></script>
  </body>
</html>
""").format(
        lang=lang, title=title, desc=desc, ap=ap, canon=canon, alt_bg=alt_bg,
        alt_en=alt_en, locale=locale, head_extra=head_extra, skip=SKIP[lang],
        header=header(lang, key), main=main, footer=footer(lang, key))
