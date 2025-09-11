const infographics = [
    {
    title: "Global renewable energy jobs key figures",
    image: "{% static 'assets/img/cost.jpg' %}"
    },
    {
    title: "Women in the solar photovoltaic sector compared with other sectors",
    image: "{% static 'assets/img/itm.jpg' %}"
    },
    {
    title: "Distribution of skills required for pico, micro and mini hydro plants",
    image: "{% static 'assets/img/panels.png' %}"
    },
    {
    title: "Renewable Energy Capacity by Region",
    image: "{% static 'assets/img/cost.jpg' %}"
    },
    {
    title: "Energy Access in Developing Countries",
    image: "{% static 'assets/img/itm.jpg' %}"
    },
    {
    title: "Future of Hydrogen Economy",
    image: "{% static 'assets/img/panels.png' %}"
    }
];

const container = document.getElementById('infographics-container');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

let currentIndex = 0;

function updateCarousel() {
    container.innerHTML = '';

    // Ko'rsatiladigan 3 ta infografikani tanlash
    const start = currentIndex;
    const end = Math.min(start + 3, infographics.length);

    for (let i = start; i < end; i++) {
    const item = infographics[i];
    const card = document.createElement('div');
    card.className = 'infographic-card';

    card.innerHTML = `
        <img src="${item.image}" alt="${item.title}" class="infographic-image" />
        <h3 class="infographic-title">${item.title}</h3>
        <div class="button-group">
        <button class="btn-download">⬇️ Download</button>
        <button class="btn-zoom">🔍</button>
        </div>
    `;
    container.appendChild(card);
    }
}

// Previous button
prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
    currentIndex--;
    updateCarousel();
    }
});

// Next button
nextBtn.addEventListener('click', () => {
    if (currentIndex + 3 < infographics.length) {
    currentIndex++;
    updateCarousel();
    }
});

// Boshlang'ich ko'rsatish
updateCarousel();

// Download tugmasi
document.querySelectorAll('.btn-download').forEach(button => {
    button.addEventListener('click', function () {
    alert('Fayl yuklandi: ' + this.closest('.infographic-card').querySelector('.infographic-title').textContent);
    });
});

// Zoom tugmasi
document.querySelectorAll('.btn-zoom').forEach(button => {
    button.addEventListener('click', function () {
    const img = this.closest('.infographic-card').querySelector('.infographic-image');
    alert('Rasm zoom qilindi: ' + img.alt);
    });
});