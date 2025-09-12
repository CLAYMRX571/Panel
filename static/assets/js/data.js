document.addEventListener("DOMContentLoaded", function () {
  console.log("Page loaded successfully!");
  
  // Masalan, "Data" so'zini bosganda boshqa sahifaga o'tish
  const breadcrumb = document.querySelector('.breadcrumb-current');
  breadcrumb.addEventListener('click', function(e) {
    e.preventDefault();
    alert("This is the Data page.");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  console.log("Featured page loaded.");

  // "View" va "PDF" havolalari interaktivligi
  const viewLink = document.querySelector('.view-link');
  const pdfLink = document.querySelector('.download-link');

  viewLink.addEventListener('click', function(e) {
    e.preventDefault();
    alert("Redirecting to the full publication...");
  });

  pdfLink.addEventListener('click', function(e) {
    e.preventDefault();
    alert("Downloading PDF file...");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  console.log("Related publications loaded.");

  // "View more" va navigatsiya tugmalarining funksiyalari
  const viewMoreLink = document.querySelector('.view-more-link');
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');

  viewMoreLink.addEventListener('click', function(e) {
    e.preventDefault();
    alert("Redirecting to all related publications...");
  });

  prevBtn.addEventListener('click', function() {
    alert("Previous publications shown.");
  });

  nextBtn.addEventListener('click', function() {
    alert("Next publications shown.");
  });
});