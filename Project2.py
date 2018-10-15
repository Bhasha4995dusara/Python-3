'''Extract all the Messages with logging Level as CRITICAL and ERROR from error_log.txt log file.
Use SMTP Module to send the information to the user as an attachment and
Get the Count of all the Logging level Messages and ' that information in the body of the message.
Take the input "File Path" and email-id from the user using command-line using argparse Module.'''

import argparse
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

parser = argparse.ArgumentParser()
parser.add_argument('filepath',help="file name from user")
parser.add_argument('email_id',help="Email-id from user")
args = parser.parse_args()
if args :

    logging.basicConfig(filename=args.filepath,level=logging.ERROR)
    logger =logging.getLogger('error_log')
    logger.setLevel(logging.WARNING)

    ch = logging.StreamHandler()
    #ch.setLevel(logging.WARNING)
    for i in ch.setLevel(logging.WARNING):
        print(i)
    #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    #ch.setFormatter(formatter)


    #logger.addHandler(ch)



























'''frommail = "bhasha.dusara@gmail.com"
tomail = "bhasha.dusara@gmail.com"
msg = MIMEMultipart()
msg['From'] = frommail
msg['To'] = tomail
msg['Subject'] = "sample mail"
body = "Body of the mail"
msg.attach(MIMEText(body,'plain'))
filename = 'error_log.txt'
attach = open("C:\\Users\\Bhasha\\PycharmProjects\\Assignments\\error_log.txt",'rb')
p = MIMEBase('application','octet-stream')
p.set_payload((attach).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('bhasha.dusara@gmail.com','computer#engineering1')
text = msg.as_string()
s.sendmail(frommail,tomail,text)
s.quit()'''

