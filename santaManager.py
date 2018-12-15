import random

# algorithm is simple (theres no algorithm) so we're not checking
# if there is possibility for creating all pairs with given excludes
# just trying some number of attempts and validaiting them
NUM_OF_ATTEMPTS = 100

def randomize(emails, excludes):
    attempt = 0
    foundPairs = False
    pairs = []

    while attempt < NUM_OF_ATTEMPTS and not foundPairs:
        try:
            pairs = createPairs(emails[:], excludes)
        except Exception:
            print("[Attempt " + str(attempt + 1) + "] Trying to find pairs again")
            attempt = attempt + 1
        else:
            if len(pairs) == len(emails):
                foundPairs = True

    return pairs

def createPairs(emails, excludes):
    result = []
    toChoose = emails[:]

    while len(emails):
        pair = popRandom(emails), popRandom(toChoose)

        if shouldBeExcluded(excludes, pair):
            # raise exception in case of block
            if len(emails) == 0 and len(toChoose) == 0:
                print "cant continue"
                raise Exception("Can't continue finding pairs, only exlcusions on list")

            # emails are on exclusion list, return them to its lists and try again
            emails.append(pair[0])
            toChoose.append(pair[1])
        else:
            # emails can be paired
             result.append(pair)

    return result

def popRandom(list):
    return list.pop(random.randrange(len(list)))

def shouldBeExcluded(excludes, pair):
    isExcluded = False

    for exclude in excludes:
        if pair[0] in exclude and pair[1] in exclude:
            isExcluded = True

    return isExcluded
