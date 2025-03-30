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
            if datafield.attrib["tag"] == "300":
                # example string "7 pages"
                cleaned = datafield[0].text.replace("unnumbered ", '')
                end_of_number_str = cleaned.split(" pages")[0]
                
                beginning_of_number_ind = end_of_number_str.rindex(" ")+1 if " " in end_of_number_str else 0

                number_string = end_of_number_str[beginning_of_number_ind:]
                if number_string.isnumeric():
                    result["page_count"] = int(number_string)
            if datafield.attrib["tag"] == "100":
                result["author"] = datafield[0].text
            if datafield.attrib["tag"] == "245":
                result["title"] = titlecase(datafield[0].text)
            if datafield.attrib["tag"] == "020":
                for subfield in datafield:
                    if subfield.attrib["code"] == "a":                    
                        result["isbn"] = subfield.text.split(" ")[0]
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

def get_cover(author: str, title: str, lib_id: int, isbn:str=None):
    author_encoded = parse.quote_plus(author)
    title_encoded = parse.quote_plus(title)
    if isbn:
        return f"https://hestia.jmrl.org/findit/Cover/Show?&size=large&recordid={lib_id}&source=Solr&isbn={isbn}&author={author_encoded}&title={title_encoded}"
    else:
        return f"https://hestia.jmrl.org/findit/Cover/Show?&size=large&recordid={lib_id}&source=Solr&author={author_encoded}&title={title_encoded}"

def get_cover_from_book(book):
    if book["isbn"]:
        return get_cover(book["author"], book["title"], book["lib_id"], book["isbn"])
    else:
        return get_cover(book["author"], book["title"], book["lib_id"])
def build_json(xml_txt_filename):
    final_json_dict = {'books':[]}
    for i, xml_string in enumerate(get_xmls(xml_txt_filename)):
        print(i)
        book_infos = get_book_infos(xml_string)
        for book in book_infos:
            book['tags'] = list(book['tags']) if 'tags' in book else None
            book['genre'] = list(book['genre']) if 'genre' in book else None
            book['isbn'] = book['isbn'] if 'isbn' in book else None
            book['page_count'] = book['page_count'] if 'page_count' in book else None
            final_json_dict["books"].append(book)
    return final_json_dict

def build_jsons(xml_txt_filenames):
    final_json_dict = {'books':[]}
    for xml_txt_filename in xml_txt_filenames:
        final_json_dict['books'].extend(build_json(xml_txt_filename)['books'])
    return final_json_dict

def complete_tag_list(book_list):
    return [tag for book in book_list if book['tags'] for tag in book['tags']]

def complete_genre_list(book_list):
    return [tag for book in book_list if book['genre'] for tag in book['genre']]


# if __name__ == '__main__':
#     with open('main.json', 'w') as file:
#         json.dump(build_jsons(['marcxml-results1.txt', 'marcxml-results2.txt', 'marcxml-results3.txt']), file, indent=4)
    
