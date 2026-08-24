import os
from dotenv import load_dotenv


sender_email =  None
app_password = None
smtp_server = None
smtp_port = None
imap_server = None


if load_dotenv() == False:
    print(".env file not found")

else:
    sender_email = os.getenv('SENDER_EMAIL')
    app_password = os.getenv('APP_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    imap_server = os.getenv('IMAP_SERVER')
if __name__ == "__main__":
    print(f"Sender_email: {sender_email}\nApp_password: {app_password}\nSmtp_server: {smtp_server}\nSmtp_port: {smtp_port}\n Imap_server: {imap_server}")

