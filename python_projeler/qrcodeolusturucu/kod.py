import qrcode

data='https://www.linkedin.com/in/mertcantutum/'
image=qrcode.make(data)
image.save('qrcode.png')
image.show()
