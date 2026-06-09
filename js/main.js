(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Footer year */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* Sticky header shadow on scroll */
  const header = document.getElementById("header");
  if (header) {
    const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobile menu */
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.getElementById("nav-collapse");
  if (toggle && menu) {
    const setOpen = (open) => {
      menu.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    };
    toggle.addEventListener("click", () =>
      setOpen(!menu.classList.contains("open"))
    );
    document.addEventListener("click", (e) => {
      if (!menu.contains(e.target) && !toggle.contains(e.target)) setOpen(false);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setOpen(false);
    });
    menu.addEventListener("click", (e) => {
      if (e.target.closest("a")) setOpen(false);
    });
    window.addEventListener("resize", () => {
      if (window.innerWidth > 960) setOpen(false);
    });
  }

  /* Scroll reveal (single observer for .reveal and [data-stagger]) */
  const revealTargets = document.querySelectorAll(".reveal, [data-stagger]");
  if (revealTargets.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealTargets.forEach((t) => t.classList.add("in"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (entry.isIntersecting) {
              entry.target.classList.add("in");
              io.unobserve(entry.target);
            }
          }
        },
        { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
      );
      revealTargets.forEach((t) => io.observe(t));
    }
  }

  /* Contact form */
  const form = document.getElementById("contact-form");
  if (form) {
    const status = document.getElementById("form-status");
    const submitBtn = form.querySelector('[type="submit"]');
    const showStatus = (ok, msg) => {
      if (!status) return;
      status.textContent = msg;
      status.className = "form-status show " + (ok ? "ok" : "err");
    };
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      const original = submitBtn ? submitBtn.textContent : "";
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Изпращане…";
      }
      try {
        const res = await fetch(form.action || "/api/contact", {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" },
        });
        let data = {};
        try { data = await res.json(); } catch (_) {}
        if (res.ok && data.ok !== false) {
          form.reset();
          showStatus(true, "Благодарим! Получихме запитването ви и ще се свържем с вас възможно най-скоро.");
        } else {
          showStatus(false, (data && data.error) || "Възникна грешка при изпращането. Моля, опитайте отново или ни се обадете.");
        }
      } catch (_) {
        showStatus(false, "Няма връзка със сървъра. Моля, пишете ни на dis99@abv.bg или се обадете на 0885 738 666.");
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = original;
        }
      }
    });
  }

  /* Count-up numbers */
  const counters = document.querySelectorAll("[data-count]");
  if (counters.length) {
    const run = (el) => {
      const to = Number(el.dataset.count);
      const suffix = el.dataset.suffix || "";
      if (reduceMotion) {
        el.textContent = to + suffix;
        return;
      }
      const dur = 2600;
      const start = performance.now();
      const tick = (now) => {
        const p = Math.min(1, (now - start) / dur);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(eased * to) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };

    if (!("IntersectionObserver" in window)) {
      counters.forEach(run);
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (entry.isIntersecting) {
              run(entry.target);
              io.unobserve(entry.target);
            }
          }
        },
        { threshold: 0.6 }
      );
      counters.forEach((c) => io.observe(c));
    }
  }
})();
