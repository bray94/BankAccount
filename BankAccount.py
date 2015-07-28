import pickle
import Graphics as graph
from Tkinter import *

class BankAccount:
	"""Creates a bank account with Name on Account and starting value. It will pull
	in either data from a file, or from the user if data doesn't exist"""

	def __init__(self, startingValue):
		self.balance = startingValue
		self.categories = []

	def categoryExistence(self, name):
		for category in self.categories:
			if category.name.lower() == name.lower():
				return True
			else: pass
		return False


	def addCategory(self, newCategory, amount):
		category = Category(newCategory, amount)
		self.categories.append(category)

	def updateCategoryInBankAccount(self, name, amount):
		for category in self.categories:
			if (category.name.lower() == name.lower()):
				category.updateCategory(amount)
			else:
				pass


	def addTransaction(self, amount, category):
		self.balance -= amount

		if(self.categoryExistence(category)):
			self.updateCategoryInBankAccount(category,amount)

		else:
			self.addCategory(category, amount)

	def deposit(self, amount):
		self.balance+= amount

	def checkBalance(self):
		return self.balance



	def quit(self):
		writeBankAccountToFile(self)




class Category:
	"""Class to add categories that transasctions will be stored under."""

	def __init__(self, name, amount):
		self.name = name
		self.amount = amount

	def updateCategory(self, amount):
		self.amount+= amount

	def getAmount(self):
		return self.amount

	def getName(self):
		return self.name

class App:
	"""Class to add the interface for the app"""

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


#Other misc. functions

def writeBankAccountToFile(account):
	f = open("data.txt","r+")
	pickle.dump(account, f)
	f.close()


def initialRead():
	try:
		f = open("data.txt" , "r")
	except IOError:
		f = open("data.txt" , "r+")
	try:
		newAccount = pickle.load(f)
		f.close()
		return newAccount
	except EOFError:
		amount = float(raw_input("What is the starting amount?"))
		newAccount = BankAccount(amount)
		return newAccount

def interface(account):
	window = Tk()
	window.geometry('450x220')
	window.title('Money Manager')
	app = App(window, account)

	window.mainloop()


def main():
	account = initialRead()
	interface(account)



if __name__ == '__main__':
	main()
	

