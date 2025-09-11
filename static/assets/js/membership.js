const data = [
    { year: 2011, value: 85 },
    { year: 2012, value: 105 },
    { year: 2013, value: 123 },
    { year: 2014, value: 138 },
    { year: 2015, value: 145 },
    { year: 2016, value: 150 },
    { year: 2017, value: 154 },
    { year: 2018, value: 159 },
    { year: 2019, value: 161 },
    { year: 2020, value: 162 },
    { year: 2021, value: 167 },
    { year: 2022, value: 168 },
    { year: 2023, value: 169 },
    { year: 2024, value: 170 },
    { year: 2025, value: 180 }
];

const maxValue = Math.max(...data.map(d => d.value));
const chartHeight = 300;

const barChart = document.getElementById('barChart');
data.forEach(item => {
    const bar = document.createElement('div');
    bar.className = 'bar';
    const height = (item.value / maxValue) * chartHeight;
    bar.style.height = `${height}px`;

    const valueLabel = document.createElement('div');
    valueLabel.className = 'value-label';
    valueLabel.textContent = item.value;

    const yearLabel = document.createElement('div');
    yearLabel.className = 'year-label';
    yearLabel.textContent = item.year;

    bar.appendChild(valueLabel);
    bar.appendChild(yearLabel);
    barChart.appendChild(bar);
});

// IRENA members list (170 countries)
const countries = [
    "Afghanistan", "Albania", "Algeria", "Angola", "Antigua and Barbuda", "Argentina",
    "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
    "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bosnia and Herzegovina",
    "Botswana", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "China", "Colombia", "Comoros",
    "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark",
    "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Eritrea",
    "Estonia", "Eswatini", "Ethiopia", "European Union", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
    "Guyana", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
    "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati", "Kuwait", "Kyrgyzstan", "Latvia", "Lebanon", "Lesotho", "Liechtenstein", "Lithuania",
    "Luxembourg", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
    "Mauritius", "Mexico", "Micronesia", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
    "Republic of Korea", "Republic of Moldova", "Romania", "Russian Federation", "Rwanda",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
    "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
    "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland", "Tajikistan",
    "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Türkiye", "Turkmenistan",
    "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United Republic of Tanzania",
    "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam",
    "Yemen", "Zambia", "Zimbabwe"
];

const membersList = document.getElementById('membersList');
countries.forEach(country => {
  const el = document.createElement('div');
  el.className = 'country';
  el.textContent = country;
  membersList.appendChild(el);
});