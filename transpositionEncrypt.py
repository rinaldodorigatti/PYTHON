import pyperclip


def main():
    mymessage = 'Common sense is not so common.'
    mykey = 10

    ciphertext = encryptmessage(mykey, mymessage)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)


def encryptmessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]

            pointer += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
