// Small app-derived review behaviors. All snapshots and runtime assets are local.
(() => {
  const table = document.querySelector('[data-sortable]');
  if (table) {
    const tbody = table.tBodies[0];
    const headers = Array.from(table.tHead.rows[0].cells);
    const collator = new Intl.Collator(undefined, { numeric: true, sensitivity: 'base' });
    const mobile = document.querySelector('.mobile-sort');
    const field = document.querySelector('#sort-field');
    const direction = document.querySelector('#sort-direction');
    let active = 0, ascending = true;
    Array.from(tbody.rows).forEach((row, i) => row.dataset.originalIndex = i);
    const sort = (column, up) => {
      const numeric = headers[column].querySelector('button').dataset.sortType === 'number';
      const rows = Array.from(tbody.rows);
      rows.sort((a, b) => {
        const left = a.cells[column].dataset.sortValue;
        const right = b.cells[column].dataset.sortValue;
        const result = numeric ? Number(left) - Number(right) : collator.compare(left, right);
        return result ? result * (up ? 1 : -1) : Number(a.dataset.originalIndex) - Number(b.dataset.originalIndex);
      });
      tbody.append(...rows);
      active = column; ascending = up;
      headers.forEach((header, i) => header.setAttribute('aria-sort', i === active ? (up ? 'ascending' : 'descending') : 'none'));
      field.value = String(column);
      direction.querySelector('span').textContent = numeric ? (up ? '0–9' : '9–0') : (up ? 'A–Z' : 'Z–A');
      direction.setAttribute('aria-label', `Sort ${up ? 'ascending' : 'descending'}. Reverse sort order`);
      direction.querySelector('svg').style.transform = up ? '' : 'rotate(180deg)';
    };
    headers.forEach((header, i) => header.querySelector('button').addEventListener('click', () => sort(i, active === i ? !ascending : true)));
    field.addEventListener('change', () => sort(Number(field.value), true));
    direction.addEventListener('click', () => sort(active, !ascending));
    mobile.hidden = false;
  }
  const search = document.querySelector('#service-search');
  const provider = document.querySelector('#provider-filter');
  if (search) {
    const filter = () => {
      let count = 0;
      document.querySelectorAll('.service-link').forEach(link => {
        const matchesName = link.textContent.toLowerCase().includes(search.value.trim().toLowerCase());
        const matchesProvider = provider.value === 'all' || link.dataset.provider === (provider.value === 'other' ? '' : provider.value);
        link.hidden = !(matchesName && matchesProvider);
        if (!link.hidden) count++;
      });
      document.querySelector('#service-count').textContent = `${count} services`;
    };
    search.addEventListener('input', filter);
    provider.addEventListener('change', filter);
    const nav = document.querySelector('#service-nav');
    const toggle = document.querySelector('#nav-toggle');
    const close = () => { nav.classList.remove('nav-open'); toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-label','Open service navigation'); };
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close service navigation' : 'Open service navigation');
      if (open) search.focus();
    });
    document.addEventListener('keydown', event => { if (event.key === 'Escape' && nav.classList.contains('nav-open')) { close(); toggle.focus(); } });
    document.body.addEventListener('htmx:after:swap', () => {
      const main = document.querySelector('#service-main');
      const id = main.querySelector('[data-service]').dataset.service;
      document.querySelectorAll('.service-link').forEach(link => {
        if (link.getAttribute('href') === `service-${id}.html`) link.setAttribute('aria-current', 'page');
        else link.removeAttribute('aria-current');
      });
      close(); main.focus();
    });
  }
  const certificate = document.querySelector('#cert-input');
  if (certificate) {
    const original = certificate.value;
    certificate.addEventListener('input', () => {
      const same = certificate.value === original;
      document.querySelector('#certificate-output').hidden = !same;
      const state = document.querySelector('#certificate-state');
      state.hidden = same;
      state.textContent = certificate.value.trim() ? 'This design preview displays only the recorded certificate.' : 'No certificate processed yet.';
    });
    document.querySelector('#copy-link-btn').addEventListener('click', async () => {
      const url = new URL(location.href);
      url.hash = btoa(certificate.value);
      try { await navigator.clipboard.writeText(url.href); document.querySelector('#copy-status').textContent = 'Link copied.'; }
      catch { document.querySelector('#copy-status').textContent = 'Copy unavailable. Select and copy the certificate manually.'; }
    });
  }
})();
