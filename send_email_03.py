import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import shutil


def send_mail(send_from: str="rinaldo.dorigatti@gmail.com", send_to: str="rinaldo.dorigatti@gmail.com",
    subject: str="test 1", text: str="test 1", server="smtp.gmail.com"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg_html = MIMEText(text, 'html')

    email_address = "rinaldo.dorigatti@gmail.com"
    email_password = "pkdynxvsgjhzpojn"

    filessrc = '/var/log/alternatives.log'
    filedest = '/home/rickyd/Téléchargements/PYHONCOURS/alternatives.log'
    files = ['alternatives.log']
    shutil.copyfile(filessrc, filedest)

    # msg.attach(MIMEText(text))
    msg.attach(msg_html)

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    try:
        smtp = smtplib.SMTP(server, 587)
        smtp.starttls()
        smtp.login(email_address, email_password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
        print("The email was sent to : ", end='')
        for o in send_to:
            print(o)
    except Exception as err:
        print("An error occured : ", err)



if __name__=='__main__':

    message = """<html>
    <head></head>
    <body>
      <h3>Bonjour Rinaldo,</h3>
      <p>Cet email à été envoyé directement par un script python<br><br>
        <a href='https://saravoyance.herokuapp.com/'><b>Mon site Pizza</b></a><br>
        </p><br>
        <p>Je me permet de vous contacter pour les raisons suivantes : <br>
        <ul>
          <li>La pizza commandée est en cours de livraison</li>
          <li>Le log des alternatives est en pièce jointe</li>
          <li>Me renvoyer le résultat dès analyses terminées</li>
        </ul><br>
        En vous remerçiant par avance, veuillez recevoir,<br>
        mes meilleures salutations.<br><br>
        <table border=0>
            <tr>
               <td style="width:100px; text-align:right;">Name : </td>
               <td style="padding-left: 6px;">Rinaldo Dorigatti</td>
           </tr>
           <tr>
               <td style="width:100px; text-align:right;">Address : </td>
               <td style="padding-left: 6px;">Chemin de la Prairie 61</td>
           </tr>
           <tr>
               <td style="width:100px; text-align:right;">Mobile : </td>
               <td style="padding-left: 6px;">+41 79 480 62 39</td>
           </tr>
           <tr>
               <td style="width:100px; text-align:right;">Email : </td>
               <td style="padding-left: 6px;">rinaldo.dorigatti@gmail.com</td>
           </tr>
       </table>
       </p>
    </body>
    </html>"""

    send_mail('diegogta5.dorigatti@gmail.com', ['rinaldo.dorigatti@gmail.com'],
    'Log alternatives log', message, "smtp.gmail.com")
