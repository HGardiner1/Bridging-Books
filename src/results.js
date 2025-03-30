let selectedRacesEthnicites = [];
let selectedReadingLevels = [];
let selectedGenres = [];

function getSelectedOptions(formId) {
    const checkboxes = document.querySelectorAll(`#${formId} input[type="checkbox"]:checked`);
    return Array.from(checkboxes).map(checkbox => checkbox.nextElementSibling.textContent);
}

let currentForm = "identity"; 

document.getElementById('nextBtn').addEventListener('click', function(event) {
    event.preventDefault(); 

    if (currentForm === "identity") {
        selectedRacesEthnicites = getSelectedOptions('identityForm');
        document.getElementById('identityForm').classList.remove('active');
        document.getElementById('readingLevelForm').classList.add('active');
        currentForm = "readingLevel"; 
    } else if (currentForm === "readingLevel") {
        selectedReadingLevels = getSelectedOptions('readingLevelForm');
        document.getElementById('readingLevelForm').classList.remove('active');
        document.getElementById('genresForm').classList.add('active');
        currentForm = "genres"; 
    } else {
        selectedGenres = getSelectedOptions('genresForm');
        window.location.href = "results-page/resultswindow.html"; 
    }
});