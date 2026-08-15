// Caitlin D'Aprano | San Francisco Real Estate — shared scripts

document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");

  // Add shadow/background once the user scrolls down
  function onScroll() {
    if (window.scrollY > 40) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  }
  window.addEventListener("scroll", onScroll);
  onScroll();

  // Mobile nav toggle
  if (toggle && navLinks) {
    toggle.addEventListener("click", function () {
      navLinks.classList.toggle("open");
    });
  }

  // Simple contact form handler (front-end only demo)
  const form = document.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const confirmation = document.querySelector("#form-confirmation");
      form.reset();
      if (confirmation) {
        confirmation.hidden = false;
        confirmation.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });
  }

  // Year in footer
  document.querySelectorAll(".current-year").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
});
