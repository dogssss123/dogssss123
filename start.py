def calculator():
	print("Welcome to my calculator!")
	while True:
		num1 = float(input("Please input your first number:"))
		operator = input("Please input your operator(+,-,*,/):")
		num2 = float(input("Please input your second number:"))


	if operator == "+":
		result = num1 + num2
	elif operator == "-":
		result = num1 - num2
	elif operator == "*":
		result = num1 * num2
	elif operator == "/":
		result = num1 / num2
	else:
		print("Some Wrong!")
		continue

	print("Result:", result)

	choice = input("Do you want to try again?(Y/N:)")

	if choice.upper() != "Y":
		break
	
	print("Thank you! This is the end:)")

calculator()






