const progressBar = document.getElementById('progressBar');
let progress = 0;

function startCycle() {
    progress = 0;
    progressBar.style.width = '0%';

    // Simulate progress from 0% to 100%
    const interval = setInterval(() => {
    progress += 1;
    progressBar.style.width = `${progress}%`;

    if (progress >= 100) {
        clearInterval(interval);
        setTimeout(() => {
        alert("Progress completed! Restarting cycle...");
        startCycle(); // Automatically restart the cycle
        }, 1000);
    }
    }, 20); // Update every 20ms for smooth animation
}

// Auto-start on page load
window.onload = () => {
    setTimeout(() => {
    startCycle();
    }, 1000);
};

function openArticle(articleId) {
    // Masalan, sahifani ochish yoki modal ochish
    alert(`You clicked on: ${articleId}`);
    
    // Agar sahifaga o'tish kerak bo'lsa:
    // window.location.href = `/${articleId}.html`;
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("Document loaded and ready.");

    // ========== FORM SUBMISSION ==========
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const emailInput = form.querySelector('input[type="email"]');
            if (!emailInput) return;

            const email = emailInput.value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!email) {
                alert("Email manzilini kiriting.");
                return;
            }

            if (!emailRegex.test(email)) {
                alert("Iltimos, to'g'ri email manzilini kiriting.");
                return;
            }

            // UX uchun toast message
            const toast = document.createElement('div');
            toast.textContent = `Obuna uchun rahmat: ${email}`;
            toast.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: #28a745;
                color: white;
                padding: 12px 24px;
                border-radius: 8px;
                z-index: 10000;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                font-family: sans-serif;
                opacity: 1;
                transition: opacity 0.5s ease;
            `;
            document.body.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                setTimeout(() => toast.remove(), 500);
            }, 3000);

            form.reset();
        });
    }

    // ========== SEARCH FUNCTIONALITY ==========
    const searchInput = document.getElementById('countrySearch');
    let debounceTimer;

    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });

        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.trim();
            clearTimeout(debounceTimer);
            if (searchTerm.length > 2) {
                debounceTimer = setTimeout(() => {
                    console.log('Debounced search:', searchTerm);
                    // API chaqiruv yoki filtr kodi shu yerga
                }, 300);
            }
        });
    }

    function performSearch() {
        const searchInput = document.getElementById('countrySearch');
        if (!searchInput) return;

        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
            console.log('Searching for:', searchTerm);
            searchInput.style.borderColor = '#198754';
            searchInput.style.boxShadow = '0 0 0 2px rgba(25,135,84,0.25)';
            setTimeout(() => {
                searchInput.style.borderColor = '';
                searchInput.style.boxShadow = '';
            }, 1000);
        } else {
            searchInput.style.borderColor = '#dc3545';
            searchInput.style.boxShadow = '0 0 0 2px rgba(220,53,69,0.25)';
            setTimeout(() => {
                searchInput.style.borderColor = '';
                searchInput.style.boxShadow = '';
            }, 1000);
        }
    }

    // ========== DARK MODE — IZOHDA QOLDIRILGAN — AGAR KERAK BO‘LSA OCHING ==========
    /*
    const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    function handleDarkModeChange(e) {
        if (e.matches) {
            document.body.classList.add('dark');
        } else {
            document.body.classList.remove('dark');
        }
    }
    darkModeMediaQuery.addEventListener('change', handleDarkModeChange);
    handleDarkModeChange(darkModeMediaQuery);
    */
});

// ========== CAROUSEL (TECHNICAL PAPERS) ==========
let currentPaperSlide = 0;
let paperSlides = [];

function initPaperCarousel() {
    paperSlides = document.querySelectorAll('.paper-card');
    if (paperSlides.length > 0) {
        showPaperSlide(currentPaperSlide);
    }
}

function showPaperSlide(index) {
    paperSlides.forEach((slide, i) => {
        slide.style.opacity = i === index ? '1' : '0';
        slide.style.visibility = i === index ? 'visible' : 'hidden';
        slide.style.transform = i === index ? 'scale(1)' : 'scale(0.95)';
    });
}

function nextPaperSlide() {
    if (paperSlides.length === 0) return;
    currentPaperSlide = (currentPaperSlide + 1) % paperSlides.length;
    showPaperSlide(currentPaperSlide);
}

function prevPaperSlide() {
    if (paperSlides.length === 0) return;
    currentPaperSlide = (currentPaperSlide - 1 + paperSlides.length) % paperSlides.length;
    showPaperSlide(currentPaperSlide);
}

// ========== CAROUSEL (INFOGRAPHICS) ==========
let currentInfographicSlide = 0;
let infographicSlides = [];

function initInfographicCarousel() {
    infographicSlides = document.querySelectorAll('.infographic-card');
    if (infographicSlides.length > 0) {
        showInfographicSlide(currentInfographicSlide);
    }
}

function showInfographicSlide(index) {
    infographicSlides.forEach((slide, i) => {
        slide.style.opacity = i === index ? '1' : '0';
        slide.style.visibility = i === index ? 'visible' : 'hidden';
        slide.style.transform = i === index ? 'scale(1)' : 'scale(0.95)';
    });
}

function nextInfographicSlide() {
    if (infographicSlides.length === 0) return;
    currentInfographicSlide = (currentInfographicSlide + 1) % infographicSlides.length;
    showInfographicSlide(currentInfographicSlide);
}

function prevInfographicSlide() {
    if (infographicSlides.length === 0) return;
    currentInfographicSlide = (currentInfographicSlide - 1 + infographicSlides.length) % infographicSlides.length;
    showInfographicSlide(currentInfographicSlide);
}

// ========== INITIALIZE CAROUSELS ==========
document.addEventListener('DOMContentLoaded', function() {
    initPaperCarousel();
    initInfographicCarousel();
});

const slider = document.querySelector('.event-slider .row');
const items = document.querySelectorAll('.event-item');
const navBtns = document.querySelectorAll('.nav-btn');

let currentIndex = 0;
const visibleItems = 3;

function showSlide(index) {
const offset = index * (100 / visibleItems);
slider.style.transform = `translateX(-${offset}%)`;
}

navBtns[0].addEventListener('click', () => {
if (currentIndex > 0) {
    currentIndex--;
    showSlide(currentIndex);
}
});

navBtns[1].addEventListener('click', () => {
if (currentIndex < items.length - visibleItems) {
    currentIndex++;
    showSlide(currentIndex);
}
});

document.querySelectorAll('.filter-btn').forEach(btn => {
btn.addEventListener('click', () => {
    btn.classList.toggle('active');
    });
});

document.querySelector('.load-more button').addEventListener('click', function() {
alert("Loading more events...");
// Here you can add AJAX or dynamic loading logic
});