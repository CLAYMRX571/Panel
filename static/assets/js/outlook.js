console.log("Global outlook page loaded successfully.");

const ctx = document.getElementById('pieChart').getContext('2d');

const chart = new Chart(ctx, {
    type: 'pie',
    data: {
    labels: [
        'Renewables',
        'Energy efficiency',
        'Electrification',
        'Hydrogen',
        'FF based CO₂ capture and storage (CCS)',
        'RE based CO₂ removals (BECCS)'
    ],
    datasets: [{
        data: [25, 25, 20, 10, 6, 14],
        backgroundColor: [
        '#0066b3', // Renewables
        '#70c5d9', // Energy efficiency
        '#fdd835', // Electrification
        '#a5d6a7', // Hydrogen
        '#455a69', // CCS
        '#90a4ae'  // BECCS
        ],
        borderWidth: 1,
        borderColor: '#fff'
        }]
    },
    options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
        display: false
        },
        tooltip: {
        callbacks: {
            label: function(context) {
            return `${context.label}: ${context.parsed.y}%`;
                }
            }
        }
    },
        animation: {
            animateRotate: true,
            animateScale: true
        }
    }
});

document.querySelector('.card-content a').addEventListener('click', function(e) {
    e.preventDefault();
    window.open('https://www.irena.org/publications/2023/Jan/World-Energy-Transitions-Outlook-2023', '_blank');
});