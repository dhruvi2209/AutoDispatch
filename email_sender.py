import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"


current_dir = Path(__file__).resolve(
).parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)


sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")



def send_email(subject, receiver_email, name, due_date, invoice_no, amount):

   
    email= EmailMessage()
    email['Subject'] = subject
    email['From'] = formataddr(("Testing Email.", f"{sender_email}"))
    email['To'] = receiver_email
    email['BCC'] = sender_email

    email.set_content(
        f"""\
        Hello {name},

        I trust this message finds you in good spirits. I'm reaching out to gently remind you that the payment of {amount} Rs for our invoice {invoice_no} is scheduled for {due_date}. I would greatly appreciate it if you could confirm that everything is progressing smoothly for the payment.

        Best regards,
        Dhruvi
        """
    )

    #alternative = HTML version
    email.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hello {name},</p>
        <p>I trust this message finds you in good spirits.</p>
        <p>I'm reaching out to gently remind you that the payment of <strong>{amount} Rs</strong> for our invoice {invoice_no} is scheduled for <strong> {due_date} </strong>.</p>
        <p>I would greatly appreciate it if you could confirm that everything is progressing smoothly for the payment.</p>
        <p>Best regards,</p>
        <p>Dhruvi</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email,password_email)
        server.send_message(email,receiver_email)


if __name__=="__main__":
    send_email(
        subject="<REPLACE>",
        name="<REPLACE>",
        receiver_email="<REPLACE>",
        due_date="11, Dec 2023",
        invoice_no="INV-21-12-009",
        amount="5"
    )



