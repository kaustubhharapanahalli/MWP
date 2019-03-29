from events import add_participant, see_participant

while True:
	print("\n")
	choice = input("Enter the serial number of your choice: \n\
1. Add Participant\n\
2. See Participant\n\
3. Exit\n\
Choice: ")

	if choice == '1':
		add_participant()

	elif choice =='2': 
		see_participant()

	else:
		break