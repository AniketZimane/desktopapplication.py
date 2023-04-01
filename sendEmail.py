import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender='aniketzimane@gmail.com'
receiver='aniketzimane2003@gmail.com'
con=smtplib.SMTP('smtp.gmail.com', 578)
con.starttls()
con.login('aniketzimane@gmail.com','Az2126@m')

message=MIMEMultipart("alternative")
message['subject']="Id card"
message['From']=sender
message['To']=receiver

text="Hey! want to know more about your self\nThen download button"
html="""/
    <html>
        <head>
        </head>
        <body>
            <p>Hiii welcome smart attendance system<br></p>
            <img src="2001170257.png">
        </body>
    </html>"""
textPart=MIMEText(text,'plain')
htmlPart=MIMEMultipart(html,'html')
message.attach(htmlPart,textPart)
con.sendmail('aniketzimane@gmail.com','aniketzimane2003@gmail.com',message.as_string())
print("main send")
con.quit()