import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(post, topic):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_APP_PASSWORD")

    receiver = sender

    msg = MIMEMultipart("alternative")

    msg["Subject"] = f"LinkedIn Post - {topic}"
    msg["From"] = sender
    msg["To"] = receiver

    hashtags = " ".join(post["hashtags"])

    html = f"""
    <html>
    <body style="font-family:Arial">

    <h2>{post['title']}</h2>

    <h3>Topic</h3>
    <p>{topic}</p>

    <h3>Hook</h3>
    <p>{post['hook']}</p>

    <h3>Body</h3>
    <p>{post['body']}</p>

    <h3>CTA</h3>
    <p>{post['cta']}</p>

    <h3>Hashtags</h3>
    <p>{hashtags}</p>

    <h3>Image Prompt</h3>
    <p>{post['image_prompt']}</p>

    </body>
    </html>
    """

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

    print("✅ Email sent.")