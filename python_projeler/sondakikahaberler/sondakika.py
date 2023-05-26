from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser= webdriver.Chrome("C:/Users/Mertcan/Desktop/chromedriver")
browser.get("https://www.trthaber.com/")

browser.fullscreen_window()
time.sleep(3)

sondk=browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/a")
sondk.click()
time.sleep(3)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

haberler=browser.find_elements(By.CLASS_NAME,"text-frame")
haberList=[]

for haber in haberler:
    haberList.append(haber.text)

with open("sondakikahaber.text","w",encoding= "UTF-8")as File:
    for son in haberList:
        File.write(son + "\n")
time.sleep(5)

browser.quit()