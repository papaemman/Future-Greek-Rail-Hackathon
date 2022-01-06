import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
PASS = os.environ.get('PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, PASS)
    
    subject = 'test mail'
    body = 'it works!!!'
    msg = f'Subject: {subject}\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS, "Receiver_mail", msg)