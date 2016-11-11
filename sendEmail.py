import smtplib

def sendEmail(receiver, code):
    print('start sending')
    sender = 'fietsenstalling@outlook.com'
    password = 'Stallen1'
    smtpserver = smtplib.SMTP('smtp-mail.outlook.com',587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(sender, password)
    header = 'To: {}\nFrom: {}\nSubject: {}\n'.format(
        receiver, sender, 'Verificatiecode fietsenstalling')
    message = header + 'Voer deze verificatiecode in om verder te gaan: ' + code
    smtpserver.sendmail(sender,receiver,message)
    smtpserver.close()
    print('done sending')
