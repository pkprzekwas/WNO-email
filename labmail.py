import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from config import CONFIG, TEXT


def prepare_msg(text, format='html', image_path=None):
    msg = MIMEMultipart()
    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(text, format)
    msg_alternative.attach(msg_text)
    fp = open(image_path, 'rb')
    msg_image = MIMEImage(fp.read())
    fp.close()
    msg_image.add_header('Content-ID', '<image1>')
    msg.attach(msg_image)
    return msg


def smtp_process(host, port, config, msg):
    try:
        s = smtplib.SMTP(host, port)
        s.ehlo()
        s.starttls()
        s.login(config['my-mail'], config['super-secret-pass'])
        s.sendmail(config['my-mail'], [config['your-mail']], msg.as_string())
        s.quit()
        return "Successfully sent email"
    except:
        return "Unsuccessful email sent"

message = prepare_msg(TEXT, 'html', 'se.png')
status = smtp_process('smtp.gmail.com', 587, CONFIG, message)

print(status)

