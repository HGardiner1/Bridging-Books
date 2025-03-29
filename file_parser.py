def parse_file(filename, start):
    current_id = 0
    id_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            
            if line.startswith('TI') and not "Title not available" in line:
                id_list.append(current_id + start)
                if current_id == 1:
                    print(current_id)
                    ind = lines.index(line)
                    print(i, lines[ind])
            if line.startswith("TI"):
                current_id += 1

    return id_list

if __name__ == '__main__':
    # Example usage
    filename = 'results1.txt'
    start = 1_000_000
    parsed_sections = parse_file(filename, start)
    print(len(parsed_sections))