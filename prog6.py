list1 = [1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]

list2 = []

for i in list1:
	if i not in list2:
		list2.append(i)

print(list2)