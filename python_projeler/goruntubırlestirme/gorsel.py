from PIL import Image

#750-610 414-414 görsellerimin boyutları
image=Image.new('RGB',(750,414),color='white') #burada yeni bir imaj oluşturdum

cat1=Image.open("D:\WebScrapıng\goruntuısleme\kedi.jpg") #burada görsellerimi açtım
cat2=Image.open("D:\WebScrapıng\goruntuısleme\kedii.jpg")

image.paste(cat1,(0,0))  #burada görsellerimi yapıştırdım
image.paste(cat2,(414,0))

image.save("D:\WebScrapıng\goruntuısleme\cat12.jpg") #yeni görselimi kaydettim


