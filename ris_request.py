import requests

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
start = 1_500_000
# Print the response
while start < 1_750_000:
    # Data
    data = {
        'f': 'RIS',
        'i[]': [f'Solr|{start+i}' for i in range(354)]
    }

    # Send POST request
    response = requests.get(url, params=data, headers=headers)
    with open("results3.txt", "a", encoding='utf-8') as file:
        file.write(response.text)
    print(start)
    start += 354
