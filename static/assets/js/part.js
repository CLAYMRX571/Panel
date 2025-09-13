document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        const title = card.querySelector('h2').textContent;
        alert(`More information about ${title} will be shown here.`);
    });
});