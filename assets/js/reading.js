(() => {
  const controls = document.querySelector('[data-reading-controls]');
  if (!controls) return;
  const entries = [...document.querySelectorAll('[data-reading-entry]')];
  const input = document.getElementById('reading-search');
  const buttons = [...document.querySelectorAll('[data-reading-topic]')];
  const empty = document.getElementById('reading-empty');
  let topic = 'all';
  function filter() {
    const query = input.value.trim().toLocaleLowerCase();
    let count = 0;
    entries.forEach(entry => {
      const visible = (topic === 'all' || entry.dataset.topics.split('|').includes(topic)) && entry.dataset.search.includes(query);
      entry.hidden = !visible;
      count += visible ? 1 : 0;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.readingTopic === topic)));
    const language = document.documentElement.lang;
    const label = language.startsWith('zh') ? '篇精读' : language.startsWith('es') ? 'lecturas' : 'readings';
    document.getElementById('reading-count').textContent = `${count} / ${entries.length} ${label}`;
    empty.hidden = count !== 0;
  }
  buttons.forEach(button => button.addEventListener('click', () => { topic = button.dataset.readingTopic; filter(); }));
  input.addEventListener('input', filter);
  document.getElementById('reading-reset').addEventListener('click', () => { topic = 'all'; input.value = ''; filter(); input.focus(); });
  controls.hidden = false;
})();
