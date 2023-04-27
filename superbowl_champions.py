import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"class": "wikitable sortable"})
rows = table.findAll("tr")[1:]

data = []
for row in rows:
    cols = row.findAll("td")
    if len(cols) >= 3:
        year = cols[0].text.strip()
        winning_team = cols[1].text.strip()
        losing_team = cols[2].text.strip()
        data.append([year, winning_team, losing_team])
df = pd.DataFrame(data, columns=["Year", "Winning Team", "Losing Team"])
print(df)