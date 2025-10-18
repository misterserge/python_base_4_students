from email.message import EmailMessage
from smtplib import SMTP
from string import Template
from pathlib import Path

template = Template(Path('template.html').read_text())
content = template.substitute(username='John')
message = EmailMessage()
message['Subject'] = 'Test Email'
message['From'] = 'test@test.com'
message['To'] = 'test@test.com'
message.set_content(content, subtype='html')
message.add_attachment(open('test.txt', 'rb').read(), maintype='text', subtype='plain', filename='test.txt')


with SMTP(host='192.168.1.100', port=1025) as server:
    server.ehlo()
    server.starttls()
    # server.login('test@test.com', 'test')
    server.send_message(message)

print('Email sent successfully')