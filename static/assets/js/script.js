// === Dropdown Toggle ===
function toggleDropdown(id) {
  const dropdowns = document.querySelectorAll('.mega-menu1, .mega-menu2, .mega-menu3');
  dropdowns.forEach(drop => {
    if (drop.id === id) {
      drop.style.display = drop.style.display === 'block' ? 'none' : 'block';
    } else {
      drop.style.display = 'none';
    }
  });
}

// Tashqariga bosilganda yopish
document.addEventListener('click', function (e) {
    if (!e.target.closest('.navbar li')) {
        document.querySelectorAll('.mega-menu1, .mega-menu2, .mega-menu3')
        .forEach(drop => drop.style.display = 'none');
  }
});

// === Marquee control ===
document.addEventListener("DOMContentLoaded", function () {
  const marquee = document.querySelector(".marquee-text");
  let isPaused = false;

    function setSpeed(speed) {
        if (marquee) {
            marquee.style.animationDuration = speed + "s";
        }
    }

function togglePause() {
    if (!marquee) return;
    if (isPaused) {
      marquee.style.animationPlayState = "running";
      isPaused = false;
    } else {
      marquee.style.animationPlayState = "paused";
      isPaused = true;
    }
}

setSpeed(15); // boshlang‘ich tezlik
});

// === Cards hover effect ===
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-5px)';
        card.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.3)';
  });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = 'none';
  });
});

// === Hero section update on card click ===
document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('.card');
    const heroImg = document.getElementById('hero-img');
    const heroTitle = document.getElementById('hero-title');
    const heroLink = document.getElementById('hero-link');
    const heroType = document.getElementById('hero-type');

    cards.forEach(card => {
        card.addEventListener('click', function () {
            const imgSrc = this.getAttribute('data-img');
            const title = this.getAttribute('data-title');
            const type = this.getAttribute('data-type');
            const linkText = this.getAttribute('data-link');

    if (heroImg && heroTitle && heroLink && heroType) {
        heroImg.src = imgSrc;
        heroTitle.textContent = title;
        heroLink.textContent = linkText;
        heroType.textContent = type;

        heroImg.style.opacity = '0';
        heroTitle.style.opacity = '0';
        heroLink.style.opacity = '0';
        heroType.style.opacity = '0';

        setTimeout(() => {
            heroImg.style.opacity = '1';
            heroTitle.style.opacity = '1';
            heroLink.style.opacity = '1';
            heroType.style.opacity = '1';
            }, 100);
        }
        });
    });
});

// === Read about us button ===
const readMoreBtn = document.querySelector('.read-more');
if (readMoreBtn) {
    readMoreBtn.addEventListener('click', function () {
        alert('Redirecting to "About Us" page...');
        // window.location.href = '/about';
    });
}

// === Nav tabs switcher ===
document.querySelectorAll('.nav-tabs a').forEach(tab => {
    tab.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelectorAll('.nav-tabs a').forEach(t => t.classList.remove('active'));
        this.classList.add('active');
    });
});

// === Newsletter subscribe ===
const subscribeBtn = document.querySelector('.subscribe');
    if (subscribeBtn) {
        subscribeBtn.addEventListener('click', function () {
        alert('Redirecting to newsletter subscription...');
        // window.location.href = '/newsletter';
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const missionHeader = document.querySelector(".mission-header");
  const backgroundMap = document.querySelector(".background-map");

  missionHeader.addEventListener("click", () => {
    backgroundMap.classList.toggle("active");
  });
});
