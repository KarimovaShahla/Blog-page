document.addEventListener('DOMContentLoaded', function() {
    // Düyməyə klik hadisəsi əlavə edin
    const customButton = document.querySelector('.button');
    if (customButton) {
      customButton.addEventListener('click', function() {
        alert('Edit!');
      });
    }
  });
  