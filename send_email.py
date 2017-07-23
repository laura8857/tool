# -*- coding: utf-8 -*-


# -----email sender and receiver email --------
import mimetypes
import smtplib
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

email_from = 'laura@deepblu.com'
email_to = 'andxxxd@gmail.com'

# email attachment
file_to_send = "path.txt"

# account and password of account
account = 'andxxxd@gmail.com'
password = 'androidxxx'

msg = MIMEMultipart()
msg["From"] = email_from
msg["To"] = email_to

# subject
msg["Subject"] = "Test for Python 中文"
# msg["preamble"] = 'You will not see this in a MIME-aware mail reader.\n'

# ----- Email 的信件內容 Message -----

part = MIMEText(u"body text including an Euro char \u20ac\n 中文測試\n ")
# part = MIMEText(u"body text including an Euro char \u20ac\n 中文測試\n ", _charset="UTF-8")
msg.attach(part)


def send_email():
    # ctype, encoding = mimetypes.guess_type(file_to_send)
    # if ctype is None or encoding is not None:
    #     ctype = "application/octet-stream"
    # maintype, subtype = ctype.split("/", 1)
    #
    # if maintype == "text":
    #     fp = open(file_to_send)
    #     attachment = MIMEText(fp.read(), _subtype=subtype)
    #     fp.close()
    # elif maintype == "image":
    #     fp = open(file_to_send, "rb")
    #     attachment = MIMEImage(fp.read(), _subtype=subtype)
    #     fp.close()
    # elif maintype == "audio":
    #     fp = open(file_to_send, "rb")
    #     attachment = MIMEAudio(fp.read(), _subtype=subtype)
    #     fp.close()
    # else:
    #     fp = open(file_to_send, "rb")
    #     attachment = MIMEBase(maintype, subtype)
    #     attachment.set_payload(fp.read())
    #     fp.close()
    #     encoders.encode_base64(attachment)
    #     attachment.add_header("Content-Disposition", "attachment", filename=file_to_send)
    #     msg.attach(attachment)

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('path.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    msg.attach(att1)



    # # --- 寄件的 SMTP mail server ---
    # server = smtplib.SMTP('smtp.company.com', 25)
    # --- 如果是 Gmail 可使用這行 ---
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # --- 如果SMTP server 不需要登入則可把 server.login 用 # mark 掉
    server.login(account, password)
    # SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()
    print('email is send.')


if __name__ == "__main__":
    send_email()
