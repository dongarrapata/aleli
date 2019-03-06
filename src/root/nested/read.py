'''
Created on Mar 6, 2019

@author: almanzor
'''
import imaplib
import email

m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
m.login("","")
m.select('"[Gmail]/All Mail"')

result, data = m.uid('search', None, "ALL") # search all email and return uids
if result == 'OK':
    for num in data[0].split():
        result, data = m.uid('fetch', num, '(RFC822)')
        if result == 'OK':
            email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
            print('From:' + email_message['From'])

m.close()
m.logout()