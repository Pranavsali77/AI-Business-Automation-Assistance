import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# =========================================
# EMAIL NOTIFICATION FUNCTION
# =========================================

def send_notification(name, email):

    try:

        sender_email = os.getenv("EMAIL_ADDRESS")

        sender_password = os.getenv("EMAIL_PASSWORD")

        admin_email = os.getenv("EMAIL_ADDRESS")

        # =====================================
        # EMAIL TO USER
        # =====================================

        subject_user = "Thank You for Contacting Us"

        body_user = f"""
Hello {name},

Thank you for contacting our AI-Powered Business Automation Assistant.

We have received your inquiry successfully.

Our team will connect with you shortly.

Regards,
AI Business Automation Team
"""

        msg_user = MIMEMultipart()

        msg_user["From"] = sender_email

        msg_user["To"] = email

        msg_user["Subject"] = subject_user

        msg_user.attach(MIMEText(body_user, "plain"))

        # =====================================
        # EMAIL TO ADMIN
        # =====================================

        subject_admin = "New Lead Captured"

        body_admin = f"""
New lead received.

Name: {name}
Email: {email}

Please check the admin dashboard.
"""

        msg_admin = MIMEMultipart()

        msg_admin["From"] = sender_email

        msg_admin["To"] = admin_email

        msg_admin["Subject"] = subject_admin

        msg_admin.attach(MIMEText(body_admin, "plain"))

        # =====================================
        # SMTP SERVER
        # =====================================

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, sender_password)

        # Send Emails
        server.send_message(msg_user)

        server.send_message(msg_admin)

        server.quit()

        print("Emails sent successfully!")

    except Exception as e:

        print(f"Email Error: {str(e)}")