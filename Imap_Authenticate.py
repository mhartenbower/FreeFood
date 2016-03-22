import imaplib, getpass, sys

class Authenticate:

    def __init__(self):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")

    def authenticate(self):
        username = raw_input("Enter your email address: ")
        password = getpass.getpass()
        try:
            typ, data = self.imap.login(username, password)
            return self.imap
        except imaplib.IMAP4.error:
            print "Authentication failed. Ensure IMAP is enabled for your email account and that your credentials are correct."
            sys.exit(1)
