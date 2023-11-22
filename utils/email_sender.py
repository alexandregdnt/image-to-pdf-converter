import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def send_email_with_pdf(recipient_email, pdf_filename):
    print("Envoi d'un email à", recipient_email)
    print("EMAIL_HOST:", os.getenv('EMAIL_HOST'))
    print("EMAIL_PORT:", os.getenv('EMAIL_PORT'))
    print("EMAIL_USER:", os.getenv('EMAIL_USER'))

    msg = EmailMessage()
    msg['Subject'] = 'Votre PDF Converti'
    msg['From'] = os.getenv('EMAIL_USER')
    msg['To'] = recipient_email
    msg.set_content('Veuillez trouver ci-joint le PDF converti.')

    with open(pdf_filename, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=pdf_filename)

    # try:
        with smtplib.SMTP(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as smtp:
            smtp.starttls()  # Ajouter cette ligne si vous voulez quand même utiliser TLS
            smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            smtp.send_message(msg)
    # except Exception as e:
    #     print("Erreur lors de l'envoi de l'email:", e)
