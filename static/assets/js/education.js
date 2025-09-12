document.addEventListener("DOMContentLoaded", function () {
    console.log("Technical papers loaded.");

// Tablar uchun funksiya
const tabButtons = document.querySelectorAll('.tab-button');
const tabContents = document.querySelectorAll('.tab-content');

tabButtons.forEach(button => {
    button.addEventListener('click', function() {
        const tabId = this.getAttribute('data-tab');

        // Barcha tugmalardan "active" ni olib tashla
        tabButtons.forEach(btn => btn.classList.remove('active'));
        // Hozirgi tugma "active" bo'lsin
        this.classList.add('active');

        // Barcha kontentlarni yashir
        tabContents.forEach(content => content.classList.remove('active'));
        // Tanlangan kontentni ko'rsat
        document.getElementById(tabId).classList.add('active');
    });
});

// "See more" havolasini bosganda
const seeMoreLink = document.querySelector('.see-more-link');
seeMoreLink.addEventListener('click', function(e) {
    e.preventDefault();
    alert("Redirecting to full list of technical papers...");
    });
});