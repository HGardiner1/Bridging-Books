
import json

def get_books_by_tag(tag: str, book_list) :
    result = []
    for book in book_list:
        if book["tags"] and tag.lower() in map(lambda s : s.lower(), book["tags"]):
            result.append(book)
    return result

def get_books_by_genre(genre: str, book_list) :
    result = []
    for book in book_list:
        if book["genre"] and genre.lower() in map(lambda s : s.lower(), book["genre"]):
            result.append(book)
    return result

with open("main_json.json") as file:
    dict = json.load(file)
    books = dict["books"]

books = get_books_by_genre("fiction", books)
print(books)
