import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices=[]
Description = []
Reviews = []


for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+phone+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phone+under+50000&requestId=79381f92-8e30-4b01-aa8a-dcf7765521a1&as-searchtext=mobile&page="+str(i)
    r=requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text,"lxml")
    box= soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div",class_="_4rR01T")
# print(names)
    for i in names:
        name = i.text
        Product_name.append(name)
    # print(Product_name)
    prices = box.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)
# print(Prices)

    desc = box.find_all("ul",class_ = "_1xgFaf")
    for i in desc:
        name=i.text
        Description.append(name)
# print(Description)

    reviews = box.find_all("div",class_= "_3LWZlK")
    for i in reviews:
        name = i.text
        Reviews.append(name)
# print(len(Reviews))

df = pd.DataFrame({"Product Name": Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
# print(df)

df.to_csv("C:/Users\soura/OneDrive/Desktop/filpkart_mobiles_under_50000.csv")



    # print(soup)
    # while True:
    # np = soup.find("a",class_="_1LKTO3" ).get("href")
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)

    # url =cnp
    # r=requests.get(url)
    # soup=BeautifulSoup(r.text,"lxml")


