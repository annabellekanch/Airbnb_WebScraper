from bs4 import BeautifulSoup
import requests
import pandas as pd

#initializing variables to hold a list of contents
Names = []
Prices = []
Reviews = []

url = "https://www.airbnb.com/s/New-York--NY/homes?adults=1&place_id=ChIJOwg_06VPwokRYv534QaPC8g&refinement_paths%5B%5D=%2Fhomes"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

#since we start on the first page of Airbnb, we only have to loop through 14 pages
for i in range(1, 14):
    np = soup.find("a", class_ = 'l1ovpqvx c1ytbx3a dir dir-ltr').get("href")
    cnp = "https://www.airbnb.com/"+np

    url = cnp
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, "lxml")

    #adding content to the lists initialized before based on their class name
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
        
#not every airbnb rental had reviews(because they are new) so we set orient to index so the keys of the passed dict "a" can be rows and then we transpose 
#the data frame this is just so we don't recieve an error because all the columns are different lengths
a = {'Names' : Names, 'Prices/night' : Prices, "Reviews" : Reviews}
df = pd.DataFrame.from_dict(a, orient = 'index')
df = df.transpose()
#converting dataframe to a csv file
df.to_csv("airbnb_newyork.csv")

