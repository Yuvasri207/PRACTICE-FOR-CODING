import smtplib

sender_email="yuvasri207@gmail.com"
rec_email="yuvasriayyappan22@gmail.com"
password=input(str('please enter your password : '))
text='hi this is yuvasri and this mail was sent using python'

server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("login success")
server.sendmail(sender_email,rec_email,text)
print('email has been sent to',rec_email)