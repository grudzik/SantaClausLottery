import email
import json
import os
import smtplib
import sys
import time


class EMAIL_Handler:
    def __init__(self, settings_path=None):
        if settings_path == None:
            SCRIPT_DIR_NAME = os.path.dirname(sys.argv[0])
            settings_path = os.path.join(SCRIPT_DIR_NAME, 'email_settings.json')

        with open(settings_path) as f:
            self.CONFIG = json.load(f)

        self.login = self.CONFIG['login']
        self.password = self.CONFIG['password']
        self.sender_email = "{}@gmail.com".format(self.login)

        self.server = smtplib.SMTP('smtp.gmail.com', 587)

        self.is_started = False

        self.__login()

    def __login(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.login, self.password)
        time.sleep(1)
        self.is_started = True

    def form_simple_message(self, subject, content):
        msg = email.message.EmailMessage()
        msg['Subject'] = subject
        msg.set_content("""\
        {}
        """.format(content))

        return msg

    def send_simple_message(self, send_to, msg):
        if self.is_started:
            msg['From'] = self.sender_email
            msg['To'] = send_to
            self.server.send_message(msg)

    def send_email(self, me, you, msg):
        if self.is_started:
            self.server.sendmail(me, you, msg)


HANDLER = EMAIL_Handler()
