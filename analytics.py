
import json

def get_ids_by_tag(tag: str, book_list) :
    ids = []
    for book in books:
        if book["tags"] and tag.lower() in map(lambda s : s.lower(), book["tags"]):
            ids.append(book["lib_id"])
    return ids

with open("main_json.json") as file:
    dict = json.load(file)
    books = dict["books"]

ids = get_ids_by_tag("divorced women", books)
print(ids)