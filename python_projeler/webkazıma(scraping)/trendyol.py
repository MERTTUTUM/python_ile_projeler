import requests
from bs4 import BeautifulSoup

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
hbrsite=requests.get("https://www.trendyol.com/aqua-di-polo-1987/unisex-siyah-gunes-gozlugu-apss012201-p-35809728",headers=headers_param)

icerik=hbrsite.content
soup=BeautifulSoup(icerik,"html.parser")
baslik=soup.find("div",attrs={"class","info-wrapper"})
gozluk=[]

for bilgi in baslik:
    gozluk.append(baslik.text)

with open("gözlük.txt","w",encoding="UTF-8") as file:
    for blg in gozluk:
     file.write(blg + "/n")