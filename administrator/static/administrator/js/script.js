function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
  
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
  }
  
  // Recuperar configuración del modo oscuro al cargar la página
  window.addEventListener('load', function() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
    const body = document.body;
  
    if (isDarkMode) {
      body.classList.add('dark-mode');
    } else {
      body.classList.remove('dark-mode');
    }
  });
  