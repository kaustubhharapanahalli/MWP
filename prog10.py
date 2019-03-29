import csv

# with open('file.csv', 'a', newline="") as myfile:
# 	wr = csv.writer(myfile, dialect='excel')
# 	wr.writerow(['Game of Thrones', 'Winter is Coming'])
# 	wr.writerow(['Game of Thrones', 'Winter is Coming'])
# 	wr.writerow(['Game of Thrones', 'Winter is Coming'])
# 	wr.writerow(['Game of Thrones', 'Winter is Coming'])
# 	wr.writerow(['Game of Thrones', 'Winter is Coming'])

with open('file.csv', 'r', newline="") as myfile:
	rd = csv.reader(myfile)
	for i in rd:
		print(i[0])
