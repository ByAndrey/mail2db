from imap_tools import MailBox
import configparser
import html2text
import pymysql

config = configparser.ConfigParser()
config.readfp(open(r'mail2db.cfg'))

server = config.get('mail1', 'server')
user = config.get('mail1', 'user')
password = config.get('mail1', 'password')

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True

with MailBox(server).login(user, password) as mailbox:
    for msg in mailbox.fetch() :
        uid = msg.uid
        from_ = msg.from_
        subject = msg.subject
        text = msg.text
        if not text:
            text = h.handle(msg.html)
        print ("UID: %s; FROM: %s; SUBJECT: %s"%(uid,from_,subject))
        print ('BODY :%s'%(text))