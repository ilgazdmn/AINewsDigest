import ssl
import smtplib
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port =465

    username = os.getenv('EMAIL_SENDER')
    password = os.getenv('GOOGLE_APP_PASSWORD')

    receiver = os.getenv('EMAIL_RECEIVER')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)