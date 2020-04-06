import sqlite3

# Define main for loops, bro
def main():
	# connects to a databse called students.db
	#to store a database in memory use :memory
	connection = sqlite3.connect('students.db')
	cur = connection.cursor()

	# this will force you to recreate the table every time 
	# you usually dont create/fill and query a table in the same file 
	cur.execute('DROP TABLE IF EXISTS student_output')
	cur.execute('CREATE TABLE student_output (first TEXT, last TEXT, tears INTEGER)')
	
	

	cur.execute('''
		INSERT INTO student_output 
		(first, last, tears)
		VALUES (?,?,?)
		''', ('Dave', 'Purdum',0))
	cur.execute('''
		INSERT INTO student_output 
		(first, last, tears)
		VALUES (?,?,?)
		''', ('Ankur', 'Gupta',100000))
	cur.execute('''
		INSERT INTO student_output 
		(first, last, tears)
		VALUES (?,?,?)
		''', ('Virtual', 'Bob',1))


		
	#save the stuff i've done
	connection.commit() 

	# this creates a list of rows that satisfy the conditions called cur
	cur.execute('SELECT first, tears FROM student_output')

	print('(First, Tears)')
	for row in cur:
		print(row)

	cur.execute('DELETE FROM student_output WHERE tears < 1')
	cur.execute('SELECT * FROM student_output')
	# for row in cur:
	# 	print(row)
	
	print(cur.fetchone())
	print(cur.fetchall()) # this produces a list containing all the things that you haven't already fetched 

	connection.close()

if __name__ == '__main__':
    main()