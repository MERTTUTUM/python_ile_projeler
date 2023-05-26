from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser= webdriver.Chrome("C:/Users/Mertcan/Desktop/chromedriver")

browser.get("https://www.trendyol.com/aqua-di-polo-1987/unisex-siyah-gunes-gozlugu-apss012201-p-35809728/yorumlar")
time.sleep(5)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)


yorumlar=browser.find_elements(By.CLASS_NAME,"comment-text")
yorumList=[]

for yorum in yorumlar:
    yorumList.append(yorum.text)

with open("yorumlar.txt","w",encoding="UTF-8") as file:
    for list in yorumList:
        file.write(list + "\n")    
time.sleep(4)

browser.quit()  