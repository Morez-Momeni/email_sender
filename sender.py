import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from rich.console import Console
from rich.table import Table

from config import sender_email, smtp_port, smtp_server, app_password


console = Console()


def add_email(email: str) -> bool:
    try:
        with open("emails.txt", "a") as file:
            file.write(f"{email}\n")

        return True

    except Exception as e:
        print(f"Add error: {e}")
        return False


def add_attachment(msg, file_path: str) -> bool:
    try:
        with open(file_path, "rb") as file:
            data = file.read()

        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(data)

        encoders.encode_base64(attachment)

        filename = os.path.basename(file_path)

        attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=filename
        )

        msg.attach(attachment)

        return True

    except Exception as e:
        print(f"Attachment error: {e}")
        return False


def send_email(
    receiver: str,
    subject: str,
    body: str,
    attachment: str | None = None
) -> bool:

    try:
        msg = MIMEMultipart()

        msg["From"] = sender_email  # type: ignore
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        if attachment:
            if not add_attachment(msg, attachment):
                return False

        with smtplib.SMTP(
            smtp_server, # type: ignore
            int(smtp_port) # type: ignore
        ) as server:  

            server.starttls()

            server.login(
                sender_email, # type: ignore
                app_password # type: ignore
            )  # type: ignore

            server.send_message(msg)

        return True

    except Exception as e:
        print(f"Email error: {e}")
        return False


def send_group_email(
    subject: str,
    body: str,
    attachment: str | None = None
):
    with open("emails.txt", "r") as file:

        for email in file:
            receiver = email.strip()

            if receiver:
                send_email(
                    receiver,
                    subject,
                    body,
                    attachment
                )


def send_html_email(
    receiver: str,
    subject: str,
    body: str,
    html: str,
    attachment: str | None = None
) -> bool:

    try:
        with open(html, "r") as file:
            template = file.read()

        msg = MIMEMultipart()

        msg["From"] = sender_email  # type: ignore
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))
        msg.attach(MIMEText(template, "html"))

        if attachment:
            if not add_attachment(msg, attachment):
                return False

        with smtplib.SMTP(
            smtp_server,  # type: ignore
            int(smtp_port) # type: ignore
        ) as server:  # type: ignore

            server.starttls()

            server.login(
                sender_email, # type: ignore
                app_password # type: ignore
            )  # type: ignore 

            server.send_message(msg)

        return True

    except Exception as e:
        print(f"Email error: {e}")
        return False


def send_group_html_email(
    subject: str,
    body: str,
    html: str,
    attachment: str | None = None
):
    with open("emails.txt", "r") as file:

        for email in file:
            receiver = email.strip()

            if receiver:
                send_html_email(
                    receiver,
                    subject,
                    body,
                    html,
                    attachment
                )


def show_recivers_email():
    table = Table(
        title="EMAILS",
        style="bright_blue"
    )

    table.add_column("ID", style="red")
    table.add_column("Email", style="white")

    with open("emails.txt", "r") as file:

        for id, email in enumerate(file, start=1):
            receiver = email.strip()

            if receiver:
                table.add_row(
                    str(id),
                    receiver
                )

    console.print(table)