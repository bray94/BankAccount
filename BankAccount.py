from Interface import *

class BankAccount:
	"""Creates a bank account with Name on Account and starting value. It will pull
	in either data from a file, or from the user if data doesn't exist"""

	def __init__(self, startingValue):
		self.balance = startingValue
		self.categories = []

	def categoryExistence(self, name):
		for category in self.categories:
			if category.getName().lower() == name.lower():
				return True
			else: pass
		return False


	def addCategory(self, newCategory, amount):
		category = Category(newCategory, amount)
		self.categories.append(category)

	def updateCategory(self, name, amount):
		for category in self.categories:
			if category.getName().lower() == name.lower():
				category.updateCategory(amount)
			else:
				pass


	def addTransaction(self, amount):
		self.balance += amount
		category = raw_input("What was it used for?")

		if(categoryExistence(category)):
			updateCategory(category,amount)

		else:
			addCategory(category, amount)


	def checkBalance(self):
		return self.balance




class Category:
	"""Class to add catehories that transasctions will be stored under."""

	def __init__(self, name, amount):
		self.name = name
		self.amount = amount

	def updateCategory(amount):
		self.amount+= amount

	def getAmount():
		return self.amount

	def getName():
		return self.name

class WriteToFile:



	def writeBankAccountToFile(self, bankAccount):
		f = open("data.txt","r+")
		for line in f:
			if (line.split())[0] == "Balance:":
				f.write("Balance: " + bankAccount.checkBalance() + "\n")
			else: pass
		f.close()

	def writeCategoryToFile(self, category):
		f = open("data.txt","r+")
		for line in f:
			if (line.split())[0] == category.getName() + ":":
				f.write(category.getName() + ": " + category.getAmount() + "\n")
			else: pass
		f.close()
			
class ReadFile:


	def initialRead(self):
		f = open("data.txt" , "r")
		newAccount = BankAccount(0.0)
		for line in f:
			if (line.split())[0] == "Balance:":
				inelist = line.split()
				amount = float((linelist[1])[1:])
				newAccount = BankAccount(amount)
			else:
				linelist = line.split()
				amount = float((linelist[1])[1:])
				name = (linelist[0])[0:-1]
				account.addCategory(name, amount)
		f.close()
		return newAccount


def main():
	initialRead = ReadFile()
	account = initialRead.initialRead()
	interface(account)



if __name__ == '__main__':
	main()
	

