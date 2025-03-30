import json
import time
import xml.etree.ElementTree as ET
from urllib import parse
from titlecase import titlecase # type: ignore
import re

def parse_file(filename, start):
    current_id = 0
    id_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith('AU'):
                id_list.append(current_id + start)
                # if current_id in range(155960, 158776):
                #     print(current_id)
                #     ind = lines.index(line)
                #     print(i, lines[ind])
                #     print(''.join(lines[ind-6:ind+10]))

            if line.startswith("ER"):
                current_id += 1
    return id_list

def filter_errors(s):
    start_index = 0
    while '<!DOCTYPE html>' in s[start_index:]:
        start = s.index('<!DOCTYPE html>', start_index)
        end = s.index('</html>\n<?', start) + len('</html>\n<?')
        s = s[:start] + '<?' + s[end:]
        start_index = start  # Update start_index to current position to avoid endless loop
    return s

def get_xmls(text_xml_filename):
    xml_list = []
    with open(text_xml_filename, 'r', encoding='utf-8') as file:
        content = file.read()
        content = filter_errors(content)
        search_string = r'<?xml version="1.0" encoding="UTF-8"?>'
        xml_list = content.split(search_string)
        xml_list = [search_string + xml for xml in xml_list if xml]
    
    return xml_list

def get_book_infos(xml) :
    root = ET.fromstring(xml)
    books = []
    #Get each book entry
    for record in root:
        result = {}
        subjects = set()
        genres = set()
        for datafield in record:
            if not datafield.attrib:
                continue
            if datafield.attrib["tag"] == "100":
                result["author"] = datafield[0].text
            if datafield.attrib["tag"] == "245":
                result["title"] = titlecase(datafield[0].text)
            if datafield.attrib["tag"] == "020":
                result["isbn"] = datafield[0].text.split(" ")[0]
            if datafield.attrib["tag"] == "650":
                for subfield in datafield:
                    if subfield.attrib["code"] == "a":
                        subjects.add(subfield.text)
                    if subfield.attrib["code"] == "v":
                        genres.add(subfield.text)
            if datafield.attrib["tag"] == "907":
                result["lib_id"] = datafield[0].text[2:9]
        if subjects:
            result["tags"] = subjects
        if genres:
            result["genre"] = genres
        books.append(result)
    return books

def get_cover(author: str, title: str, isbn: str, lib_id: int):
    author_encoded = parse.quote_plus(author)
    title_encoded = parse.quote_plus(title)
    return f"https://hestia.jmrl.org/findit/Cover/Show?&size=large&recordid={lib_id}&source=Solr&isbn={isbn}&author={author_encoded}&title={title_encoded}"

def get_cover_from_book(book):
    get_cover(book["author"], book["title"], book["isbn"], book["lib_id"])

def build_json(xml_txt_filename):
    final_json_dict = {'books':[]}
    for xml_string in get_xmls(xml_txt_filename):
        book_infos = get_book_infos(xml_string)
        for book in book_infos:
            book['tags'] = list(book['tags']) if 'tags' in book else None
            book['genre'] = list(book['genre']) if 'genre' in book else None
            final_json_dict["books"].append(book)
    return final_json_dict

# if __name__ == '__main__':
#     # open final_json1, 2, 3 and merge them
#     with open("final_json1.json", encoding='utf-8') as f1, open('final_json2.json', encoding='utf-8') as f2, open('final_json3.json', encoding='utf-8') as f3:
#         j1, j2, j3 = json.load(f1), json.load(f2), json.load(f3)
#         final_final_json = {'books': j1['books'] + j2['books'] + j3['books']}
#         with open("main_json.json", "w", encoding='utf-8') as file:
#             json.dump(final_final_json, file, indent=4)
#     print(len(final_final_json['books']))
    
