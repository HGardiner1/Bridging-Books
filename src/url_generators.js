


function generateLibkUrl(book) {
    if (!book) {
      throw new Error("Invalid book object or missing lib_id");
    }
    
    const baseUrl = "https://hestia.jmrl.org/findit/Record/";
    return `${baseUrl}${encodeURIComponent(book.lib_id)}`;
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