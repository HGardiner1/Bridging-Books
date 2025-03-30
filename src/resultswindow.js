document.addEventListener('DOMContentLoaded', function() {
    // Use fetch to load the JSON file
    const bookContainer = document.getElementById('book-container');
    fetch('../main.json')  // Adjust the path if necessary to point to the correct folder
      .then(response => response.json())
      .then(books => {
        books['books'].slice(0,10).forEach((book) => {
        console.log(book);
        // Create a card container
        const card = document.createElement('div');
        card.className = "bg-white shadow-lg rounded-lg overflow-hidden hover:shadow-2xl transition-shadow";

        // Build the inner HTML for each card
        card.innerHTML = `
        <div class="flex items-center p-4 rounded shoadow-lg">
            <!-- Image with some margin to ensure it's not touching the border -->
            <img
            src="${10}"
            alt="${book.title}"
            class="w-32 h-auto object-cover mr-4 rounded shadow-lg transform transition-transform duration-300 hover:scale-[1.02]"
            />
            
            <!-- Text area on the right, aligned to the right -->
            <div class="text-left">
            <h2 class="text-xl font-semibold mb-1">${book.title}</h2>
            <p class="text-sm text-gray-500 mb-2">by ${book.author}</p>
            <p class="text-gray-700 mb-4">${10}</p>
            <a
                href="${10}"
                target="_blank"
                class="inline-block px-4 py-2 bg-indigo-500 text-white text-sm rounded active:bg-indigo-600 transition-colors transform transition-transform duration-300 hover:scale-[1.02]"
            >
                Get from Library
            </a>
            </div>
        </div>
        `;

        // Append the card to our grid container
        bookContainer.appendChild(card);
        });
    })
    .catch(error => console.error('Error loading the books:', error));
});
