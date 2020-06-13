import sys
class Customer:
	'''Customer class with bank related operations'''
	bankname='DURGASOFT'
	
	def __init__(self,name,balance=0):
		self.name=name
		self.balance=balance
	
	def deposit(self,amt):
		self.balance=self.balance+amt
		print('After deposit the balance:',self.balance)
		
	def withdraw(self,amt):
		if amt>self.balance:
			print('Insufficient Funds..cannot perform this operation')
			sys.exit()
		
		self.balance=self.balance-amt
		print('After withdraw The Balance:',self.balance)
		
print('Welcome to',Customer.bankname)
name=input('Enter Your Name:')
c=Customer(name)
while True:
	print('d-Deposit\nw-Withdraw\ne-Exit')
	option=input('Choose Your Option:')
	if option=='d' or option=='D':
		amt=float(input('Enter the amount to depost:'))
		c.deposit(amt)
		
	elif option=='w' or option=='W':
		amt=float(input('Enter the amount to withdraw:'))
		c.withdraw(amt)
	elif option=='e' or option=='E':
		print('thanks For Banking')
		sys.exit()
		
	else:
		print('choose valid option:')
		
		'''Welcome to DURGASOFT
Enter Your Name:pawan
d-Deposit
w-Withdraw
e-Exit
Choose Your Option:d
Enter the amount to depost:12000
After deposit the balance: 12000.0
d-Deposit
w-Withdraw
e-Exit
Choose Your Option:w
Enter the amount to withdraw:5000
After withdraw The Balance: 7000.0
d-Deposit
w-Withdraw
e-Exit
Choose Your Option:e
thanks For Banking'''