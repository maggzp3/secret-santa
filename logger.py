import emailSender
import datetime

def saveResultOnServer(pairs, emails, excludes):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    message = "Logged on " + date + "\n\nWith given mail addresses: " + str(emails) + "\n\nAnd given excludes: " + str(excludes) + "\n\n\n\nCreated pairs: " + str(pairs)

    emailSender.sendLogFile(message, date)
