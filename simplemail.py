    '''
Step-1 :-> Setting up Gmail App Password
'''
# We will use smtp (Simple Mail Transfer Protocol)

# Step-2 -> using SMTPLIB we start comminication

import smtplib

# first we will make the protocal 

server = smtplib.SMTP('smtp.gmail.com',587)
print(server)

# start comminication 

server.starttls()

# we will login

server.login('jagadeeshboyalla3384@gmail.com','vtwn grat hxat gokz')
print("Login Sucessfull")


# messgae 

messgae = "Welcome to my Wrold. This Automation mail..."

# send mail

server.sendmail('jagadeeshboyalla3384@gmail.com','jagadeeshsrkr3384@gmail.com',messgae)
print("Sucess")