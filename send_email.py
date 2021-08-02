#import pandas as pd 
import smtplib
#e = pd.read_excel("email.xlsx")
#emails = e['emails'].values
emails = ['sanjay109kuthoor@gmail.com','s109kuthoor@gmail.com']
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("sanjay.p@ug.cusat.ac.in","*****")
msg = 'hello checking the script'
subject ='Hello There!'
body="subject:{}\n\n{}".format(subject,msg)
for email in emails :
    server.sendmail("sanjay.p@ug.cusat.ac.in",email,body)

server.quit()
