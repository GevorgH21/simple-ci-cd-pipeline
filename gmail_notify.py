import os
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(f"GitHub Actions CI/CD Job finished with status: {os.getenv('JOB_STATUS')}")
msg['Subject'] = 'CI/CD Pipeline Notification'
msg['From'] = os.getenv("GMAIL_USER")
msg['To'] = os.getenv("GMAIL_USER")  # You can change this if needed

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASS"))
    smtp.send_message(msg)

