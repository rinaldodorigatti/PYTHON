

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTER_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
print(LETTER_AND_SPACE)


def loaddictionnary():
    englishwords = {}
    try:
        dictionnaryfile = open('dictionnary.txt')
        for word in dictionnaryfile.read().split('\n'):
            englishwords[word] = None
        dictionnaryfile.close()
    except FileNotFoundError as nffe:
        print("Error to open file", nffe)
    return englishwords


ENGLISH_WORDS = loaddictionnary()


def getenglishcount(message):
    message = message.upper()
    message = removenonletters(message)
    possiblewords = message.split()

    if not possiblewords:
        return 0.0

    matches = 0
    for word in possiblewords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possiblewords)


def removenonletters(message):
    lettersonly = []
    for symbol in message:
        if symbol in LETTER_AND_SPACE:
            lettersonly.append(symbol)
    return ''.join(lettersonly)


def isenglish(message, wordpercent=20, letterpercent=85):
    wordsmatch = getenglishcount(message) * 100 >= wordpercent
    numletter = len(removenonletters(message))
    messageletterspercentage = float(numletter) / len(message) * 100
    lettersmatch = messageletterspercentage >= letterpercent
    return wordsmatch and lettersmatch


print(isenglish('Is this sentence English text?'))
