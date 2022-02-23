import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
qr = "Name: Asley Nicole C. Marzan Github link: https://github.com/aslynicole"
  
# Generate QR code
url = pyqrcode.create(qr) 
# Create and save the png file naming "myqr.png"
url.png('QRCODEIMG.png', scale = 6)



  
