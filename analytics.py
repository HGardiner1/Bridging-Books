
import json
from file_parser import get_cover_from_book

def get_books_by_tag(tag: str, book_list) :
    result = []
    for book in book_list:
        if not book["tags"]:
            continue
        book["tags"] = [tag.lower() for tag in book["tags"]]
        for book_tag in book["tags"]:
            if tag.lower() in book_tag:
                result.append(book)
    return result

def get_books_by_genre(genre: str, book_list) :
    result = []
    for book in book_list:
        if not book["genre"]:
            continue
        book["genre"] = [genre.lower() for genre in book["genre"]]
        for book_genre in book["genre"]:
            if genre.lower() in book_genre:
                result.append(book)
    return result

with open("main_json.json") as file:
    dict = json.load(file)
    books = dict["books"]

result = get_books_by_tag("FROG", books)

print(result)