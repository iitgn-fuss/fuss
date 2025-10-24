// Reading Time Calculator
function calculateReadingTime() {
  const content = document.querySelector('.page-content');
  if (!content) return;

  const text = content.textContent || content.innerText;
  const wordsPerMinute = 200; // Average reading speed
  const words = text.trim().split(/\s+/).length;
  const readingTime = Math.ceil(words / wordsPerMinute);

  // Create reading time element
  const readingTimeElement = document.createElement('div');
  readingTimeElement.className = 'reading-time';
  readingTimeElement.innerHTML = `<small>📖 Estimated reading time: ${readingTime} minute${readingTime > 1 ? 's' : ''}</small>`;
  readingTimeElement.style.cssText = `
    margin-bottom: 1rem;
    color: #7f8c8d;
    font-size: 0.9rem;
  `;

  // Insert before the content
  content.parentNode.insertBefore(readingTimeElement, content);
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', calculateReadingTime);