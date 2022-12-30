
from ftplib import FTP_TLS
import os


def ftptest(server, port, name, password):
    ftph = FTP_TLS()
    try:
        ftph.connect(server, port)
    except Exception as err:
        error = 'can not connect server: %s %s' % (server, err)
        ftph.close()
        return error
    try:
        ftph.login(name, password)
        ftph.prot_p()
    except Exception as err:
        error = 'ftp username or password error %s' % err
        ftph.close()
        return error

    ftph.close()

    return "Connect OK"


def ftpupload(server, port, name, password, ftppath, uploadfilepath):
    ftph = ''
    try:
        ftph = FTP_TLS()
        ftph.connect(server, port)
        ftph.login(name, password)
        ftph.prot_p()
    except Exception as err:
        ftph.close()
        return 'ftp can not connect %s' % err
    try:
        ftph.cwd(ftppath)
    except Exception as err:
        print('Error : ', err)
        ftph.mkd(ftppath)
        ftph.cwd(ftppath)
    # p,f=os.path.split(uploadfilepath)
    p, f = os.path.split(uploadfilepath)
    try:
        fileh = open(uploadfilepath, 'rb')
    except Exception as err:
        ftph.close()
        return 'uploadfile can not be opened %s' % err
    try:
        # ftph.storbinary('STOR ', fileh, 1024)
        ftph.storbinary('STOR ' + f, fileh, 1024)
    except Exception as err:
        fileh.close()
        ftph.close()
        return 'ftp upload error %s' % err
    fileh.close()
    ftph.close()    
    return "UPLOAD transfer OK"


def ftpdownload(server, port, name, password, ftppath, uploadfilepath):
    ftph = ''
    try:
        ftph = FTP_TLS()
        ftph.connect(server, port)
        ftph.login(name, password)
        ftph.prot_p()
    except Exception as err:
        ftph.close()
        return 'ftp can not connect %s' % err
    try:
        ftph.cwd(ftppath)
    except Exception as err:
        print('Error : ', err)
        ftph.mkd(ftppath)
        ftph.cwd(ftppath)
    # p,f=os.path.split(uploadfilepath)
    # p,f=os.path.split(uploadfilepath)
    try:
        fileh = open(uploadfilepath, 'wb')
    except Exception as err:
        ftph.close()
        return 'downloadfile can not be opened %s' % err
    try:
        # ftph.retrbinary('RETR ',fileh,1024)
        ftph.retrbinary('RETR %s' % uploadfilepath, fileh.write)
    except Exception as err:
        fileh.close()
        ftph.close()
        return 'ftp upload error %s' % err
    fileh.close()
    ftph.close()    
    return "DOWNLOAD transfer OK"

    
if __name__ == '__main__':
    print(ftptest('192.168.122.150', 21, 'rickyd', 'lu48cie'))
    print(ftpupload('192.168.122.150', 21, 'rickyd', 'lu48cie', 'upload', r'monFichier.txt'))
    print(ftpdownload('192.168.122.150', 21, 'rickyd', 'lu48cie', 'upload', r'all_suse_ldap_base.ldif'))
