from gtts import gTTS
import os

dosya=open("D:\WebScrapıng\yazıokuyucu\deneme.txt","r",encoding="UTF-8").read()
konusma=gTTS(text= dosya,lang='tr',slow=False)
konusma.save("deneme.mp3")
os.system("deneme.mp3")