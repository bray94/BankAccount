from Interface import *
import pickle

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


	def addTransaction(self, amount):
		self.balance -= amount
		category = raw_input("What was it used for?")

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



def writeBankAccountToFile(account):
	f = open("data.txt","r+")
	pickle.dump(account, f)
	f.close()


def initialRead():
	f = open("data.txt" , "r+")
	try:
		newAccount = pickle.load(f)
		f.close()
		return newAccount
	except EOFError:
		amount = float(raw_input("What is the starting amount?"))
		newAccount = BankAccount(amount)
		return newAccount

def main():
	account = initialRead()
	interface(account)



if __name__ == '__main__':
	main()
	

