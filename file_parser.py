def parse_file(filename, start):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().split("TI  - ")
    
    # Split by empty newline (double newline)
    id_list = []
    for i, line in enumerate(content):
        if "Title not available" in line:
            continue
        else:
            id_list.append(i + start + 1)

    print(id_list)
    print("Length: ", len(id_list))
    return id_list

if __name__ == '__main__':
    # Example usage
    filename = 'results3.txt'
    start = 1_500_000
    parsed_sections = parse_file(filename, start)
