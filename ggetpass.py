
import getpass

try:
    puser = getpass.getpass()
except Exception as error:
    print("Error : ", error)
else:
    print("password entered : ", puser)

try:
    luser = getpass.getuser()
except Exception as error:
    print("Error : ", error)
else:
    print("User : ", luser)
