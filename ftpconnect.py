from ftplib import FTP_TLS


def connect():
    connexion = FTP_TLS()
    connexion.debugging = 2
    connexion.connect('192.168.122.150', 21)
    connexion.login('rickyd', 'lu48cie')
    return connexion


conn = connect()
conn.prot_p()
conn.retrlines('LIST')


"""
# Connect, but only using SSL version 2 aor 3
from ftplib import FTP_TLS
import ssl

def connect():
    ftp = FTP_TLS()
    ftp.ssl_version = ssl.PROTOCOL_SSLv23
    ftp.debugging = 2
    ftp.connect('192.168.122.150', 21)
    ftp.login('rickyd', 'lu48cie')
    return ftp
"""

"""
# Connect, but only using TLS version 1.2
from ftplib import FTP_TLS
import ssl

def connect():
    ftp = FTP_TLS()
    ftp.ssl_version = ssl.PROTOCOL_TLSv1_2
    ftp.debugging = 2
    ftp.connect('localhost', 2121)
    ftp.login('developer', 'password')
    return ftp

ftp = connect()
ftp.retrlines('LIST')
"""