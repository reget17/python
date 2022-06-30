import requests
from bs4 import BeautifulSoup
import csv
import time
import random

headers = {
    "referer": "https://1000.menu/food-table",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

# res = requests.get("https://1000.menu/food-table", headers=headers)

# with open("page.html", "w") as file:
#     file.write(res.text)

with open("page.html") as file:
    res = file.read()

page = BeautifulSoup(res, 'lxml')
links = page.find(class_="catalog_tree").find_all(class_="podcatalog")

products = {}

for item in links:
    category_name = item.find(class_="name").find("a").text
    category_link = "https://1000.menu" + \
        item.find(class_="name").find("a").get("href")
    products[category_name] = category_link

count = 0

for item, link in products.items():
    # if count < 9: 
    #     count += 1
    #     continue
    res = requests.get(link, headers=headers)
    page = BeautifulSoup(res.text, "lxml")
    if page.find(class_="wide-box").find(id="food-table"):
        table = page.find(class_="wide-box").find(id="food-table").findAll("tr")
        
        with open(f"products/{item}.csv", "w", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            titles = table[0].findAll("th")
            titles_data = []
            titles_data.append(titles[0].text.strip())
            titles_data.append(titles[1].text.strip())
            titles_data.append(titles[2].text.strip())
            titles_data.append(titles[3].text.strip())
            titles_data.append(titles[4].text.strip())
            titles_data.append(titles[5].text.strip())
            
            writer.writerow(titles_data)

            del table[0]

        with open(f"products/{item}.csv", "a", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            
            for tr in table:
                data = tr.findAll("td")
                
                product_data = []
                product_data.append(data[0].text.strip())
                product_data.append(float(data[1].text.strip()))
                product_data.append(float(data[2].text.strip()))
                product_data.append(float(data[3].text.strip()))
                product_data.append(float(data[4].text.strip()))
                product_data.append(data[5].text.strip())
                writer.writerow(product_data)
        
        print(f"Загрузка страницы {item} завершена. Осталось {len(products)-count} страниц")
        count += 1
        time.sleep(random.randrange(2, 4))

