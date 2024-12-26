import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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