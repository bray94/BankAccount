from Tkinter import *

def interface(account):
	window = Tk()
	window.geometry('450x220')
	window.title('Money Manager')
	app = App(window, account)

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
class App:

	def __init__(self, window, account):
		self.account = account
		self.window= window	

		self.amount = Label(self.window, fg="red", text = "$"+str(self.account.checkBalance()))
		self.amount.place(x=225, y=20)

		self.addButton = Button(self.window, text = "Add Transaction" , command = self.addTransactionInput)
		self.addButton.place(x=25, y=20)

		self.depositButton = Button(self.window, text = "Deposit" , command = self.depositInput)
		self.depositButton.place(x=25, y=70)

		self.balanceButton = Button(self.window, text = "Check Balance" , command = self.checkBalanceDialog)
		self.balanceButton.place(x=25, y=120)

		self.quitButton = Button(self.window, text = "Quit" , command = self.quitProgram)
		self.quitButton.place(x=25, y=170)

		self.entry = Entry(self.window)
		self.entry.place(x=225, y=120)
		self.entry.pack

		self.entry2 = Entry(self.window)

		self.submit = Button(self.window, text = "Submit", command=self.submit)

		
	def addTransactionInput(self):
		amount = int(self.entry.get())
		
		self.entry2.place 
		self.submit.place(x=225, y=170)

		self.entry.delete(0, END)
		self.entry.insert(0, "Thanks!")


		

		amount = self.submit

		print amount
		print "A transaction would be added"

	def submit(self):
		return self.entry2.get()

	def	submitCategory(self):
		pass


	def depositInput(self):
		pass

	def checkBalanceDialog(self):
		print "balance would be checked"

	def quitProgram(self):
		self.account.quit()
		self.window.quit()

if __name__ == '__main__':
    main()  


