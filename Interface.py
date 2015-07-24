import Tkinter

def interface(account):
	window = Tkinter.Tk()

	app = ApplicationWindow(window)

	window.mainloop()



"""
	while on:
		refreshWindow()
		answer = raw_input("What would you like to do?\nAdd Transaction\nDeposit\nCheck Balance\nQuit\n\n")

		if (answer.split()[0]).lower() == "add":
			amount = input("How much was the transaction? ")
			account.addTransaction(amount)
		elif (answer.split()[0]).lower() == "deposit":
			amount = input("How much would you like to deposit? ")
			account.deposit(amount)
		elif (answer.split()[0]).lower() == "check":
			print (str(account.checkBalance()) + "\n")
		elif (answer.split()[0]).lower() == "quit":
			on = False
			account.quit()
		else:
			print ("Not a valid command. Try again.\n\n")
"""
	
def ApplicationWindow(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background = "white")

		self.parent = parent

		self.parent.title("Money Manager")

		self.running()

	def running(self):

		self.pack(fill = BOTH, expand = 1)

		addButton = Button(self, text = "Add Transaction" , command = addTransactionInput())
		addButton.place(x=125, y=20)

		depositButton = Button(self, text = "Deposit" , command = depositInput())
		depositButton.place(x=125, y=70)

		balanceButton = Button(self, text = "Check Balance" , command = checkBalanceDialog())
		balanceButton.place(x=125, y=120)

		quitButton = Button(self, text = "Quit" , command = self.quit)
		quitButton.place(x=125, y=170)


		
	def addTransactionInput(self):
		addButton.pack_forget()
		depositButton.pack_forget()
		balanceButton.pack_forget()
		quitButton.pack_forget()

		pass

	def depositInput(self):
		pass

	def checkBalanceInput(self):
		pass


		if (answer.split()[0]).lower() == "add":
			amount = input("How much was the transaction? ")
			account.addTransaction(amount)
		elif (answer.split()[0]).lower() == "deposit":
			amount = input("How much would you like to deposit? ")
			account.deposit(amount)
		elif (answer.split()[0]).lower() == "check":
			print (str(account.checkBalance()) + "\n")
		elif (answer.split()[0]).lower() == "quit":
			on = False
			account.quit()
		else:
			print ("Not a valid command. Try again.\n\n")

if __name__ == '__main__':
    main()  


