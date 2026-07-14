import json
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

    linkedin_post = f"""
🚀 {post['hook']}

{post['body']}

{post['cta']}

{hashtags}
"""

    image_specification = json.dumps(
        post["image_specification"],
        indent=4
    )

    html = f"""
    <html>
    <body style="font-family:Arial; line-height:1.6; max-width:800px; margin:auto;">

    <h2>📌 Today's LinkedIn Post</h2>

    <div style="background:#f5f5f5;padding:20px;border-radius:8px;white-space:pre-wrap;">
{linkedin_post}
    </div>

    <hr>

    <h2>🖼 Image Specification</h2>

    <div style="background:#eef6ff;padding:20px;border-radius:8px;white-space:pre-wrap;">
{image_specification}
    </div>

    <hr>

    <p><b>Instructions</b></p>

    <ol>
        <li>Copy the LinkedIn post.</li>
        <li>Copy the Image Specification.</li>
        <li>Paste it into your ChatGPT Images Project.</li>
        <li>Generate the image.</li>
        <li>Publish the post with the generated image on LinkedIn.</li>
    </ol>

    </body>
    </html>
    """

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

    print("✅ Email sent.")