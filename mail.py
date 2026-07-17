import os

class Config():
    # ...

  # Flask-Mail Konfiguration: Zugangsdaten für den SMTP-Server, über den die App Mails verschickt
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 ## Standard-Port für TLS-verschlüsselte SMTP-Verbindungen
    MAIL_USE_TLS = True # Standard-Port für TLS-verschlüsselte SMTP-Verbindungen

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # Benutzername für den SMTP-Server, in diesem Fall die E-Mail-Adresse des 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # Passwort für den SMTP-Server, in diesem Fall das App-Passwort für die E-Mail-Adresse
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
