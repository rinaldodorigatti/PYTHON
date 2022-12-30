import math
import pyperclip


def main():
    mymessage = 'Cenoonommstmme oo snnio. s s c'
    mykey = 8

    plaintext = decryptmessage(mykey, mymessage)
    print(plaintext + '|')
    pyperclip.copy(plaintext)


def decryptmessage(key, message):

    numofcolumns = math.ceil(len(message) / key)
    numofrows = key
    numofshadedboxes = (numofcolumns * numofrows) - len(message)

    plaintext = [''] * numofcolumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numofcolumns) or (col == numofcolumns - 1 and row >= numofrows - numofshadedboxes):
            col = 0
            row += 1

    return ''.join(plaintext)


if __name__ == '__main__':
    main()
