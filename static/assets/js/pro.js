// Interaktivlik: kartani bosganda xabar chiqarish
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
    const title = card.querySelector('h2').textContent;
    alert(`More information about ${title} will be shown here.`);
    });
});

// Download tugmasi bosilganda
document.querySelector('.download-btn').addEventListener('click', () => {
    alert('Brochure downloading...');
});