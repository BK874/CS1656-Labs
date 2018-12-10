# Brian Knotten
# CS1656
# Lab 10

# Creating SQLite Databases, creating and populating tables, executing SQL queries

# SQLite is an in-process library that implements a self-contained, serverless,
# zero-configuration, transactional SQL database engine. It does not a have a
# separate server process and writes directly to ordinary disk files.
import sqlite3 as lite
import pandas

# To connect to a database, use the connect() method, which either returns a
# connection object or creates a database if one does not already exist
con = lite.connect('cs1656wed.sqlite')

# We get the cursor object from the connection, which is used to traverse the
# the records from the result set. The "with" keyword can be used to have the
# Python interpreter auto release the resources by closing the connection, provide
# error handling, and commit the changes. Otherwise each update must be committed
# manually. Committing ~ saving the changes.
# Call the execute() method of the cursor to execute the SQL statements.

# Create a Rankings table in the database:
#with con:
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS Courses')
#cur.execute("CREATE TABLE Courses(cid INT, number INT, professor TEXT, major TEXT, year INT, semester TEXT)")

cur.execute('DROP TABLE IF EXISTS Majors')
#cur.execute("CREATE TABLE Majors(sid INT, major TEXT)")

cur.execute('DROP TABLE IF EXISTS Grades')
#cur.execute("CREATE TABLE Grades(sid INT, cid INT, credits INT, grade INT)")

cur.execute('DROP TABLE IF EXISTS Students')
#cur.execute("CREATE TABLE Students(sid INT, firstName, TEXT, lastName TEXT, yearStarted INT)")

# Insert data row by row
df1 = pandas.read_csv('students.csv')
df1.to_sql('students', con, if_exists='append', index=False)

df2 = pandas.read_csv('grades.csv')
df2.to_sql('grades', con, if_exists='append', index=False)

df3 = pandas.read_csv('courses.csv')
df3.to_sql('courses', con, if_exists='append', index=False)

df4 = pandas.read_csv('majors.csv')
df4.to_sql('majors', con, if_exists='append', index=False)

# Select all data from the table
cur.execute("SELECT * FROM students")

# To retreive data after SELECTing, treat the cursor as an iterator and call the
# cursor's "fetchone()" method to retrievev a single matching row, or call
# fetchall() to get a list of the matching rows.
for row in cur.execute("SELECT * FROM students"):
    print(row)

cur.execute("SELECT * FROM students")
df5 = pandas.DataFrame(cur.fetchall(), columns=[column[0] for column in cur.description])
print(df5)

# Determine how many courses were passed per semester (plus year)
q3a = """
SELECT year, semester, count(*)
FROM courses NATURAL JOIN grades
WHERE grade > 0
GROUP BY year, semester
"""
cur.execute(q3a)
print(cur.fetchall())

# Create "allgrades" view that compiles student grades and display it via a
# dataframe

cur.execute("DROP VIEW IF EXISTS allgrades")
q4c = """
CREATE VIEW allgrades AS
SELECT s.firstName, s.lastName, m.major AS ms,
       c.number, c.major AS mc, g.grade
FROM students AS s, majors AS m, grades AS g, courses AS c
WHERE s.sid = m.sid AND g.sid = s.sid AND g.cid = c.cid
"""
cur.execute(q4c)
print(pandas.DataFrame(cur.execute("SELECT * FROM allgrades").fetchall(),
                 columns=[column[0] for column in cur.description]))

cur.close()
con.close()
