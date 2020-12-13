import smtplib #for sending emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add = '<enter your email>'
    to_add = '<enter designated email>'
    subject = "Finance Stock Report"

    msg = MIMEMultipart() #code block sets up objects for from,to and subject sections
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    body = "<b>Today's Finance Report is Attached.</b>"
    msg.attach(MIMEText(body,'html'))

    my_file = open(filename, 'rb')

    # code block attaches file
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename = ' + filename )
    msg.attach(part)


    message = msg.as_string()
    server = smtplib.SMTP('<enter gmail server',<enter server number>)
    server.starttls() # encryption
    server.login(<set up permissions within your gmail and put the password here>) # personal login info
    server.sendmail(from_add, to_add, message)
    server.quit();
