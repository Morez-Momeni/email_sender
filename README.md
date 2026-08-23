<div align="center">

# EMAIL SENDER

### A clean and powerful CLI-based email sending tool built with Python.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,25:0ea5e9,50:2563eb,75:4f46e5,100:020617&height=220&section=header&text=EMAIL%20SENDER&fontSize=55&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=CLI%20Email%20Automation%20Tool&descAlignY=60&descSize=18" width="100%"/>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-0ea5e9?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CLI-Argparse-2563eb?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Email-Automation-4f46e5?style=for-the-badge"/>
</p>

</div>

---

## About

**Email Sender** is a lightweight Python-based command-line email tool designed to make sending emails to individual or multiple recipients simple and manageable.

The project combines a clean email-sending core with a practical CLI interface, allowing recipients to be managed directly from the terminal.

The goal is simple:

> **Manage recipients. Prepare your message. Send.**

---

## Features

- Group email sending
- Recipient management
- Add new email addresses from the CLI
- Display saved recipients
- Edit recipient list directly with Nano
- Command-line interface powered by `argparse`
- Subject and message input from the terminal
- Separated email-sending logic
- Simple and lightweight project structure

---

## CLI

The application is controlled directly from the terminal.

### Send to a group

```bash
python main.py -g
```

The program asks for:

```text
Enter subject:
Enter body:
```

and sends the message to the saved recipients.

---

### Add a recipient

```bash
python main.py --add user@example.com
```

The email address is passed directly to the recipient manager.

The email value is required:

```bash
python main.py --add
```

will result in an `argparse` error because `--add` expects an email address.

---

### Show recipients

```bash
python main.py --show
```

Displays the currently saved recipient list.

---

### Edit recipients

```bash
python main.py --edit
```

Opens the recipient file using **Nano**:

```text
nano emails.txt
```

This makes it possible to manually manage the recipient list directly from the terminal.

---

## Command Overview

| Command | Description |
|---|---|
| `-g` | Send an email to the saved recipient group |
| `--add EMAIL` | Add an email address to the recipient list |
| `--show` | Show saved recipients |
| `--edit` | Open the recipient file with Nano |
| `--help` | Show CLI help |

---

## Project Structure

```text
email-sender/
│
├── main.py
├── sender.py
├── emails.txt
│
├── templates/
│   └── ...
│
├── logs/
│   └── ...
│
├── .env
├── requirements.txt
└── README.md
```

### `main.py`

The CLI entry point.

Responsible for parsing command-line arguments and deciding which operation should be executed.

### `sender.py`

Contains the core email functionality and recipient management logic.

### `emails.txt`

Stores the saved recipient addresses.

### `templates/`

Contains HTML email templates used by the project.

### `logs/`

Stores email-sending history and logs.

### `.env`

Contains sensitive configuration such as email credentials.

**Never commit `.env` to Git.**

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd email-sender
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create your environment configuration:

```bash
touch .env
```

Add your email configuration to `.env`.

---

## Usage

Start by checking the available commands:

```bash
python main.py --help
```

Example workflow:

```bash
python main.py --add user1@example.com
python main.py --add user2@example.com
python main.py --show
python main.py -g
```

Or manually edit the recipient list:

```bash
python main.py --edit
```

---

## CLI Philosophy

The project is intentionally built around the terminal.

Instead of creating a large graphical interface, the application keeps the workflow fast and simple:

```text
        ┌──────────────────┐
        │    main.py       │
        │   CLI Interface  │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │    argparse      │
        │ Command Parsing  │
        └────────┬─────────┘
                 │
       ┌─────────┼─────────┬──────────┐
       │         │         │          │
      -g        -s      --html    --show
       │         │         │          │
       ▼         ▼         ▼          ▼
    Group     Single    HTML      Show
     Send      Send      Send    Recipients
       │         │         │
       └─────────┼─────────┘
                 │
                 ▼
           Recipients
                 │
                 ▼
           Email SMTP
```

---

## Security

Sensitive credentials should never be hard-coded into the source code.

Use environment variables through `.env` instead.

Make sure `.env` is included in `.gitignore`:

```text
.env
```

---

## Roadmap

- [x] Basic email sending
- [x] Group email sending
- [x] Recipient storage
- [x] Add recipient from CLI
- [x] Show recipients
- [x] Edit recipients with Nano
- [x] CLI argument parsing
- [x] HTML email selection from CLI
- [ ] Attachment support
- [ ] Improved logging
- [ ] Scheduled sending


---

<div align="center">

### Built with Python

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,25:0ea5e9,50:2563eb,75:4f46e5,100:020617&height=120&section=footer&animation=twinkling" width="100%"/>

</div>