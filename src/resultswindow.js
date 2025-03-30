TAGS_WE_WANT = ["Mystery"];
GENRES_WE_WANT = ["Fiction"];

document.addEventListener('DOMContentLoaded', function() {
    // Use fetch to load the JSON file
    const bookContainer = document.getElementById('book-container');
    const loadingElement = document.getElementById('loading-container');
    title = document.getElementById('title');
    fetch('../main.json')  // Adjust the path if necessary to point to the correct folder
      .then(response => response.json())
      .then(booksData => {  // Use consistent variable name (booksData)
        let books = booksData.books;  // Make sure books is declared and booksData structure is correct
        books = getBooksByTags(TAGS_WE_WANT, books);
        books = getBooksByGenres(GENRES_WE_WANT, books);
        books = books.slice(0, 10);
        books.forEach(book => {
            // Create a card container
            const card = document.createElement('div');
            card.className = "bg-white shadow-lg rounded-lg overflow-hidden hover:shadow-2xl transition-shadow";

            let desc = book.description;
            let cut = 50; // set this to where you want to cut the description

            if (desc.length > cut) {
                let lastSpace = desc.lastIndexOf(' ', cut);
                desc = lastSpace > 0 ? desc.substring(0, lastSpace) + '...' : desc.substring(0, cut) + '...';
            }

            card.innerHTML = `
            <div class="flex items-center p-4 rounded shoadow-lg">
                <!-- Image with some margin to ensure it's not touching the border -->
                <img
                src="${generateImageUrl(book)}"
                alt="${book.title}"
                class="w-32 h-auto object-cover mr-4 rounded shadow-lg transform transition-transform duration-300 hover:scale-[1.02]"
                />
                
                <!-- Text area on the right, aligned to the right -->
                <div class="text-left">
                <h2 class="text-xl font-semibold mb-1">${book.title}</h2>
                <p class="text-sm text-gray-500 mb-2">by ${book.author}</p>
                <p class="text-gray-700 mb-4">${desc}</p>
                <a
                    href="${generateLibUrl(book)}"
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
    .catch(error => console.error('Error loading the books:', error))
    .finally(() => {
        // Hide the loading spinner once fetching is complete
        loadingElement.style.display = 'none';
        title.innerHTML = "Your Book Becommendations:";
    });
});

function getBooksByTags(tags, bookList) {
    const lowerTags = tags.map(tag => tag.toLowerCase());
    return bookList.filter(book => 
      book.tags && book.tags.some(bookTag => 
        lowerTags.some(tag => bookTag.toLowerCase().includes(tag))
      )
    );
  }
  
  function getBooksByGenres(genres, bookList) {
    const lowerGenres = genres.map(genre => genre.toLowerCase());
    return bookList.filter(book => 
      book.genre && book.genre.some(bookGenre => 
        lowerGenres.some(genre => bookGenre.toLowerCase().includes(genre))
      )
    );
  }
  
  function getBooksOverLength(pageCount, bookList) {
    return bookList.filter(book => book.page_count && book.page_count >= pageCount);
  }

  function generateImageUrl(book) {
    if (!book) {
        throw new Error("Invalid book object or missing lib_id");
    }

    author_encoded = encodeURIComponent(book.author);
    title_encoded = encodeURIComponent(book.title);
    if (book.isbn) {
        return `https://hestia.jmrl.org/findit/Cover/Show?&size=large&recordid=${book.lib_id}&source=Solr&isbn=${book.isbn}&author=${author_encoded}&title=${title_encoded}`;
    }
    else {
        return `https://hestia.jmrl.org/findit/Cover/Show?&size=large&recordid=${book.lib_id}&source=Solr&author=${author_encoded}&title=${title_encoded}`;
    }
}

function generateLibUrl(book) {
    if (!book) {
      throw new Error("Invalid book object or missing lib_id");
    }
    
    const baseUrl = "https://hestia.jmrl.org/findit/Record/";
    return `${baseUrl}${encodeURIComponent(book.lib_id)}`;
}