
# coding: utf-8

# # CS 1656 – Introduction to Data Science 
# ## Instructor: Alexandros Labrinidis 
# ## Teaching Assistant:  Tahereh Arabghalizi
# ## Additional Credits: Evangelos Karageorgos, Agha Zuha, Anatoli Shein
# ## SQLite in Python
# 
# In this lab we will learn how to create SQLite Databases, create tables, populate tables, and execute SQL queries.
# 
# Start off by importing slite3, which comes installed with Anaconda's package list.

# In[1]:


import  sqlite3 as lite


# ### Introduction to SQLite 
# SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. Unlike most other SQL databases, SQLite does not have a separate server process. SQLite reads and writes directly to ordinary disk files.

# ### Creating and Connecting to SQLite Database
# To connect to a database, use the connect() method which returns a connection object. If a database with that name does not exist, connect() method creates a database.

# In[2]:


con = lite.connect('cs1656wed.sqlite')


# ### Create/Drop Tables & Insert Data
# From the connection, we get the cursor object. The cursor is used to traverse the records from the result set. 
# By using the with keyword, the Python interpreter automatically releases the resources by closing the connection, provides error handling and __commits__ the changes. Otherwise, each update to the database has to be committed manually. You can think of commit as saving the changes.
# 
# We call the execute() method of the cursor to execute the SQL statements.Let's start by creating a Rankings table in the database. 

# In[3]:


#with con:
cur = con.cursor() 
cur.execute('DROP TABLE IF EXISTS Courses')
#cur.execute("CREATE TABLE Courses(cid INT, number INT, professor TEXT, major TEXT, year INT, semester TEXT)")

cur.execute('DROP TABLE IF EXISTS Majors')
#cur.execute("CREATE TABLE Majors(sid INT, major TEXT)")

cur.execute('DROP TABLE IF EXISTS Grades')
#cur.execute("CREATE TABLE Grades(sid INT, cid INT, credits INT, grade INT)")

cur.execute('DROP TABLE IF EXISTS Students')
#cur.execute("CREATE TABLE Students(sid INT, firstName TEXT, lastName TEXT, yearStarted INT)")

    


# Now data can be inserted in the table using two ways. You could either insert each row one by one as shown below, 

# In[4]:


import pandas

df1 = pandas.read_csv('students.csv')
df1.to_sql('students', con, if_exists='append', index=False)

df2 = pandas.read_csv('grades.csv')
df2.to_sql('grades', con, if_exists='append', index=False)

df3 = pandas.read_csv('courses.csv')
df3.to_sql('courses', con, if_exists='append', index=False)

df4 = pandas.read_csv('majors.csv')
df4.to_sql('majors', con, if_exists='append', index=False)


# Or a easier way to insert all rows together is by using executemany() method. But before we try the second method of inserting data, let's first drop the exising table and create it again.

# ### Select, Where, Orderby
# To select all data from the table, 

# In[5]:


cur.execute("SELECT * FROM students")


# To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator and call the cursor’s fetchone() method to retrieve a single matching row, or call fetchall() to get a list of the matching rows.

# In[6]:


for row in cur.execute("select * from students"):
    print(row)
cur.execute("select * from students")
df5 = pandas.DataFrame(cur.fetchall(), columns=[column[0] for column in cur.description])
df5


# Now, let's find out how many courses were passed per semester (plus year)

# In[7]:


q3a = """
SELECT year, semester, count(*) 
FROM courses natural join grades 
WHERE grade > 0
GROUP BY year, semester
"""
cur.execute(q3a)
cur.fetchall()


# Let's create a view called 'alldata' that compiles student grades, and show the view using a dataframe.

# In[8]:


cur.execute("DROP VIEW IF EXISTS allgrades")
q4c = """
create view allgrades as
SELECT s.firstName, s.lastName, m.major as ms, 
       c.number, c.major as mc, g.grade 
FROM students as s, majors as m, grades as g, courses as c
WHERE s.sid = m.sid AND g.sid = s.sid AND g.cid = c.cid
"""
cur.execute(q4c)
pandas.DataFrame(cur.execute("select * from allgrades").fetchall(), columns=[column[0] for column in cur.description])


# ### Tasks
# 
# __T1) Show how many courses were passed (grade>0) per student per semester (plus year). Show student id, year, semester and the count.__

# In[9]:


q3b = """
SELECT sid, year, semester, count(*) 
FROM courses natural join grades 
WHERE grade > 0
GROUP BY sid, year, semester
"""
cur.execute(q3b)
cur.fetchall()


# __T2) Same as T1, but show student first and last name instead of student id. Also only show results for students passing at least two courses for every semester.__

# In[10]:


q3b = """
SELECT firstName, lastName, year, semester, count(*) 
FROM courses natural join grades natural join students
WHERE grade > 0
GROUP BY firstName, lastName, year, semester
HAVING count(*) >= 2
"""
cur.execute(q3b)
cur.fetchall()


# __T3) Show the students that have failed at a course in their majors (firstName, lastName, major, courseNumber), utilizing the 'allgrades' view.__

# In[11]:


q6a = """
SELECT firstName, lastName, mc as major, number as courseNumber
FROM allgrades
WHERE ms = mc and grade = 0
"""
cur.execute(q6a)
cur.fetchall()


# __T4) Same as T3, but without utilizing the view.__

# In[12]:


q6a = """
SELECT s.firstName, s.lastName, m.major, c.number as courseNumber
FROM students s, courses c, grades g, majors m
WHERE m.sid=s.sid and g.sid=s.sid and g.cid=c.cid and c.major=m.major and g.grade = 0
"""
cur.execute(q6a)
cur.fetchall()


# __T5) Show the professors in decreasing order of 'success' (professor, success). Success will be defined as the number of students passing any of the sourses with grade >= 2.__

# In[13]:


q6a = """
SELECT c.professor, count(g.sid) as success FROM courses c INNER JOIN grades g ON g.cid=c.cid
WHERE g.grade>=2
group by c.professor order by success desc
"""
cur.execute(q6a)
cur.fetchall()


# __T6) Show a report of the courses (course_number, student_names, avg_grade). Column 'student_names' will contain the first and last names (seperated by a space) of all students taking the course, each name being seperated by ', ' (eg. 'John Doe, Mary Jane'). Only students that passed a specific course (grade>=2) will be considered. Also, the report should only contain courses with avg_grade > 3.__

# In[14]:


q6a = """
SELECT c.number as course_number, group_concat(s.firstName || ' ' || s.lastName, ', ') as student_names, avg(g.grade) as avg_grade
FROM students s, courses c, grades g
WHERE g.sid=s.sid and g.cid=c.cid and g.grade>=2.0
GROUP BY c.number
HAVING avg_grade > 3
order by avg_grade desc
"""
cur.execute(q6a)
cur.fetchall()


# In[15]:


cur.close()
con.close()

