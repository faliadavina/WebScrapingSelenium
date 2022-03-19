from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
import json
from datetime import datetime

s = Service("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://editorial.rottentomatoes.com/guide/140-essential-action-movies-to-watch-now/")
today = datetime.today()

dt_string = today.strftime("%H:%M:%S")
movieslist = []
i = 1

for movies in driver.find_elements(by=By.CLASS_NAME, value="row.countdown-item"):
    print(movies.text)
    for img in movies.find_elements(by=By.TAG_NAME, value="img"):
        print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
        i = i + 1
        
        movieslist.append(
            {"Image": img.get_attribute("src"),
             "Judul": movies.text.split("\n")[0].split("(",1)[0],
             "TahunRilis": movies.text.split("\n")[0].split(" (", 1)[1].split(")")[0],
             "Rate": movies.text.split("\n")[1],
             "Starring": movies.text.split("\n")[5].split("Starring: ",1)[1],
             "WaktuScraping": dt_string
                }
            )
hasil_scrap = open("D:\PY\ScrapSelenium.json", "w")
json.dump(movieslist, hasil_scrap, indent = 6)
hasil_scrap.close()

driver.quit()
