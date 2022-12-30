import ftplib


ftp_connect = ftplib.FTP_TLS()
ftp_connect.debugging = 0
ftp_connect.connect('192.168.122.150', 21)
ftp_connect.login('rickyd', 'lu48cie')

ftp_connect.prot_p()
unFichier = open('monFichier.txt', 'rb')
ftp_connect.storbinary('STOR monFichier.txt', unFichier)
unFichier.close()
ftp_connect.quit()
