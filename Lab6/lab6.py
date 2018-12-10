# Brian Knotten
# CS1656
# Lab 6

import time
import datetime

# To get the neo4j database password from the user
import getpass
print("Give me your neo4j password:")
neopass = getpass.getpass()

from neo4j import GraphDatabase
# Connect to the database
uri = "bolt://localhost:7687"
#auth=("neo4j", neopass)
driver = GraphDatabase.driver(uri, auth=("neo4j", neopass))

# Start new session
session = driver.session()

# Start new transaction
transaction = session.begin_transaction()

# Query 1: Find the actor named "Tom Hanks"
result = transaction.run("""
MATCH (tom:Actor {name: 'Tom Hanks'})
RETURN tom
;""")
for record in result:
    print("Query 1 Match: ")
    print (record)

# Query 2: Find the movie with title "Avatar"
result2 = transaction.run("""
MATCH (avatar:Movie {title: 'Avatar'})
RETURN avatar.title
;""")
for record in result2:
    print("Query 2 Match: ")
    print(record)

# Query 3: Find all movies released in the 1990s
start = time.mktime(datetime.datetime.strptime("01/01/1990", "%m/%d/%Y").timetuple()) * 1000
end = time.mktime(datetime.datetime.strptime("12/31/1999", "%m/%d/%Y").timetuple()) * 1000

result3 = transaction.run("""
MATCH (movie:Movie)
WHERE toFloat(movie.releaseDate) > {}
AND toFloat(movie.releaseDate) < {}
RETURN movie.title
;""".format(start, end))
for record in result3:
    print("Query 3 Match: ")
    print(record)

# Query 4: List all Tom Hanks movies
result4 = transaction.run("""
MATCH (movie:Movie) <-[:ACTS_IN]- (tom:Actor)
WHERE tom.name = "Tom Hanks"
RETURN movie.title
;""")
for record in result4:
    print("Query 4 Match: ")
    print(record)

# Query 5: Who directed Avatar
# result5 = transaction.run("""
# MATCH (dir:Director) -[:DIRECTED]-> (movie:Movie)
# WHERE movie.title = "Avatar"
# RETURN dir.name
# ;""")
# for record in result5:
#     print("Query 5 match: ")
#     print(record)
result5 = transaction.run("""
MATCH (avatar {title: 'Avatar'}) <-[:DIRECTED]- (dir)
RETURN dir.name
;""")
for record in result5:
    print("Query 5 match: ")
    print(record)

# Query 6: Tom Hanks' co-actors
result6 = transaction.run("""
MATCH (tom:Actor {name: "Tom Hanks"}) -[:ACTS_IN]-> (movie:Movie) <-[:ACTS_IN]- (actor:Actor)
RETURN actor.name
;""")
for record in result6:
    print("Query 6 match: ")
    print(record)

# Query 7: How (many?) people are related to "Avatar"
result7 = transaction.run("""
MATCH (people:Person) -[relatedTo]- (:Movie {title: 'Avatar'})
RETURN people.name, Type(relatedTo), relatedTo
;""")
for record in result7:
    print("Query 7 match: ")
    print (record)

# Query 8: Extend Tom Hanks co-actors, to find co-co-actors who
# haven't worked with Tom Hanks
result8 = transaction.run("""
MATCH (tom:Actor {name: 'Tom Hanks'}) -[:ACTS_IN]-> (movie) <-[:ACTS_IN]- (actors), (actors) -[:ACTS_IN]-> (movie2) <-[:ACTS_IN]- (coActors)
WHERE NOT (tom) -[:ACTS_IN]-> (movie2)
RETURN coActors.name AS Recommended, count(*) AS Strength
ORDER BY Strength DESC
;""")
for record in result8:
    print("Query 8 match: ")
    print (record)

# Query 9: Find someone to introduce Tom Hanks to Tom Cruise.
result9 = transaction.run("""
MATCH (tom:Actor {name: 'Tom Hanks'}) -[:ACTS_IN]-> (movie) <-[:ACTS_IN]- (actors), (actors) -[:ACTS_IN]-> (movie2) <-[:ACTS_IN]- (cruise:Actor {name: 'Tom Cruise'})
RETURN tom, movie, actors, movie2, cruise
;""")
for record in result9:
    print("Query 9 match: ")
    print (record)
    
transaction.close()
session.close()
