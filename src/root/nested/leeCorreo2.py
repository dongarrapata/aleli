'''
Created on Mar 21, 2019

@author: almanzor
'''
import imaplib, email, json

with open('config.json', 'r') as f:
    config = json.load(f)

correo = config['GMAIL']['EMAIL'] # correo gmail
contrasena = config['GMAIL']['PASSWORD'] # contrasena gmail

m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
m.login(correo, contrasena)
m.select('"[Gmail]/All Mail"')

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

result, data = m.uid('search', None, "ALL")
if result == 'OK':
    for num in data[0].split():
        result, data = m.uid('fetch', num, '(RFC822)')
        if result == 'OK':
            email_message = email.message_from_bytes(data[0][1])
            print(get_body(email_message))
            print('From: ' + email_message['From'])
            
m.close()
m.logout()