import os
import smtplib
import zipfile
from email.mime.image import MIMEImage
from email.mime.message import MIMEMessage
from os import path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from run import Anomaly

def sendSelected(anomal):

    part =MIMEText('В данном письме представлен кадр с аномалией от ' + anomal.date.strftime("%Y-%m-%d %H:%M:%S"))
    msg = MIMEMultipart()
    msg['From'] = "deadlorpa@gmail.com"
    msg['To'] = "deadlorpa@gmail.com"
    msg.attach(part)
    for root, dirs, files in os.walk('anomal'):  # Список всех файлов и папок в директории folder
        for file in files:
            if file == anomal.img:
                with open(file, 'rb') as fp:
                    img = MIMEImage(fp.read())
                    msg.attach(img)

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('deadlorpa@gmail.com', 'MyDeadL0RPA')
    smtpObj.sendmail("deadlorpa@gmail.com", "deadlorpa@gmail.com", msg.as_string())
    smtpObj.quit()

def send():

    # Проверяем, существует ли файл
    if path.exists("anomal"):
        z = zipfile.ZipFile('anomal.zip', 'w')  # Создание нового архива
        for root, dirs, files in os.walk('anomal'):  # Список всех файлов и папок в директории folder
            for file in files:
                z.write(os.path.join(root, file))  # Создание относительных путей и запись файлов в архив
                os.remove(os.path.join(root, file)) # удаляем файл в папке
        z.close()

    filepath = "anomal.zip"
    # Compose attachment
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filepath))

    part1 = MIMEText('В данном архиве содержатся кадры запечатлённых аномалий')

    # Compose message
    msg = MIMEMultipart()
    msg['From'] = "deadlorpa@gmail.com"
    msg['To'] = "deadlorpa@gmail.com"
    msg.attach(part)
    msg.attach(part1)

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('deadlorpa@gmail.com', 'MyDeadL0RPA')
    smtpObj.sendmail("deadlorpa@gmail.com", "deadlorpa@gmail.com", msg.as_string())
    smtpObj.quit()
