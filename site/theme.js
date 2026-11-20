// Run in the head so a stored preference applies before content is painted.
(function () {
  try {
    var saved = localStorage.getItem("uvy-theme");
    if (saved === "light" || saved === "dark")
      document.documentElement.dataset.theme = saved;
  } catch (_) {}
  document.addEventListener("DOMContentLoaded", function () {
    var picker = document.getElementById("theme");
    picker.value = document.documentElement.dataset.theme || "system";
    picker.parentElement.hidden = false;
    picker.addEventListener("change", function () {
      if (picker.value === "system")
        delete document.documentElement.dataset.theme;
      else document.documentElement.dataset.theme = picker.value;
      try {
        if (picker.value === "system") localStorage.removeItem("uvy-theme");
        else localStorage.setItem("uvy-theme", picker.value);
      } catch (_) {}
    });
  });
})();
