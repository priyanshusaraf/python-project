import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()
server.login('SENDERS EMAIL ID', 'SENDERS PASSWORD')
msg = MIMEMultipart()
msg['from'] = 'SENDERS EMAIL ID '
msg['to'] = 'RECIEVERS EMAIL ID' 
msg['subject'] ="heyyyy you! hows life!!!"
with open("message.txt", "r") as f:
    message = f.read()
msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
server.sendmail('SENDERS EMAIL', 'RECIEVERS EMAIL ID', text)
