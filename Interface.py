def interface(account):
	on = True


	while on:
		answer = raw_input("What would you like to do?\nAdd Transaction\nDeposit\nCheck Balance\nQuit\n\n")

		if (answer.split()[0]).lower() == "add":
			amount = input("How much was the transaction?")
			account.addTransaction(amount)
		elif (answer.split()[0]).lower() == "deposit":
			amount = input("How much would you like to deposit?")
			account.deposit(amount)
		elif (answer.split()[0]).lower() == "check":
			print (str(account.checkBalance()) + "\n")
		elif (answer.split()[0]).lower() == "quit":
			on = False
			account.quit()
		else:
			print ("Not a valid command. Try again.\n\n")

	


