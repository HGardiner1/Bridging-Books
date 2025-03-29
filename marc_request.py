import requests
from file_parser import parse_file
from urllib.parse import urlencode

# Base URL
url = "https://hestia.jmrl.org/findit/Cart/doExport"

# Headers
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
}

ids = parse_file("results1.txt", start=1_000_000)
# Print the response
for i in range(0,len(ids), 1):
    # Data
    data = {
        'f': 'MARCXML',
        'i[]': [f'Solr|{ids[j]}' for j in range(1)]
    }

    # query_string = urlencode(data, doseq=True)
    # full_url = url + '?' + query_string
    
    # print(full_url)

    # Send POST request
    response = requests.get(url, params=data, headers=headers)
    with open("marcxml-results2.txt", "a+", encoding='utf-8') as file:
        file.write(response.text)
    print(ids[i])

