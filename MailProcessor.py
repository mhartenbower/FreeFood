import imaplib, email, Imap_Authenticate

class MailProcessor:

    def __init__(self):
        pass

    def setFolder(self, imap):
        imap.select('inbox')

    def extractText(self, email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                    emailString = emailString + part.get_payload()
            return emailString
        elif maintype == 'text':
            return email_message_instance.get_payload()

    def getLatestEmail(self, imap):
        result, data = imap.uid('search', None, 'ALL')
        latest_email_uid = data[0].split()[-1]
        result, data = imap.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        return self.extractText(email_message)

def main():
    authenticate = Imap_Authenticate.Authenticate()
    imap = authenticate.authenticate()
    mail = MailProcessor()
    mail.setFolder(imap)
    latestEmail = mail.getLatestEmail(imap)
    print latestEmail

if __name__ == "__main__":
    main()
