import csv

events_dict = {'1': 'CS 1.6', '2':'Google It', '3':'Treasure Hunt'}

def add_participant():
	name = input("Enter Participant Name: ")
	event = input("Enter the serial number of an event from the following list:\n\
1. CS\n\
2. Google It \n\
3. Treasure Hunt \n\
Event Serial Number: ")

	with open('events.csv', 'a', newline="") as myfile:
	 	wr = csv.writer(myfile, dialect='excel')
	 	wr.writerow([name, events_dict[event]])


def see_participant():
	with open('events.csv', 'r', newline="") as myfile:
		rd = csv.reader(myfile)
		print("-"*50)
		for i in rd:
			print(i[0], i[1], sep=' - ')
			print("-"*50)

if __name__ == '__main__':
	add_participant()
	print(participant_details)
	see_participant()

