import smtplib #simple mail transfer protocol library/module
connection=smtplib.SMTP('smtp.gmail.com',587)#smtp domain name,port no.
connection.ehlo()#smtp gmail k sath hmara server connect ho jayega
connection.starttls()#encryption start 
connection.login('kumarsharmapawan190@gmail.com','Mukesh12@')#login through your email_id,password
connection.sendmail('kumarsharmapawan190@gmail.com','babitadevi8877068@gmail.com','subject:hello \n \n this is msg')#send mail through sender email address, reciever email address,subject
connection.quit()#disconnect

#name should be anythiong but not email because email is a module. 
#if you get error 
#then go to google -->type https://myaccount.google.com//esssecureapps
#then allow to ON