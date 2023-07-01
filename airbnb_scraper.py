from bs4 import BeautifulSoup
import requests
import pandas as pd

Names = []
Prices = []
Reviews = []

url = "https://www.airbnb.com/s/New-York--NY/homes?adults=1&place_id=ChIJOwg_06VPwokRYv534QaPC8g&refinement_paths%5B%5D=%2Fhomes"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

for i in range(1, 14):
    np = soup.find("a", class_ = 'l1ovpqvx c1ytbx3a dir dir-ltr').get("href")
    cnp = "https://www.airbnb.com/"+np

    url = cnp
    r = requests.get(url)


    soup = BeautifulSoup(r.text, "lxml")

    name = soup.find_all("div", class_ = "t1jojoys dir dir-ltr")
    for i in name:
        n = i.text
        Names.append(n)

    price = soup.find_all("span", class_ = "_1y74zjx")
    for i in price:
        n = i.text 
        Prices.append(n)

    review = soup.find_all("span",class_ = "r1dxllyb dir dir-ltr")
    for i in review:
        n = i.text 
        Reviews.append(n)
        

a = {'Names' : Names, 'Prices/night' : Prices, "Reviews" : Reviews}
df = pd.DataFrame.from_dict(a, orient = 'index')
df = df.transpose()
df.to_csv("airbnb_newyork.csv")

