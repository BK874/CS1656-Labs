# Brian Knotten
# CS1656
# Lab 5

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
result3 = transaction.run("""
MATCH (movie:Movie)
WHERE movie.releaseDate >= 1990 and movie.releaseDate <= 1999
RETURN movie.title
;""")
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
result5 = transaction.run("""
MATCH (dir:Director) -[:DIRECTED]-> (movie:Movie)
WHERE movie.title = "Avatar"
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
;""")
for record in result7:
    print("Query 7 match: ")
    print (record)

# Query 8: Extend Tom Hanks co-actors, to find co-co-actors who
# haven't worked with Tom Hanks
result8 = transaction.run("""
;""")
for record in result8:
    print("Query 8 match: ")
    print (record)

# Query 9: Find someone to introduce Tom Hanks to Tom Cruise.
result9 = transaction.run("""
;""")
for record in result9:
    print("Query 9 match: ")
    print (record)
    
transaction.close()
session.close()
