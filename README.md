# 📧 Email Sender

A professional email sending tool with support for:
- Multiple recipients
- File attachments
- HTML templates
- Logging
- Scheduled sending

## Project Structure
- `main.py` – CLI entry point
- `config.py` – Loads environment variables
- `sender.py` – Core email sending logic
- `templates/` – HTML email templates
- `logs/` – Sending history logs
- `.env` – Sensitive configuration

## How to Use
1. Fill `.env` with your credentials.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py --help`
