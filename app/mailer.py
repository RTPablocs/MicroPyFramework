import smtplib
from email.mime.text import MIMEText


class MailSender:

    def __init__(self):
        self.mail_server = ''
        self.port = 25
        self.mail_sender = ''

    def send_mail(self, user_mail, msg):
        server = smtplib.SMTP(self.mail_server, self.port)
        try:
            server.sendmail(self.mail_sender, user_mail, msg.as_string())
        finally:
            server.quit()

    def send_welcome(self, user_mail):
        msg = MIMEText('Welcome to app')
        msg['To'] = user_mail
        msg['From'] = self.mail_sender
        msg['Subject'] = 'Welcome to our app'

        self.send_mail(user_mail, msg)
        return {'code': '200 OK', 'action': 'Email sent'}
