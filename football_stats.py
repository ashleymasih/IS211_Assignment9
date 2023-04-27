import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/?sortcol=td&sortdir=descending'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'TableBase-table'})
if table is not None:
    headers = table.find_all('th')
    header_names = [header.text.strip() for header in headers]
    player_data = OrderedDict()
    data_rows = table.find_all('tr')[1:21]
    for row in data_rows:
        cells = row.find_all('td')
        player_data.clear()  
        for i, cell in enumerate(cells):
            player_data[header_names[i]] = cell.text.strip()
        print(player_data)
else:
    print('Table not found!')