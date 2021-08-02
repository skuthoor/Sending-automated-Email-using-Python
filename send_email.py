#import pandas as pd 
import smtplib
#e = pd.read_excel("email.xlsx")
#emails = e['emails'].values
emails = [] # reciver mail address
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("@gmail.com","password") #senders email with password
msg = 'message to be send'
subject ='Hello There!'
body="subject:{}\n\n{}".format(subject,msg)
for email in emails :
    server.sendmail("@gmail",email,body)

server.quit()
