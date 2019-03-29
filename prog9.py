def add(a, b):
	print("Inside the function")
	print(a)
	print(b)
	print('='*20)

	c = a + b
	print(c)
	add(a, b)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))	

print("Outside the function")
print(a)
print(b)

# def subtract():
# 	a = 20
# 	b = 10
# 	c = a - b
# 	print(c)

# subtract()