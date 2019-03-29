import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'eventmanager.sqlite3')

try:
	events_sql = "CREATE TABLE event_manager (id integer PRIMARY KEY, participant_name text NOT NULL, event integer NOT NULL, contant_number real NOT NULL, amount integer NOT NULL)"
	cur.execute(customers_sql)

except sqlite3.OperationalError: 
	pass

def db_connect(db_path=DEFAULT_PATH):  
	con = sqlite3.connect(db_path)
	return con


events_dict = {'1': 'CS 1.6', '2':'Google It', '3':'Treasure Hunt'}

def add_participant():
	name = input("Enter Participant Name: ")
	event = input("Enter the serial number of an event from the following list:\n\
1. CS\n\
2. Google It \n\
3. Treasure Hunt \n\
Event Serial Number: ")


def see_participant():
	pass