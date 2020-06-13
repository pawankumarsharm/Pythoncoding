import smtplib,webbrowser,getpass
def get_mail():
	servicesAvailable=['hotmail','gmail','yahoo','outlook']
	while True:
		mail_id=input('E-mail :')
		if '@' in mail_id and '.com' in mail_id: #kumarsharmapawan190@gmail.com
			symbol_pos=mail_id.find('@')
			dotcom_pos=mail_id.find('.com')
			sp=mail_id[symbol_pos+1:dotcom_pos]
			if sp in servicesAvailable:
				return mail_id,sp #it return tuple('kumarsharmapawan190@gmail.com,gmail)
				break
			else:
				print('sorry! we do not provide service for '+sp)
				print('we provide services only for:hotmail/gmail/yahoo,ouytlook')
				continue
		else:
			print('invalid E-mail retype again:')
			continue

def set_smtp_domain(serviceProvider):#it take only one input because we provide only one argument
	if serviceProvider=='gmail':
		return 'smtp.gmail.com'
	elif serviceProvider=='outlook' or serviceProvider=='hotmail':
		return 'smtp-mail.outlook.com'
	elif serviceProvider=='yahoo':
		return 'smtp.mail.yahoo.com'
		
print('Welcome you can send an E-mail through this program')
print('Please enter your E-mail and password:')
e_mail,serviceProvider=get_mail()
print('Your service provider is:'+serviceProvider)
password=input('Password:')#getpass.getpass('Password:')
while True:
	try:
		smtpDomain=set_smtp_domain(serviceProvider)
		connection=smtplib.SMTP(smtpDomain,587)#smtp domain name
		connection.ehlo()#smtp gmail k sath hmara server connect ho jayega
		connection.starttls()#encryption start 
		connection.login(e_mail,password)#login through user email_id,password
		
		
	except:
		#if smtplib.SMTPServerDisconnected:
			#print(server)
		if serviceProvider=='gmail':
			print('login unsuccessfull, there are two possible reasons:') 
			print('1.)you typed wrong username or password')
			print("2.) you are using Gmail there is an option in gmail 'Allow less secure apps: ON")
			print('Do you want to us to open a webpage from where you can enable this option?')
			answer=input('yes or no ?:')
			if answer=='yes':
				webbrowser.open(' https://myaccount.google.com//esssecureapps')
			else:
				print('we dont open webpage for you , you can go to " https://myaccount.google.com//esssecureapp"')
			print('please retype your e-mail and password also')
			e_mail,serviceProvider=get_mail()
			password=input('Password:')#getpass.getpass('Password:')
			continue
		else:
			print('Login Unsuccessfull,most possible you typedd wrong username or password')
			print('please retype your e-mail andf password')
			e_mail,serviceProvider=get_mail()
			password=input('Password:')#getpass.getpass('Password:')
			continue
	else:
		print('Login successfull')
		break
		
print('please type receiver E-mail address')
receiverAddress,receiverSP=get_mail()
print('Now Please type Subject and Message')
Subject=input("Subject:")
Message=input('Message:')
connection.sendmail(e_mail,receiverAddress,('subject:'+str(Subject) + '\n \n' +str(Message)))#send mail through sender email address, reciever email address,subject
print("Email send successfully")
connection.quit()#disconnect

		
	