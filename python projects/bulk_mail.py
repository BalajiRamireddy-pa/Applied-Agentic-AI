# bulk mail with attachment
# gmail smtp automation

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_mail = input("enter your gmail id: ").strip()

if "@gmail.com" not in sender_mail:
    print("not a valid gmail id, try again")
    exit()

app_pass = ""
   

if not app_pass:
    print("app password not found, set GMAIL_APP_PASSWORD env variable first")
    exit()

subject = "Email Automation Using Python - Bulk mail attachment"
body = "In this project we will understand how python be useful in real world applications"
file_to_send = "simplemail.py"   # change this to whatever file u want to send

n = int(input("how many people u wanna send to? "))

mail_list = []
for i in range(n):
    m = input(f"recipient {i+1} email: ").strip()
    if "@gmail.com" in m:
        mail_list.append(m)
    else:
        print(m, "-> invalid format, skipping this one")

if len(mail_list) == 0:
    print("no valid emails given, exiting")
    exit()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_mail, app_pass)

for receiver in mail_list:
    msg = MIMEMultipart()
    msg["From"] = sender_mail
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body))

    with open(file_to_send, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_to_send))
        msg.attach(part)

    server.sendmail(sender_mail, receiver, msg.as_string())
    print("sent to", receiver)

server.quit()
print("done, all mails sent")
