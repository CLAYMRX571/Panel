const timeline = document.getElementById('timeline');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

let scrollPosition = 0;
const eventWidth = 280; 
const gap = 80; 
const visibleEvents = 3;

function scrollToIndex(index) {
    const offset = index * (eventWidth + gap);
    timeline.scrollLeft = offset;
}

function updateButtons() {
    const maxScroll = timeline.scrollWidth - timeline.clientWidth;
    prevBtn.disabled = scrollPosition <= 0;
    nextBtn.disabled = scrollPosition >= maxScroll;
}

prevBtn.addEventListener('click', () => {
    if (scrollPosition > 0) {
    scrollPosition -= (eventWidth + gap);
    timeline.scrollLeft = scrollPosition;
    updateButtons();
    }
});

nextBtn.addEventListener('click', () => {
    const maxScroll = timeline.scrollWidth - timeline.clientWidth;
    if (scrollPosition < maxScroll) {
    scrollPosition += (eventWidth + gap);
    timeline.scrollLeft = scrollPosition;
    updateButtons();
    }
});

timeline.addEventListener('scroll', () => {
    scrollPosition = timeline.scrollLeft;
    updateButtons();
});

// Initial setup
updateButtons();