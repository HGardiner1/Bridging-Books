// Function to load the navbar into the page
function loadNavbar() {
    fetch('navbar.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('navbar-container').innerHTML = data;
        });
}

// load the navbar when the page is loaded
window.onload = loadNavbar;