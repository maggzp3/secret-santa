import smtplib
import codecs
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

config = codecs.open("config", 'r').read().split(":")
user = config[0]
password = config[1]

def sendSantaMail(pair):
    mailReceiver = pair[0]
    makesGiftTo = pair[1]

    mailTemplate = codecs.open("mail_draft.html", 'r').read().replace("$to", makesGiftTo)

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = mailReceiver
    msg['Subject'] = "SECRET SANTA"

    msg.attach(MIMEText(mailTemplate, 'html'))

    SMTPSender(user, msg)
    SMTPSender(mailReceiver, msg)

def sendLogFile(message, date):
    msg = MIMEText(message)
    msg['From'] = user
    msg['To'] = user
    msg['Subject'] = "Log file, secret santa " + date

    SMTPSender(user, msg)

def SMTPSender(receiver, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    server.login(user, password)

    body = msg.as_string()
    server.sendmail(user, receiver, body)
    server.quit()
