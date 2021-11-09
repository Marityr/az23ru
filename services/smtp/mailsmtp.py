from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import smtplib
import os

from dotenv import load_dotenv


load_dotenv()

def mail_smtp():
    PASWORDSMTP = 'gvugmgivnuqytvmq'
    LOGINSMTP = os.getenv('LOGINSMTP')
    REPICIENTSMTP = os.getenv('REPICIENTSMTP')
    # create message object instance
    msg = MIMEMultipart()

    message = "Файл прикреплен в вложении"

    # setup the parameters of the message
    password = f"{PASWORDSMTP}"
    msg['From'] = f"{LOGINSMTP}"
    msg['To'] = f"{REPICIENTSMTP}"
    msg['Subject'] = "Список заказов из АБЦП с 21-09-01 до 21-11-10"

    # add in the message body
    msg.attach(MIMEText(message, 'html'))

    files = [
        'myexel.xlsx',
    ]

    for a_file in files:
        attachment = open(a_file, 'rb')
        file_name = os.path.basename(a_file)
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
        part.add_header('Content-Disposition',
                        'attachment',
                        filename=file_name)
    encoders.encode_base64(part)
    msg.attach(part)
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

    server.quit()
