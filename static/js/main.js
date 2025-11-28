// static/js/main.js

document.addEventListener("DOMContentLoaded", () => {
  const nav = document.getElementById("main-nav");
  const navToggle = document.getElementById("nav-toggle");
  const themeToggle = document.getElementById("theme-toggle");
  const heroPhoto = document.getElementById("hero-photo");
  const preloader = document.getElementById("preloader");
  const body = document.body;

  // --- PRELOADER CONTROL ---
  window.addEventListener("load", () => {
    // allow the signature animation to play a bit
    const MIN_DURATION = 2300; // ms
    setTimeout(() => {
      if (preloader) {
        preloader.classList.add("preloader-hide");
      }
      body.classList.remove("preloading");
      body.classList.add("ready");
    }, MIN_DURATION);
  });

  // --- Mobile nav toggle ---
  if (navToggle && nav) {
    navToggle.addEventListener("click", () => {
      nav.classList.toggle("open");
    });
  }

  // --- Smooth scroll for internal links ---
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (!href || href === "#") return;

      const targetId = href.slice(1);
      const target = document.getElementById(targetId);
      if (target) {
        e.preventDefault();
        const yOffset = -80;
        const y =
          target.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({ top: y, behavior: "smooth" });

        if (nav && nav.classList.contains("open")) {
          nav.classList.remove("open");
        }
      }
    });
  });

  // --- Active nav link on scroll ---
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll("#main-nav a");

  const setActiveNavLink = () => {
    let currentId = "";
    const scrollY = window.pageYOffset + 120;

    sections.forEach((section) => {
      const offsetTop = section.offsetTop;
      const offsetHeight = section.offsetHeight;
      if (scrollY >= offsetTop && scrollY < offsetTop + offsetHeight) {
        currentId = section.id;
      }
    });

    navLinks.forEach((link) => {
      link.classList.toggle(
        "active",
        link.getAttribute("href") === `#${currentId}`
      );
    });
  };

  window.addEventListener("scroll", setActiveNavLink);
  setActiveNavLink();

  // --- Theme toggle with localStorage ---
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "light") {
    body.classList.remove("theme-dark");
    body.classList.add("theme-light");
  } else {
    body.classList.add("theme-dark");
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const isDark = body.classList.contains("theme-dark");
      if (isDark) {
        body.classList.remove("theme-dark");
        body.classList.add("theme-light");
        localStorage.setItem("theme", "light");
      } else {
        body.classList.remove("theme-light");
        body.classList.add("theme-dark");
        localStorage.setItem("theme", "dark");
      }
    });
  }

  // --- Hero photo fade/parallax on scroll (if you already had this, keep it) ---
  if (heroPhoto) {
    const updateHeroPhoto = () => {
      const threshold = 260;
      if (window.scrollY > threshold) {
        body.classList.add("hero-photo-hidden");
      } else {
        body.classList.remove("hero-photo-hidden");
      }
    };

    window.addEventListener("scroll", updateHeroPhoto);
    updateHeroPhoto();
  }

  // --- Reveal-on-scroll animations ---
  const revealEls = document.querySelectorAll(".reveal-on-scroll");
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.16,
    }
  );

  revealEls.forEach((el) => observer.observe(el));
});
