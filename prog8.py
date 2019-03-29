fruits = {'apple':'sweet', 'mango':'sweet'}

key_1 = input("Enter a key: ")
value_1 = input("Enter a value: ")

if key_1 not in fruits.keys():
	fruits[key_1] =  value_1

print(fruits)