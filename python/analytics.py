
import json
from file_parser import get_cover_from_book

ASIAN_AMERICAN_TAGS = ["Asian American", "Asians", "Chinese Americans", "Japanese Americans", "Indian Americans", "Korean Americans"]
AFRICAN_AMERICAN_TAGS = ["African American"]
LATIN_AMERICAN_TAGS = ["Hispanic", "Latin American", "Mexican American", "Guatemalans", "Peruvians", "Brazilian American", "Puerto Ricans", "Cuban American", "Dominican Americans"]
AMERICAN_INDIAN_TAGS = ["Indians of North America"]

CHILDRENS_GENRES = ["Juvemile", "Picture Book"]
YA_GENRES = ["Young Adult"]
ADULT_BOOK_LENGTH = 150

ROMANCE_TAGS = ["Romance", "Relationship"]
MYSTERY_TAGS = ["Mystery", "Thriller"]
SCIENCE_FICTION_TAGS = ["Science fiction"]
NONFICTION_GENRE = ["Biography"]
NONFICTION_TAG = ["History"]


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

def get_books_over_length(page_count: int, book_list) :
    result = []
    for book in book_list:
        if book["page_count"] and book["page_count"] >= page_count:
            result.append(book)
    return result

with open("main_json.json") as file:
    dict = json.load(file)
    books = dict["books"]

sample_books = []
mystery_sample_books = []
for tag in ASIAN_AMERICAN_TAGS:
    sample_books.extend(get_books_by_tag(tag, books))

for tag in MYSTERY_TAGS:
    mystery_sample_books.extend(get_books_by_tag(tag, sample_books))

print(len(mystery_sample_books))
mystery_sample_books = get_books_over_length(150, mystery_sample_books)
for book in mystery_sample_books:
    print(book["title"])