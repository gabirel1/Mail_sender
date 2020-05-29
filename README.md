# Mail_sender

Python script to send emails

REQUIREMENTS : Python3

USAGE : either ```./mailer.py``` or ```python3 mailer.py```

/!\ verify execution rights /!\

Before use you will have to edit the following files :

* config.py : 

              * EMAIL is your email
              * PASSWORD is your email password
              * SUBJECT is the subject of your mail
              * SMTP_ADRESS is the smtp adress of your mail provider
              * PORT is the smtp port used by the smtp of your mail provider

* dest_list.txt :

              * Put the email of the persons you want to send mails to (you can put more than one)
              /!\ One per line, no error handling is done /!\
              
 
* message.html :

              * In this file you must write the message you want to send
