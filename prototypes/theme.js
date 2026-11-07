// First visit follows the OS. The top-right button stores an explicit host-only override.
(() => {
  const density = new URLSearchParams(location.search).get('density');
  if (['compact', 'spacious'].includes(density)) document.documentElement.dataset.density = density;
  let saved;
  try {
    saved = document.cookie.split('; ').find(value => value.startsWith('uvy-theme='))?.slice(10);
  } catch {}
  let explicit = saved === 'light' || saved === 'dark' ? saved : null;
  const system = matchMedia('(prefers-color-scheme: dark)');
  const apply = () => {
    const dark = explicit ? explicit === 'dark' : system.matches;
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
    const toggle = document.querySelector('#theme-toggle');
    if (toggle) {
      toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
      toggle.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    }
  };
  apply();
  system.addEventListener('change', () => { if (!explicit) apply(); });
  document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('#theme-toggle');
    toggle.hidden = false;
    apply();
    toggle.addEventListener('click', () => {
      explicit = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try {
        document.cookie = `uvy-theme=${explicit}; Path=/; Max-Age=31536000; SameSite=Lax${location.protocol === 'https:' ? '; Secure' : ''}`;
      } catch {}
      apply();
    });
  });
})();
