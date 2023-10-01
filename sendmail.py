import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open('token.json') as f:
    token = json.load(f)

sender_email = token["sender_email"]

def send_mail(target_email: str) -> None:
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = target_email
    message["Subject"] = "【第十七屆成大單車節】報名確認信及招工 Bonus 表單填寫提醒"

    with open(".\\body_content.txt", "r") as file:
        text_content = file.read()

    body = text_content
    message.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, token["password"])

        text = message.as_string()
        server.sendmail(sender_email, target_email, text)
        print("成功發送")
    except Exception as e:
        print("發送失敗", str(e))
    finally:
        server.quit()