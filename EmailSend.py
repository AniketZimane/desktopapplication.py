import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox

fromaddr = "aniketzimane2003@gmail.com"
toaddr = "aniketzimane@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Student identy card'
body = 'this card generate from smart attenance management system'
msg.attach(MIMEText(body, 'plain'))
filename = "Identycard/img2001170252.png"
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment;filename=%s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "vqkxqdrjjmrpawkw")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()





# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from tkinter import messagebox
# try:
#     fromaddr = "aniketzimane2003@gmail.com"
#     toaddr = "aniketzimane@gmail.com"
#     msg = MIMEMultipart()
#     msg['From'] = fromaddr
#     msg['To'] = toaddr
#     msg['Subject'] = 'Student identy card'
#     body = 'this card generate from smart attenance management system'
#     msg.attach(MIMEText(body, 'plain'))
#     filename = "2001170252.png"
#     attachment = open(filename, 'rb')
#     p = MIMEBase('application', 'octet-stream')
#     p.set_payload((attachment).read())
#     encoders.encode_base64(p)
#     p.add_header('Content-Disposition', "attachment;filename=%s" % filename)
#     msg.attach(p)
#     s = smtplib.SMTP('smtp.gmail.com', 578)
#     s.starttls()
#     s.login(fromaddr, "vqkxqdrjjmrpawkw")
#     text = msg.as_string()
#     s.sendmail(fromaddr, toaddr, text)
#     s.quit()
# except:
#     messagebox.showerror("Error","Server serror....try after some time")