from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser= webdriver.Chrome("C:/Users/Mertcan/Desktop/chromedriver")

browser.get("https://www.hepsiburada.com/hp-15s-fq5003nt-intel-core-i7-1255u-16gb-512gb-ssd-15-6-ips-freedos-tasinabilir-bilgisayar-6g0g5ea-pm-HBC00003331OC-yorumlari")
time.sleep(5)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

aciklama=browser.find_elements(By.CLASS_NAME,"hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw")
yorumList=[]

for yorum in aciklama:
    yorumList.append(yorum.text)

with open("hpsburad.txt","w",encoding="UTF-8") as file:
    for acklm in yorumList:
        file.write(acklm + "\n")

time.sleep(4)

browser.quit()





       
