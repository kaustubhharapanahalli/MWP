import sqlite3
from bank import *

con = db_connect()
cur = con.cursor()

# Creating database tables for Accounts and Transactions
try:
	customers_sql = "CREATE TABLE accounts (id integer PRIMARY KEY, account_name text NOT NULL, account_no integer NOT NULL, balance real NOT NULL, pin integer NOT NULL)"
	cur.execute(customers_sql)

	transactions_sql = """CREATE TABLE transactions (id integer PRIMARY KEY, amount real NOT NULL, balance integer NOT NULL, operation text NOT NULL, account_no integer NOT NULL"""
	cur.execute(transactions_sql)

except sqlite3.OperationalError: 
	pass


accounts = {}
# account_no = 1001
cur.execute("SELECT account_no FROM accounts")
results = cur.fetchall()
# print(results)
# print(results[-1])
if results == []:
	account_no = 1001
else:
	account_no = results[-1][0]+1

print("-"*50)
print("Welcome to Iron Bank")




while True:
	print("Hey! What would you like to do today?\n\n\
		1. Create Account\n\
		2. Check Transactions\n\
		3. Deposit Amount\n\
		4. Withdraw Amount\n\
		5. Show Balance\n\
		6. Exit\n")

	choice = int(input("Enter your option: "))

	if choice == 1:
		acc_name = input("Enter account name: ")
		balance = input("Enter the opening balance: ")
		pin = int(input("Enter a PIN for your Account: "))

		account = AccountManager(con, acc_name, account_no, balance, pin)


		print(f"Hi {account.account_name}! Your account is created successfully! Your Account number is {account.account_no}")

		account_no += 1


	elif choice == 2:
		acc_no = int(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))
		cur.execute("SELECT account_no, pin FROM accounts WHERE account_no = 1001")
		pin_result = cur.fetchall()
		if pin_result != []:
			epin = pin_result[-1][-1]
		# print(epin)

		if upin == epin:
			cur.execute("SELECT amount, balance, operation FROM transactions WHERE account_no = 1001")
			result = cur.fetchall()
			# print(result)
			if result != []:
				pass
			else:
				print(f"There are no tranasction history as of now for your account {acc_no}.")
			# print("In")
			# cur.execute("SELECT balance FROM accounts WHERE account_no = 1001")
			# result = cur.fetchall()
			# print(result[0][0])
			# statement = accounts[acc_no].account_statement()
			# print(statement)

		else:
			print("\n\nInvalid Credentials. Please enter again!\n\n")

	elif choice == 3:
		try:
			account = AccountManager

		acc_no = int(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))
		cur.execute("SELECT account_no, pin FROM accounts WHERE account_no = 1001")
		pin_result = cur.fetchall()
		if pin_result != []:
			epin = pin_result[-1][-1]

		if upin == epin:
			amount = int(input("Enter the amount to be deposited: "))
			account.deposit(con, acc_no, amount)

		else:
			print("\n\nInvalid Credentials. Please enter again!\n\n")

	elif choice == 4:
		acc_no = int(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))
		cur.execute("SELECT account_no, pin FROM accounts WHERE account_no = 1001")
		pin_result = cur.fetchall()
		if pin_result != []:
			epin = pin_result[-1][-1]

		if upin == epin:
			amount = int(input("Enter the amount to be withdraw: "))
			accounts[acc_no].withdraw(con, acc_no, amount)

		else:
			print("\n\nInvalid Credentials. Please enter again!\n\n")

	elif choice == 5:
		acc_no = int(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))
		# print(acc_no, type(acc_no))
		cur.execute("SELECT account_no, pin FROM accounts WHERE account_no = 1001")
		result = cur.fetchall()
		# print(result[-1][-1])
		epin = result[-1][-1]

		if upin == epin:
			cur.execute("SELECT balance FROM accounts WHERE account_no = 1001")
			result = cur.fetchall()
			print(f"Your current balance is {result[0][0]}")
	else:
		break