function loadNavbar() {
    console.log('Navbar is being loaded...');  // Debugging log
    fetch('navbar.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('navbar-container').innerHTML = data;
        })
        .catch(error => console.error('Error loading navbar:', error));
}

window.onload = loadNavbar;
