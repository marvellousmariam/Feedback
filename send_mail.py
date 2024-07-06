import smtplib
from email.mime.text import MIMEText

def send_mail(name,dealer,ratng,comment):
    port=2525
    smtp_server='sandbox.smtp.mailtrap.io'
    login='00d56e591cfbb7'
    password='ccb36f367092ae'
    message=f"<h3>New Feedback Submittion</h3><ul><li>Customer Name:{name}</li><li>Car Dealer:{dealer}</li><li>Dealer Rating:{ratng}</li><li>Comment:{comment}</li></ul>"
    
    sender_email="from@example.com"
    receiver_email='to@example.com'
    msg=MIMEText(message,'html')
    msg['Subject']='Tesla Submittion'
    msg['From']=send_mail
    msg['TO']=receiver_email
    #send emai
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg)