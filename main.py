import os
import subprocess
import argparse

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from sender import (
    send_group_email,
    show_recivers_email,
    add_email,
    send_email,
    send_group_html_email
)

from receiver import receive_last_email


console = Console()


parser = argparse.ArgumentParser(
    description="Command-line tool for managing and sending group emails"
)


parser.add_argument(
    "-g",
    action="store_true",
    help="Send a group email to all recipients listed in emails.txt"
)


parser.add_argument(
    "-s",
    action="store_true",
    help="Send single email"
)


parser.add_argument(
    "--show",
    action="store_true",
    help="Display all email addresses stored in emails.txt"
)


parser.add_argument(
    "--edit",
    action="store_true",
    help="Edit emails.txt manually using the nano editor"
)


parser.add_argument(
    "--add",
    metavar="EMAIL",
    help="Add a new email address to emails.txt"
)


parser.add_argument(
    "--html",
    action="store_true",
    help="Send group email with HTML template"
)


parser.add_argument(
    "--recieve",
    action="store_true",
    help="Receive your last email"
)


args = parser.parse_args()


if args.g:
    console.print(
        Panel.fit(
            "SEND GROUP EMAIL",
            style="bold red"
        )
    )

    subject = Prompt.ask("Enter subject")
    body = Prompt.ask("Enter body")

    attachment = Prompt.ask(
        "Attachment path (optional)",
        default=""
    )

    if attachment == "":
        attachment = None

    send_group_email(
        subject,
        body,
        attachment
    )


if args.show:
    show_recivers_email()


if args.add:
    add_email(args.add)


if args.edit:
    subprocess.run(["nano", "emails.txt"])


if args.s:
    console.print(
        Panel.fit(
            "SEND SINGLE EMAIL",
            style="bold cyan"
        )
    )

    receiver = Prompt.ask("Enter Email")
    subject = Prompt.ask("Enter subject")
    body = Prompt.ask("Enter body")

    attachment = Prompt.ask(
        "Attachment path (optional)",
        default=""
    )

    if attachment == "":
        attachment = None

    send_email(
        receiver,
        subject,
        body,
        attachment
    )


if args.html:
    console.print(
        Panel.fit(
            "SEND GROUP HTML EMAIL",
            style="bold green"
        )
    )

    path = "/home/morez/Projects/email_sender/templates/"
    templates = os.listdir(path)

    subject = Prompt.ask("Enter subject")
    body = Prompt.ask("Enter body")

    table = Table(
        title="TEMPLATES",
        style="blue"
    )

    table.add_column("ID", style="red")
    table.add_column("TEMPLATE", style="green")

    for id, temp in enumerate(templates, start=1):
        table.add_row(
            str(id),
            temp
        )

    console.print(table)

    html = Prompt.ask("Choose your template")

    html_path = os.path.join(
        path,
        html
    )

    attachment = Prompt.ask(
        "Attachment path (optional)",
        default=""
    )

    if attachment == "":
        attachment = None

    send_group_html_email(
        subject,
        body,
        html_path,
        attachment
    )


if args.recieve:
    receive_last_email()

