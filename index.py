class Atm():
	users = {'1602':{'Name':'Pratik','Account':12235,'Mobile':9132458657,'Balance':100000},
		'1202':{'Name':'Anchal','Account':13243,'Mobile':9243564782,'Balance':200000},
		'1234':{'Name':'Varun','Account':14636,'Mobile':9543673456,'Balance':300000},
		'5678':{'Name':'Sanket','Account':11237,'Mobile':9164367894,'Balance':400000},
		'9101':{'Name':'Nathan','Account':12225,'Mobile':7564829457,'Balance':500000}}

	def information(self,pin):
		print('Name:',self.users[pin]['Name'])
		print('Account:',self.users[pin]['Account'])
		print('Mobile:',self.users[pin]['Mobile'])
		print('Balance:',self.users[pin]['Balance'])

	def pinchange(self,pin):
		newpin = input("Enter New PIN")
		self.users[newpin] = self.users[pin]
		print("PIN changed Successfully")
		del self.users[pin]
		return newpin

	def balance(self,pin):
		print("Your balance is",self.users[pin]['Balance'])

	def withdrawal(self,pin):
		amount = float(input("Enter the amount you wish to withdraw: "))
		balance = float(self.users[pin]['Balance'])
		if (balance - amount) < 0:
			print("You do not have enough balance to proceed with the transaction,Please check your account balance.")
		else:
			print("Please Wait for Cash and remove your card.....")

	def deposit(self):
		print("Please enter the cash and press Enter")
		input()

	def pin_validation(self,pin):
		validated = False
		if pin in self.users.keys():
			validated = True
		return validated


if __name__ == '__main__':
	while True:
		count = 0
		i = 3
		pin = input("Enter your PIN: ")
		user = Atm()
		validate = user.pin_validation(pin)
		if validate:
			try:
				op = input('''
Press a number according to your operation required:
	1.Account Information.
	2.PIN Change
	3.Balance Inquiry
	4.Withdrawal
	5.Deposit
	6.Exit
Your Option: ''')
				if op == '1':
					user.information(pin)
				elif op == '2':
					pin = user.pinchange(pin)
				elif op == '3':
					user.balance(pin)
				elif op == '4':
					user.withdrawal(pin)
				elif op == '5':
					user.deposit()
				elif op == '6':
					break
				else:
					print("Wrong input,please select valid option")
			except Exception as e:
				print("Account Error:",e)
		else:
			count +=1
			if count == 3:
				print("Account blocked,please try again later.")
			else:
				print("Wrong pin entered, Attempts remaining {}".format(i-count))
