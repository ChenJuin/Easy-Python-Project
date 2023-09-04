#Import Library
import qrcode
#Generate QR Code
url=''
img=qrcode.make(url)
img.save("a.jpg")