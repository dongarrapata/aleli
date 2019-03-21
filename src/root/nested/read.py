'''
Created on Mar 6, 2019

@author: almanzor
'''
import imaplib
import email

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
m.login("correodietas@gmail.com","dietas1234")
m.select('"[Gmail]/All Mail"')

result, data = m.uid('search', None, "ALL") # search all email and return uids
if result == 'OK':
    for num in data[0].split():
        result, data = m.uid('fetch', num, '(RFC822)')
        if result == 'OK':
            email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
            print('From:' + email_message['From'])
            print(get_body(email_message))

m.search(None,'(FROM "msarmientonavarro@gmail.com")')

#===============================================================================
# m.close()
# m.logout()
#===============================================================================

'''
scacA
'''