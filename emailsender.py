import smtplib
#u have to go to sender email account setting and click on button on less secure app access section To make it work.
to = input("enter email :")
content = input("Enter body of mail : ")


def send(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("coderworld.pro@gmail.com", "Karnal@123")
    server.sendmail("coderworld.pro@gmail.com", to, content)
    server.close()


send(to, content)

