import sys
import os
import time
import transpositionEncrypt
import transpositionDecrypt


def main():
    inputfilename = "frankenstein.txt"
    outputfilename = "frankenstein_encrypted.txt"
    mykey = 10
    mymode = 'encrypt'

    if not os.path.exists(inputfilename):
        print("The file %s doesn't exists ! quitting..." % inputfilename)
        sys.exit()

    if os.path.exists(outputfilename):
        print("This file %s already exists, owerwrite ? (C) continue or (Q) quit ?" % outputfilename)
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileobj = open(inputfilename)
    content = fileobj.read()
    fileobj.close()

    print('%sing...' % (mymode.title()))

    starttime = time.time()
    translated = ''
    if mymode == 'encrypt':
        translated = transpositionEncrypt.encryptmessage(mykey, content)
    elif mymode == 'decrypt':
        translated = transpositionDecrypt.decryptmessage(mykey, content)
    totaltime = round(time.time() - starttime, 2)
    print('%sion time: %s seconds' % (mymode.title(), totaltime))

    outputfileobj = open(outputfilename, 'w')
    outputfileobj.write(translated)
    outputfileobj.close()

    print('Done %sing %s (%s characters).' % (mymode, inputfilename, len(content)))
    print('%sed file is %s.' % (mymode.title(), outputfilename))


if __name__ == '__main__':
    main()
