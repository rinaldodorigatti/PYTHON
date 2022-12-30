
import os
import sys
import smtplib


print(os.getcwd())
print(sys.copyright)

fd = "/home/rickyd/Documents/QTPROJET/Python/GFG.txt"
file = open(fd, 'w')
file.write("Hello\n")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

checkFile = os.path.exists(fd)
print(checkFile)

"""
fd = "/home/rickyd/Documents/QTPROJET/Python/GFG.txt"
file = os.popen(fd, 'w')
file.write("Hello")"""


class test:
    def __init__(self, name: str='', age: int=10, email: str=''):
        self.name = name
        self.age = age
        self.email = email

    def printE(self, city: str=''):
        print(self.name, self.age, city, self.email)


def myfunc(name: str="A"):
    print('C''est le : ', name)


def sendEmail():
    sender = "rinaldo.dorigatti@gmail.com"
    receiver = "rinaldo.dorigatti@gmail.com"
    user = 'rinaldo.dorigatti@gmail.com'
    passw = 'pkdynxvsgjhzpojn'
    # message = "Message_you_need_to_send"
    message = """From: Diego Dorigatti <diegogta5.dorigatti@gmail.com>
    To: Lala <rinaldo.dorigatti@gmail.com>
    Subject: SMTP HTML e-mail test\r\n\r\n

    This is an e-mail message to be sent in HTML format

    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
    """

    try:
        # smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        # smtpObj.ehlo()
        # smtpObj.starttls()
        # smtpObj.ehlo()
        # smtpObj.login(user, passw)
        # smtpObj = smtplib.SMTP('smtp.gmail.com', 25)
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(user, passw)
        smtpObj.sendmail(from_addr=sender, to_addrs=[receiver], msg=message)
        smtpObj.quit()
        print("Successfully sent email")
    except Exception as err:
        print("Error: unable to send email", err)


def send_email(to, subject, message):
    from email.message import EmailMessage

    try:
        email_address = 'rinaldo.dorigatti@gmail.com'
        email_password = 'pkdynxvsgjhzpojn'
        email_sender = 'diegogta5.dorigatti@gmail.com'

        if email_address is None or email_password is None:
            print("Did you set email address and password correctly?")
            return False

        # create email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_sender
        msg['To'] = to
        msg.set_content(message)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("Mail has been sent to %s" % to)
        return True
    except Exception as e:
        print("Problem during send email")
        print(str(e))
    return False


def main():
    d = "G"
    myfunc(d)
    u = test('Rinaldo', 56, 'rickyd@gmail.com')
    u.printE("Renens")
    sendEmail()
    # send_email('rinaldo.dorigatti@gmail.com', 'Coucou maman', 'Mon amour de maman')


if __name__=='__main__':
    main()
