import qrcode
print("Welcome to QR code generator\nyou can make a qr code of :\nTEXT\nWEBSITE LINK\nIMAGES\n")
s=str(input("Enter your link : "))
qr=qrcode.make(s)
qr.save("qrcode.png")
print("QR code generated successfully !")