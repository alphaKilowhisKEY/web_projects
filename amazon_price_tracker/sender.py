import smtplib
from email.mime.text import MIMEText


def send_notification(subject, body, sender, recipients, password, link):
    new_body = body + " Check the link: " + link
    msg = MIMEText(new_body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("[+] Message was successfully sent.")    