import sqlite3

def insertStudent(first, last, tears):
	with connection:
		cur.execute('''INSERT INTO student_output
		(first,last,tears)
		VALUES (?,?,?)''', (first, last, tears)) 

def getStudents():
		cur.execute('SELECT * FROM student_output')

def updateTears(first,last,moretears):
	with connection:
		cur.execute(''' UPDATE student_output 
			SET tears=:moretears 
			WHERE first=:first AND last=:last''',{'first':first, 'last':last, 'moretears':moretears})
		

connection = sqlite3.connect('students.db')
cur = connection.cursor()
# Define main for loops, bro
def main():
	# connects to a databse called students.db
	#to store a database in memory use :memory
	

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

	# DELETE is a SQL command that removes rows according to its parameters, it is formed similarly to SELECT in terms of syntax 
	cur.execute('DELETE FROM student_output WHERE tears < 1')
	cur.execute('SELECT * FROM student_output')
	# for row in cur:
	# 	print(row)
	updateTears('Ankur', 'Gupta', 10)
	
	# here, the cursor basically iterates over the results 
	print(cur.fetchone())
	print(cur.fetchall()) # this produces a list containing all the things that you haven't already fetched 

	print()
	cur.execute('SELECT * FROM student_output')
	resultlist=cur.fetchall()
	print(resultlist[0][0], 'has the following number of tears', resultlist[0][2])

	# this command inserts via a dictionary 
	cur.execute('''INSERT INTO student_output
		(first,last,tears)
		VALUES (:first,:last,:tears)''', {'first':'Madonna','last':'','tears':0}) 
	cur.execute('''INSERT INTO student_output
			(first,last,tears)
			VALUES (:first,:last,:tears)''', {'first':'Bob','last':'Bob','tears':15}) 

	cur.execute('SELECT * FROM student_output WHERE last= "Bob"')

	# fetches a list of a specified length 
	print(cur.fetchmany(2))


	# now we're gonna insert with a function 
	insertStudent('Bob','Bobbity',20)

	connection.close()

if __name__ == '__main__':
    main()