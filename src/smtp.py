import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from src.logger import logger

# TODO: https://github.com/google/gmail-oauth2-tools/wiki/OAuth2DotPyRunThrough

class smtp:
    def __init__(self, server, loginName, loginPassword):
        self._logger = logger()
        self._loginName = loginName
        self._message = MIMEMultipart()
        self._message['From'] = loginName
        self._message['Subject'] = ''
        self._message['To'] = ''
        self._logger.info('SMTP to server ' + server)
        self._server = smtplib.SMTP(server)
        self._server.ehlo()
        self._server.starttls()
        self._logger.info('Attempting loggin for user ' + loginName)
        self._server.login(loginName, loginPassword)
    
    def __del__(self):
        self._logger.info('Closing server')
        self._server.close()
    
    def setSubject(self, subject):
        self._logger.info('Setting mail subject to: ' + subject)
        self._message.replace_header('Subject', subject)
    
    def setBody(self, body):
        self._logger.info('Setting mail body to: ' + body)
        self._message.attach(MIMEText(body))

    def attachImage(self, filePath):
        self._logger.info('Adding image: ' + filePath)
        fileData = open(filePath, 'rb').read()
        image = MIMEImage(fileData, name = os.path.basename(filePath))
        self._message.attach(image)
        
    def cleanAttachments(self):
        self._message.set_payload([])

    def send(self, to):
        self._logger.info('Sending mail to: ' + str(to))
        self._message.replace_header('To', ','.join(to))
        self._server.sendmail(self._loginName, to, self._message.as_string())
