// Scroll Progress Bar
function initScrollProgressBar() {
  const progressBar = document.getElementById('scroll-progress-bar');
  if (!progressBar) return;

  function updateProgressBar() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrollPercent = (scrollTop / scrollHeight) * 100;

    progressBar.style.width = scrollPercent + '%';
  }

  window.addEventListener('scroll', updateProgressBar);
  updateProgressBar(); // Initial call
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initScrollProgressBar);