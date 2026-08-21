import os
from dotenv import load_dotenv


sender_email =  None
app_password = None
smtp_server = None
smtp_port = None

if load_dotenv() == False:
    print(".env file not found")

else:
    sender_email = os.getenv('SENDER_EMAIL')
    app_password = os.getenv('APP_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

if __name__ == "__main__":
    print(f"Sender_email: {sender_email}\nApp_password: {app_password}\nSmtp_server: {smtp_server}\nSmtp_port: {smtp_port}")

