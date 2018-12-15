emails = []
excludes = []

def process(raw):
    emailsDone = False

    #start processing emails
    for line in raw:
        if line == "\n":
            emailsDone = True
            continue

        if not emailsDone:
            email = line.rstrip()
            emails.append(email)
            excludes.append(excludeItself(email))
        else:
            pair = line.rstrip().split(":")
            newExclude = (pair[0], pair[1])

            excludes.append(newExclude)

def getEmails(raw):
    return emails

def getExcludes(raw):
    return excludes

def excludeItself(email):
    return email + ":" + email
