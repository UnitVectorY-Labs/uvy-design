// Apply the saved preference before content is painted. CSS handles the OS default.
(function () {
  const root = document.documentElement;
  root.classList.add("js");
  try {
    const saved =
      root.dataset.exampleTheme || localStorage.getItem("uvy-theme");
    if (saved === "light" || saved === "dark") root.dataset.theme = saved;
  } catch (_) {}
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-enable-with-js]").forEach((control) => {
      control.disabled = false;
    });
    document.querySelectorAll("[data-requires-js]").forEach((control) => {
      control.hidden = false;
    });
    const system = matchMedia("(prefers-color-scheme: dark)");
    const theme = document.getElementById("theme");
    const reset = document.getElementById("theme-reset");
    function updateTheme() {
      const dark = root.dataset.theme
        ? root.dataset.theme === "dark"
        : system.matches;
      theme.setAttribute(
        "aria-label",
        dark ? "Switch to light theme" : "Switch to dark theme",
      );
      theme.title = theme.getAttribute("aria-label");
      theme.querySelector("[data-icon=moon]").toggleAttribute("hidden", dark);
      theme.querySelector("[data-icon=sun]").toggleAttribute("hidden", !dark);
      reset.hidden = !root.dataset.theme;
    }
    function chooseTheme(value) {
      if (value) root.dataset.theme = value;
      else delete root.dataset.theme;
      try {
        if (value) localStorage.setItem("uvy-theme", value);
        else localStorage.removeItem("uvy-theme");
      } catch (_) {}
      updateTheme();
    }
    theme.hidden = false;
    updateTheme();
    theme.addEventListener("click", function () {
      const dark = root.dataset.theme
        ? root.dataset.theme === "dark"
        : system.matches;
      chooseTheme(dark ? "light" : "dark");
    });
    reset.addEventListener("click", function () {
      chooseTheme(null);
      if (sidebar && sidebar.hasAttribute("data-open")) setOpen(false, false);
      theme.focus();
    });
    system.addEventListener("change", updateTheme);
    window.addEventListener("storage", function (event) {
      if (event.key === "uvy-theme") {
        if (event.newValue === "light" || event.newValue === "dark")
          root.dataset.theme = event.newValue;
        else delete root.dataset.theme;
        updateTheme();
      }
    });

    const sidebar = document.getElementById("sidebar");
    if (!sidebar) return;
    const menu = document.getElementById("menu");
    const close = document.getElementById("menu-close");
    const backdrop = document.getElementById("menu-backdrop");
    const mobile = matchMedia("(max-width: 48rem)");
    const background = [
      document.querySelector(".site-header"),
      document.querySelector(".workspace"),
      document.querySelector("footer"),
    ];
    function setOpen(open, restoreFocus) {
      open = open && mobile.matches;
      sidebar.toggleAttribute("data-open", open);
      sidebar.inert = mobile.matches && !open;
      backdrop.hidden = !open;
      menu.setAttribute("aria-expanded", String(open));
      document.body.classList.toggle("drawer-open", open);
      background.forEach((element) => {
        if (element) element.inert = open;
      });
      if (open) {
        sidebar.setAttribute("role", "dialog");
        sidebar.setAttribute("aria-modal", "true");
        close.focus();
      } else {
        sidebar.removeAttribute("role");
        sidebar.removeAttribute("aria-modal");
        if (restoreFocus) menu.focus();
      }
    }
    menu.hidden = false;
    close.hidden = false;
    menu.addEventListener("click", () => setOpen(true, false));
    close.addEventListener("click", () => setOpen(false, true));
    backdrop.addEventListener("click", () => setOpen(false, true));
    function selectLocalSection() {
      const links = [...sidebar.querySelectorAll('nav a[href^="#"]')];
      if (!links.length) return;
      const current =
        links.find((link) => link.getAttribute("href") === location.hash) ||
        links[0];
      links.forEach((link) => {
        if (link === current) link.setAttribute("aria-current", "location");
        else link.removeAttribute("aria-current");
      });
    }
    selectLocalSection();
    window.addEventListener("hashchange", selectLocalSection);
    sidebar.addEventListener("click", (event) => {
      if (event.target.closest("a") && mobile.matches) setOpen(false, true);
    });
    sidebar.addEventListener("keydown", (event) => {
      if (!sidebar.hasAttribute("data-open")) return;
      if (event.key === "Escape") {
        event.preventDefault();
        setOpen(false, true);
      }
      if (event.key === "Tab") {
        const targets = [
          ...sidebar.querySelectorAll(
            'a[href],button,input,select,[tabindex="0"]',
          ),
        ].filter(
          (element) =>
            !element.hidden &&
            element.getClientRects().length &&
            !element.disabled,
        );
        const first = targets[0],
          last = targets[targets.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      }
    });
    mobile.addEventListener("change", () => {
      const active = document.activeElement;
      const inside = sidebar.contains(active);
      setOpen(false, false);
      if (mobile.matches && inside) menu.focus();
      else if (!mobile.matches && (active === menu || active === close))
        theme.focus();
    });
    setOpen(false, false);
    const search = document.getElementById("nav-search");
    if (search) {
      search.closest(".nav-filters").hidden = false;
      search.addEventListener("input", function () {
        let count = 0;
        sidebar.querySelectorAll("nav a").forEach((link) => {
          link.hidden = !link.textContent
            .toLowerCase()
            .includes(search.value.trim().toLowerCase());
          if (!link.hidden) count++;
        });
        document.getElementById("nav-empty").hidden = count > 0;
      });
    }
  });
})();
