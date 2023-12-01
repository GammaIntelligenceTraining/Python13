import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
# port = 587
smtp_server = "smtp.zone.eu"
login = "python-learning@mrartful.com"
password = "**********"

reciever_email = "roman.kutselepa@gmail.com"
message = MIMEMultipart()
message['Subject'] = 'Test email!'
message['From'] = 'Roman <' + login + '>'
message['To'] = reciever_email

text = 'Hello, this message was sent with python script'
html = """
<h2>This is a test email</h2>
<p style="color: dodgerblue;">If you see this it means all good!</p>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
# try:
#     server = smtplib.SMTP(smtp_server, port)
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(login, password)
# except Exception as e:
#     print(e)


with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(login, reciever_email, message.as_string())