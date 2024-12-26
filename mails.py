import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


def send_email(user_email, user_password, smtp_server, smtp_port, recipient_email, data):
    
    try:
        message = MIMEMultipart()
        message['From'] = user_email
        message['To'] = recipient_email
        message['Subject'] = data.get('objet', 'Sans objet')

        message.attach(MIMEText(data.get('contenue', ''), 'plain'))

       
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(user_email, user_password)
            server.sendmail(user_email, recipient_email, message.as_string())
            print("E-mail envoyé avec succès !")

    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")

def handle_send_email(data):
    load_dotenv(dotenv_path=".env")
    admin_mail = os.getenv("SENDER_MAIL")
    admin_password = os.getenv("PASSWORD")
    recv_mail = os.getenv("RECV_MAIL")
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    send_email(admin_mail, admin_password, SMTP_SERVER, SMTP_PORT, recv_mail, data)