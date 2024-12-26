import os
from dotenv import load_dotenv
from mails import send_email

load_dotenv()

admin_mail = os.getenv("SENDER_MAIL")
admin_password = os.getenv("PASSWORD")
recv_mail = os.getenv("RECV_MAIL")
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587

data = {
    "objet" : "test market app",
    "contenue" : "lorammmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
}

send_email(admin_mail, admin_password, SMTP_SERVER, SMTP_PORT, recv_mail, data)
