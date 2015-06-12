class BankAccount:

	def __init__(self, startingValue, nameOnAccount):
		self.balance = startingValue
		self.nameOnAccount = nameOnAccount
		self.categories = []

	def categoryExistence(self, name):
		for category in self.categories:
			if category.getName().lower() == name.lower():
				return True
			else: pass
		 return False


	def addCategory(self, newCategory):
		category = Category(newCategory)
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
			addCategory(category)
			updateCategory(amount)


	def checkBalance():
		return self.balance




class Category:

	def __init__(self, name):
		self.name = name
		self.amount = 0.00

	def updateCategory(amount):
		self.amount+= amount

	def getAmount():
		return self.amount

	def getName():
		return self.name

	
