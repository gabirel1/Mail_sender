#!/usr/bin/python3

import smtplib
import config
import email
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL=config.EMAIL
PASSWORD=config.PASSWORD
SUBJECT=config.SUBJECT
SMTP_ADRESS=config.SMTP_ADRESS
PORT=config.PORT
ATTACHED_FILE=config.FILE

def send_mail(to, text) :
    server = smtplib.SMTP(SMTP_ADRESS, PORT)
    print("settling server")

    server.starttls()
    print("server started")

    server.login(EMAIL, PASSWORD)
    print("logged in")

    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = to
    message["Subject"] = SUBJECT
    message.attach(MIMEText(text, 'html'))

    if (ATTACHED_FILE != "") :
        filename = ATTACHED_FILE
        attachement = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachement).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachement; filename = "+filename)
        message.attach(part)
        print("attachement file added")

    server.sendmail(EMAIL, to, message.as_string())
    print("Mail sucessfully sent")

    server.close()
    print("server closed")

def get_mail_content() :
    try :
        file = open('message.html')
    except :
        print("You must enter an existing file /!\ remember that we doesn't handle file content errors")
        exit(84)
    
    message = file.read()
    return (message)

def get_recipient() :
    count = 0
    try :
        file = open('dest_list.txt', 'r')
    except :
        print("You must enter an existing file /!\ remember that we doesn't handle file content errors")
        exit(84)

    message = get_mail_content()

    while True: 
        count += 1
        line = file.readline() 
        if not line:
            break
        print("Mail {}: {}".format(count, line.strip()))
        send_mail(line, message)
    file.close() 

if __name__=='__main__' :
    get_recipient()