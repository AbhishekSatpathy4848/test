import base64
import binascii
from flask import Flask, request, Response
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

def send_email():
    email = 'abhisheksatpathy4848@gmail.com'
    password = 'diqs dvtt wkgi vfaq'  #using Google App Passwords

    message = MIMEMultipart()
    message["From"] = "Solmelu"
    message["Subject"] = "Solmelu: Feedback from User"
    message["To"] = "abhisheksatpathy.211it002@nitk.edu.in"
    messageText = MIMEText("testing emails")
    message.attach(messageText)
    # # binary_pdf = open(path, 'rb')
    # # payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # # payload.set_payload((binary_pdf).read())
    # encoders.encode_base64(payload)
    # message.attach(payload)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email,password)
    server.sendmail(email, "abhisheksatpathy.211it002@nitk.edu.in", message.as_string())
    server.quit()
    print("email sent successfully")

def decode_base_64(image_data):
    try:
        image = base64.b64decode(image_data, validate=True)
        return image
    except binascii.Error as e:
        print(e)

def save_image(image, image_name):
    with open(image_name, "wb") as f:
        f.write(image)

@app.route('/send-mail')
def hello_world():
    # image = decode_base_64(request.json["image_data"])
    # save_image(image, "uploaded_image.png")
    send_email()
    return Response(status=201)

@app.route('/')
def index():
    return "Use /send-mail to send email"

if __name__ == '__main__':
    app.run()