def parse_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().split("TI  - ")
    
    # Split by empty newline (double newline)
    start = 1_250_000
    id_list = []
    for i, line in enumerate(content):
        if "Title not available" in line:
            continue
        else:
            id_list.append(i + start)

    print(id_list)
    print("Length: ", len(id_list))
    return id_list

# Example usage
filename = 'results2.txt'
parsed_sections = parse_file(filename)
