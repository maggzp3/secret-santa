import codecs
import dataProcessor
import santaManager
import emailSender
import logger

def main():
    # get raw input from file
    inputFile = codecs.open("input", 'r')
    inputData = inputFile.readlines()

    # process data
    dataProcessor.process(inputData)
    emails = dataProcessor.getEmails(inputData)
    excludes = dataProcessor.getExcludes(inputData)

    # create pairs
    pairs = santaManager.randomize(emails, excludes)

    # send appropiate emails
    for pair in pairs:
        emailSender.sendSantaMail(pair)

    # save log file on smpt server
    logger.saveResultOnServer(pairs, emails, excludes)

if __name__ == "__main__":
    main()
