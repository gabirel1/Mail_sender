#!/usr/bin/python3

import smtplib
import config
from email.mime.text import MIMEText

EMAIL=config.EMAIL
PASSWORD=config.PASSWORD
SUBJECT=config.SUBJECT

def send_mail(to) :
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    print("server started")
    server.login(EMAIL, PASSWORD)
    print("logged in")
    message = MIMEText("")
    message["From"] = EMAIL
    message["To"] = to
    message["Subject"] = SUBJECT
    server.sendmail(EMAIL, to, message.as_string())
    print("Mail sucessfully sent")


def get_recipient() :
    file = open('dest_list.txt', 'r')
    count = 0
    mail_to = ""

    while True: 
        count += 1

        # Get next line from file 
        line = file.readline() 

        # if line is empty 
        # end of file is reached 
        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))
        send_mail(line)
    file.close() 

if __name__=='__main__' :
    get_recipient()