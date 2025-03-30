s = "1 online resource (240 pages)"

cleaned = s.replace("unnumbered", '').replace(",", "").replace("(", '').strip()

delim = ''
if 'pages' in cleaned:
    delim = "pages"
elif 'p.' in cleaned:
    delim = "p."
elif 'leaves' in cleaned:
    delim = "leaves"

end_of_number_str = cleaned.split(delim)[0].strip()
beginning_of_number_ind = end_of_number_str.rindex(" ")+1 if " " in end_of_number_str else 0
number_string = end_of_number_str[beginning_of_number_ind:]
number_string = number_string.split('-')[-1] # take the second value if in a range

print(int(number_string))