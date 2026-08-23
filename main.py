import subprocess
import argparse
from sender import send_group_email, show_recivers_email, add_email, send_email

parser = argparse.ArgumentParser(
    description="Command-line tool for managing and sending group emails"
)

parser.add_argument(
    "-g",
    action="store_true",
    help="Send a group email to all recipients listed in emails.txt (prompts for subject and body)"
)

parser.add_argument(
    "-s",
     action="store_true",
     help="send single email"
     )

parser.add_argument(
    "--show",
    action="store_true",
    help="Display all email addresses stored in emails.txt"
)

parser.add_argument(
    "--edit",
    action="store_true",
    help="Edit emails.txt manually using the nano editor (add/remove addresses)"
)

parser.add_argument(
    "--add",
    metavar="EMAIL",
    help="Add a new email address to the end of emails.txt (e.g., --add user@example.com)"
)


args = parser.parse_args()

if args.g:
    subject = input("Enter subject: ").strip()
    body = input("Enter body: ").strip()
    send_group_email(subject, body)

if args.show:
    show_recivers_email()

if args.add:
    add_email(args.add)

if args.edit:
    subprocess.run(["nano", "emails.txt"])

if args.s:
    reciver = input("Enter Email:").strip()
    subject = input("Enter subject: ").strip()
    body = input("Enter body: ").strip()
    send_email(reciver,subject,body)