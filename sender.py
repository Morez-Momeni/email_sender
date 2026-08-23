import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rich.console import Console
from rich.table import Table
from config import sender_email,smtp_port,smtp_server,app_password

console = Console()

def add_email(email: str) -> bool:
    try:
        with open("emails.txt","a") as file:
            file.write(f"{email}\n")
        return True
    except Exception as e:
        print(f"Add error: {e}")
        return False

def send_email(receiver: str, subject: str, body: str) -> bool:
    with open("templates/otp.html","r") as file:
        html = file.read()
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email # type: ignore
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP(smtp_server, int(smtp_port)) as server: # type: ignore
            server.starttls()
            server.login(sender_email, app_password) # type: ignore
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

def send_group_email(subject: str, body: str):
    with open("emails.txt","r") as file:
        for email in file:
            reciver = email.strip()
            if reciver:
                send_email(reciver,subject,body)

def show_recivers_email():
    table = Table(title="EMAILS" , style="bright_blue")
    table.add_column("ID", style="red")
    table.add_column("Email", style="white")

    with open("emails.txt","r") as file:
        for id ,email in enumerate(file,start=1):
            reciver = email.strip()
            if reciver:
                table.add_row(str(id), email)
        console.print(table)