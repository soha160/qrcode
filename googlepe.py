import qrcode as qr

upi_id = input("enter your UPI ID = ")

googlepe_url = f'upi://pay?pa={upi_id}&pn=Recipient'

googlepe_qr = qr.make(googlepe_url)

googlepe_qr.save("googlepe_qr.png")

googlepe_qr.show()