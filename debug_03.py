import logging
import os

filen = 'debug.log'
wfile = 'write_file.txt'

if os.path.exists(filen):
    os.remove(filen)
    print('File removed : %s' % filen)
else:
    print("File doesn't exists %s" % filen)

if os.path.exists(wfile):
    os.remove(wfile)
    print('File removed : %s' % wfile)
else:
    print("File doesn't exists %s" % wfile)

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Ca c'est du debug")
logging.info("Ca c'est du info")
logging.warning("Ca c'est du warning")
logging.error("Ca c'est du error")
logging.critical("Ca c'est du critical")

fileout = open('debug.log', 'r')
# print(fileout.read())   read all the file
line_text = fileout.readlines()
for g in line_text:
    print(g, end='')
fileout.close()

fileout2 = open('debug.log', 'r')
# test = fileout2.read()          read all file content
# test = fileout2.readline()      read the first line
# test = fileout2.readline(10)    read 10 first character
# test = fileout2.readlines()     read all file content in a list
test = fileout2.readline()
print("-" * 30)
print(test)
fileout2.close()

datas = ['Temps', 10, 'Delai', 20, 'Fin']
text_file = open(wfile, 'w')
for o in datas:
    text_file.writelines(str(o) + " ")
text_file.write("\n")
text_file.close()

errgetc = ''
errgetf = ''
errgetargs = ''
errgetd = ''
try:
    read_wfile = open('tutu.txt', 'r')
except FileNotFoundError as err:
    print('Error to open file :', err)
    errgetc = err.errno
    errgetf = err.filename
    errgetargs = err.args
    errgetd = err.strerror

finally:
    if errgetc == 2:
        print('NOT Ok file read')
    else:
        print('Ok file read')

print("CODE : " + str(errgetc) + "\nFILE : " + errgetf + "\nARGS : " + str(errgetargs) + "\nSTRR : " + errgetd)

"""
for i in range(0, len(datas)):
    datas.append(i)
"""
