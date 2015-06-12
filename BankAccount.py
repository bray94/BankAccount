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
		self.amount += amount
		category = raw_input("What was it used for?")

		if(categoryExistence(category)):
			updateCategory(category,amount)

		else:
			addCategory(category, amount)


	def checkBalance(self):
		return self.balance




class Category:
"""Class to add catehories that transasctions will be stores under """

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

	def writeBankAccountToFile(BankAccount):
		f = open("data.txt","r+")
		for line in f:
			if (line.split())[0] == "Balance:":
				f.write("Balance: " + BankAccount.checkBalance() + "\n")
			else: pass
		f.close()

	def writeCategoryToFile(Category):
		f = open("data.txt","r+")
		for line in f:
			if (line.split())[0] == Category.getName() + ":":
				f.write(Category.getName() + ": " + Category.getAmount() + "\n")
			else: pass
		f.close()
			
class ReadFile:

	def initialRead():
		f = open("data.txt" , "r")
		for line in f:
			if (line.split())[0] == "Balance:":
				account = BankAccount(float(((line.split())[1])[1:]))
			else:
				account.addCategory(((line.split())[0])[0:-1] float(((line.split())[1])[1:]))
		f.close()
		return account


def main():
	account = initialRead()
	interface(account)



if __name__ == '__main__':
	main()
	

