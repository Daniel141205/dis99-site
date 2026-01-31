
(function () {
    // Footer year
    const year = document.getElementById("year");
    if (year) year.textContent = new Date().getFullYear();

    // Mobile menu
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
            const isOpen = menu.classList.contains("open");
            isOpen ? closeMenu() : openMenu();
        });

        document.addEventListener("click", (e) => {
            if (!menu.contains(e.target) && !toggle.contains(e.target)) closeMenu();
        });

        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") closeMenu();
        });

        menu.addEventListener("click", (e) => {
            const a = e.target.closest("a");
            if (a) closeMenu();
        });
    }

    const targets = document.querySelectorAll(".reveal, .stagger");
    if (targets.length) {
        const io = new IntersectionObserver(
            (entries) => {
                for (const entry of entries) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("show");
                        io.unobserve(entry.target);
                    }
                }
            },
            { threshold: 0.12, rootMargin: "0px 0px -10% 0px" }
        );

        targets.forEach((t) => io.observe(t));
    }

    const counters = document.querySelectorAll(".counter");
    if (counters.length) {
        const animate = (el) => {
            const target = Number(el.dataset.target || "0");
            const start = performance.now();
            const dur = 3000;

            const tick = (now) => {
                const t = Math.min(1, (now - start) / dur);
                const eased = 1 - Math.pow(1 - t, 3); // easeOutCubic
                el.textContent = Math.round(eased * target).toString();
                if (t < 1) requestAnimationFrame(tick);
                else el.textContent = target.toString();
            };

            requestAnimationFrame(tick);
        };

        const io = new IntersectionObserver(
            (entries) => {
                for (const entry of entries) {
                    if (entry.isIntersecting) {
                        if (entry.target.dataset.done === "1") return;
                        entry.target.dataset.done = "1";
                        animate(entry.target);
                        io.unobserve(entry.target);
                    }
                }
            },
            { threshold: 0.35 }
        );

        counters.forEach((c) => io.observe(c));
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
