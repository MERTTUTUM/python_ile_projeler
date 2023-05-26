from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser= webdriver.Chrome("C:/Users/Mertcan/Desktop/chromedriver")

browser.get("https://tr.linkedin.com/")

browser.fullscreen_window()
time.sleep(5)

login = browser.find_element(By.XPATH, "/html/body/nav/div/a[2]")
login.click()
time.sleep(5)

email=browser.find_element(By.XPATH,"//*[@id='username']")
password=browser.find_element(By.XPATH,"//*[@id='password']")

email.send_keys("mail adresiniz")
password.send_keys("şifreniz")

login_button= browser.find_element(By.CSS_SELECTOR,"#organic-div > form > div.login__form_action_container > button")
login_button.click()
time. sleep(5)

#search_bar= browser.find_element(By.XPATH,"//*[@id='global-nav-search']/div/button/li-icon/svg")
#search_bar.send_keys("#python")
#search_bar.send_keys(Keys.RETURN)
#time.sleep(5)

contacts= browser.find_element(By.XPATH,"//*[@id='global-nav']/div/nav/ul/li[2]/a")
contacts.click()
time.sleep(5)

contact_button= browser.find_element(By.CLASS_NAME,"mn-community-summary__entity-info")
contact_button.click()
time.sleep(3)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

followers = browser.find_elements(By.CLASS_NAME,"mn-connection-card__details")
followerList=[]

for follower in followers:
    followerList.append(follower.text)

with open ("follower.txt","w",encoding = "UTF-8") as file:
    for follower in followerList:
        file.write(follower + "/n")
time.sleep(5)

browser.quit()        
