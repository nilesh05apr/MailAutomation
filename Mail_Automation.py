import smtplib,ssl
from email.message import EmailMessage
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

user = '<Sender\'s Email>'
pas = '<Sender\'s Password>' 
msg = []
for i in range(1000):
	with open("text.txt") as fp:
		msg.append(EmailMessage())
		msg[-1].set_content(fp.read())
		msg[-1]['subject'] = "#Subject of mail"
		msg[-1]['from'] = '<Senders mail>'
		msg[-1]['to'] = '<Receivers Email>'



for i in range(1000):
	s = smtplib.SMTP(host='smtp.gmail.com',port=587)
	s.ehlo()
	s.starttls(context=ssl.create_default_context())
	s.login(user=user,password=pas)
	s.send_message(msg[i])
	s.quit()