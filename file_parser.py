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

def get_xml_lists(text_xml_filename):
    xml_list = []
    with open(text_xml_filename, 'r', encoding='utf-8') as file:
        content = file.read()
        search_string = r'<?xml version="1.0" encoding="UTF-8"?>'
        xml_list = content.split(search_string)
        xml_list = [search_string + xml for xml in xml_list if xml]

    return xml_list


if __name__ == '__main__':
    # Example usage
    # filename = 'results1.txt'
    # start = 1_000_000
    # parsed_sections = parse_file(filename, start)
    # print(len(parsed_sections))
    print([len(s) for s in get_xml_lists("marcxml-results1.txt")])