import os
import sqlite3
import datetime
from time import sleep

STATUSES = {
	0: 'To do',
	1: 'Done'
}

con = sqlite3.connect('task_2/todo.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS items(
	id INTEGER PRIMARY KEY UNIQUE,
	item TEXT NOT NULL,
	status TEXT NOT NULL,
	date TEXT
)''')

def add_item():
	print('Add item:')
	cur.execute('INSERT INTO items(item, status, date) VALUES(?, ?, ?)', (input(), STATUSES.get(0), ''))
	con.commit()
	print('That\'s all? [y/n]')
	match input():
		case 'n':
			os.system('cls')
			return add_item()
		case _:
			os.system('cls')
			return show_menu()
		
def delete_item():
	print('Remove items')
	for row in cur.execute('SELECT * FROM items'):
		print(f'[{row[0]}] {row[1]} - {row[2]} {row[3]}')
	print('\nSelect item(s) to remove or type \'q\' to return')
	print('Exmp: 1 2 5 or 2')
	value = input()
	match value:
		case 'q':
			os.system('cls')
			return show_menu()
		case _:
			indexes = value.split()
			for index in indexes:
				row = cur.execute(f'SELECT * FROM items WHERE id={index}')
				if row.fetchone() is None:
					print(f'There is no item for index [{index}]')
					sleep(2)
					os.system('cls')
					delete_item()
				else:
					cur.execute(f'DELETE FROM items WHERE id={index}')
					con.commit()
			
			print('Success!')
			sleep(2)
			os.system('cls')
			return show_menu()
			

def mark_item():
	for row in cur.execute('SELECT * FROM items'):
		print(f'[{row[0]}] {row[1]} - {row[2]} {row[3]}')
	print('\nSelect item(s) to mark \'Done\' or type \'q\' to return')
	print('Exmp: 1 2 5 or 2')
	value = input()
	match value:
		case 'q':
			os.system('cls')
			return show_menu()
		case _:
			indexes = value.split()
			for index in indexes:
				row = cur.execute(f'SELECT * FROM items WHERE id={index}')
				if row.fetchone() is None:
					print(f'There is no item for index [{index}]')
					sleep(2)
					os.system('cls')
					return mark_item()
				else:
					x = datetime.datetime.now()
					year = x.strftime("%Y")
					month = x.strftime("%m")
					day = x.strftime("%d")
					cur.execute(f'UPDATE items SET status = \'Done\', date = \'{year}/{month}/{day}\' WHERE id={index}')
					con.commit()
			
			print('Success!')
			sleep(2)
			os.system('cls')
			show_menu()

def show_items():
	for row in cur.execute('SELECT * FROM items'):
		print(f'[{row[0]}] {row[1]} - {row[2]} {row[3]}')

	rows = cur.execute('SELECT * FROM items WHERE status = \'Done\'')
	print(f'you`ve completed {len(rows.fetchall())} tasks!')

	print('\nReturn?')
	input()
	os.system('cls')
	show_menu()

def show_menu():
	print('[1] List items')
	print('[2] Add an item')
	print('[3] Remove an item')
	print('[4] Mark an item')
	print('[-] Close')
	print('Select an option:')
	match input():
		case '1':
			os.system('cls')
			show_items()
		case '2':
			os.system('cls')
			add_item()
		case '3':
			os.system('cls')
			delete_item()
		case '4':
			os.system('cls')
			mark_item()
		case _:
			pass

show_menu()



		