import qrcode
from qrcode.image.pure import PymagingImage
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=2,
)

# Add QR data
qr.add_data('Raghu K.\nWashingon DC\n123.456.6789\nrk.keypki@yopmail.com\nDroneModel:CHN DJ\nSerial=111-222-DC')
qr.make(fit=True)

#Create QR image and save it. \
img = qr.make_image(fill_color="black", back_color="skyblue")
img.save('mydroneID.png')
#Show image
img.show('mydroneID.png')
#EOL
