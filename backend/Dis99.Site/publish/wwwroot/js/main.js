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

        // Close when clicking outside
        document.addEventListener("click", (e) => {
            if (!menu.contains(e.target) && !toggle.contains(e.target)) closeMenu();
        });

        // Close with ESC
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") closeMenu();
        });

        // Close after clicking a menu link (mobile UX)
        menu.addEventListener("click", (e) => {
            const a = e.target.closest("a");
            if (a) closeMenu();
        });
    }

    // Scroll reveal + stagger (ONE observer)
    const targets = document.querySelectorAll(".reveal, .stagger");
    if (targets.length) {
        const io = new IntersectionObserver(
            (entries) => {
                for (const entry of entries) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("show");
                        io.unobserve(entry.target); // animate once
                    }
                }
            },
            { threshold: 0.12, rootMargin: "0px 0px -10% 0px" }
        );

        targets.forEach((t) => io.observe(t));
    }

    // Count-up animation
    const nums = document.querySelectorAll("[data-count]");
    if (nums.length) {
        const animate = (el) => {
            const to = Number(el.dataset.count);
            const start = performance.now();
            const dur = 900;

            const tick = (now) => {
                const t = Math.min(1, (now - start) / dur);
                const eased = 1 - Math.pow(1 - t, 3); // easeOutCubic
                el.textContent = Math.round(eased * to).toString();
                if (t < 1) requestAnimationFrame(tick);
            };

            requestAnimationFrame(tick);
        };

        const numIO = new IntersectionObserver(
            (entries) => {
                for (const entry of entries) {
                    if (entry.isIntersecting) {
                        animate(entry.target);
                        numIO.unobserve(entry.target);
                    }
                }
            },
            { threshold: 0.4 }
        );

        nums.forEach((n) => numIO.observe(n));
    }
})();
