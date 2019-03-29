a = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
b = []
search = int(input("Enter search element: "))

for i, val in enumerate(a):
	if val is search:
		b.append(i)

print(b)