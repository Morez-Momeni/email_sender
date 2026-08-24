import imaplib
from email import message_from_bytes
from email.header import decode_header
from config import sender_email , imap_server , app_password

def decode_text(value):
    if not value:
        return ""

    decoded = decode_header(value)
    result = ""

    for part, encoding in decoded:
        if isinstance(part, bytes):
            result += part.decode(encoding or "utf-8", errors="replace")
        else:
            result += part

    return result

def receive_last_email():

    mail = imaplib.IMAP4_SSL(imap_server) # type: ignore

    mail.login(sender_email, app_password) # type: ignore

    mail.select("INBOX")

    status, messages = mail.search(None, "UNSEEN")

    email_ids = messages[0].split()

    latest_email_id = email_ids[-1]
    status, data = mail.fetch(latest_email_id, "(RFC822)")

    message = message_from_bytes(data[0][1])  # type: ignore


    print("From:", decode_text(message["From"]))
    print("To:", decode_text(message["To"]))
    print("Subject:", decode_text(message["Subject"]))
    print("Date:", decode_text(message["Date"]))

    mail.close()
    mail.logout()