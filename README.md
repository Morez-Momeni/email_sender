\<div *align*="center">

**# EMAIL SENDER**

**### A clean and powerful CLI-based email automation tool built with Python.**

\<img src="https\://capsule-render.vercel.app/api?type=waving&color=0:020617,25:0ea5e9,50:2563eb,75:4f46e5,100:020617&height=220&section=header&text=EMAIL%20SENDER&fontSize=55&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=CLI%20Email%20Automation%20Tool&descAlignY=60&descSize=18" width="100%"/>

\<p>

  \<img src="https\://img.shields.io/badge/Python-3.x-0ea5e9?style=for-the-badge&logo=python&logoColor=white"/>

  \<img src="https\://img.shields.io/badge/CLI-Argparse-2563eb?style=for-the-badge"/>

  \<img src="https\://img.shields.io/badge/SMTP-Email-4f46e5?style=for-the-badge"/>

  \<img src="https\://img.shields.io/badge/IMAP-Receiving-6366f1?style=for-the-badge"/>

\</p>

\</div>

**---**

**## About**

**\*\*Email Sender\*\*** is a lightweight Python-based command-line email automation tool designed to make sending and receiving emails directly from the terminal simple and manageable.

The project provides a CLI interface for sending emails to individual recipients or groups, selecting HTML templates, managing recipients, and fetching received emails through IMAP.

The goal is simple:

\> **\*\*Manage recipients. Prepare your message. Send. Receive.\*\***

**---**

**## Features**

\* Individual email sending

\* Group email sending

\* HTML email sending

\* Recipient management

\* Add new email addresses from the CLI

\* Display saved recipients

\* Edit recipient list directly with Nano

\* Fetch received emails using IMAP

\* Display the latest received emails

