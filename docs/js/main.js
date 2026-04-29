(function () {
    const year = document.getElementById("year");
    if (year) year.textContent = new Date().getFullYear();

    const toggle = document.querySelector(".nav-toggle");
    const menu = document.querySelector(".nav-menu");

    function closeMenu() {
        if (!menu) return;
        menu.classList.remove("open");
        toggle?.setAttribute("aria-expanded", "false");
    }

    function openMenu() {
        if (!menu) return;
        menu.classList.add("open");
        toggle?.setAttribute("aria-expanded", "true");
    }

    if (toggle && menu) {
        toggle.addEventListener("click", () => {
            menu.classList.contains("open") ? closeMenu() : openMenu();
        });

        document.addEventListener("click", (e) => {
            if (!menu.contains(e.target) && !toggle.contains(e.target)) closeMenu();
        });

        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") closeMenu();
        });

        menu.addEventListener("click", (e) => {
            if (e.target.closest("a")) closeMenu();
        });
    }

    const revealTargets = document.querySelectorAll(".reveal, .stagger");

    if ("IntersectionObserver" in window && revealTargets.length) {
        const revealObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("show");
                        revealObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12, rootMargin: "0px 0px -10% 0px" }
        );

        revealTargets.forEach((target) => revealObserver.observe(target));
    } else {
        revealTargets.forEach((target) => target.classList.add("show"));
    }

    const counters = document.querySelectorAll(".counter");

    function animateCounter(el) {
        const target = Number(el.dataset.target || "0");
        const start = performance.now();
        const duration = 3000;

        function tick(now) {
            const progress = Math.min(1, (now - start) / duration);
            const eased = 1 - Math.pow(1 - progress, 3);

            el.textContent = Math.round(eased * target).toString();

            if (progress < 1) {
                requestAnimationFrame(tick);
            } else {
                el.textContent = target.toString();
            }
        }

        requestAnimationFrame(tick);
    }

    if ("IntersectionObserver" in window && counters.length) {
        const counterObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting && entry.target.dataset.done !== "1") {
                        entry.target.dataset.done = "1";
                        animateCounter(entry.target);
                        counterObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.35 }
        );

        counters.forEach((counter) => counterObserver.observe(counter));
    } else {
        counters.forEach((counter) => {
            counter.textContent = counter.dataset.target || "0";
        });
    }

    const contactForm = document.getElementById("contactForm");

    if (contactForm) {
        contactForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const status = document.getElementById("formStatus");
            const btn = document.getElementById("sendBtn");

            const setStatus = (type, text) => {
                if (!status) return;
                status.classList.remove("ok", "err", "show");
                status.textContent = text;
                status.classList.add("show", type === "ok" ? "ok" : "err");
            };

            const oldText = btn ? btn.textContent : "";

            if (btn) {
                btn.disabled = true;
                btn.textContent = "Изпращане…";
            }

            setStatus("ok", "Изпращане…");

            const topic = contactForm.querySelector("#topic")?.value || "";
            const map = {
                accounting: "Текущо счетоводство",
                vat: "ДДС / VIES",
                payroll: "ТРЗ / служители",
                annual: "Годишно приключване (ГФО)",
                consulting: "Консултация / казус",
                other: "Друго",
            };

            const topicBg = map[topic] || "Запитване";

            try {
                const fd = new FormData(contactForm);

                fd.set("_subject", `Запитване: ${topicBg} | Счетоводна къща „ДИС 99“`);

                const senderEmail = contactForm.querySelector("#email")?.value || "";
                if (senderEmail) fd.set("_replyto", senderEmail);

                const res = await fetch("https://formsubmit.co/ajax/hristt72@abv.bg", {
                    method: "POST",
                    headers: { Accept: "application/json" },
                    body: fd,
                });

                if (res.ok) {
                    contactForm.reset();
                    setStatus("ok", "✅ Запитването е изпратено успешно!");
                    setTimeout(() => location.reload(), 1800);
                } else {
                    setStatus("err", "❌ Неуспешно изпращане. Опитайте отново.");
                }
            } catch {
                setStatus("err", "❌ Грешка при връзка. Опитайте отново.");
            } finally {
                if (btn) {
                    btn.disabled = false;
                    btn.textContent = oldText || "Изпрати";
                }
            }
        });
    }
})();