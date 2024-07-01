import qrcode
from PIL import Image

# create an object for qrcode
qr = qrcode.QRCode( version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10,
    border=4,
)

# add data into our qrcode
qr.add_data("https://github.com/sojun15")
qr.make(fit=True)

# make a qrcode image
imag = qr.make_image(fill_color='blue')
imag.save('GitHub.png')