\* Command-line interface powered by \`argparse\`

\* Subject and message input directly from the terminal
* Optional file attachments for single, group, and HTML emails

\* Separated email-sending logic

\* SMTP support for sending emails

\* IMAP support for receiving emails

\* Simple and lightweight project structure

**---**

**## CLI**

The application is controlled entirely from the terminal using \`argparse\`.

**### Send to a group**

\`\`\`bash

python main.py -g

\`\`\`

The program asks for:

\`\`\`text

Enter subject:

Enter body:

\`\`\`

The message is then sent to all saved recipients. An attachment can optionally be provided by entering its file path; pressing Enter skips the attachment.

**---**

**### Send to a single recipient**

\`\`\`bash

python main.py -s

\`\`\`

The program handles the single-recipient sending workflow from the terminal. It also asks for an optional attachment path.

**---**

**### Send an HTML email**

\`\`\`bash

python main.py --html

\`\`\`

This mode allows an HTML template to be selected and sent as an HTML email. An optional file attachment can also be added.

HTML templates are stored inside:

\`\`\`text

templates/

\`\`\`

**---**

**### Receive emails**

\`\`\`bash

python main.py --recieve

\`\`\`

This connects to the mail server using **\*\*IMAP\*\*** and fetches received emails.

The receiver can be used to inspect the latest messages directly from the terminal.

Example:

\`\`\`text

Subject: Hello

From: user\@example.com

Message body...

\`\`\`

**---**

**### Add a recipient**

\`\`\`bash

python main.py --add user\@example.com

\`\`\`

The email address is passed directly to the recipient manager.

The email value is required:

\`\`\`bash

python main.py --add

\`\`\`

will result in an \`argparse\` error because \`--add\` expects an email address.

**---**

**### Show recipients**

\`\`\`bash

python main.py --show

\`\`\`

Displays the currently saved recipient list.

**---**

**### Edit recipients**

\`\`\`bash

python main.py --edit

\`\`\`

Opens the recipient file using **\*\*Nano\*\***:

\`\`\`text

nano emails.txt

\`\`\`

This makes it possible to manually manage the recipient list directly from the terminal.

**---**

**## Command Overview**

\| Command       | Description                                  |

\| ------------- | -------------------------------------------- |

\| \`-g\`          | Send an email to the saved recipient group   |

\| \`-s\`          | Send an email to a single recipient          |

\| \`--html\`      | Send an HTML email using a template          |

\| \`--recieve\`   | Fetch and display received emails using IMAP |

\| \`--add EMAIL\` | Add an email address to the recipient list   |

\| \`--show\`      | Show saved recipients                        |

\| \`--edit\`      | Open the recipient file with Nano            |

\| \`--help\`      | Show CLI help                                |

**---**

**## Architecture**

The application follows a simple command-line architecture.

\`\`\`text

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

       ┌─────────┼─────────┬──────────┬──────────────┐

       │         │         │          │              │

      -g        -s      --html   --recieve      --show

       │         │         │          │              │

       ▼         ▼         ▼          ▼              ▼

    Group     Single    HTML      Inbox        Show

     Send      Send      Send     Fetcher    Recipients

       │         │         │          │

       └─────────┼─────────┘          │

                 │                    │

                 ▼                    ▼

           Recipients            Latest emails

                 │

                 ▼

           Email SMTP

\`\`\`

The main entry point receives the command, \`argparse\` determines the requested operation, and the appropriate part of the application handles the task.

Sending operations use **\*\*SMTP\*\***, while receiving operations use **\*\*IMAP\*\***.

**---**

**## Email Flow**

**### Sending**

\`\`\`text

CLI Command

     │

     ▼

  argparse

     │

     ▼

Recipient Manager

     │

     ▼

Message Builder

     │

     ▼

    SMTP

     │

     ▼

Recipient

\`\`\`

**### Receiving**

\`\`\`text

CLI Command

     │

     ▼

  argparse

     │

     ▼

   IMAP

     │

     ▼

 Mailbox

     │

     ▼

Latest Emails

     │

     ▼

Terminal

\`\`\`

**---**

**## Project Structure**

\`\`\`text

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

├── .gitignore

├── requirements.txt

└── README.md

\`\`\`

**### \`main.py\`**

The CLI entry point.

Responsible for parsing command-line arguments and deciding which operation should be executed.

**### \`sender.py\`**

Contains the core email functionality, sending logic, and recipient management.

**### \`emails.txt\`**

Stores the saved recipient addresses.

**### \`templates/\`**

Contains HTML email templates used by the project.

**### \`logs/\`**

Stores email-sending history and application logs.

**### \`.env\`**

Contains sensitive configuration such as email credentials.

**\*\*Never commit \`.env\` to Git.\*\***

**---**

**## Installation**

Clone the repository:

\`\`\`bash

git clone \<repository-url>

cd email-sender

\`\`\`

Install the dependencies:

\`\`\`bash

pip install -r requirements.txt

\`\`\`

Create your environment configuration:

\`\`\`bash

touch .env

\`\`\`

Add your email configuration to \`.env\`.

Example:

\`\`\`text

EMAIL=your\_email\@example.com

PASSWORD=your\_app\_password

\`\`\`

Make sure the environment file is ignored by Git.

**---**

**## Usage**

Start by checking the available commands:

\`\`\`bash

python main.py --help

\`\`\`

**### Example sending workflow**

\`\`\`bash

python main.py --add user1\@example.com

python main.py --add user2\@example.com

python main.py --show

python main.py -g

\`\`\`

**### Single email workflow**

\`\`\`bash

python main.py -s

\`\`\`

**### HTML email workflow**

\`\`\`bash

python main.py --html

\`\`\`

**### Receive emails**

\`\`\`bash

python main.py --recieve

\`\`\`

**### Manage recipients**

\`\`\`bash

python main.py --show

\`\`\`

\`\`\`bash

python main.py --edit

\`\`\`

**---**

**## SMTP & IMAP**

The project uses two different email protocols for its main operations.

**### SMTP**

**\*\*SMTP (Simple Mail Transfer Protocol)\*\*** is used for sending emails.

\`\`\`text

Application

     │

     ▼

   SMTP

     │

     ▼

Mail Server

     │

     ▼

Recipient

\`\`\`

**### IMAP**

**\*\*IMAP (Internet Message Access Protocol)\*\*** is used for accessing received emails.

\`\`\`text

Mail Server

     │

     ▼

   IMAP

     │

     ▼

Application

     │

     ▼

Terminal

\`\`\`

Using both protocols allows the application to work as both an email sender and a basic terminal-based email receiver.

**---**

**## CLI Philosophy**

The project is intentionally built around the terminal.

Instead of creating a large graphical interface, the application keeps the workflow fast, simple, and scriptable.

The user interacts with the application through commands:

\`\`\`text

-g

    Group Send

-s

    Single Send

\--html

    HTML Send

\--recieve

    Inbox Fetcher

\--add EMAIL

    Add Recipient

\--show

    Show Recipients

\--edit

    Edit Recipients

\`\`\`

Each command maps to a specific part of the email workflow while keeping the application lightweight.

**---**

**## Security**

Sensitive credentials should never be hard-coded into the source code.

Use environment variables through \`.env\` instead.

Make sure \`.env\` is included in \`.gitignore\`:

\`\`\`text

.env

\`\`\`

If you are using Gmail, use an **\*\*App Password\*\*** rather than your normal account password when required.

Never commit credentials, API keys, or app passwords to Git.

**---**

**## Roadmap**

\* [x] Basic email sending

\* [x] Single email sending

\* [x] Group email sending

\* [x] Recipient storage

\* [x] Add recipient from CLI

\* [x] Show recipients

\* [x] Edit recipients with Nano

\* [x] CLI argument parsing

\* [x] HTML email selection from CLI

\* [x] SMTP email sending

\* [x] IMAP email receiving

\* [x] Fetch and display latest received emails

\* [x] Attachment support

**---**

\<div *align*="center">

**### Built with Python**

\<img src="https\://capsule-render.vercel.app/api?type=waving&color=0:020617,25:0ea5e9,50:2563eb,75:4f46e5,100:020617&height=120&section=footer&animation=twinkling" width="100%"/>

\</div>