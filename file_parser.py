import xml.etree.ElementTree as ET
from titlecase import titlecase

def parse_file(filename, start):
    current_id = 0
    id_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            
            if line.startswith('AU'):
                id_list.append(current_id + start)
                if current_id == 849:
                    print(current_id)
                    ind = lines.index(line)
                    print(i, lines[ind])

            if line.startswith("ER"):
                current_id += 1
    return id_list

def get_xmls(text_xml_filename):
    xml_list = []
    with open(text_xml_filename, 'r', encoding='utf-8') as file:
        content = file.read()
        search_string = r'<?xml version="1.0" encoding="UTF-8"?>'
        xml_list = content.split(search_string)
        xml_list = [search_string + xml for xml in xml_list if xml]

    return xml_list

def get_book_info(xml) :
    root = ET.fromstring(xml)
    result = {}

    #Get each book entry
    record = root[0]
    subjects = set()
    for datafield in record:
        if datafield.attrib:
            if datafield.attrib["tag"] == "100":
                result["author"] = datafield[0].text
            if datafield.attrib["tag"] == "245":
                result["title"] = titlecase(datafield[0].text)
            if datafield.attrib["tag"] == "020":
                result["isbn"] = int(datafield[0].text.strip(" :"))
            if datafield.attrib["tag"] == "650":
                subjects.add(datafield[0].text)

    print(result)

if __name__ == '__main__':
    # Example usage
    # filename = 'results1.txt'
    # start = 1_000_000
    # parsed_sections = parse_file(filename, start)
    # print(len(parsed_sections))

    # s = get_xmls("marcxml-results2.txt")[0]
    # with open("samplexml.xml", "w", encoding="utf8") as f:
    #     f.write(s)
    with open("samplexml.xml", "r", encoding="utf8") as f:
        content = f.read()
    get_book_info(content)