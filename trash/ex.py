import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import codecs
f = codecs.open("mail_draft2.html", 'r')

fromaddr = "kontakt.pipsztaki@gmail.com"
legit_pass = "a6a6a6a6"

toaddr = "maggzp3@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"

body = "<b>YOUR MESSAGE HERE</b>"
msg.attach(MIMEText(f.read(), 'html'))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login(fromaddr, legit_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
