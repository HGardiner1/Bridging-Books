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

ids = parse_file("results3.txt", start=1_500_000)
print(len(ids))
# Print the response
step = 354
for i in range(0,len(ids), step):
    # Data
    data = {
        'f': 'MARCXML',
        'i[]': [f'Solr|{ids[j+i]}' for j in range(min(step, len(ids)-i))]
    }

    # query_string = urlencode(data, doseq=True)
    # full_url = url + '?' + query_string
    # print(full_url)

    # Send POST request
    response = requests.get(url, params=data, headers=headers)
    with open("marcxml-results3.txt", "a+", encoding='utf-8') as file:
        file.write(response.text)
    print(ids[i])

