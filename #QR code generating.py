#QR code generating
import qrcode
X=input("Enter data:")
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=10,
)
qr.add_data(a)
qr.make(fit=True)

img=qr.make_image(fill_color="black", back_color="White")
img.save(f"z1z2z3.png")

img.show()