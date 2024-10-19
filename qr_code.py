import qrcode

#Taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for payment apps
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QR to imapge file (option)
#phonepe_qr.save('phonepe_qr.png')
#paytm_qr.save('paytm_qr.png')
#google_pay_qr.save('google_pay_qr.png')

#Display the QR codes (you may need to install PIL/pillow libary)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()