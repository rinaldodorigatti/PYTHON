import smtplib
import email.utils
from email.message import EmailMessage
import ssl

SENDER = 'diegogta5.dorigatti@gmail.com'
SENDERNAME = 'Diego Dorigatti'

RECIPIENT = 'rinaldo.dorigatti@gmail.com'

USERNAME_SMTP = 'rinaldo.dorigatti@gmail.com'

# PASSWORD_SMTP_FILE = 'pkdynxvsgjhzpojn'
password_smtp = 'pkdynxvsgjhzpojn'

HOST = "smtp.gmail.com"
PORT = 587

SUBJECT = 'Email Delivery Test (Python smtplib)'

BODY_TEXT = ("Email Delivery Test\r\n"
             "This email was sent through the Email Delivery SMTP "
             "Interface using the Python smtplib package."
            )

BODY_HTML = """<html>
<head></head>
<body>
  <h1>Email Delivery SMTP Email Test</h1>
  <p>This email was sent with Email Delivery using the
    <a href='https://www.python.org/'>Python</a>
    <a href='https://docs.python.org/3/library/smtplib.html'>
    smtplib</a> library.</p>
</body>
</html>"""

"""
with open(PASSWORD_SMTP_FILE) as f:
    password_smtp = f.readline().strip()"""

msg = EmailMessage()
msg['Subject'] = SUBJECT
msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
msg['To'] = RECIPIENT

msg.add_alternative(BODY_TEXT, subtype='text')
msg.add_alternative(BODY_HTML, subtype='html')

try:
    server = smtplib.SMTP(HOST, PORT)
    server.ehlo()
    server.starttls(context=ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None))
    server.ehlo()
    server.login(USERNAME_SMTP, password_smtp)
    server.sendmail(SENDER, RECIPIENT, msg.as_string())
    server.close()

except Exception as e:
    print(f"Error: {e}")
else:
    print("Email successfully sent!")
