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
    
    html = f"""
    <html>
    <body style="font-family:Arial; line-height:1.6; max-width:800px; margin:auto;">
    
    <h2>📌 Today's LinkedIn Post</h2>
    
    <div style="background:#f5f5f5;padding:20px;border-radius:8px;white-space:pre-wrap;">
    {linkedin_post}
    </div>
    
    <hr>
    
    <h2>🖼 Image Prompt</h2>
    
    <div style="background:#eef6ff;padding:20px;border-radius:8px;white-space:pre-wrap;">
    {post['image_prompt']}
    </div>
    
    <hr>
    
    <p><b>Instructions</b></p>
    
    <ol>
    <li>Copy the LinkedIn Post.</li>
    <li>Generate the image using the Image Prompt.</li>
    <li>Attach the image.</li>
    <li>Publish on LinkedIn.</li>
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