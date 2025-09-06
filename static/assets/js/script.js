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

            // UX uchun toast message (alert emas)
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
            `;
            document.body.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transition = 'opacity 0.5s ease';
                setTimeout(() => toast.remove(), 500);
            }, 3000);

            form.reset(); // Formani tozalash
        });
    }

    // ========== SEARCH FUNCTIONALITY ==========
    const searchInput = document.getElementById('countrySearch');
    let debounceTimer;

    if (searchInput) {
        // Enter bilan qidirish
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });

        // Real-time qidirish (debounce bilan)
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.trim();
            clearTimeout(debounceTimer);
            if (searchTerm.length > 2) {
                debounceTimer = setTimeout(() => {
                    console.log('Debounced search:', searchTerm);
                    // Bu yerga API chaqiruv yoki filter qilish kodi keladi
                }, 300);
            }
        });
    }

    function performSearch() {
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

    // ========== DARK MODE — Agar CSS da .dark yo'q bo'lsa, bu qismni OLIB TASHLANG ==========
    // const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    // function handleDarkModeChange(e) {
    //     if (e.matches) {
    //         document.documentElement.classList.add('dark');
    //     } else {
    //         document.documentElement.classList.remove('dark');
    //     }
    // }
    // darkModeMediaQuery.addEventListener('change', handleDarkModeChange);
    // handleDarkModeChange(darkModeMediaQuery); // Dastlabki holat
});