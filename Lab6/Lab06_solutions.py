#CS 1656 – Introduction to Data Science
#Instructor: Alexandros Labrinidis
#Teaching Assistant: Tahereh Arabghalizi
#Lab06

# Use the following to get the neo4j database password from the user
import getpass
print ("Give me your neo4j password:")
neopass = getpass.getpass()
#print ("You typed:", neopass)

from neo4j import GraphDatabase
#Connect to the database
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", neopass))

#Start new session
session = driver.session()

#Start new transaction
transaction = session.begin_transaction()



#Queries
#Q1) Find the actor named "Tom Hanks".


result = transaction.run("""
MATCH (tom:Actor {name: 'Tom Hanks'})
RETURN tom
;""")
for record in result:
    print (record)
"""	
<Record tom=<Node id=524 labels={'Actor', 'Director', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}>>
Tasks
"""


#Q2) Find the movie with title "Avatar".


result = transaction.run("""
MATCH (avatar {title: 'Avatar'})
RETURN avatar
;""")
for record in result:
    print (record)
"""	
<Record avatar=<Node id=345 labels={'Movie'} properties={'studio': 'Twentieth Century Fox Film Corporation', 'releaseDate': '1261090800000', 'imdbId': 'tt0499549', 'runtime': 162, 'description': "Disabled Marine Jake Sully travels to planet Pandora to become an avatar, ingratiate himself with the natives and help Americans mine lucrative unobtainium. But he finds himself in an interstellar conflict after falling for Na'vi warrior Neytiri.", 'language': 'en', 'title': 'Avatar', 'version': 1465, 'trailer': 'http://www.youtube.com/watch?v=aVdO-cx-McA', 'imageUrl': 'http://cf1.imgobject.com/posters/374/4bd29ddd017a3c63e8000374/avatar-mid.jpg', 'genre': 'Action', 'tagline': 'Enter the World of Pandora', 'lastModified': '1300200001000', 'id': '19995', 'homepage': 'http://www.avatarmovie.com/'}>>
"""

#Q3) Find movies released in the 1990s.


import time
import datetime
​
start = time.mktime(datetime.datetime.strptime("01/01/1990", "%m/%d/%Y").timetuple())*1000
end = time.mktime(datetime.datetime.strptime("12/31/1999", "%m/%d/%Y").timetuple())*1000
​
result = transaction.run("""
MATCH (nineties:Movie)
WHERE toFloat(nineties.releaseDate) > {}
AND toFloat(nineties.releaseDate) < {}
RETURN nineties.title
;""".format(start, end))
for record in result:
    print (record)
"""	
<Record nineties.title='Independence Day'>
<Record nineties.title='The Matrix'>
<Record nineties.title='Men In Black'>
<Record nineties.title='Forrest Gump'>
<Record nineties.title='Star Wars: Episode I - The Phantom Menace'>
<Record nineties.title='Star Trek: Generations'>
<Record nineties.title='Star Trek: Insurrection'>
<Record nineties.title='Apollo 13'>
<Record nineties.title='Philadelphia'>
<Record nineties.title='The Green Mile'>
<Record nineties.title='Leon: The Professional'>
<Record nineties.title='Four Rooms'>
<Record nineties.title='Judgment Night'>
<Record nineties.title='American Beauty'>
<Record nineties.title='The Fifth Element'>
<Record nineties.title='Magnetic Rose'>
<Record nineties.title='Cannon Fodder'>
<Record nineties.title='Unforgiven'>
<Record nineties.title='12 Monkeys'>
<Record nineties.title='Absolute Power'>
<Record nineties.title='American History X'>
<Record nineties.title='Mars Attacks!'>
<Record nineties.title='Before Sunrise'>
<Record nineties.title='Megacities'>
<Record nineties.title='Armageddon'>
<Record nineties.title='All About My Mother'>
<Record nineties.title='Lock, Stock and Two Smoking Barrels'>
<Record nineties.title='Run Lola Run'>
<Record nineties.title='Three Colours: Blue'>
<Record nineties.title='Three Colours: White'>
<Record nineties.title='Three Colours: Red'>
<Record nineties.title='Pretty Woman'>
<Record nineties.title='The Big Lebowski'>
<Record nineties.title='Princess Mononoke'>
<Record nineties.title='Groundhog Day'>
<Record nineties.title='Mifunes Sidste Sang'>
<Record nineties.title='Breaking The Waves'>
<Record nineties.title="Knockin' On Heaven's Door">
<Record nineties.title='Der Bewegte Mann'>
<Record nineties.title='Edward Scissorhands'>
<Record nineties.title='Predator 2'>
<Record nineties.title='Star Trek VI: The Undiscovered Country'>
<Record nineties.title='The Fisher King'>
<Record nineties.title='Blown Away'>
<Record nineties.title='Jackie Brown'>
<Record nineties.title='Back to the Future Part III'>
<Record nineties.title='Braveheart'>
<Record nineties.title='Star Trek: First Contact'>
<Record nineties.title="Boys Don't Cry">
<Record nineties.title="Muriel's Wedding">
<Record nineties.title='Natural Born Killers'>
<Record nineties.title='The Godfather: Part III'>
<Record nineties.title='In China They Eat Dogs'>
<Record nineties.title='Ghost'>
<Record nineties.title='Live Flesh'>
<Record nineties.title='The Silence of the Lambs'>
<Record nineties.title='Fargo'>
<Record nineties.title='The Shawshank Redemption'>
<Record nineties.title='Terminator 2: Judgment Day'>
<Record nineties.title='Strange Days'>
<Record nineties.title='Barton Fink'>
<Record nineties.title='A River Runs Through It'>
<Record nineties.title='Meet Joe Black'>
<Record nineties.title='Beverly Hills Cop III'>
<Record nineties.title='The Celebration'>
<Record nineties.title='Jenseits Der Stille'>
<Record nineties.title='True Romance'>
<Record nineties.title='Jurassic Park'>
<Record nineties.title='The Lost World: Jurassic Park'>
<Record nineties.title='Inspector Gadget'>
<Record nineties.title='Magnolia'>
<Record nineties.title='Night on Earth'>
<Record nineties.title='Bang Boom Bang'>
<Record nineties.title='Eyes Wide Shut'>
<Record nineties.title='Batman Returns'>
<Record nineties.title="Miller's Crossing">
<Record nineties.title='Lisbon Story'>
<Record nineties.title='French Kiss'>
<Record nineties.title="Things to Do in Denver When You're Dead">
<Record nineties.title='Basic Instinct'>
<Record nineties.title='The Straight Story'>
<Record nineties.title='The Hate'>
<Record nineties.title='The English Patient'>
<Record nineties.title='Batman Forever'>
<Record nineties.title='Batman & Robin'>
<Record nineties.title="Schindler's List">
<Record nineties.title='Cube'>
<Record nineties.title='Leaving Las Vegas'>
<Record nineties.title='The Idiots'>
<Record nineties.title='Romeo + Juliet'>
<Record nineties.title='My Own Private Idaho'>
<Record nineties.title='Bandyta'>
<Record nineties.title='Pi'>
<Record nineties.title='Wild at Heart'>
<Record nineties.title='Good Will Hunting'>
<Record nineties.title='Being John Malkovich'>
<Record nineties.title='Reservoir Dogs'>
<Record nineties.title='Killing Zoe'>
<Record nineties.title='Notting Hill'>
<Record nineties.title='Fire'>
<Record nineties.title='Ed Wood'>
<Record nineties.title='Casino'>
<Record nineties.title='Once Were Warriors'>
<Record nineties.title='Wallace & Gromit: The Wrong Trousers'>
<Record nineties.title='Wallace & Gromit: A Close Shave'>
<Record nineties.title="There's Something About Mary">
<Record nineties.title='The Horse Whisperer'>
<Record nineties.title='Basquiat'>
<Record nineties.title='Fight Club'>
<Record nineties.title='Starship Troopers'>
<Record nineties.title='The Mummy'>
<Record nineties.title='To Die For'>
<Record nineties.title='Dances with Wolves'>
<Record nineties.title='Wag the Dog'>
<Record nineties.title='Titanic'>
<Record nineties.title='Wild Things'>
<Record nineties.title='The Bodyguard'>
<Record nineties.title='The Ninth Gate'>
<Record nineties.title='Trainspotting'>
<Record nineties.title='Interview with the Vampire'>
<Record nineties.title='The Usual Suspects'>
<Record nineties.title='Life Is Beautiful'>
<Record nineties.title='Lost Highway'>
<Record nineties.title='Boyz N The Hood'>
<Record nineties.title='Twister'>
<Record nineties.title='Central do Brasil'>
<Record nineties.title='Pulp Fiction'>
<Record nineties.title='Contact'>
<Record nineties.title='Dead Man Walking'>
<Record nineties.title='The Bridges Of Madison County'>
<Record nineties.title='Short Cuts'>
<Record nineties.title='GoldenEye'>
<Record nineties.title='Four Weddings And A Funeral'>
<Record nineties.title='The Piano'>
<Record nineties.title='Tomorrow Never Dies'>
<Record nineties.title='Zugvögel – einmal nach Inari'>
<Record nineties.title='The Sixth Sense'>
<Record nineties.title='Face/Off'>
<Record nineties.title='From Dusk Till Dawn'>
<Record nineties.title='Braindead'>
<Record nineties.title='Army of Darkness'>
<Record nineties.title='Goodfellas'>
<Record nineties.title='Home Alone'>
<Record nineties.title='Home Alone 2: Lost in New York'>
<Record nineties.title='Winterschläfer'>
<Record nineties.title='Gattaca'>
<Record nineties.title='Kolja'>
<Record nineties.title='Mrs. Doubtfire'>
<Record nineties.title='City of Angels'>
<Record nineties.title='Cruel Intentions'>
<Record nineties.title='Pünktchen und Anton'>
<Record nineties.title='Se7en'>
<Record nineties.title='Aladdin'>
<Record nineties.title='Animal Farm'>
<Record nineties.title='Austin Powers: International Man of Mystery'>
<Record nineties.title='Austin Powers: The Spy Who Shagged Me'>
<Record nineties.title='Sleepers'>
<Record nineties.title='JFK'>
<Record nineties.title='Jin-Roh: The Wolf Brigade'>
<Record nineties.title='Playing by Heart'>
<Record nineties.title='The X-Files: Fight the Future'>
<Record nineties.title='The Mask'>
<Record nineties.title='Saving Private Ryan'>
<Record nineties.title='Sleepless in Seattle'>
<Record nineties.title='Total Recall'>
<Record nineties.title='Toy Story'>
<Record nineties.title='Toy Story 2'>
<Record nineties.title='Cool Runnings'>
<Record nineties.title='Sliver'>
<Record nineties.title='Hook'>
<Record nineties.title='Antonia'>
<Record nineties.title='A Few Good Men'>
<Record nineties.title='Crash'>
<Record nineties.title='The Flintstones'>
<Record nineties.title='Schlafes Bruder'>
<Record nineties.title='Delicatessen'>
<Record nineties.title='The City of the Lost Children'>
<Record nineties.title='The Thomas Crown Affair'>
<Record nineties.title='Dead Man'>
<Record nineties.title='Galaxy Quest'>
<Record nineties.title='Gremlins 2: The New Batch'>
<Record nineties.title='Godzilla'>
<Record nineties.title='Lethal Weapon 3'>
<Record nineties.title='Lethal Weapon 4'>
<Record nineties.title='Heat'>
<Record nineties.title='Kindergarten Cop'>
<Record nineties.title='Mission: Impossible'>
<Record nineties.title='Seven Years in Tibet'>
<Record nineties.title='Heavenly Creatures'>
<Record nineties.title='Die Siebtelbauern'>
<Record nineties.title='Sommersby'>
<Record nineties.title='Arlington Road'>
<Record nineties.title='Black Cat, White Cat'>
<Record nineties.title='Point Break'>
<Record nineties.title='The Thirteenth Floor'>
<Record nineties.title='The Talented Mr. Ripley'>
<Record nineties.title='The Remains of the Day'>
<Record nineties.title='Gloomy Sunday'>
<Record nineties.title='Bean'>
<Record nineties.title='Torrente - El Brazo Tonto de la Ley'>
<Record nineties.title='A Brief History of Time'>
<Record nineties.title='The Hi-Lo Country'>
<Record nineties.title='Rocky V'>
<Record nineties.title='Out of Sight'>
<Record nineties.title='City Slickers'>
<Record nineties.title='Cutthroat Island'>
<Record nineties.title='The Rapture'>
<Record nineties.title='M. Butterfly'>
<Record nineties.title='Lovers of the Arctic Circle'>
<Record nineties.title='Anna and the King'>
<Record nineties.title='The Virgin Suicides'>
<Record nineties.title='The Wisdom of Crocodiles'>
<Record nineties.title='Clean, Shaven'>
<Record nineties.title='Metal Skin'>
<Record nineties.title='Laws of Gravity'>
<Record nineties.title='Begotten'>
<Record nineties.title='Der Totmacher'>
<Record nineties.title='1492: Conquest of Paradise'>
<Record nineties.title='Cool As Ice'>
<Record nineties.title='Teenage Mutant Ninja Turtles II: The Secret of the Ooze'>
<Record nineties.title='Teenage Mutant Ninja Turtles'>
<Record nineties.title='Teenage Mutant Ninja Turtles III'>
<Record nineties.title='Thelma & Louise'>
<Record nineties.title='Office Space'>
<Record nineties.title='Flatliners'>
<Record nineties.title='23'>
<Record nineties.title='I Stand Alone'>
<Record nineties.title='Carne'>
<Record nineties.title='Pig'>
<Record nineties.title='Die Hard with a Vengeance'>
<Record nineties.title='Die Hard 2'>
<Record nineties.title="What's Eating Gilbert Grape">
<Record nineties.title='Primal Fear'>
<Record nineties.title='Cape Fear'>
<Record nineties.title='The Double Life of Veronique'>
<Record nineties.title='A Bronx Tale'>
<Record nineties.title='When Saturday Comes'>
<Record nineties.title='Fever Pitch'>
<Record nineties.title='Still Crazy'>
<Record nineties.title='Liar Liar'>
<Record nineties.title='The People vs. Larry Flynt'>
<Record nineties.title='Une Vraie Jeune Fille'>
<Record nineties.title='Fried Green Tomatoes'>
<Record nineties.title='Free Willy'>
<Record nineties.title='Speed'>
<Record nineties.title='Speed 2: Cruise Control'>
<Record nineties.title='Forces of Nature'>
<Record nineties.title='The Net'>
<Record nineties.title='The Vanishing'>
<Record nineties.title='A Time to Kill'>
<Record nineties.title="Bill & Ted's Bogus Journey">
<Record nineties.title='00 Schneider - Jagd auf Nihil Baxter'>
<Record nineties.title='Praxis Dr. Hasenbein'>
<Record nineties.title='Texas - Doc Snyder hält die Welt in Atem'>
<Record nineties.title='Absolute Giganten'>
<Record nineties.title='State of Grace'>
<Record nineties.title='The Hunt for Red October'>
<Record nineties.title='Little Buddha'>
<Record nineties.title='Misery'>
<Record nineties.title='Con Air'>
<Record nineties.title='Death Machine'>
<Record nineties.title='Copycat'>
<Record nineties.title='No Code of Conduct'>
<Record nineties.title='Jungle Fever'>
<Record nineties.title='The Cider House Rules'>
<Record nineties.title='Bird on a Wire'>
<Record nineties.title='Michael Collins'>
<Record nineties.title='City of Hope'>
<Record nineties.title='The Big One'>
<Record nineties.title='Canadian Bacon'>
<Record nineties.title='May Fools'>
<Record nineties.title='La cérémonie'>
<Record nineties.title='Velvet Goldmine'>
<Record nineties.title='Nowhere'>
<Record nineties.title='Trick'>
<Record nineties.title="Devil's Advocate">
<Record nineties.title='Dogma'>
<Record nineties.title='Alias'>
<Record nineties.title='Entrapment'>
<Record nineties.title='Poddle Springs'>
<Record nineties.title='Man on the Moon'>
<Record nineties.title='Beyond Rangoon'>
<Record nineties.title='Dr. Mordrid'>
<Record nineties.title='Fear and Loathing in Las Vegas'>
<Record nineties.title='Les yeux dans les bleus'>
<Record nineties.title='Malcolm X'>
<Record nineties.title='Open Your Eyes'>
<Record nineties.title='Don Juan DeMarco'>
<Record nineties.title='The 13th Warrior'>
<Record nineties.title='Manta, Manta'>
<Record nineties.title='Twin Peaks: Fire Walk With Me'>
<Record nineties.title='Shakespeare in Love'>
<Record nineties.title='Nell'>
<Record nineties.title='eXistenZ'>
<Record nineties.title='Swept from the Sea'>
<Record nineties.title='A Perfect Murder'>
<Record nineties.title='Fools Rush In'>
<Record nineties.title="Benny's Video">
<Record nineties.title='Sister Act'>
<Record nineties.title="Lorenzo's Oil">
<Record nineties.title='Hard Target'>
<Record nineties.title='The Bachelor'>
<Record nineties.title='Jack & Sarah'>
<Record nineties.title='Infinity'>
<Record nineties.title='Touch and Die'>
<Record nineties.title='Iron Eagle III'>
<Record nineties.title='Savior'>
<Record nineties.title='Unforgettable'>
<Record nineties.title='The Real McCoy'>
<Record nineties.title="Mr. Holland's Opus">
<Record nineties.title='Addicted to Love'>
<Record nineties.title='Pusher'>
<Record nineties.title='While You Were Sleeping'>
<Record nineties.title='Shattered'>
<Record nineties.title='Cyberjack'>
<Record nineties.title='Flirting with Disaster'>
<Record nineties.title='Nick of Time'>
<Record nineties.title='The Getaway'>
<Record nineties.title='Romeo is Bleeding'>
<Record nineties.title='The Heist'>
<Record nineties.title='Tycus'>
<Record nineties.title='Solar Crisis'>
<Record nineties.title='American Pie'>
<Record nineties.title='L.A. Story'>
<Record nineties.title='Rush Hour'>
<Record nineties.title='Payback'>
<Record nineties.title='L.A. Confidential'>
<Record nineties.title='Days of Thunder'>
<Record nineties.title='Color of Night'>
<Record nineties.title='Wedlock'>
<Record nineties.title='Hostile Waters'>
<Record nineties.title='The Storm Riders'>
<Record nineties.title='Berlin Snuff'>
<Record nineties.title='Cop Land'>
<Record nineties.title="Carla's Song">
<Record nineties.title='The Flickering Flame'>
<Record nineties.title='Body of Evidence'>
<Record nineties.title='Lost in Space'>
<Record nineties.title='Chill Factor'>
<Record nineties.title='Breakdown'>
<Record nineties.title='Stargate'>
<Record nineties.title='The Revengers Comedies'>
<Record nineties.title='Manta - Der Film'>
<Record nineties.title='Maus und Katz'>
<Record nineties.title='Alles nur Tarnung'>
<Record nineties.title='Aimee & Jaguar'>
<Record nineties.title='Nightwatch'>
<Record nineties.title='Zerschmetterte Träume - Eine Liebe in Fesseln'>
<Record nineties.title='Sonnenallee'>
<Record nineties.title='Malice'>
<Record nineties.title='Chasing Amy'>
<Record nineties.title='Utz'>
<Record nineties.title='The House of the Spirits'>
<Record nineties.title="The General's Daughter">
<Record nineties.title='Bicentennial Man'>
<Record nineties.title='Jakob the Liar'>
<Record nineties.title="Jacob's Ladder">
<Record nineties.title='Clerks'>
<Record nineties.title='Mallrats'>
<Record nineties.title='Kafka'>
<Record nineties.title='Der Kinoerzähler'>
<Record nineties.title='Space Jam'>
<Record nineties.title='Avalon'>
<Record nineties.title='Gespräch mit dem Biest'>
<Record nineties.title="A Pyromaniac's Love Story">
<Record nineties.title='Hurenglück'>
<Record nineties.title='Executive Decision'>
<Record nineties.title='Sneakers'>
<Record nineties.title='Wilsberg - Und die Toten lässt man ruhen'>
<Record nineties.title='Taxi'>
<Record nineties.title='Jesus'>
<Record nineties.title='Holy Matrimony'>
<Record nineties.title='Le Radeau de la Méduse'>
<Record nineties.title='Bonsoir'>
<Record nineties.title="Tableau d'honneur">
<Record nineties.title='Fallout'>
<Record nineties.title='Eugénie Grandet'>
<Record nineties.title='Joseph'>
<Record nineties.title='Double Dragon'>
<Record nineties.title='Vacas'>
<Record nineties.title='The Final Cut'>
<Record nineties.title='La Ardilla roja'>
<Record nineties.title='Le bonheur des autres'>
<Record nineties.title='Porté disparu'>
<Record nineties.title='Harley Davidson and the Marlboro Man'>
<Record nineties.title='Tierra'>
<Record nineties.title='Running Out of Time'>
<Record nineties.title='Tie Me Up! Tie Me Down!'>
<Record nineties.title='Belle Époque'>
<Record nineties.title='Madame Bovary'>
<Record nineties.title='Hola, ¿estás sola?'>
<Record nineties.title='Joe Versus the Volcano'>
<Record nineties.title='Only the Lonely'>
<Record nineties.title='Mr. Destiny'>
<Record nineties.title='Prelude to a Kiss'>
<Record nineties.title='Mr. Jones'>
<Record nineties.title='The Specialist'>
<Record nineties.title='Deconstructing Harry'>
<Record nineties.title='The Game'>
<Record nineties.title='In the Mouth of Madness'>
<Record nineties.title='Pleasantville'>
<Record nineties.title='Dark City'>
<Record nineties.title='The Blair Witch Project'>
<Record nineties.title='Sleepy Hollow'>
<Record nineties.title='It'>
<Record nineties.title='Ring'>
<Record nineties.title='Memoirs of an Invisible Man'>
<Record nineties.title='Titanic'>
<Record nineties.title='Esther'>
<Record nineties.title='Abraham'>
<Record nineties.title='Genesi: La creazione e il diluvio'>
<Record nineties.title='Jacob'>
<Record nineties.title='Moses'>
<Record nineties.title='Indochine'>
<Record nineties.title='David'>
<Record nineties.title='Naked Lunch'>
<Record nineties.title='The Borrowers'>
<Record nineties.title='fl 19,99'>
<Record nineties.title='3 Misses'>
<Record nineties.title='Addams Family Values'>
<Record nineties.title='The Adventures of Priscilla, Queen of the Desert'>
<Record nineties.title='Ah Pook Is Here'>
<Record nineties.title='All Stars'>
<Record nineties.title='Les Amants du Pont-Neuf'>
<Record nineties.title='The Birdcage Inn'>
<Record nineties.title='Clifford'>
<Record nineties.title='Reality Bites'>
<Record nineties.title='Same Old Song'>
<Record nineties.title='And the Band Played On'>
<Record nineties.title='An Angel at My Table'>
<Record nineties.title='Angel Baby'>
<Record nineties.title='The Apostle'>
<Record nineties.title='As Good as It Gets'>
<Record nineties.title="The Astronaut's Wife">
<Record nineties.title='Au petit Marguery'>
<Record nineties.title='The Addams Family'>
<Record nineties.title='B. Monkey'>
<Record nineties.title='Backdraft'>
<Record nineties.title='The First Wives Club'>
<Record nineties.title='Moon 44'>
<Record nineties.title='Michael'>
<Record nineties.title='20.000 Leagues Under the Sea'>
<Record nineties.title='20.000 Leagues Under the Sea'>
<Record nineties.title='The Lost World'>
<Record nineties.title='Pacific Heights'>
<Record nineties.title='Appetite'>
<Record nineties.title='The Lost World'>
<Record nineties.title='The Lost World'>
<Record nineties.title='The Lost World'>
<Record nineties.title='Gods and Monsters'>
<Record nineties.title='Frankenstein'>
<Record nineties.title='Frankenstein'>
<Record nineties.title='Ace Ventura: Pet Detective'>
<Record nineties.title='Doctor Dolittle'>
<Record nineties.title='Frankenstein'>
<Record nineties.title='Mystery Science Theater 3000: The Movie'>
<Record nineties.title='Frankenstein Unbound'>
<Record nineties.title='I Love You to Death'>
<Record nineties.title='House of Frankenstein'>
<Record nineties.title='Frankenstein and Me'>
<Record nineties.title='Alvin and the Chipmunks meet Frankenstein'>
<Record nineties.title="Rock 'n' Roll Frankenstein">
<Record nineties.title='The Frankenstein Files: How Hollywood Made a Monster'>
<Record nineties.title="Making Frankensense of 'Young Frankenstein'">
<Record nineties.title='Bangkok Dangerous'>
<Record nineties.title='Beavis and Butt-Head Do America'>
<Record nineties.title='Billy Frankenstein'>
<Record nineties.title="She's Alive! Creating the Bride of Frankenstein">
<Record nineties.title='No Telling'>
<Record nineties.title='100 Years of Horror: The Frankenstein Family'>
<Record nineties.title='100 Years of Horror: Baron Frankenstein'>
<Record nineties.title='Monster Mash: The Movie'>
<Record nineties.title="It's Alive: The True Story of Frankenstein">
<Record nineties.title='Frankenstein: The College Years'>
<Record nineties.title='Lust for Frankenstein'>
<Record nineties.title='Pirates of Silicon Valley'>
<Record nineties.title='Frankenstein: A Cinematic Scrapbook'>
<Record nineties.title='Atomic Samurai'>
<Record nineties.title='Frankenstein Reborn!'>
<Record nineties.title='Boy Frankenstein'>
<Record nineties.title='Ritorno dalla morte'>
<Record nineties.title='MacGyver: Lost Treasure of Atlantis'>
<Record nineties.title='Under Siege 2: Dark Territory'>
<Record nineties.title='Legionnaire'>
<Record nineties.title='Lebensborn'>
<Record nineties.title='Girl, Interrupted'>
<Record nineties.title='Emma'>
<Record nineties.title='Clockmaker'>
<Record nineties.title='Prêt-à-porter'>
<Record nineties.title='Bogus'>
<Record nineties.title='A River Made to Drown in'>
<Record nineties.title='Ransom'>
<Record nineties.title='I Know What You Did Last Summer'>
<Record nineties.title='I Still Know What You Did Last Summer'>
<Record nineties.title='54'>
<Record nineties.title='Flesh Gordon meets the Cosmic Cheerleaders'>
<Record nineties.title='Frankie and Johnny'>
<Record nineties.title='El Camino de las Hormigas'>
<Record nineties.title='Primavera'>
<Record nineties.title='Jam Dwór Polski'>
<Record nineties.title='My Girl'>
<Record nineties.title='Benny & Joon'>
<Record nineties.title='Checkpoint'>
<Record nineties.title='Three Seasons'>
<Record nineties.title='Les petites bonnes'>
<Record nineties.title='Lenin: The Train'>
<Record nineties.title='Oh, what a Night'>
<Record nineties.title='The Scary Movie'>
<Record nineties.title='Scary Texas Movie'>
<Record nineties.title='Scream'>
<Record nineties.title='Scream 2'>
<Record nineties.title='Titanic 2000'>
<Record nineties.title='Ma vie est un enfer'>
<Record nineties.title='Serial Lover'>
<Record nineties.title='Nach Fünf im Urwald'>
<Record nineties.title='Kikujiro no natsu'>
<Record nineties.title='Monsieur Truffaut Meets Mr. Hitchcock'>
<Record nineties.title='The Flower of My Secret'>
<Record nineties.title="The Birds II: Land's End">
<Record nineties.title='I Woke Up Early The Day I Died'>
<Record nineties.title='The Nasty Girl'>
<Record nineties.title="L'Autrichienne">
<Record nineties.title='Dallas Doll'>
<Record nineties.title='Rosemarie Nitribitt - Tod einer Edelhure'>
<Record nineties.title='Das Mädchen Rosemarie'>
<Record nineties.title='Les Miserables'>
<Record nineties.title='G.I. Jane'>
<Record nineties.title='Der große Abgang'>
<Record nineties.title='Frauenmörder Arved Imiela'>
<Record nineties.title='Das Phantom - Die Jagd nach Dagobert'>
<Record nineties.title='Legends of the Fall'>
<Record nineties.title="The Devil's Own">
<Record nineties.title='Indecent Proposal'>
<Record nineties.title='French Twist'>
<Record nineties.title='Tod der Engel'>
<Record nineties.title='Jamón, jamón'>
<Record nineties.title='Elizabeth'>
<Record nineties.title="Hearts of Darkness: A Filmmaker's Apocalypse">
<Record nineties.title='The Count of Monte Cristo'>
<Record nineties.title='Hot Chocolate'>
<Record nineties.title='Sense and Sensibility'>
<Record nineties.title='Mermaids'>
<Record nineties.title='Die Sieger'>
<Record nineties.title='Fleur bleue'>
<Record nineties.title='La Vie des morts'>
<Record nineties.title='Pappa ante Portas'>
<Record nineties.title='Body Snatchers'>
<Record nineties.title='Van Gogh'>
<Record nineties.title='Heart of Darkness'>
<Record nineties.title='Runaway Bride'>
<Record nineties.title='Ghost Dog: The Way of the Samurai'>
<Record nineties.title='Final Analysis'>
<Record nineties.title='The Jackal'>
<Record nineties.title='Guilty as Sin'>
<Record nineties.title='Edge of Seventeen'>
<Record nineties.title='10 Things I Hate About You'>
<Record nineties.title='Drop Zone'>
<Record nineties.title='Mimic'>
<Record nineties.title='Adieu, plancher des vaches!'>
<Record nineties.title='Pan Tadeusz'>
<Record nineties.title='Love Is the Devil: Study for a Portrait of Francis Bacon'>
<Record nineties.title="L'homme sur les quais">
<Record nineties.title='Boogie Nights'>
<Record nineties.title="Prospero's Books">
<Record nineties.title='The Baby of Mâcon'>
<Record nineties.title='I Love Vienna'>
<Record nineties.title="La tête en l'air">
<Record nineties.title='The Crazy Stranger'>
<Record nineties.title="Coupable d'innocence ou Quand la raison dort">
<Record nineties.title='Prorva'>
<Record nineties.title='Jean Galmot, aventurier'>
<Record nineties.title='Combat de fauves'>
<Record nineties.title="Beretta's Island">
<Record nineties.title='Marquise'>
<Record nineties.title='Schulz & Schulz II: Aller Anfang ist schwer'>
<Record nineties.title='Schulz & Schulz IV: Neue Welten, alte Lasten'>
<Record nineties.title='Scandal: On the Other Side'>
<Record nineties.title='Three of Hearts'>
<Record nineties.title='Carnal Cruise'>
<Record nineties.title='Two Shades of Blue'>
<Record nineties.title='Red Shoe Diaries'>
<Record nineties.title='Dust Devil'>
<Record nineties.title='Red Shoe Diaries 2: Double Dare'>
<Record nineties.title="Red Shoe Diaries 3: Another Woman's Lipstick">
<Record nineties.title='Red Shoe Diaries 4: Auto Erotica'>
<Record nineties.title='Gengis Khan'>
<Record nineties.title='Pleasurecraft'>
<Record nineties.title='Virtual Sexuality'>
<Record nineties.title='Red Shoe Diaries 5: Weekend Pass'>
<Record nineties.title='Red Shoe Diaries 16: Temple of Flesh'>
<Record nineties.title='Red Shoe Diaries 6: How i met my Husband'>
<Record nineties.title="You're Dead">
<Record nineties.title='Red Shoe Diaries 10: Slow Train'>
<Record nineties.title='Red Shoe Diaries 9: Hotline'>
<Record nineties.title='Red Shoe Diaries 8: Night of Abandon'>
<Record nineties.title='Red Shoe Diaries 7: Burning Up'>
<Record nineties.title="Red Shoe Diaries 11: Farmer's Daughter">
<Record nineties.title='Red Shoe Diaries 13: Four on the Floor'>
<Record nineties.title="Without You I'm Nothing">
<Record nineties.title='Hum Dil De Chuke Sanam'>
<Record nineties.title='Dancing at Lughnasa'>
<Record nineties.title='Beowulf'>
<Record nineties.title='Animated Epics: Beowulf'>
<Record nineties.title='Not Mozart: Letters, Riddles and Writs'>
<Record nineties.title='Intimate Nights'>
<Record nineties.title='The Fugitive'>
<Record nineties.title='Finders, Keepers'>
<Record nineties.title='Dead Weekend'>
<Record nineties.title='RoboCop 2'>
<Record nineties.title='RoboCop 3'>
<Record nineties.title="Hollywood Rated 'R'">
<Record nineties.title='Playboy: Voluptuous Vixens'>
<Record nineties.title='Wet and Wild Summer'>
<Record nineties.title='Hunks in Hedonism'>
<Record nineties.title='Perfect Lies'>
<Record nineties.title='Playboy: The Story of X'>
<Record nineties.title='Playboy: Voluptuous Vixens II'>
<Record nineties.title='Acting on Impulse'>
<Record nineties.title='Sher Mountain Killings Mystery'>
<Record nineties.title='Liebe ist Geschmackssache'>
<Record nineties.title='Playboy: 101 Ways to Excite Your Lover'>
<Record nineties.title='Possessed by the Night'>
<Record nineties.title='Center of the Web'>
<Record nineties.title='Man of the Year'>
<Record nineties.title='Hardball'>
<Record nineties.title='The Mummy Lives'>
<Record nineties.title='Knight Moves'>
<Record nineties.title='Slaves of Sin'>
<Record nineties.title='Schöne Bescherung'>
<Record nineties.title='St. Pauli Nacht'>
<Record nineties.title='Heat After Dark'>
<Record nineties.title='Der Hurenstreik - Eine Liebe auf St. Pauli'>
<Record nineties.title='Heidi und Erni: Wahnsinnig romantisch'>
<Record nineties.title='Blue in the Face'>
<Record nineties.title='Brain Dead'>
<Record nineties.title='De Noorderlingen'>
<Record nineties.title='De jurk'>
<Record nineties.title='The Ice Storm'>
<Record nineties.title='Fireworks'>
<Record nineties.title='St. Pauli in St. Peter'>
<Record nineties.title='Rothenbaumchaussee'>
<Record nineties.title='Es geschah am hellichten Tag'>
<Record nineties.title='Also schlafwandle ich am hellichten Tage'>
<Record nineties.title='Charleys Tante'>
<Record nineties.title='The Patriot'>
<Record nineties.title='Six Days Seven Nights'>
<Record nineties.title='Kiss of Death'>
<Record nineties.title='One Eight Seven'>
<Record nineties.title="Carlito's Way">
<Record nineties.title="Bram Stoker's Dracula">
<Record nineties.title='Spice World'>
<Record nineties.title='Can I Be Your Bratwurst, Please?'>
<Record nineties.title='Glatteis'>
<Record nineties.title='Sisi und der Kaiserkuß'>
<Record nineties.title='Dreamcatcher'>
<Record nineties.title='The Dream Catcher'>
<Record nineties.title='Nettoyage à sec'>
<Record nineties.title='Pizza Colonia'>
<Record nineties.title='Prince Valiant'>
<Record nineties.title='Sister Act 2: Back in the Habit'>
<Record nineties.title='Junior'>
<Record nineties.title='Mousehunt'>
<Record nineties.title='The Chamber'>
<Record nineties.title='Der Weihnachtsmörder'>
<Record nineties.title='The Very Thought of You'>
<Record nineties.title='Fröhlich Geschieden'>
<Record nineties.title='Meine beste Feindin'>
<Record nineties.title='Taking Care of Business'>
<Record nineties.title='SLC Punk'>
<Record nineties.title='Three Kings'>
<Record nineties.title='Die Ratte'>
<Record nineties.title='Practical Magic'>
<Record nineties.title='Star Command'>
<Record nineties.title='Till the End of the Night'>
<Record nineties.title='Tatie Danielle'>
<Record nineties.title="Other People's Money">
<Record nineties.title='Premières neiges'>
<Record nineties.title='The Takeover'>
<Record nineties.title='Guarding Tess'>
<Record nineties.title='Melissa'>
<Record nineties.title='Melissa'>
<Record nineties.title='Arachnophobia'>
<Record nineties.title='Nattevagten'>
<Record nineties.title='Turbo: A Power Rangers Movie'>
<Record nineties.title='First Knight'>
<Record nineties.title='Life'>
<Record nineties.title='Life Stinks'>
<Record nineties.title='Schtonk!'>
<Record nineties.title='Idle Hands'>
<Record nineties.title='Wir können auch anders ...'>
<Record nineties.title='Die Architekten'>
<Record nineties.title='Der Tag des Jorun'>
<Record nineties.title='Godzilla vs. Mechagodzilla II'>
<Record nineties.title='Dancing with Danger'>
<Record nineties.title='The Peacemaker'>
<Record nineties.title='The Cure'>
<Record nineties.title='The Rookie'>
<Record nineties.title='Homeward Bound: The Incredible Journey'>
<Record nineties.title='For Those who hunt the Wounded down'>
<Record nineties.title='Outbreak'>
<Record nineties.title='Welcome to Woop Woop'>
<Record nineties.title='Horse Sense'>
<Record nineties.title='Rising Sun'>
<Record nineties.title='American Heart'>
<Record nineties.title='Jack'>
<Record nineties.title='Merlin'>
<Record nineties.title='Vendetta II: The New Mafia'>
<Record nineties.title='Search for the Jewel of Polaris: Mysterious Museum'>
<Record nineties.title='One Fine Day'>
<Record nineties.title='Alive'>
<Record nineties.title='The Rage: Carrie 2'>
<Record nineties.title='Sleeping with the Enemy'>
<Record nineties.title='Einfach nur Liebe'>
<Record nineties.title='Sonatine'>
<Record nineties.title='Earth'>
<Record nineties.title='The Time Shifters'>
<Record nineties.title='Shine'>
<Record nineties.title='Blackfire'>
<Record nineties.title='Return 1993'>
<Record nineties.title='The Match Factory Girl'>
<Record nineties.title='I Hired a Contract Killer'>
<Record nineties.title='In the Name of the Father'>
<Record nineties.title='Robin Hood: Men in Tights'>
<Record nineties.title='Highlander II: The Quickening'>
<Record nineties.title='Highlander III: The Sorcerer'>
<Record nineties.title='Get Shorty'>
<Record nineties.title='Ich bin meine eigene Frau'>
<Record nineties.title='Hard Eight'>
<Record nineties.title='Train de vie'>
<Record nineties.title='A Life Less Ordinary'>
<Record nineties.title='Desperado'>
<Record nineties.title='Tuvalu'>
<Record nineties.title='Alien 3'>
<Record nineties.title='Alien Resurrection'>
<Record nineties.title="This Boy's Life">
<Record nineties.title='My Name Is Joe'>
<Record nineties.title='Ronin'>
<Record nineties.title='Midnight in the Garden of Good and Evil'>
<Record nineties.title='Kauas pilvet karkaavat'>
<Record nineties.title='Meet the Feebles'>
<Record nineties.title='Alice'>
<Record nineties.title='Kika'>
<Record nineties.title='8MM'>
<Record nineties.title='Poetic Justice'>
<Record nineties.title='Howards End'>
<Record nineties.title='The Naked Man'>
<Record nineties.title='Robin Hood: Prince Of Thieves'>
<Record nineties.title='The Boondock Saints'>
<Record nineties.title='Trahir'>
<Record nineties.title='Asfalt Tango'>
<Record nineties.title='Airboss'>
<Record nineties.title='When night is falling'>
<Record nineties.title='Event Horizon'>
<Record nineties.title='Swallowtail Butterfly'>
<Record nineties.title='Pump up the Volume'>
<Record nineties.title='Murder in the First'>
<Record nineties.title='Quem matou Pixote?'>
<Record nineties.title='Angels and Insects'>
<Record nineties.title='Top of the Food Chain'>
<Record nineties.title='Dumb & Dumber'>
<Record nineties.title='Highway 61'>
<Record nineties.title='Wild Wild West'>
<Record nineties.title="Weekend at Bernie's II">
<Record nineties.title='Devil in a Blue Dress'>
<Record nineties.title='Little Voice'>
<Record nineties.title='¿Bin ich schön?'>
<Record nineties.title='Schlaraffenland'>
<Record nineties.title='Dangerous Beauty'>
<Record nineties.title='The Lion King'>
<Record nineties.title='Dick Tracy'>
<Record nineties.title='Bringing Out The Dead'>
<Record nineties.title='Deep Impact'>
<Record nineties.title='My Best Fiend'>
<Record nineties.title='Orgazmo'>
<Record nineties.title='Snake Eyes'>
<Record nineties.title='Who Am I?'>
<Record nineties.title='Steel Chariots'>
<Record nineties.title='The Thin Red Line'>
<Record nineties.title='Albino Alligator'>
<Record nineties.title='Nirvana'>
<Record nineties.title='Hellraiser: Bloodline'>
<Record nineties.title='The Outpost'>
<Record nineties.title='Macht'>
<Record nineties.title='Evita'>
<Record nineties.title='Timecop'>
<Record nineties.title='Conspiracy Theory'>
<Record nineties.title='Mercury Rising'>
<Record nineties.title='Casper'>
<Record nineties.title='DragonHeart'>
<Record nineties.title='Jumanji'>
<Record nineties.title='Under Siege'>
<Record nineties.title='The Shadow'>
<Record nineties.title='Steel'>
<Record nineties.title='Metro'>
<Record nineties.title='The Truth About Cats & Dogs'>
<Record nineties.title="Wayne's World">
<Record nineties.title="Wayne's World 2">
<Record nineties.title="My Best Friend's Wedding">
<Record nineties.title='Silberdisteln'>
<Record nineties.title='Deep Blue Sea'>
<Record nineties.title='Antz'>
<Record nineties.title='Crimson Tide'>
<Record nineties.title='The Out-of-Towners'>
<Record nineties.title='Lord of Illusions'>
<Record nineties.title='Felidae'>
<Record nineties.title='Disclosure'>
<Record nineties.title='Milk Money'>
<Record nineties.title='The River Wild'>
<Record nineties.title='The Insider'>
<Record nineties.title='For Love or Money'>
<Record nineties.title='Big Daddy'>
<Record nineties.title='The Prophecy 2'>
<Record nineties.title='A Chinese Ghost Story III'>
<Record nineties.title="Gone Fishin'">
<Record nineties.title='Terminal Velocity'>
<Record nineties.title='Only You'>
<Record nineties.title='Demon Knight'>
<Record nineties.title='Just Cause'>
<Record nineties.title='Europa'>
<Record nineties.title='The Brady Bunch Movie'>
<Record nineties.title='Tank Girl'>
<Record nineties.title='Die verschiedenen Gesichter des Sergej Eisenstein'>
<Record nineties.title='Mighty Morphin Power Rangers: The Movie'>
<Record nineties.title='Living In Oblivion'>
<Record nineties.title='Free Willy 2 - The Adventure Home'>
<Record nineties.title='Nur über meine Leiche'>
<Record nineties.title='Dying Young'>
<Record nineties.title='Young Guns II'>
<Record nineties.title='The American President'>
<Record nineties.title='Home for the Holidays'>
<Record nineties.title='To Wong Foo, Thanks for Everything, Julie Newmar'>
<Record nineties.title='Sudden Death'>
<Record nineties.title='Snow White: A Tale of Terror'>
<Record nineties.title='Mary Reilly'>
<Record nineties.title='Medicine Man'>
<Record nineties.title='Echte Kerle'>
<Record nineties.title='Sgt. Bilko'>
<Record nineties.title='The Craft'>
<Record nineties.title='Down Periscope'>
<Record nineties.title='Screamers'>
<Record nineties.title='The Quest'>
<Record nineties.title='Broken Arrow'>
<Record nineties.title='Hot Shots! Part Deux'>
<Record nineties.title='The Wedding Banquet'>
<Record nineties.title='Now and Then'>
<Record nineties.title='Poison Ivy'>
<Record nineties.title='Eraser'>
<Record nineties.title='Männerpension'>
<Record nineties.title='Virtuosity'>
<Record nineties.title='The Good Son'>
<Record nineties.title='Ace Ventura: When Nature Calls'>
<Record nineties.title='The Faculty'>
<Record nineties.title='Freejack'>
<Record nineties.title='Jingle All the Way'>
<Record nineties.title='Beautiful Girls'>
<Record nineties.title='Rennschwein Rudi Rüssel'>
<Record nineties.title='Botte Di Natale'>
<Record nineties.title='Hudson Hawk'>
<Record nineties.title='Phenomenon'>
<Record nineties.title='Tesis'>
<Record nineties.title='Orlando'>
<Record nineties.title='Up Close & Personal'>
<Record nineties.title='Bound'>
<Record nineties.title='Multiplicity'>
<Record nineties.title='Microcosmos'>
<Record nineties.title='The Island of Dr. Moreau'>
<Record nineties.title='High School High'>
<Record nineties.title="Smilla's Sense of Snow">
<Record nineties.title='Mortal Kombat'>
<Record nineties.title='The Man in the Iron Mask'>
<Record nineties.title='The Last Boy Scout'>
<Record nineties.title='The Avengers'>
<Record nineties.title='Der Eisbär'>
<Record nineties.title='La Femme Nikita'>
<Record nineties.title='Ghost in the Shell'>
<Record nineties.title='The Nutty Professor'>
<Record nineties.title='Clear and Present Danger'>
<Record nineties.title='Last Man Standing'>
<Record nineties.title='The Mask of Zorro'>
<Record nineties.title='Kids'>
<Record nineties.title='Species'>
<Record nineties.title='Universal Soldier'>
<Record nineties.title='Cliffhanger'>
<Record nineties.title="Look Who's Talking Too">
<Record nineties.title='Maverick'>
<Record nineties.title='Anaconda'>
<Record nineties.title='The Last of the Mohicans'>
<Record nineties.title='Tremors'>
<Record nineties.title='Donnie Brasco'>
<Record nineties.title='El Mariachi'>
<Record nineties.title='Asterix in Amerika'>
<Record nineties.title='Death Becomes Her'>
<Record nineties.title='Boys on the Side'>
<Record nineties.title='In the Line of Fire'>
<Record nineties.title='Jerry Maguire'>
<Record nineties.title='Lionheart'>
<Record nineties.title='Set  It Off'>
<Record nineties.title='2 Days in the Valley'>
<Record nineties.title='Die Drei Mädels von der Tankstelle'>
<Record nineties.title='Private Parts'>
<Record nineties.title='Police Story 4 - First Strike'>
<Record nineties.title='Double Team'>
<Record nineties.title='An American Werewolf in Paris'>
<Record nineties.title='Red Corner'>
<Record nineties.title='Another Stakeout'>
<Record nineties.title='Great Expectations'>
<Record nineties.title='Fallen'>
<Record nineties.title='Sieben Monde'>
<Record nineties.title='Picture Perfect'>
<Record nineties.title='The Man Who Knew Too Little'>
<Record nineties.title='Murder at 1600'>
<Record nineties.title='Money Talks'>
<Record nineties.title='Wrongfully Accused'>
<Record nineties.title='Cascadeur - Die Jagd nach dem Bernsteinzimmer'>
<Record nineties.title='Kai Rabe gegen die Vatikankiller'>
<Record nineties.title='Liebe Deine Nächste!'>
<Record nineties.title='The Dinner Game'>
<Record nineties.title='A Civil Action'>
<Record nineties.title='Virus'>
<Record nineties.title='Disturbing Behaviour'>
<Record nineties.title='Soldier'>
<Record nineties.title='The Full Monty'>
<Record nineties.title='A Night at the Roxbury'>
<Record nineties.title='Go'>
<Record nineties.title='Bordello of Blood'>
<Record nineties.title='Der Campus'>
<Record nineties.title='The Edge'>
<Record nineties.title='Grosse Pointe Blank'>
<Record nineties.title='Kiss the Girls'>
<Record nineties.title='Mr. Magoo'>
<Record nineties.title='Los Sin Nombre'>
<Record nineties.title='Primary Colors'>
<Record nineties.title='Stepmom'>
<Record nineties.title='Anastasia'>
<Record nineties.title='Apt Pupil'>
<Record nineties.title='Jungle 2 Jungle'>
<Record nineties.title='Babe: Pig in the City'>
<Record nineties.title='The Big Hit'>
<Record nineties.title='The Borrowers'>
<Record nineties.title='Brassed Off'>
<Record nineties.title='Election'>
<Record nineties.title='Bulworth'>
<Record nineties.title='Ever After: A Cinderella Story'>
<Record nineties.title='The Corruptor'>
<Record nineties.title='Deep Rising'>
<Record nineties.title='Desperate Measures'>
<Record nineties.title='Black Mask'>
<Record nineties.title="Buffalo '66">
<Record nineties.title='Cookies Fortune'>
<Record nineties.title='Celebrity'>
<Record nineties.title='He Got Game'>
<Record nineties.title='South Park: Bigger, Longer & Uncut'>
<Record nineties.title='Scent of a Woman'>
<Record nineties.title='The Nightmare Before Christmas'>
<Record nineties.title='The Bone Collector'>
<Record nineties.title='Judge Dredd'>
<Record nineties.title="A Bug's Life">
<Record nineties.title="You've Got Mail">
<Record nineties.title='Half Baked'>
<Record nineties.title='The Crow'>
<Record nineties.title='Werner - Volles Rooäää'>
<Record nineties.title='Kleines Arschloch - Der Film'>
<Record nineties.title='Crying Freeman'>
<Record nineties.title='Glengarry Glen Ross'>
<Record nineties.title='Werner - Das muß kesseln!!!'>
<Record nineties.title='Menace II Society'>
<Record nineties.title='Comedian Harmonists'>
<Record nineties.title='Ballermann 6'>
<Record nineties.title='Candyman'>
<Record nineties.title='Analyze This'>
<Record nineties.title='Bio-Dome'>
<Record nineties.title='Sniper'>
<Record nineties.title='Ricochet'>
<Record nineties.title='The Adventures of Ford Fairlane'>
<Record nineties.title='Darkman'>
<Record nineties.title='King of New York'>
<Record nineties.title='A Perfect World'>
<Record nineties.title='A Walk in the Clouds'>
<Record nineties.title='Any Given Sunday'>
<Record nineties.title='Asterix & Obelix take on Caesar'>
<Record nineties.title='The Fan'>
<Record nineties.title='The Dentist'>
<Record nineties.title='Hard to Kill'>
<Record nineties.title='Dazed and Confused'>
<Record nineties.title='Flubber'>
<Record nineties.title='Not Without My Daughter'>
<Record nineties.title='The Bonfire of the Vanities'>
<Record nineties.title='Little Women'>
<Record nineties.title='Quigley Down Under'>
<Record nineties.title='That Thing You Do!'>
<Record nineties.title='Last Action Hero'>
<Record nineties.title='Double Impact'>
<Record nineties.title='Hot Shots!'>
<Record nineties.title='Babe'>
<Record nineties.title='Clueless'>
<Record nineties.title='Single White Female'>
<Record nineties.title='Super Mario Bros.'>
<Record nineties.title='The Legend of Sleepy Hollow'>
<Record nineties.title='Of Mice and Men'>
<Record nineties.title="Romy and Michele's High School Reunion">
<Record nineties.title='Coneheads'>
<Record nineties.title='Happy Gilmore'>
<Record nineties.title='Kleine Haie'>
<Record nineties.title="Dante's Peak">
<Record nineties.title='Beverly Hills Ninja'>
<Record nineties.title='The Juror'>
<Record nineties.title='On Deadly Ground'>
<Record nineties.title='The Glimmer Man'>
<Record nineties.title='The Negotiator'>
<Record nineties.title='Rossini, oder die mörderische Frage, wer mit wem schlief'>
<Record nineties.title='Loaded Weapon 1'>
<Record nineties.title='Ring 2'>
<Record nineties.title='Voll Normaaal'>
<Record nineties.title='Uncle Sam'>
<Record nineties.title='Sweet and Lowdown'>
<Record nineties.title='Assassins'>
<Record nineties.title='Blood In Blood Out'>
<Record nineties.title='Rasen'>
<Record nineties.title='Holy Man'>
<Record nineties.title='Home Alone 3'>
<Record nineties.title='Hope Floats'>
<Record nineties.title='Everyone Says I Love You'>
<Record nineties.title="The Lion King II: Simba's Pride">
<Record nineties.title='Bad Boys'>
<Record nineties.title='Demolition Man'>
<Record nineties.title='Werner - Beinhart!'>
<Record nineties.title='Jack Frost'>
<Record nineties.title='Kundun'>
<Record nineties.title='Der Grosse Bagarozy'>
<Record nineties.title='Cry-Baby'>
<Record nineties.title='Lolita'>
<Record nineties.title='Mad City'>
<Record nineties.title='Major League: Back to the Minors'>
<Record nineties.title='Air Force One'>
<Record nineties.title='Detroit Rock City'>
<Record nineties.title='Enemy of the State'>
<Record nineties.title='The Rock'>
<Record nineties.title='Waterworld'>
<Record nineties.title='The New Swiss Family Robinson'>
<Record nineties.title='Thursday'>
<Record nineties.title="Marvin's Room">
<Record nineties.title='The Parent Trap'>
<Record nineties.title='The Mighty'>
<Record nineties.title='Mighty Joe Young'>
<Record nineties.title='Mortal Kombat: Annihilation'>
<Record nineties.title='Mystery Men'>
<Record nineties.title='Lake Placid'>
<Record nineties.title='The Phantom'>
<Record nineties.title='Phantoms'>
<Record nineties.title="Jane Austen's Mafia!">
<Record nineties.title='The Prince of Egypt'>
<Record nineties.title='The Dreamlife of Angels'>
<Record nineties.title='The Opposite of Sex'>
<Record nineties.title='Perdita Durango'>
<Record nineties.title='My Favorite Martian'>
<Record nineties.title='Patriot Games'>
<Record nineties.title='Stop! Or My Mom Will Shoot'>
<Record nineties.title='Urban Legend'>
<Record nineties.title='Striptease'>
<Record nineties.title='Die Apothekerin'>
<Record nineties.title='The Siege'>
<Record nineties.title='Johnny Mnemonic'>
<Record nineties.title='The Cable Guy'>
<Record nineties.title='Otto - Der Liebesfilm'>
<Record nineties.title='Shallow Grave'>
<Record nineties.title='Dangerous Minds'>
<Record nineties.title='The Postman'>
<Record nineties.title='Das merkwürdige Verhalten geschlechtsreifer Großstädter zur Paarungszeit'>
<Record nineties.title='The Pelican Brief'>
<Record nineties.title='Vampires'>
<Record nineties.title='End of Days'>
<Record nineties.title='The Brave'>
<Record nineties.title='Children of the Revolution'>
<Record nineties.title='Herr Ober!'>
<Record nineties.title='La estrategia del caracol'>
<Record nineties.title='The Saint'>
<Record nineties.title='Das Leben ist eine Baustelle'>
<Record nineties.title='Beauty and the Beast'>
<Record nineties.title='Very Bad Things'>
<Record nineties.title='The Messenger: The Story of Joan of Arc'>
<Record nineties.title='The Three Musketeers'>
<Record nineties.title='Escape from L.A.'>
<Record nineties.title='Man Bites Dog'>
<Record nineties.title='Stuart Little'>
<Record nineties.title='Smoke'>
<Record nineties.title='Sphere'>
<Record nineties.title='Mickey Blue Eyes'>
<Record nineties.title='U-Turn'>
<Record nineties.title="White Men Can't Jump">
<Record nineties.title='Waking Ned Devine'>
<Record nineties.title='The Lawnmower Man'>
<Record nineties.title='Cadillac Man'>
<Record nineties.title='The Witches'>
<Record nineties.title='The Freshman'>
<Record nineties.title='Men at Work'>
<Record nineties.title='The Russia House'>
<Record nineties.title='Homo Faber'>
<Record nineties.title='Marked for Death'>
<Record nineties.title='Madonna: Truth or Dare'>
<Record nineties.title='Buffy the Vampire Slayer'>
<Record nineties.title='Message in a Bottle'>
<Record nineties.title='Muppets from Space'>
<Record nineties.title='Hideous Kinky'>
<Record nineties.title="A Midsummer Night's Dream">
<Record nineties.title='Nachtgestalten'>
<Record nineties.title='Ravenous'>
<Record nineties.title='Sliding Doors'>
<Record nineties.title='Species II'>
<Record nineties.title='The Sweet Hereafter'>
<Record nineties.title='Swingers'>
<Record nineties.title='Snow Falling on Cedars'>
<Record nineties.title='Rounders'>
<Record nineties.title='Solo für Klarinette'>
<Record nineties.title='A Simple Plan'>
<Record nineties.title='Straight Shooter'>
<Record nineties.title='Pokémon: The First Movie'>
<Record nineties.title='Funny Games'>
<Record nineties.title='Autumn Tale'>
<Record nineties.title='A Tale of Winter'>
<Record nineties.title='The Rocketeer'>
<Record nineties.title='Switch'>
<Record nineties.title='Hamlet'>
<Record nineties.title='Dazlak'>
<Record nineties.title='What About Bob?'>
<Record nineties.title='Return to Paradise'>
<Record nineties.title='Summer of Sam'>
<Record nineties.title='Thinner'>
<Record nineties.title='Karniggels'>
<Record nineties.title='Jason Goes to Hell:The Final Friday'>
<Record nineties.title='Stigmata'>
<Record nineties.title='Patch Adams'>
<Record nineties.title="She's All That">
<Record nineties.title='If Lucy Fell'>
<Record nineties.title='Forever Young'>
<Record nineties.title='Congo'>
<Record nineties.title='The Prince of Tides'>
<Record nineties.title='Spawn'>
<Record nineties.title='Bugsy'>
<Record nineties.title='Until the End of the World'>
<Record nineties.title='Teaching Mrs. Tingle'>
<Record nineties.title='Dobermann'>
<Record nineties.title='Thunderbolt'>
<Record nineties.title='The Dark Half'>
<Record nineties.title='Wing Commander'>
<Record nineties.title='Wishmaster'>
<Record nineties.title='Les couloirs du temps : Les visiteurs 2'>
<Record nineties.title='True Crime'>
<Record nineties.title='Shiri'>
<Record nineties.title='Volcano'>
<Record nineties.title='Resurrection'>
<Record nineties.title='Universal Soldier: The Return'>
<Record nineties.title='Tea with Mussolini'>
<Record nineties.title='14 Tage lebenslänglich'>
<Record nineties.title='Premutos - der gefallene Engel'>
<Record nineties.title='For Richer or Poorer'>
<Record nineties.title='Irren ist männlich'>
<Record nineties.title='The Legend of 1900'>
<Record nineties.title='My Cousin Vinny'>
<Record nineties.title='Drop Dead Fred'>
<Record nineties.title='An American Tail: Fievel Goes West'>
<Record nineties.title='Plunkett & MacLeane'>
<Record nineties.title='The Iron Giant'>
<Record nineties.title='The Emperor and the Assassin'>
<Record nineties.title='The Limey'>
<Record nineties.title='For Love of the Game'>
<Record nineties.title="Käpt'n Blaubär - Der Film">
<Record nineties.title='Wolf'>
<Record nineties.title="Angela's Ashes">
<Record nineties.title='Double Jeopardy'>
<Record nineties.title='Mansfield Park'>
<Record nineties.title='The Hurricane'>
<Record nineties.title='Girl on the Bridge'>
<Record nineties.title='Deuce Bigalow: Male Gigolo'>
<Record nineties.title='The Player'>
<Record nineties.title='Raise the Red Lantern'>
<Record nineties.title='Encino Man'>
<Record nineties.title='Housesitter'>
<Record nineties.title='Flodder in Amerika!'>
<Record nineties.title='Strictly Ballroom'>
<Record nineties.title='Hoffa'>
<Record nineties.title='The Distinguished Gentleman'>
<Record nineties.title='Romper Stomper'>
<Record nineties.title='Nowhere to run'>
<Record nineties.title='The Mighty Ducks'>
<Record nineties.title='Swing Kids'>
<Record nineties.title='Abgeschminkt!'>
<Record nineties.title='Dragon: The Bruce Lee Story'>
<Record nineties.title='Jennifer 8'>
<Record nineties.title='Red Rock West'>
<Record nineties.title='Hackers'>
<Record nineties.title='Mad Dog and Glory'>
<Record nineties.title='Faraway, So Close!'>
<Record nineties.title='Chaplin'>
<Record nineties.title='The Age of Innocence'>
<Record nineties.title='The Muppet Christmas Carol'>
<Record nineties.title="Beethoven's 2nd">
<Record nineties.title='Hocus Pocus'>
<Record nineties.title='Manhattan Murder Mystery'>
<Record nineties.title='So I Married an Axe Murderer'>
<Record nineties.title='Fearless'>
<Record nineties.title='Shadowlands'>
<Record nineties.title='The High Crusade'>
<Record nineties.title='No Escape'>
<Record nineties.title='Rapa Nui'>
<Record nineties.title='When a Man Loves a Woman'>
<Record nineties.title='The Silence of the Hams'>
<Record nineties.title='Eat Drink Man Woman'>
<Record nineties.title='La Reine Margot'>
<Record nineties.title="Don't drink the water">
<Record nineties.title='Ostkreuz'>
<Record nineties.title='Corrina, Corrina'>
<Record nineties.title='The Road to Wellville'>
<Record nineties.title='The Basketball Diaries'>
<Record nineties.title='Tin Cup'>
<Record nineties.title='Guest House Paradiso'>
<Record nineties.title='Ghost Dad'>
<Record nineties.title='My Father the Hero'>
<Record nineties.title='Drop Dead Gorgeous'>
<Record nineties.title='Perfect Blue'>
<Record nineties.title='Bats'>
<Record nineties.title='Bitter Moon'>
<Record nineties.title='Point of No Return'>
<Record nineties.title='The Man Without a Face'>
<Record nineties.title='Miracle on 34th Street'>
<Record nineties.title='Forget Paris'>
<Record nineties.title='Pocahontas'>
<Record nineties.title='Death and the Maiden'>
<Record nineties.title='Abbuzze! Der Badesalz Film'>
<Record nineties.title='The Scarlet Letter'>
<Record nineties.title='White Squall'>
<Record nineties.title='Spy Hard'>
<Record nineties.title='The Doors'>
<Record nineties.title='Passenger 57'>
<Record nineties.title='James and the Giant Peach'>
<Record nineties.title='Kondom des Grauens'>
<Record nineties.title='Fear'>
<Record nineties.title='The Hunchback of Notre Dame'>
<Record nineties.title='The Crow: City of Angels'>
<Record nineties.title='The Arrival'>
<Record nineties.title='When We Were Kings'>
<Record nineties.title='Hamlet'>
<Record nineties.title='East is East'>
<Record nineties.title='Three to Tango'>
<Record nineties.title='Luna Papa'>
<Record nineties.title='The Ghost and the Darkness'>
<Record nineties.title="Il Fantasma dell'opera">
<Record nineties.title='Die Musterknaben 2'>
<Record nineties.title='George of the Jungle'>
<Record nineties.title="Don't Be a Menace to South Central While Drinking Your Juice in the Hood">
<Record nineties.title='Bob Roberts'>
<Record nineties.title='The Englishman Who Went Up a Hill But Came Down a Mountain'>
<Record nineties.title='Contract Killer'>
<Record nineties.title='Once Upon a Time in China'>
<Record nineties.title='Once Upon a Time in China II'>
<Record nineties.title='Once Upon a Time in China III'>
<Record nineties.title='Once Upon a Time in China & America'>
<Record nineties.title='Lovers'>
<Record nineties.title='Mr. Nice Guy'>
<Record nineties.title='Friday'>
<Record nineties.title='Threesome'>
<Record nineties.title='Godzilla 2000'>
<Record nineties.title='Gettysburg'>
<Record nineties.title='Needful Things'>
<Record nineties.title='It Could Happen to You'>
<Record nineties.title='The Waterboy'>
<Record nineties.title='Suicide Kings'>
<Record nineties.title='Mulan'>
<Record nineties.title='D3: The mighty Ducks'>
<Record nineties.title='Happiness'>
<Record nineties.title='Courage Under Fire'>
<Record nineties.title='Samurai Fiction'>
<Record nineties.title='Space Truckers'>
<Record nineties.title='The Chase'>
<Record nineties.title='Hero'>
<Record nineties.title='Universal Soldier II: Brothers in Arms'>
<Record nineties.title='The Jungle Book'>
<Record nineties.title='El día de la bestia'>
<Record nineties.title='Bulletproof'>
<Record nineties.title='Quick Change'>
<Record nineties.title='The Client'>
<Record nineties.title="La fille de d'Artagnan">
<Record nineties.title='Toy Soldiers'>
<Record nineties.title='The Frighteners'>
<Record nineties.title='Das Superweib'>
<Record nineties.title='Showgirls'>
<Record nineties.title='King Ralph'>
<Record nineties.title='In & Out'>
<Record nineties.title='Kein Pardon'>
<Record nineties.title='Candyman: Farewell to the Flesh'>
<Record nineties.title='Matilda'>
<Record nineties.title='Duck Tales The Movie: Treasure of the Lost Lamp'>
<Record nineties.title='On Your Mark'>
<Record nineties.title='Lord of the Flies'>
<Record nineties.title='The Evil Cult'>
<Record nineties.title='Nixon'>
<Record nineties.title='Maximum Risk'>
<Record nineties.title='Charlie & Louise - Das doppelte Lottchen'>
<Record nineties.title='Switchback'>
<Record nineties.title='The Ref'>
<Record nineties.title='Muppet Treasure Island'>
<Record nineties.title='I Love Trouble'>
<Record nineties.title='The Little Rascals'>
<Record nineties.title='Superstau'>
<Record nineties.title='Pet Sematary II'>
<Record nineties.title='Desert Heat'>
<Record nineties.title='Kalifornia'>
<Record nineties.title='Babylon 5: A Call to Arms'>
<Record nineties.title='Too Young to Die?'>
<Record nineties.title='Babylon 5: The River of Souls'>
<Record nineties.title='Die tödliche Maria'>
<Record nineties.title='Beautiful Thing'>
<Record nineties.title='Babylon 5: In the Beginning'>
<Record nineties.title='Babylon 5: Thirdspace'>
<Record nineties.title='Babylon 5: The Gathering'>
<Record nineties.title='Gorgeous'>
<Record nineties.title='New Jack City'>
<Record nineties.title='Farinelli: voce regina'>
<Record nineties.title='Project: ALF'>
<Record nineties.title='Knight Rider 2000'>
<Record nineties.title='Armour of God II: Operation Condor'>
<Record nineties.title='Wallace & Gromit: The Best of Aardman Animation'>
<Record nineties.title='Halloween: The Curse of Michael Myers'>
<Record nineties.title='Diabolique'>
<Record nineties.title='Mulholland Falls'>
<Record nineties.title="L'Amant">
<Record nineties.title='Farewell My Concubine'>
<Record nineties.title='The Birdcage'>
<Record nineties.title='Blue Streak'>
<Record nineties.title='The Wedding Singer'>
<Record nineties.title='Awakenings'>
<Record nineties.title='Major Payne'>
<Record nineties.title='Il Postino'>
<Record nineties.title='Ri¢hie Ri¢h'>
<Record nineties.title='Damage'>
<Record nineties.title='The Relic'>
<Record nineties.title='Billy Madison'>
<Record nineties.title='Dei Mudder sei Gesicht'>
<Record nineties.title='The Beverly Hillbillies'>
<Record nineties.title='Arizona Dream'>
<Record nineties.title='Internal Affairs'>
<Record nineties.title='Workaholic'>
<Record nineties.title='City Hall'>
<Record nineties.title='Boomerang'>
<Record nineties.title='Major League II'>
<Record nineties.title='Singles'>
<Record nineties.title='Tremors 2: Aftershocks'>
<Record nineties.title='Striking Distance'>
<Record nineties.title='Audition'>
<Record nineties.title='Fly Away Home'>
<Record nineties.title='Problem Child'>
<Record nineties.title='Flodder 3'>
<Record nineties.title='The Hand that Rocks the Cradle'>
<Record nineties.title='Presumed Innocent'>
<Record nineties.title='Stalingrad'>
<Record nineties.title='Head above Water'>
<Record nineties.title='Chungking Express'>
<Record nineties.title='Die Musterknaben'>
<Record nineties.title='Eddie'>
<Record nineties.title='The Associate'>
<Record nineties.title='Indien'>
<Record nineties.title='Human Traffic'>
<Record nineties.title='Nuns on the Run'>
<Record nineties.title='Police Story 3: Super Cop'>
<Record nineties.title='The Rescuers Down Under'>
<Record nineties.title='Léolo'>
<Record nineties.title='Tai Chi Master'>
<Record nineties.title='Honey, I Blew Up the Kid'>
<Record nineties.title='Secrets & Lies'>
<Record nineties.title='D2: The Mighty Ducks'>
<Record nineties.title='Go Trabi Go 2 - Das war der wilde Osten'>
<Record nineties.title='Lucky Luke'>
<Record nineties.title="Child's Play 2">
<Record nineties.title="Child's Play 3">
<Record nineties.title='City Hunter'>
<Record nineties.title='Robinson Crusoe'>
<Record nineties.title="Baby's Day Out">
<Record nineties.title='Die Blume der Hausfrau'>
<Record nineties.title='Fallen Angels'>
<Record nineties.title='Daylight'>
<Record nineties.title='Freeway'>
<Record nineties.title='The Next Karate Kid'>
<Record nineties.title='The Secret Garden'>
<Record nineties.title='Aladdin and the King of Thieves'>
<Record nineties.title='Shall we dansu?'>
<Record nineties.title='The Meteor Man'>
<Record nineties.title='Fatherland'>
<Record nineties.title='Psycho'>
<Record nineties.title='Hard Rain'>
<Record nineties.title='Far and Away'>
<Record nineties.title="Freddy's Dead: The Final Nightmare">
<Record nineties.title='A League of Their Own'>
<Record nineties.title='Todesspiel'>
<Record nineties.title='Extreme Measures'>
<Record nineties.title='Hardware'>
<Record nineties.title="City Slickers II: The Legend of Curly's Gold">
<Record nineties.title='Dead or Alive - Hanzaisha'>
<Record nineties.title='My Girl 2'>
<Record nineties.title='The Madness of King George'>
<Record nineties.title='8 1/2 Women'>
<Record nineties.title='S.P.Q.R. 2000 e 1/2 anni fa'>
<Record nineties.title='Warlock'>
<Record nineties.title='Bowfinger'>
<Record nineties.title='Never Been Kissed'>
<Record nineties.title='The Indian in the Cupboard'>
<Record nineties.title="She's the One">
<Record nineties.title='Regarding Henry'>
<Record nineties.title='Wilde'>
<Record nineties.title='EDtv'>
<Record nineties.title='House on Haunted Hill'>
<Record nineties.title='Tommy Boy'>
<Record nineties.title='Bullets Over Broadway'>
<Record nineties.title='The Hard Way'>
<Record nineties.title='The Crying Game'>
<Record nineties.title='The Santa Clause'>
<Record nineties.title='The Long Kiss Goodnight'>
<Record nineties.title="National Lampoon's Vegas Vacation">
<Record nineties.title='Honey, We Shrunk Ourselves'>
<Record nineties.title='Sleepwalkers'>
<Record nineties.title='Dead Presidents'>
<Record nineties.title='Welcome to the Dollhouse'>
<Record nineties.title='Mighty Aphrodite'>
<Record nineties.title='Quiz Show'>
<Record nineties.title='Nine Months'>
<Record nineties.title='Un indien dans la ville'>
<Record nineties.title='Rosetta'>
<Record nineties.title='Fire, Ice & Dynamite'>
<Record nineties.title='Dead Again'>
<Record nineties.title='Suburban Commando'>
<Record nineties.title='Family Plan'>
<Record nineties.title='Addams Family Reunion'>
<Record nineties.title='Repossessed'>
<Record nineties.title='Kazaam'>
<Record nineties.title='Money Train'>
<Record nineties.title='Grumpy Old Men'>
<Record nineties.title='Little Man Tate'>
<Record nineties.title='Lawnmower Man 2: Beyond Cyberspace'>
<Record nineties.title='Bandits'>
<Record nineties.title='The Sandlot'>
<Record nineties.title='Kingpin'>
<Record nineties.title='Rushmore'>
<Record nineties.title='Police Academy 7: Mission to Moscow'>
<Record nineties.title='Helden wie wir'>
<Record nineties.title='Small Soldiers'>
<Record nineties.title='Dave'>
<Record nineties.title='Blues Brothers 2000'>
<Record nineties.title='Hellraiser III: Hell on Earth'>
<Record nineties.title='The Exorcist III'>
<Record nineties.title='Serial Mom'>
<Record nineties.title="Nobody's Fool">
<Record nineties.title='Another 48 Hrs.'>
<Record nineties.title='New Nightmare'>
<Record nineties.title='Toys'>
<Record nineties.title='hypnose'>
<Record nineties.title='Rear Window'>
<Record nineties.title="Nich' mit Leo">
<Record nineties.title='The Haunting'>
<Record nineties.title='Blast from the Past'>
<Record nineties.title='Three Men and a Little Lady'>
<Record nineties.title='Fucking Åmål'>
<Record nineties.title='Cronos'>
<Record nineties.title='Following'>
<Record nineties.title='The Commitments'>
<Record nineties.title='Die Bademeister – Weiber, saufen, Leben retten'>
<Record nineties.title='Street Fighter'>
<Record nineties.title='Cyrano de Bergerac'>
<Record nineties.title='101 Dalmatians'>
<Record nineties.title='Halloween H20: 20 Years Later'>
<Record nineties.title='Nothing to Lose'>
<Record nineties.title='Stadtgespräch'>
<Record nineties.title='Les visiteurs'>
<Record nineties.title='Go Trabi Go'>
<Record nineties.title='The Replacement Killers'>
<Record nineties.title='Un Piede in paradiso'>
<Record nineties.title="La guerre de l'eau">
<Record nineties.title='The Girl Next Door'>
<Record nineties.title='I.Q.'>
<Record nineties.title='Buena Vista Social Club'>
<Record nineties.title='Rob Roy'>
<Record nineties.title='Cherche famille désespérément'>
<Record nineties.title='Hard Boiled'>
<Record nineties.title="Peter's Friends">
<Record nineties.title='Guyver: Dark Hero'>
<Record nineties.title="The Hairdresser's Husband">
<Record nineties.title='Naked in New York'>
<Record nineties.title='Beethoven'>
<Record nineties.title='U.S. Marshals'>
<Record nineties.title='Leprechaun'>
<Record nineties.title='Doc Hollywood'>
<Record nineties.title='Amistad'>
<Record nineties.title='The Van'>
<Record nineties.title='Father of the Bride'>
<Record nineties.title='Bad Girls'>
<Record nineties.title='Kuch Kuch Hota Hai'>
<Record nineties.title='Pecker'>
<Record nineties.title='Air America'>
<Record nineties.title='Renaissance Man'>
<Record nineties.title='Fair Game'>
<Record nineties.title='Sabrina'>
<Record nineties.title='How To Make An American Quilt'>
<Record nineties.title='Father of the Bride Part II'>
<Record nineties.title='Jade'>
<Record nineties.title='Barb Wire'>
<Record nineties.title='Late Show'>
<Record nineties.title='The Horseman on the Roof'>
<Record nineties.title='Oscar'>
<Record nineties.title='Curly Sue'>
<Record nineties.title='Underground'>
<Record nineties.title='Keiner liebt mich'>
<Record nineties.title='Bullet in the Head'>
<Record nineties.title='Captain Cosmotic'>
<Record nineties.title='Allein unter Frauen'>
<Record nineties.title='Dolores Claiborne'>
<Record nineties.title='Bride of Chucky'>
<Record nineties.title='Nothing but Trouble'>
<Record nineties.title='The Hudsucker Proxy'>
<Record nineties.title='Joan of Arc'>
<Record nineties.title='Chacun cherche son chat'>
<Record nineties.title='Peut-être'>
<Record nineties.title='The Langoliers'>
<Record nineties.title="Joe's Apartment">
<Record nineties.title='Tombstone'>
<Record nineties.title='Hercules'>
<Record nineties.title='Much Ado About Nothing'>
<Record nineties.title='The Rainmaker'>
<Record nineties.title='The Prophecy'>
<Record nineties.title="Look Who's Talking Now">
<Record nineties.title='AI'>
<Record nineties.title='Gagarin, ya vas lyubila'>
<Record nineties.title='Fortress'>
<Record nineties.title='From Dusk Till Dawn 2: Texas Blood Money'>
<Record nineties.title='Oi! Warning'>
<Record nineties.title='The Quick and the Dead'>
<Record nineties.title='Dracula: Dead and Loving it'>
<Record nineties.title='Instinct'>
<Record nineties.title='Made in America'>
<Record nineties.title='Village of the Damned'>
<Record nineties.title='Chain Reaction'>
<Record nineties.title='El viaje'>
<Record nineties.title='Sin querer'>
<Record nineties.title='Dennis the Menace'>
<Record nineties.title='Bad Lieutenant'>
<Record nineties.title='Fierce Creatures'>
<Record nineties.title='Der Sandmann'>
<Record nineties.title='Green Card'>
<Record nineties.title='Vampire in Brooklyn'>
<Record nineties.title='What Dreams May Come'>
<Record nineties.title='Wyatt Earp'>
<Record nineties.title='Defending Your Life'>
<Record nineties.title='Heart and Souls'>
<Record nineties.title='Dokumentarfilm - Eine Anleitung'>
<Record nineties.title='Legend of the Drunken Master'>
<Record nineties.title='12 Angry Men'>
<Record nineties.title='The Story of Us'>
<Record nineties.title='White Fang'>
<Record nineties.title='The Acid House'>
<Record nineties.title='The Night Flier'>
<Record nineties.title='Curdled'>
<Record nineties.title="Mo' Money">
<Record nineties.title='Emma'>
<Record nineties.title='Das Erste Semester'>
<Record nineties.title='Home Fries'>
<Record nineties.title='The Road Home'>
<Record nineties.title='The Paper'>
<Record nineties.title='Sapho'>
<Record nineties.title='Thunderheart'>
<Record nineties.title='Driving Me Crazy'>
<Record nineties.title='Sen no Rikyu'>
<Record nineties.title='In the Army Now'>
<Record nineties.title='Breakfast of Champions'>
<Record nineties.title='Candyman: Day of the Dead'>
<Record nineties.title='The Gingerbread Man'>
<Record nineties.title="Gridlock'd">
<Record nineties.title='Sling Blade'>
<Record nineties.title="Fathers' Day">
<Record nineties.title="Akira Kurosawa's Dreams">
<Record nineties.title='Honeymoon in Vegas'>
<Record nineties.title='Sirens'>
<Record nineties.title='The Last Supper'>
<Record nineties.title='Titus'>
<Record nineties.title='Critters 4'>
<Record nineties.title='Fresa y chocolate'>
<Record nineties.title="L'appartement">
<Record nineties.title='Senseless'>
<Record nineties.title='Olsen-bandens sidste stik'>
<Record nineties.title='Citizen X'>
<Record nineties.title='First Kid'>
<Record nineties.title='Godzilla vs. Destoroyah'>
<Record nineties.title='Cop and ½'>
<Record nineties.title='The Long Hello and Short Goodbye'>
<Record nineties.title='Wishmaster 2: Evil Never Dies'>
<Record nineties.title='Pushing Tin'>
<Record nineties.title='A Very Brady Sequel'>
<Record nineties.title='Street Fighter II : The Animated Movie'>
<Record nineties.title='One Night Stand'>
<Record nineties.title='Random Hearts'>
<Record nineties.title='La belle noiseuse'>
<Record nineties.title='Playing God'>
<Record nineties.title='Live Wire'>
<Record nineties.title='Pippi Longstocking'>
<Record nineties.title='Kaspar Hauser'>
<Record nineties.title='Backbeat'>
<Record nineties.title='Der Skipper'>
<Record nineties.title='Billy Bathgate'>
<Record nineties.title='Memphis Belle'>
<Record nineties.title='Nelly & Monsieur Arnaud'>
<Record nineties.title='Viol@'>
<Record nineties.title='I Went Down'>
<Record nineties.title='Feeling Minnesota'>
<Record nineties.title='Undercover Blues'>
<Record nineties.title='The Snapper'>
<Record nineties.title='Powder'>
<Record nineties.title='Critters 3: You Are What They Eat'>
<Record nineties.title='Croupier'>
<Record nineties.title='Ridicule'>
<Record nineties.title='La Gloire de mon père'>
<Record nineties.title='Le château de ma mère'>
<Record nineties.title='Flashback'>
<Record nineties.title='Inventing the Abbotts'>
<Record nineties.title='Leap of Faith'>
<Record nineties.title='Navy Seals'>
<Record nineties.title='Johnny Stecchino'>
<Record nineties.title='Greedy'>
<Record nineties.title='Curiosity & the Cat'>
<Record nineties.title='All Over Me'>
<Record nineties.title='Full Speed'>
<Record nineties.title='Gossenkind'>
<Record nineties.title='Pianese Nunzio, 14 anni a maggio'>
<Record nineties.title='Steel Sharks'>
<Record nineties.title='Amerikana'>
<Record nineties.title='Belly'>
<Record nineties.title='Split Second'>
<Record nineties.title='Cannibal! The Musical'>
<Record nineties.title='Airborne'>
<Record nineties.title='Gen-X Cops'>
<Record nineties.title='The People Under the Stairs'>
<Record nineties.title='Scooby-Doo on Zombie Island'>
<Record nineties.title='Rapid Fire'>
<Record nineties.title='Showdown in Little Tokyo'>
<Record nineties.title='American Me'>
<Record nineties.title='Son in Law'>
<Record nineties.title='FernGully: The Last Rainforest'>
<Record nineties.title="China O'Brien II">
<Record nineties.title='Beauty and the Beast: The Enchanted Christmas'>
<Record nineties.title="A Chinese Odyssey Part One: Pandora's Box">
<Record nineties.title='Scooby-Doo in Arabian Nights'>
<Record nineties.title='The Tit and the Moon'>
<Record nineties.title='Olive, the Other Reindeer'>
<Record nineties.title='Hooves of Fire'>
<Record nineties.title='Two Hands'>
<Record nineties.title='October Sky'>
<Record nineties.title='The Stand'>
<Record nineties.title='Empire Records'>
<Record nineties.title='Free Enterprise'>
<Record nineties.title='The Doom Generation'>
<Record nineties.title='The Mangler'>
<Record nineties.title='Puddle Cruiser'>
<Record nineties.title='True Colors'>
<Record nineties.title='Eddie Izzard: Definite Article'>
<Record nineties.title='Eddie Izzard: Dress to Kill'>
<Record nineties.title='Eddie Izzard: Glorious'>
<Record nineties.title='Eddie Izzard: Unrepeatable'>
<Record nineties.title='Airheads'>
<Record nineties.title='Vuxna människor'>
<Record nineties.title='MacGyver: Trail to Doomsday'>
<Record nineties.title='All I Want For Christmas'>
<Record nineties.title="Annabelle's Wish">
<Record nineties.title='Bottle Rocket'>
<Record nineties.title='Grand Canyon'>
<Record nineties.title='Immortal Beloved'>
<Record nineties.title='Pocahontas II: Journey to a New World'>
<Record nineties.title='Holy Smoke'>
<Record nineties.title='Africa The Serengeti'>
<Record nineties.title='Alaska Spirit of the Wild'>
<Record nineties.title='Amazon'>
<Record nineties.title='Cosmic Voyage'>
<Record nineties.title='Fresh'>
<Record nineties.title='Head On'>
<Record nineties.title='The Boys'>
<Record nineties.title='The Power of One'>
<Record nineties.title='Superstar'>
<Record nineties.title='The Castle'>
<Record nineties.title='Return to the Blue Lagoon'>
<Record nineties.title='Madadayo'>
<Record nineties.title='Citizen Ruth'>
<Record nineties.title='Scarfies'>
<Record nineties.title='What Becomes of the Broken Hearted?'>
<Record nineties.title='Kurt & Courtney'>
<Record nineties.title='The Craic'>
<Record nineties.title='A Bright Shining Lie'>
<Record nineties.title="Geri's Game">
<Record nineties.title='When Trumpets Fade'>
<Record nineties.title='Raising Cain'>
<Record nineties.title='Blank Check'>
<Record nineties.title='8 Heads in a Duffel Bag'>
<Record nineties.title='Dil To Pagal Hai'>
<Record nineties.title='Captain America'>
<Record nineties.title='Black Sheep'>
<Record nineties.title='Baraka'>
<Record nineties.title='Terror Firmer'>
<Record nineties.title='BASEketball'>
<Record nineties.title='Slacker'>
<Record nineties.title='Teen Spirit: The Tribute to Kurt Cobain'>
<Record nineties.title='Bad Boy Bubby'>
<Record nineties.title='Kunoichi ninpô chô Yagyû gaiden: Edobana jigoku-hen'>
<Record nineties.title='Brainscan'>
<Record nineties.title='Cool World'>
<Record nineties.title='American Movie'>
<Record nineties.title='Revenge'>
<Record nineties.title='Beyond the Mat'>
<Record nineties.title='Hoop Dreams'>
<Record nineties.title='Ninja Scroll'>
<Record nineties.title='The Red Violin'>
<Record nineties.title='Fire Down Below'>
<Record nineties.title='Searching for Bobby Fischer'>
<Record nineties.title='Trojan War'>
<Record nineties.title='The Secret of Roan Inish'>
<Record nineties.title='Almost Heroes'>
<Record nineties.title='Captain Ron'>
<Record nineties.title='Out For Justice'>
<Record nineties.title='Jungle Emperor Leo'>
<Record nineties.title='The Sex Monster'>
<Record nineties.title='Gang Related'>
<Record nineties.title='PCU'>
<Record nineties.title='Drive Me Crazy'>
<Record nineties.title='La ley de Herodes'>
<Record nineties.title='The Pentagon Wars'>
<Record nineties.title='The Rugrats Movie'>
<Record nineties.title='Michael Madana Kamarajan'>
<Record nineties.title='Bullet'>
<Record nineties.title='Body Shots'>
<Record nineties.title='Black Beauty'>
<Record nineties.title='Gia'>
<Record nineties.title='Rudy'>
<Record nineties.title='Stealing Beauty'>
<Record nineties.title='Dead Man on Campus'>
<Record nineties.title='Patlabor 2: The Movie'>
<Record nineties.title='Dirty Work'>
<Record nineties.title='Outside Providence'>
<Record nineties.title='Deceiver'>
<Record nineties.title='In the Company of Men'>
<Record nineties.title='Kuffs'>
<Record nineties.title='Beau Travail'>
<Record nineties.title='Un air de famille'>
<Record nineties.title='Slums of Beverly Hills'>
<Record nineties.title='Dogfight'>
<Record nineties.title='School Ties'>
<Record nineties.title='Pride and Prejudice'>
<Record nineties.title='The Return of Superfly'>
<Record nineties.title='Varsity Blues'>
<Record nineties.title='Erskineville Kings'>
<Record nineties.title='Bandit Queen'>
<Record nineties.title='Gotti'>
<Record nineties.title='George Lucas in Love'>
<Record nineties.title='Good Burger'>
<Record nineties.title='Heavyweights'>
<Record nineties.title='Tenchi Muyô! In Love 2: Haruka naru omoi'>
<Record nineties.title='The Cement Garden'>
<Record nineties.title='The Hot Spot'>
<Record nineties.title='Bongwater'>
<Record nineties.title="Pooh's Grand Adventure: The Search for Christopher Robin">
<Record nineties.title='Proof'>
<Record nineties.title='Welcome to Sarajevo'>
<Record nineties.title="McHale's Navy">
<Record nineties.title='Batman: Mask of the Phantasm'>
<Record nineties.title='Miami Blues'>
<Record nineties.title='Thumb Wars'>
<Record nineties.title='Guyver'>
<Record nineties.title='The Breaks'>
<Record nineties.title="Can't Hardly Wait">
<Record nineties.title='Brink!'>
<Record nineties.title='The Loss of Sexual Innocence'>
<Record nineties.title='Only Yesterday'>
<Record nineties.title='La Patinoire'>
<Record nineties.title='La Cité de la Peur'>
<Record nineties.title='Kaptein Sabeltann og hemmeligheten i Kjuttaviga'>
<Record nineties.title='Love Stinks'>
<Record nineties.title='Speechless'>
<Record nineties.title='The Pagemaster'>
<Record nineties.title='Eagles: Hell Freezes Over'>
<Record nineties.title='Alice: Through the Looking Glass'>
<Record nineties.title='Buddy'>
<Record nineties.title='Mystery, Alaska'>
<Record nineties.title='Eight Days a Week'>
<Record nineties.title='The Hunted'>
<Record nineties.title='The Hunted'>
<Record nineties.title='Antarctica'>
<Record nineties.title='200 Cigarettes'>
<Record nineties.title='Ashes of Time Redux'>
<Record nineties.title='CB4'>
<Record nineties.title='Newsies'>
<Record nineties.title='The Wrong Guy'>
<Record nineties.title='After the Rain'>
<Record nineties.title='Twin Town'>
<Record nineties.title='I.D.'>
<Record nineties.title='Pelisky'>
<Record nineties.title='Cerni baroni'>
<Record nineties.title='Metropolitan'>
<Record nineties.title="Mickey's Once Upon A Christmas">
<Record nineties.title="Don't Tell Mom the Babysitter's Dead">
<Record nineties.title='The BFG'>
<Record nineties.title='Muttertag'>
<Record nineties.title='Atlantis'>
<Record nineties.title='Love and a .45'>
<Record nineties.title='Agnes Brown'>
<Record nineties.title='Kissing a Fool'>
<Record nineties.title='PNYC: Portishead - Roseland New York'>
<Record nineties.title='Cirque du Soleil: Quidam'>
<Record nineties.title='Cirque du Soleil: La Nouba'>
<Record nineties.title='Cirque du Soleil: Saltimbanco'>
<Record nineties.title='The Triumph of the Nerds: The Rise of Accidental Empires'>
<Record nineties.title='At First Sight'>
<Record nineties.title='Destiny in Space'>
<Record nineties.title='Mission to Mir'>
<Record nineties.title='Wolves'>
<Record nineties.title='Grumpier Old Men'>
<Record nineties.title='Fire in the Sky'>
<Record nineties.title='Invasion'>
<Record nineties.title='Robot Jox'>
<Record nineties.title='Sabrina the Teenage Witch'>
<Record nineties.title='Doctor Who'>
<Record nineties.title='Do Not Disturb'>
<Record nineties.title='The Big Kahuna'>
<Record nineties.title='Love and human remains'>
<Record nineties.title='Der Todesking'>
<Record nineties.title='Storm of the Century'>
<Record nineties.title='Sarah, Plain and Tall'>
<Record nineties.title='Skylark'>
<Record nineties.title="What's Love Got to Do with It">
<Record nineties.title='Class Action'>
<Record nineties.title='All The Rage'>
<Record nineties.title='The Kennedys of Massachusetts'>
<Record nineties.title='A Goofy Movie'>
<Record nineties.title='Only the Strong'>
<Record nineties.title='Bravo Two Zero'>
<Record nineties.title='Trekkies'>
<Record nineties.title='Tokyo Decadence'>
<Record nineties.title='Multi-Facial'>
<Record nineties.title='A Brighter Summer Day'>
<Record nineties.title='Batman & Mr. Freeze: SubZero'>
<Record nineties.title='Anton'>
<Record nineties.title='Den sidste viking'>
<Record nineties.title='Kangaroos: Faces in the Mob'>
<Record nineties.title='VeggieTales: Dave and the Giant Pickle'>
<Record nineties.title='The Occult History of the Third Reich'>
<Record nineties.title='Faces of Death IV'>
<Record nineties.title='Faces of Death V'>
<Record nineties.title='Faces of Death VI'>
<Record nineties.title='The Return of Jafar'>
<Record nineties.title='Gen 13'>
<Record nineties.title='The Land Before Time II: The Great Valley Adventure'>
<Record nineties.title='Jägarna'>
<Record nineties.title='Selena'>
<Record nineties.title='Great Expectations'>
<Record nineties.title='Torsk på Tallinn'>
<Record nineties.title='House Party 2'>
<Record nineties.title='House Party  3'>
<Record nineties.title='Freebird... The Movie'>
<Record nineties.title='The Adventures of Elmo in Grouchland'>
<Record nineties.title='Last Night'>
<Record nineties.title='La classe américaine'>
<Record nineties.title='Juice'>
<Record nineties.title='Phantasm III'>
<Record nineties.title='Phantasm IV'>
<Record nineties.title='Zero Effect'>
<Record nineties.title='Safe Men'>
<Record nineties.title='The Wood'>
<Record nineties.title='The Best Man'>
<Record nineties.title='Simply Irresistible'>
<Record nineties.title='Highway to Hell'>
<Record nineties.title='Dating the Enemy'>
<Record nineties.title='My Neighbors the Yamadas'>
<Record nineties.title='Eddie Izzard: Live at the Ambassadors'>
<Record nineties.title='The Big Steal'>
<Record nineties.title='Gladiator'>
<Record nineties.title='Purasuchikku ritoru'>
<Record nineties.title='Tromeo and Juliet'>
<Record nineties.title='Career Opportunities'>
<Record nineties.title='A Place To Be Loved'>
<Record nineties.title='Higher Learning'>
<Record nineties.title='With Honors'>
<Record nineties.title='The Stupids'>
<Record nineties.title='Mercy Mission: The Rescue of Flight 771'>
<Record nineties.title='3 Ninjas'>
<Record nineties.title='Campfire Tales'>
<Record nineties.title='Hercules Returns'>
<Record nineties.title='The Jack Bull'>
<Record nineties.title='Sonic The Hedgehog: The Movie'>
<Record nineties.title='Future Sport'>
<Record nineties.title='Aspen Extreme'>
<Record nineties.title='Tell Me Something'>
<Record nineties.title='Schizopolis'>
<Record nineties.title='The Mod Squad'>
<Record nineties.title='The Brothers McMullen'>
<Record nineties.title='Commandments'>
<Record nineties.title='Dick'>
<Record nineties.title='Panic Mechanic'>
<Record nineties.title="Sweet 'n Short">
<Record nineties.title="There's a Zulu on My Stoep">
<Record nineties.title='Othello'>
<Record nineties.title='Cyborg 2'>
<Record nineties.title='Waiting For Guffman'>
<Record nineties.title='The Spirit of Christmas'>
<Record nineties.title='The Spirit of Christmas'>
<Record nineties.title="Doug's 1st Movie">
<Record nineties.title='A Time to Revenge'>
<Record nineties.title='Pocket Ninjas'>
<Record nineties.title='The Cutting Edge'>
<Record nineties.title='A Christmas Carol'>
<Record nineties.title='Spriggan'>
<Record nineties.title='Barcelona'>
<Record nineties.title='The Return of the Texas Chainsaw Massacre'>
<Record nineties.title='Bingo'>
<Record nineties.title='F/X2'>
<Record nineties.title='Nine Inch Nails: Closure'>
<Record nineties.title='Raisins Sold Out: The California Raisins II'>
<Record nineties.title='The General'>
<Record nineties.title='Akele Hum Akele Tum'>
<Record nineties.title='Truman'>
<Record nineties.title='Skyggen'>
<Record nineties.title="The Young Poisoner's Handbook">
<Record nineties.title='Akumulátor 1'>
<Record nineties.title='The Last Days of Disco'>
<Record nineties.title='Spotswood'>
<Record nineties.title='The Boxer'>
<Record nineties.title='Jetsons: The Movie'>
<Record nineties.title='Persuasion'>
<Record nineties.title="I'll Be Home for Christmas">
<Record nineties.title='Land Girls'>
<Record nineties.title="The Batman Superman Movie: World's Finest">
<Record nineties.title='X - The Movie'>
<Record nineties.title='Trucks'>
<Record nineties.title='The Object of My Affection'>
<Record nineties.title='Homegrown'>
<Record nineties.title='Omega Doom'>
<Record nineties.title='Character '>
<Record nineties.title='The Temp'>
<Record nineties.title='Eye For An Eye'>
<Record nineties.title='Battle Angel Alita'>
<Record nineties.title="Apartheid's Last Stand">
<Record nineties.title='The Mating Habits of the Earthbound Human'>
<Record nineties.title='Paradise Lost: The Child Murders at Robin Hood Hills'>
<Record nineties.title='Houseguest'>
<Record nineties.title='Behind the Planet of the Apes'>
<Record nineties.title='A Murder of Crows'>
<Record nineties.title='The Odyssey'>
<Record nineties.title='The Land Before Time VI: The Secret of Saurus Rock'>
<Record nineties.title='Notícias de uma Guerra Particular'>
<Record nineties.title='Miami Rhapsody'>
<Record nineties.title='Dunston Checks In'>
<Record nineties.title='El Maestro de esgrima'>
<Record nineties.title='Street Fighter Alpha: The Movie'>
<Record nineties.title='Jeffrey'>
<Record nineties.title='Death Warrant'>
<Record nineties.title='Riki-Oh: The Story of Ricky'>
<Record nineties.title='The Man In The Moon'>
<Record nineties.title='Unlawful Entry'>
<Record nineties.title='UFC 1: The Beginning'>
<Record nineties.title='UFC 2: No Way Out'>
<Record nineties.title='UFC 3: The American Dream'>
<Record nineties.title='UFC 4: Revenge Of The Warriors'>
<Record nineties.title='UFC 5: Return Of The Beast'>
<Record nineties.title='UFC 6: Clash Of The Titans'>
<Record nineties.title='UFC 7: The Brawl In Buffalo'>
<Record nineties.title='UFC 8: David vs. Goliath'>
<Record nineties.title='UFC 9: Motor City Madness'>
<Record nineties.title='UFC 10: The Tournament'>
<Record nineties.title='UFC 11: The Proving Ground'>
<Record nineties.title='UFC 12: Judgement Day'>
<Record nineties.title='UFC 13: The Ultimate Force'>
<Record nineties.title='UFC 14: Showdown'>
<Record nineties.title='UFC 15: Collision Course'>
<Record nineties.title='UFC 16: Battle In The Bayou'>
<Record nineties.title='UFC 17: Redemption'>
<Record nineties.title='UFC 18: Road To The Heavyweight Title'>
<Record nineties.title='UFC 19: Young Guns'>
<Record nineties.title='UFC 20: Battle For The Gold'>
<Record nineties.title='UFC 21: Return Of The Champions'>
<Record nineties.title='UFC 22: There Can Be Only One Champion'>
<Record nineties.title='UFC 23: Ultimate Japan 2'>
<Record nineties.title="Billy's Hollywood Screen Kiss">
<Record nineties.title='Only Clouds Move the Stars'>
<Record nineties.title='Surviving the Game'>
<Record nineties.title='Legends - Live At Montreux'>
<Record nineties.title='Mrs Brown'>
<Record nineties.title='Spanking the Monkey'>
<Record nineties.title='Hamilton'>
<Record nineties.title='The Leopard Son'>
<Record nineties.title='Barney Songs'>
<Record nineties.title="Barney's Great Adventure">
<Record nineties.title='The Legend of Fong Sai-Yuk'>
<Record nineties.title='Fleetwood Mac - The Dance'>
<Record nineties.title="Scooby-Doo and the Witch's Ghost">
<Record nineties.title="CIA - America's Secret Warriors">
<Record nineties.title='Galapagos: The Enchanted Voyage'>
<Record nineties.title='Ring of Fire'>
<Record nineties.title='The Living Sea'>
<Record nineties.title='Tropical Rainforest'>
<Record nineties.title='Two Years In Galapagos'>
<Record nineties.title='Brokedown Palace'>
<Record nineties.title='Dudley Do-Right'>
<Record nineties.title='Where The Day Takes You'>
<Record nineties.title='Camp Nowhere'>
<Record nineties.title='Trial and Error'>
<Record nineties.title='Sunshine'>
<Record nineties.title='UFC 11.5 Ultimate Ultimate 2'>
<Record nineties.title='UFC 7.5 Ultimate Ultimate'>
<Record nineties.title='Omen IV: The Awakening'>
<Record nineties.title='My Fellow Americans'>
<Record nineties.title='Freaked'>
<Record nineties.title='1201'>
<Record nineties.title='Fist of Legend'>
<Record nineties.title='The Legend II'>
<Record nineties.title='Crossworlds'>
<Record nineties.title='Tekken: The Motion Picture'>
<Record nineties.title='Kull the Conqueror'>
<Record nineties.title='A Simple Wish'>
<Record nineties.title='Chris Rock: Bigger and Blacker'>
<Record nineties.title='UFC 15.5: Ultimate Japan 1'>
<Record nineties.title='UFC 17.5: Ultimate Brazil'>
<Record nineties.title='The Beautician and the Beast'>
<Record nineties.title='Gypsy'>
<Record nineties.title='Tri karte za Hollywood'>
<Record nineties.title='Safe Sex'>
<Record nineties.title='Dance With Me'>
<Record nineties.title='Hush'>
<Record nineties.title='The Pest'>
<Record nineties.title='He Said, She Said'>
<Record nineties.title='Hell'>
<Record nineties.title='After Life'>
<Record nineties.title='Bleeder'>
<Record nineties.title='Impromptu'>
<Record nineties.title='Tetsuo II: Body Hammer'>
<Record nineties.title='Crusty Demons of Dirt 2'>
<Record nineties.title='Henry & June'>
<Record nineties.title='Leprechaun 2'>
<Record nineties.title='8 Seconds'>
<Record nineties.title='Out to Sea'>
<Record nineties.title="Dragon Ball GT - A Hero's Legacy">
<Record nineties.title='Chris Rock: Bring the Pain'>
<Record nineties.title='The Grifters'>
<Record nineties.title='The Program'>
<Record nineties.title='Obecná škola'>
<Record nineties.title='Love in Paris'>
<Record nineties.title='Como agua para chocolate'>
<Record nineties.title='Dream Lover'>
<Record nineties.title='Big Night'>
<Record nineties.title='El callejón de los milagros'>
<Record nineties.title='Better Than Chocolate'>
<Record nineties.title='Boxing Helena'>
<Record nineties.title='Poison Ivy II'>
<Record nineties.title='Poison Ivy: The New Seduction'>
<Record nineties.title='Sibirskiy tsiryulnik'>
<Record nineties.title='The Secret Adventures of Tom Thumb'>
<Record nineties.title='Castle Freak'>
<Record nineties.title='Sódóma Reykjavík'>
<Record nineties.title='Days of Being Wild'>
<Record nineties.title='Black Dog'>
<Record nineties.title='Happy Together'>
<Record nineties.title='The Assignment'>
<Record nineties.title='Embrace of the Vampire'>
<Record nineties.title='Exit to Eden'>
<Record nineties.title='Something to Talk About'>
<Record nineties.title='The Babe'>
<Record nineties.title='Kids in the Hall Brain candy'>
<Record nineties.title='Gummo'>
<Record nineties.title='The Other Sister'>
<Record nineties.title='City of Industry'>
<Record nineties.title='B.A.P.S.'>
<Record nineties.title='The Whole Wide World'>
<Record nineties.title='Bamse i trollskogen'>
<Record nineties.title='Rowan Atkinson: Not Just a Pretty Face'>
<Record nineties.title='La Nouvelle Eve'>
<Record nineties.title='Crusty 4: Gold Bless the Freaks'>
<Record nineties.title='Neon Genesis Evangelion: The End of Evangelion'>
<Record nineties.title='Folks!'>
<Record nineties.title='Free Willy 3: The Rescue'>
<Record nineties.title='Revenge of the Nerds III: The Next Generation'>
<Record nineties.title='Fled'>
<Record nineties.title='Flesh and Bone'>
<Record nineties.title='Forever Mine'>
<Record nineties.title='Foxfire'>
<Record nineties.title='Soul Music'>
<Record nineties.title='Oxygen'>
<Record nineties.title='Psy'>
<Record nineties.title='Uncovered'>
<Record nineties.title='Hands on a Hard Body: The Documentary'>
<Record nineties.title='Go Fish'>
<Record nineties.title='Best Laid Plans'>
<Record nineties.title='Beyond the Law'>
<Record nineties.title='Clean Slate'>
<Record nineties.title='Meltdown'>
<Record nineties.title='The East Is Red'>
<Record nineties.title='Red Dragon'>
<Record nineties.title='Swordsman II'>
<Record nineties.title='The Defender'>
<Record nineties.title='Eye of the Beholder'>
<Record nineties.title='Jerky Boys: The Movie'>
<Record nineties.title='Mr. Baseball'>
<Record nineties.title="Jet Li's The Enforcer">
<Record nineties.title='Last Hero in China'>
<Record nineties.title='Blue Juice'>
<Record nineties.title='Twin Dragons'>
<Record nineties.title='Doppelganger'>
<Record nineties.title='Haunted'>
<Record nineties.title='Magnificent Butcher'>
<Record nineties.title='Liu zhi qin mo'>
<Record nineties.title='The Bride with White Hair'>
<Record nineties.title='Macross Plus'>
<Record nineties.title='Jie zi zhan shi'>
<Record nineties.title='Crime Story'>
<Record nineties.title='Swordsman'>
<Record nineties.title='House Arrest'>
<Record nineties.title='Maborosi'>
<Record nineties.title='Kite'>
<Record nineties.title='3 Ninjas Kick Back'>
<Record nineties.title='Flight of the Intruder'>
<Record nineties.title="We're Back! A Dinosaur's Story">
<Record nineties.title='Jawbreaker'>
<Record nineties.title='Den eneste ene'>
<Record nineties.title="Betsy's Wedding">
<Record nineties.title='Spiklenci slasti'>
<Record nineties.title='Faust'>
<Record nineties.title="Comme un poisson hors de l'eau">
<Record nineties.title='Quest for Camelot'>
<Record nineties.title='Nirvana: MTV Unplugged in New York'>
<Record nineties.title='Ernest goes to Jail'>
<Record nineties.title='Rolling Stones Rock and Roll Circus'>
<Record nineties.title='FernGully 2: The Magical Rescue'>
<Record nineties.title='Rosencrantz and Guildenstern Are Dead'>
<Record nineties.title='The Adventures of Pinocchio'>
<Record nineties.title='Moll Flanders'>
<Record nineties.title='Darkman II: The Return of Durant'>
<Record nineties.title='Darkman III: Die Darkman Die'>
<Record nineties.title='The Land Before Time III: The Time of the Great Giving'>
<Record nineties.title='Záhrada'>
<Record nineties.title='AC/DC: Live at Donington'>
<Record nineties.title='Pearl Jam - Single Video Theory'>
<Record nineties.title='All Dogs Go to Heaven 2'>
<Record nineties.title='Light It Up'>
<Record nineties.title='Pure Luck'>
<Record nineties.title='The Wingless Bird'>
<Record nineties.title='Strays'>
<Record nineties.title='Delta Force 2 - The Colombian Connection'>
<Record nineties.title='LadyBugs'>
<Record nineties.title='Above The Rim'>
<Record nineties.title='A Little Princess'>
<Record nineties.title='Diggstown'>
<Record nineties.title='The Second Arrival'>
<Record nineties.title='Before the Rain'>
<Record nineties.title='Graveyard Shift'>
<Record nineties.title='Dancehall Queen'>
<Record nineties.title='The Land Before Time IV: Journey Through the Mists'>
<Record nineties.title='The Land Before Time V: The Mysterious Island'>
<Record nineties.title='The Cowboy Way'>
<Record nineties.title='The Night of the Living Dead'>
<Record nineties.title='Excellent Cadavers'>
<Record nineties.title='Shadows and Fog'>
<Record nineties.title='A Pure Formality'>
<Record nineties.title='Leprechaun 3'>
<Record nineties.title='Leprechaun 4: In Space'>
<Record nineties.title='Jury Duty'>
<Record nineties.title='Sleep With Me'>
<Record nineties.title='Meeting People Is Easy'>
<Record nineties.title='Mr. Nanny'>
<Record nineties.title='White Sands'>
<Record nineties.title='Strike!'>
<Record nineties.title='Dark Angel'>
<Record nineties.title='Dilwale Dulhania Le Jayenge'>
<Record nineties.title='Tribulation 99: Alien Anomalies Under America'>
<Record nineties.title='Held Up'>
<Record nineties.title='Hornblower The Even Chance'>
<Record nineties.title="God of Gamblers' Return">
<Record nineties.title='The Scent of Green Papaya'>
<Record nineties.title='Lifepod'>
<Record nineties.title='Airspeed'>
<Record nineties.title='The Death of the Incredible Hulk'>
<Record nineties.title='Bartok the Magnificent'>
<Record nineties.title='Bent'>
<Record nineties.title='Decampitated'>
<Record nineties.title="L'Homme que j'aime">
<Record nineties.title='Baazigar'>
<Record nineties.title='The Arrow'>
<Record nineties.title='Carry On Columbus'>
<Record nineties.title='Shoujo Kakumei Utena: Adolescence Mokushiroku'>
<Record nineties.title='The Amy Fisher Story'>
<Record nineties.title='Two If by Sea'>
<Record nineties.title='Der Laden'>
<Record nineties.title='Stomp Out Loud'>
<Record nineties.title='I Think I Do'>
<Record nineties.title='Blue Chips'>
<Record nineties.title='100 Days Before The Command'>
<Record nineties.title='The Interview'>
<Record nineties.title='The Players Club'>
<Record nineties.title='Breast Men'>
<Record nineties.title='The War'>
<Record nineties.title='Marco'>
<Record nineties.title='The Joy Luck Club'>
<Record nineties.title='Best Men'>
<Record nineties.title="'Weird Al' Yankovic: (There's No) Going Home">
<Record nineties.title='Bernie'>
"""

#Q4) List all Tom Hanks movies.


result = transaction.run("""
MATCH (tom:Actor {name: 'Tom Hanks'})-[:ACTS_IN]->(tomHanksMovies)
RETURN tom,tomHanksMovies
;""")
for record in result:
    print (record)
"""	
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=70162 labels={'Movie'} properties={'releaseDate': '492991200000', 'imdbId': 'tt0090274', 'runtime': 107, 'description': 'Lawrence is a rich kid with a bad accent and a large debt. After his father refuses to help him out, Lawrence escapes his angry debtors by jumping on a Peace Corp flight to Southeast Asia, where he is assigned to build a bridge for the local villagers with American-As-Apple-Pie WSU Grad Tom Tuttle and the beautiful and down-to earth Beth Wexler.', 'language': 'en', 'title': 'Volunteers', 'version': 99, 'imageUrl': 'http://cf1.imgobject.com/posters/1c4/4cd23a8e5e73d650210011c4/volunteers-mid.jpg', 'genre': 'Comedy', 'tagline': 'Ready or not, here they come.', 'lastModified': '1301904904000', 'id': '19259', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=64118 labels={'Movie'} properties={'studio': 'Magnolia Pictures', 'releaseDate': '1199142000000', 'imdbId': 'tt0460810', 'runtime': 87, 'description': 'When a law school dropout answers an advertisement to be a personal assistant he unknowingly signs on to work for a belligerent has-been magician struggling to resurrect his career. This leads to a journey across the country staging the comeback of a lifetime.', 'language': 'en', 'title': 'The Great Buck Howard', 'version': 202, 'trailer': 'http://www.youtube.com/watch?v=1627', 'imageUrl': 'http://cf1.imgobject.com/posters/fe7/4bc94b15017a3c57fe020fe7/the-great-buck-howard-mid.jpg', 'genre': 'Comedy', 'tagline': 'Greatness is a state of mind.', 'lastModified': '1301906257000', 'id': '16279', 'homepage': 'http://greatbuckhowardmovie.com/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=55655 labels={'Movie'} properties={'studio': 'Columbia Pictures', 'releaseDate': '1242338400000', 'imdbId': 'tt0808151', 'runtime': 138, 'description': 'The Pope died and the conclave has been called for. Four candidates were chosen. However, before the voting, the four candidates are killed one by one. The killer leaves clues that seems to say that he/she is from the Illuminati. Strangely though, the Illuminati was long thought to be extinct. Who is the mastermind? Who revived the Illuminati? What do they want?', 'language': 'en', 'title': 'Angels & Demons', 'version': 506, 'trailer': 'http://www.youtube.com/watch?v=ArdNQUUcZOM', 'imageUrl': 'http://cf1.imgobject.com/posters/341/4bed5b81017a3c37a0000341/angels-demons-mid.jpg', 'genre': 'Crime', 'tagline': 'The holiest event of our time. Perfect for their return.', 'lastModified': '1301900919000', 'id': '13448', 'homepage': 'http://www.angelsanddemons.com/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=52840 labels={'Movie'} properties={'releaseDate': '457308000000', 'imdbId': 'tt0086927', 'runtime': 105, 'description': "This outrageously funny look at one man's final moments of bachelorhood stars Tom Hanks as Rick, reluctant recipient of a bachelor bash given by a group of friends who view partying as their full-time religion. Rick's worried fiancée, Debbie (Tawny Kitaen), dresses up in disguise and crashes the party to spy on her future husband. ", 'language': 'en', 'title': 'Bachelor Party', 'version': 220, 'trailer': 'http://www.youtube.com/watch?v=VJhzlV3X5so', 'imageUrl': 'http://cf1.imgobject.com/posters/9d1/4bc938ec017a3c57fe0179d1/bachelor-party-mid.jpg', 'genre': 'Comedy', 'tagline': "A man's tradition every woman should know about.", 'lastModified': '1302021635000', 'id': '12309', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=43971 labels={'Movie'} properties={'releaseDate': '603673200000', 'imdbId': 'tt0096734', 'runtime': 101, 'description': "When secretive new neighbors move in next door, suburbanite Ray Peterson and his friends let their paranoia get the best of them as they start to suspect the newcomers of evildoings and commence an investigation. But it's hardly how Ray, who much prefers drinking beer, reading his newspaper and watching a ball game on the tube expected to spend his vacation.", 'language': 'en', 'title': "The 'Burbs", 'version': 163, 'trailer': 'http://www.youtube.com/watch?v=1944', 'imageUrl': 'http://cf1.imgobject.com/posters/fca/4d4788367b9aa15bb500bfca/the-burbs-mid.jpg', 'genre': 'Comedy', 'tagline': "He's a man of peace in a savage land... Suburbia.", 'lastModified': '1301907678000', 'id': '11974', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=42198 labels={'Movie'} properties={'releaseDate': '709941600000', 'imdbId': 'tt0104694', 'runtime': 128, 'description': 'Small-town sisters Dottie and Kit join an all-female baseball league formed after World War II brings pro baseball to a standstill. When their team hits the road with its drunken coach, the siblings find troubles and triumphs on and off the field.', 'language': 'en', 'title': 'A League of Their Own', 'version': 168, 'imageUrl': 'http://cf1.imgobject.com/posters/257/4bc9336b017a3c57fe015257/a-league-of-their-own-mid.jpg', 'genre': 'Comedy', 'tagline': 'To achieve the incredible you have to attempt the impossible.', 'lastModified': '1302039195000', 'id': '11287', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=41179 labels={'Movie'} properties={'releaseDate': '490572000000', 'imdbId': 'tt0089543', 'runtime': 92, 'description': 'A man is mistaken as a spy by the CIA when he arrives at the airport with one red shoe.', 'language': 'en', 'title': 'The Man with One Red Shoe', 'version': 192, 'trailer': 'http://www.youtube.com/watch?v=tqbuWpkoth0', 'imageUrl': 'http://cf1.imgobject.com/posters/27e/4bc93150017a3c57fe01427e/the-man-with-one-red-shoe-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301904333000', 'id': '10905', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=39758 labels={'Movie'} properties={'releaseDate': '511311600000', 'imdbId': 'tt0091541', 'runtime': 91, 'description': 'After being evicted from their Manhattan apartment, a couple buy what looks like the home of their dreams - only to find themselves saddled with a bank-account-draining nightmare. Struggling to keep their relationship together as their rambling mansion falls to pieces around them, the two watch in hilarious horror as everything - including the kitchen sink, disppears into the Money Pit.', 'language': 'en', 'title': 'The Money Pit', 'version': 102, 'trailer': 'http://www.youtube.com/watch?v=1947', 'imageUrl': 'http://cf1.imgobject.com/posters/c93/4bc92e42017a3c57fe012c93/the-money-pit-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1302044489000', 'id': '10466', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=38829 labels={'Movie'} properties={'studio': 'Pixar Animation Studios', 'releaseDate': '1276812000000', 'imdbId': 'tt0435761', 'runtime': 103, 'description': "Woody, Buzz, and the rest of Andy's toys haven't been played with in years. With Andy about to go to college, the gang find themselves accidentally left at a nefarious day care center. The toys must band together to escape and return home to Andy.", 'language': 'en', 'title': 'Toy Story 3', 'version': 971, 'trailer': 'http://www.youtube.com/watch?v=TNMpa5yBf5o', 'imageUrl': 'http://cf1.imgobject.com/posters/011/4cdb8b335e73d605e6000011/toy-story-3-mid.jpg', 'genre': 'Animation', 'tagline': 'No toy gets left behind.', 'lastModified': '1301900808000', 'id': '10193', 'homepage': 'http://disney.go.com/toystory/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=37581 labels={'Movie'} properties={'releaseDate': '551397600000', 'imdbId': 'tt0092925', 'runtime': 106, 'description': "They're so bad at being bad... but so much worse at being good!", 'language': 'en', 'title': 'Dragnet', 'version': 124, 'trailer': 'http://www.youtube.com/watch?v=D3AmdKuFYSM', 'imageUrl': 'http://cf1.imgobject.com/posters/051/4bf57f80017a3c772c000051/dragnet-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301902665000', 'id': '10023', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=35099 labels={'Movie'} properties={'releaseDate': '842652000000', 'imdbId': 'tt0117887', 'runtime': 108, 'description': 'A Pennsylvania band scores a hit in 1964 and rides the star-making machinery as long as it can, with lots of help from its manager.', 'language': 'en', 'title': 'That Thing You Do!', 'version': 148, 'imageUrl': 'http://cf1.imgobject.com/posters/e0e/4bc92755017a3c57fe00fe0e/that-thing-you-do-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1301902975000', 'id': '9591', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=35088 labels={'Movie'} properties={'releaseDate': '661734000000', 'imdbId': 'tt0099165', 'runtime': 125, 'description': 'Take one Wall Street tycoon, his Fifth Avenue mistress, a reporter hungry for fame, and make the wrong turn in The Bronx...then sit back and watch the sparks fly.', 'language': 'en', 'title': 'The Bonfire of the Vanities', 'version': 188, 'imageUrl': 'http://cf1.imgobject.com/posters/201/4c6088755e73d63462000201/the-bonfire-of-the-vanities-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1301903336000', 'id': '9586', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=34820 labels={'Movie'} properties={'releaseDate': '913935600000', 'imdbId': 'tt0128853', 'runtime': 119, 'description': "In this valentine to modern romance, book superstore magnate Joe Fox and independent book shop owner Kathleen Kelly fall in love in the anonymity of the Internet -- both blissfully unaware that he's trying to put her out of business.", 'language': 'en', 'title': "You've Got Mail", 'version': 284, 'trailer': 'http://www.youtube.com/watch?v=jCetfaS7GAo', 'imageUrl': 'http://cf1.imgobject.com/posters/a07/4d55b2da5e73d617c7006a07/you-ve-got-mail-mid.jpg', 'genre': 'Comedy', 'tagline': 'Someone you pass on the street may already be the love of your life.', 'lastModified': '1301970051000', 'id': '9489', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=32281 labels={'Movie'} properties={'studio': 'DreamWorks SKG', 'releaseDate': '976143600000', 'imdbId': 'tt0162222', 'runtime': 143, 'description': "Chuck, a top international manager for FedEx, and Kelly, a Ph.D. student, are in love and heading towards marriage. Then Chuck's plane to Malaysia ditches at sea during a terrible storm. He's the only survivor, and he washes up on a tiny island with nothing but some flotsam and jetsam from the aircraft's cargo. Can he survive in this tropical wasteland? Will he ever return to woman he loves?", 'language': 'en', 'title': 'Cast Away', 'version': 288, 'trailer': 'http://www.youtube.com/watch?v=-2-NJ2HJEkQ', 'imageUrl': 'http://cf1.imgobject.com/posters/232/4c79b5ce5e73d613d8000232/cast-away-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301901343000', 'id': '8358', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=30040 labels={'Movie'} properties={'studio': 'Touchstone Pictures', 'releaseDate': '599612400000', 'imdbId': 'tt0098536', 'runtime': 97, 'description': 'Scott Turner has 3 days left in the local police department before he moves to a bigger city to get some "real" cases, not just misdemeanors. Then Amos Reed is murdered, and Scott Turner sets himself on the case. The closest thing to a witness in the case is Amos Reed\'s dog, Hooch, which Scott Turner has to take care of if it\'s going to avoid being "put to sleep".', 'language': 'en', 'title': 'Turner & Hooch', 'version': 378, 'trailer': 'http://www.youtube.com/watch?v=gHc_eaKhKlo', 'imageUrl': 'http://cf1.imgobject.com/posters/eb9/4bc91e52017a3c57fe00beb9/turner-hooch-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301904352000', 'id': '6951', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=29354 labels={'Movie'} properties={'studio': 'Universal Pictures', 'releaseDate': '1198191600000', 'imdbId': 'tt0472062', 'runtime': 97, 'description': "A drama based on a Texas congressman Charlie Wilson's covert dealings in Afghanistan, where his efforts to assist rebels in their war with the Soviets have some unforeseen and long-reaching effects.", 'language': 'en', 'title': "Charlie Wilson's War", 'version': 320, 'trailer': 'http://www.youtube.com/watch?v=410', 'imageUrl': 'http://cf1.imgobject.com/posters/375/4d5a2b785e73d65e85000375/charlie-wilson-s-war-mid.jpg', 'genre': 'Comedy', 'tagline': 'Based on a true story. You think we could make all this up?', 'lastModified': '1301901834000', 'id': '6538', 'homepage': 'http://www.charliewilsonswar.net/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=26194 labels={'Movie'} properties={'studio': 'DreamWorks', 'releaseDate': '976143600000', 'imdbId': 'tt0250730', 'runtime': 88, 'description': 'No overview found.', 'language': 'en', 'title': 'Shooting War', 'version': 88, 'imageUrl': 'http://cf1.imgobject.com/posters/389/4ce219557b9aa168af000389/shooting-war-mid.jpg', 'genre': 'Documentary', 'tagline': '', 'lastModified': '1301943862000', 'id': '5707', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=25505 labels={'Movie'} properties={'studio': 'Touchstone Pictures', 'releaseDate': '1080255600000', 'imdbId': 'tt0335245', 'runtime': 104, 'description': 'An eccentric, if not charming Southern professor and his crew pose as a band in order to rob a casino, all under the nose of his unsuspecting landlord: a sharp old woman.', 'language': 'en', 'title': 'The Ladykillers', 'version': 225, 'imageUrl': 'http://cf1.imgobject.com/posters/ff6/4cbf22625e73d67784000ff6/the-ladykillers-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301903100000', 'id': '5516', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=21072 labels={'Movie'} properties={'studio': 'The Zanuck Company', 'releaseDate': '1026424800000', 'imdbId': 'tt0257044', 'runtime': 119, 'description': "Hit man Michael Sullivan, known in his 1930s Chicago world as The Angel of Death, is on the run after his wife and son are murdered. With his surviving son in tow, Michael sets out to exact brutal vengeance. Complicating matters are a reporter, Al Capone's enforcer and other shady characters.", 'language': 'en', 'title': 'Road to Perdition', 'version': 362, 'imageUrl': 'http://cf1.imgobject.com/posters/023/4c11d16f7b9aa17ec5000023/road-to-perdition-mid.jpg', 'genre': 'Action', 'tagline': 'Every son holds the future for his father.', 'lastModified': '1301901482000', 'id': '4147', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=16195 labels={'Movie'} properties={'studio': 'Touchstone Pictures', 'releaseDate': '447634800000', 'imdbId': 'tt0088161', 'runtime': 111, 'description': "A star-studded cast including Tom Hanks, Daryl Hannah and John Candy join together for this hilarious comedy. The fun starts when a successful businessman (Hanks) falls in love with the girl of his dreams (Daryl Hannah). There's one big complication though; he's fallen hook, line and sinker for a mermaid.", 'language': 'en', 'title': 'Splash', 'version': 85, 'imageUrl': 'http://cf1.imgobject.com/posters/c5c/4bc91726017a3c57fe008c5c/splash-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1301902869000', 'id': '2619', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=16044 labels={'Movie'} properties={'studio': 'Amblin Entertainment', 'releaseDate': '636937200000', 'imdbId': 'tt0099892', 'runtime': 102, 'description': 'Hypochondriac Joe Banks finds out he has six months to live, quits his dead end job, musters the courage to ask his female co-workder out on a date, and is then hired to jump into a volcano by a mysterious visitor.', 'language': 'en', 'title': 'Joe Versus the Volcano', 'version': 89, 'imageUrl': 'http://cf1.imgobject.com/posters/b1c/4bc916f0017a3c57fe008b1c/joe-versus-the-volcano-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1301904643000', 'id': '2565', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=14711 labels={'Movie'} properties={'studio': 'Gracie Films', 'releaseDate': '581292000000', 'imdbId': 'tt0094737', 'runtime': 104, 'description': 'When a boy wishes to be big at a magic wish machine, he wakes up the next morning and finds himself in an adult body literally overnight.', 'language': 'en', 'title': 'Big', 'version': 384, 'trailer': 'http://www.youtube.com/watch?v=J62jciQ1PbY', 'imageUrl': 'http://cf1.imgobject.com/posters/055/4c55c6ec5e73d63a6c000055/big-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1302022400000', 'id': '2280', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=8176 labels={'Movie'} properties={'studio': 'Pixar Animation Studios', 'releaseDate': '942447600000', 'imdbId': 'tt0120363', 'runtime': 92, 'description': 'During a garage sale Andy’s mother sells some of Andy’s old things including his favorite toy Woody to a collector. Buzz Lightyear and the other toys begin a reckless mission to save their friend. The sequel to the revolutionary computer animated feature film Toy Story.', 'language': 'en', 'title': 'Toy Story 2', 'version': 272, 'trailer': 'http://www.youtube.com/watch?v=Lu0sotERXhI', 'imageUrl': 'http://cf1.imgobject.com/posters/cc4/4cbbc7a35e73d67786000cc4/toy-story-2-mid.jpg', 'genre': 'Adventure', 'tagline': 'The toys are back!', 'lastModified': '1300260981000', 'id': '863', 'homepage': 'http://disney.go.com/disneyvideos/animatedfilms/toystory/getflash.html'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=8168 labels={'Movie'} properties={'studio': 'Pixar Animation Studios', 'releaseDate': '816994800000', 'imdbId': 'tt0114709', 'runtime': 81, 'description': 'Woody the cowboy is young Andy’s favorite toy. Yet this changes when Andy get the new super toy Buzz Lightyear for his birthday. Now that Woody is no longer number one he plans his revenge on Buzz. Toy Story is a milestone in film history for being the first feature film to use entirely computer animation.', 'language': 'en', 'title': 'Toy Story', 'version': 231, 'trailer': 'http://www.youtube.com/watch?v=KYz2wyBy3kc', 'imageUrl': 'http://cf1.imgobject.com/posters/d90/4bc90db3017a3c57fe004d90/toy-story-mid.jpg', 'genre': 'Adventure', 'tagline': 'The adventure takes off!', 'lastModified': '1300261194000', 'id': '862', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=8139 labels={'Movie'} properties={'studio': 'Tristar Pictures', 'releaseDate': '740959200000', 'imdbId': 'tt0108160', 'runtime': 105, 'description': 'A young boy who tries to set his dad up on a date after the death of his mother. He calls into a radio station to talk about his dad’s loneliness which soon leads the dad into meeting a Journalist Annie who flies to Seattle to write a story about the boy and his dad.  Yet Annie ends up with more than just a story in this popular romantic comedy.', 'language': 'en', 'title': 'Sleepless in Seattle', 'version': 158, 'trailer': 'http://www.youtube.com/watch?v=1341', 'imageUrl': 'http://cf1.imgobject.com/posters/2c0/4c879fee5e73d66b5e0002c0/sleepless-in-seattle-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1300261966000', 'id': '858', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=8132 labels={'Movie'} properties={'studio': 'DreamWorks SKG', 'releaseDate': '901231200000', 'imdbId': 'tt0120815', 'runtime': 170, 'description': 'As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, with a fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with penetrating German-held territory and bringing the boy home.', 'language': 'en', 'title': 'Saving Private Ryan', 'version': 346, 'trailer': 'http://www.youtube.com/watch?v=5ci-ApiC1nI', 'imageUrl': 'http://cf1.imgobject.com/posters/e2b/4cd0ffcc5e73d65025000e2b/saving-private-ryan-mid.jpg', 'genre': 'Action', 'tagline': 'In the Last Great Invasion of the Last Great War, The Greatest Danger for Eight Men was Saving... One.', 'lastModified': '1300262159000', 'id': '857', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=6359 labels={'Movie'} properties={'studio': 'Amblin Entertainment', 'releaseDate': '1040770800000', 'imdbId': 'tt0264464', 'runtime': 141, 'description': "Frank W. Abagnale Jr. is a cunning con man -- posing as a doctor, lawyer and pilot all before turning 21. He's also a deft forger, and his work attracts the attention of FBI agent Carl Hanratty, who makes it his mission to put Frank behind bars. But Frank not only eludes capture, he revels in the pursuit, even taking time to taunt Carl by phone.", 'language': 'en', 'title': 'Catch Me If You Can', 'version': 190, 'trailer': 'http://www.youtube.com/watch?v=hFj3OXVL_wQ', 'imageUrl': 'http://cf1.imgobject.com/posters/a1c/4bc90a7f017a3c57fe003a1c/catch-me-if-you-can-mid.jpg', 'genre': 'Comedy', 'tagline': 'The true story of a real fake.', 'lastModified': '1300095474000', 'id': '640', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=5965 labels={'Movie'} properties={'studio': 'Amblin Entertainment', 'releaseDate': '1087509600000', 'imdbId': 'tt0362227', 'runtime': 124, 'description': 'A comedy that shows how the America immigration office deals with a East-European foreigner without a country. Director Steven Spielberg gives us a humorous look into the difficulties one man with very little English knowledge faces while stuck in a New York airport while his country is at civil war.', 'language': 'en', 'title': 'The Terminal', 'version': 164, 'trailer': 'http://www.youtube.com/watch?v=Xm1xrJD5aW8', 'imageUrl': 'http://cf1.imgobject.com/posters/c5a/4d507c6c7b9aa13aaf00dc5a/the-terminal-mid.jpg', 'genre': 'Comedy', 'tagline': 'Life is waiting.', 'lastModified': '1299970507000', 'id': '594', 'homepage': 'http://www.theterminal-themovie.com/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=5934 labels={'Movie'} properties={'studio': ' Columbia Pictures', 'releaseDate': '1147989600000', 'imdbId': 'tt0382625', 'runtime': 149, 'description': 'A murder inside the Louvre and clues in Da Vinci paintings lead to the discovery of a religious mystery protected by a secret society for two thousand years, which could shake the foundations of Christianity.', 'language': 'en', 'title': 'The Da Vinci Code', 'version': 304, 'trailer': 'http://www.youtube.com/watch?v=pE7apZzCIAA', 'imageUrl': 'http://cf1.imgobject.com/posters/011/4c493bf27b9aa115fc000011/the-da-vinci-code-mid.jpg', 'genre': 'Drama', 'tagline': 'So Dark The Con Of Man', 'lastModified': '1299971059000', 'id': '591', 'homepage': 'http://www.sonypictures.com/homevideo/thedavincicode/index.html'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=1073 labels={'Movie'} properties={'studio': 'Gracie Films', 'releaseDate': '1185487200000', 'imdbId': 'tt0462538', 'runtime': 87, 'description': "After Homer accidentally pollutes the town's water supply, Springfield is encased in a gigantic dome by the EPA and the Simpsons are  declared fugitives.", 'language': 'en', 'title': 'The Simpsons Movie', 'version': 440, 'trailer': 'http://www.youtube.com/watch?v=AB7VF980cEA', 'imageUrl': 'http://cf1.imgobject.com/posters/429/4bc901e5017a3c57fe000429/the-simpsons-movie-mid.jpg', 'genre': 'Animation', 'tagline': 'See our family. And feel better about yours.', 'lastModified': '1299913538000', 'id': '35', 'homepage': 'http://www.simpsonsmovie.com/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=780 labels={'Movie'} properties={'studio': 'Warner Bros. Pictures', 'releaseDate': '944780400000', 'imdbId': 'tt0120689', 'runtime': 188, 'description': "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cellblock's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.", 'language': 'en', 'title': 'The Green Mile', 'version': 200, 'trailer': 'http://www.youtube.com/watch?v=ctRK-4Vt7dA', 'imageUrl': 'http://cf1.imgobject.com/posters/c01/4bc90828017a3c57fe002c01/the-green-mile-mid.jpg', 'genre': 'Crime', 'tagline': 'Miracles do happen.', 'lastModified': '1299985732000', 'id': '497', 'homepage': 'http://thegreenmile.warnerbros.com/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=774 labels={'Movie'} properties={'releaseDate': '756601200000', 'imdbId': 'tt0107818', 'runtime': 125, 'description': 'No one would take his case until one man was willing to take on the system. Two competing lawyers join forces to sue a prestigious law firm for aids discrimination. As their unlikely friendship develops their courage overcomes the prejudice and corruption of their powerful adversaries.', 'language': 'en', 'title': 'Philadelphia', 'version': 148, 'imageUrl': 'http://cf1.imgobject.com/posters/ac4/4bc92922017a3c57fe010ac4/philadelphia-mid.jpg', 'genre': 'Drama', 'tagline': '', 'lastModified': '1300170007000', 'id': '9800', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=756 labels={'Movie'} properties={'studio': 'Universal Pictures', 'releaseDate': '803772000000', 'imdbId': 'tt0112384', 'runtime': 140, 'description': "Technical troubles scuttle the Apollo 13 lunar mission in 1971, risking the lives of astronaut Jim Lovell  and his crew in director Ron Howard's chronicle of this true-life story, which turns a failed journey into a thrilling saga of heroism. Drifting more than 200,000 miles from Earth, the astronauts work furiously with the ground crew to avert tragedy.", 'language': 'en', 'title': 'Apollo 13', 'version': 236, 'trailer': 'http://www.youtube.com/watch?v=nEl0NsYn1fU', 'imageUrl': 'http://cf1.imgobject.com/posters/177/4d68030e7b9aa13636000177/apollo-13-mid.jpg', 'genre': 'Action', 'tagline': 'Houston, we have a problem.', 'lastModified': '1299974865000', 'id': '568', 'homepage': ''}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=746 labels={'Movie'} properties={'studio': 'Castle Rock Entertainment', 'releaseDate': '1098309600000', 'imdbId': 'tt0338348', 'runtime': 100, 'description': "This is the story of a young hero boy on Christmas Eve who boards on a powerful magical train that's headed to the North Pole and Santa Claus's home. What unfolds is an an adventure which follows a doubting boy, who takes an extraordinary train ride to the North Pole; during this ride, he embarks on a journey of self-discovery which shows him that the wonder of life never fades for those who believe.", 'language': 'en', 'title': 'The Polar Express', 'version': 956, 'trailer': 'http://www.youtube.com/watch?v=ATUt_-p2XqM', 'imageUrl': 'http://cf1.imgobject.com/posters/eab/4d6039ac5e73d63105000eab/the-polar-express-mid.jpg', 'genre': 'Adventure', 'tagline': 'Journey Beyond Your Imagination.', 'lastModified': '1300185594000', 'id': '5255', 'homepage': 'http://wwws.warnerbros.de/movies/polarexpress/'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> tomHanksMovies=<Node id=522 labels={'Movie'} properties={'studio': 'Paramount Pictures', 'releaseDate': '772322400000', 'imdbId': 'tt0109830', 'runtime': 142, 'description': 'Forrest Gump, affetto da un leggero deficit mentale, racconta seduto in una panchina il suo passato e il suo amore per Jenny. Forrest ha affrontato vari momenti della storia americana, compresa la guerra in Vietnam, riuscendo a cavarsela in qualsiasi situazione.', 'language': 'en', 'title': 'Forrest Gump', 'version': 274, 'trailer': 'http://www.youtube.com/watch?v=obaW5wZw3rE', 'imageUrl': 'http://cf1.imgobject.com/posters/062/4d0ae6a57b9aa10982000062/forrest-gump-mid.jpg', 'genre': 'Action', 'tagline': 'La vita è come una scatola di cioccolatini, non sai mai quello che ti capita!', 'lastModified': '1299913624000', 'id': '13', 'homepage': ''}>>
"""

#Q5) Who directed "Avatar".


result = transaction.run("""
MATCH (avatar {title: 'Avatar'})<-[:DIRECTED]-(directors)
RETURN directors.name
;""")
for record in result:
    print (record)
	
#<Record directors.name='James Cameron'>


#Q6) Tom Hanks' co-actors.


result = transaction.run("""
MATCH (tom:Actor {name:'Tom Hanks'})-[:ACTS_IN]->(m)<-[:ACTS_IN]-(coActors)
RETURN coActors.name
;""")
for record in result:
    print (record)
"""	
<Record coActors.name='Rita Wilson'>
<Record coActors.name='John Candy'>
<Record coActors.name="Conan O'Brien">
<Record coActors.name='Patrick Fischler'>
<Record coActors.name='Kelly Ripa'>
<Record coActors.name='Jon Stewart'>
<Record coActors.name='Adam Scott'>
<Record coActors.name='Colin Hanks'>
<Record coActors.name='Jay Leno'>
<Record coActors.name='Steve Zahn'>
<Record coActors.name='Emily Blunt'>
<Record coActors.name='John Malkovich'>
<Record coActors.name='Paul Richards'>
<Record coActors.name='Aaron Denius Garcia'>
<Record coActors.name='Shervin Davatgar'>
<Record coActors.name='Cristy Joy Slavis'>
<Record coActors.name='Jason Ciok'>
<Record coActors.name='Les Feltmate'>
<Record coActors.name='Dave Johnson'>
<Record coActors.name='Jerred Berg'>
<Record coActors.name='Ted Hollis'>
<Record coActors.name='August Fredrik'>
<Record coActors.name='Jon Lucero'>
<Record coActors.name='Jeffrey Boehm'>
<Record coActors.name='Laura Mary Clarke'>
<Record coActors.name='Luca Costa'>
<Record coActors.name='Stephen Sepher'>
<Record coActors.name='Richard Schimmelpfenneg'>
<Record coActors.name='Ed Francis Martin'>
<Record coActors.name='Joel Shock'>
<Record coActors.name='Jonas Fisch'>
<Record coActors.name='Bryan Friday'>
<Record coActors.name='Michael Arturo'>
<Record coActors.name='Curt Lowens'>
<Record coActors.name='Craig Seitz'>
<Record coActors.name='Nancy Guerriero'>
<Record coActors.name='Calvin Dean'>
<Record coActors.name='Kristof Konrad'>
<Record coActors.name='Luis Fernandez-Gil'>
<Record coActors.name='James Tumminia'>
<Record coActors.name='Pascal Petardi'>
<Record coActors.name='Skoti Collins'>
<Record coActors.name='Michael Patrick Breen'>
<Record coActors.name='Rashmi'>
<Record coActors.name='Yan Cui'>
<Record coActors.name='Victor Alfieri'>
<Record coActors.name='Shelby Zemanek'>
<Record coActors.name='Kimberley Joseph'>
<Record coActors.name='Endre Hules'>
<Record coActors.name='Gino Conforti'>
<Record coActors.name='Arlo Hemphill'>
<Record coActors.name='Masasa Moyo'>
<Record coActors.name='Norbert Weisser'>
<Record coActors.name='Nikolaj Lie Kaas'>
<Record coActors.name='Elya Baskin'>
<Record coActors.name='Thure Lindhardt'>
<Record coActors.name='Pierfrancesco Favino'>
<Record coActors.name='Ursula Brooks'>
<Record coActors.name='Carmen Argenziano'>
<Record coActors.name='Allen Dula'>
<Record coActors.name='Cosimo Fusco'>
<Record coActors.name='Ayelet Zurer'>
<Record coActors.name='David Pasquesi'>
<Record coActors.name='Stellan Skarsgård'>
<Record coActors.name='Armin Mueller-Stahl'>
<Record coActors.name='Ewan McGregor'>
<Record coActors.name='George Grizzard'>
<Record coActors.name='Adrian Zmed'>
<Record coActors.name='Tawny Kitaen'>
<Record coActors.name='Gale Gordon'>
<Record coActors.name='Courtney Gains'>
<Record coActors.name='Brother Theodore'>
<Record coActors.name='Henry Gibson'>
<Record coActors.name='Wendy Schaal'>
<Record coActors.name='Corey Feldman'>
<Record coActors.name='Rick Ducommun'>
<Record coActors.name='Bruce Dern'>
<Record coActors.name='Cory Danziger'>
<Record coActors.name='Carrie Fisher'>
<Record coActors.name='Ann Cusack'>
<Record coActors.name='Renée Coleman'>
<Record coActors.name='Don S. Davis'>
<Record coActors.name='Bitty Schram'>
<Record coActors.name='Tracy Reiner'>
<Record coActors.name="Rosie O'Donnell">
<Record coActors.name='Megan Cavanagh'>
<Record coActors.name='Bill Pullman'>
<Record coActors.name='Garry Marshall'>
<Record coActors.name='David Strathairn'>
<Record coActors.name='Jon Lovitz'>
<Record coActors.name='Lori Petty'>
<Record coActors.name='Madonna Louise Veronica Ciccone'>
<Record coActors.name='Geena Davis'>
<Record coActors.name='James Belushi'>
<Record coActors.name='Edward Herrmann'>
<Record coActors.name='Carrie Fisher'>
<Record coActors.name='Charles Durning'>
<Record coActors.name='Lori Singer'>
<Record coActors.name='Dabney Coleman'>
<Record coActors.name='Joe Mantegna'>
<Record coActors.name='Maureen Stapleton'>
<Record coActors.name='Alexander Godunov'>
<Record coActors.name='Shelley Long'>
<Record coActors.name='Estelle Harris'>
<Record coActors.name='Don Rickles'>
<Record coActors.name='John Ratzenberger'>
<Record coActors.name='Wallace Shawn'>
<Record coActors.name='Bonnie Hunt'>
<Record coActors.name='Whoopi Goldberg'>
<Record coActors.name='Michael Keaton'>
<Record coActors.name='Ned Beatty'>
<Record coActors.name='Joan Cusack'>
<Record coActors.name='Tim Allen'>
<Record coActors.name='Alexandra Paul'>
<Record coActors.name='Harry Morgan'>
<Record coActors.name='Christopher Plummer'>
<Record coActors.name='Dan Aykroyd'>
<Record coActors.name='Giovanni Ribisi'>
<Record coActors.name='Ethan Embry'>
<Record coActors.name='Charlize Theron'>
<Record coActors.name='Steve Zahn'>
<Record coActors.name='Johnathon Schaech'>
<Record coActors.name='Liv Tyler'>
<Record coActors.name='Tom Everett Scott'>
<Record coActors.name='Morgan Freeman'>
<Record coActors.name='Saul Rubinek'>
<Record coActors.name='Kim Cattrall'>
<Record coActors.name='Melanie Griffith'>
<Record coActors.name='Bruce Willis'>
<Record coActors.name='Greg Kinnear'>
<Record coActors.name='Katie Sagona'>
<Record coActors.name='Meg Ryan'>
<Record coActors.name='Dmitri S. Boudrine'>
<Record coActors.name='Peter von Berg'>
<Record coActors.name='Semion Sudarikov'>
<Record coActors.name='David Allen Brooks'>
<Record coActors.name='Leonid Citer'>
<Record coActors.name='Lari White'>
<Record coActors.name='Paul Sanchez'>
<Record coActors.name='Chris Noth'>
<Record coActors.name='Helen Hunt'>
<Record coActors.name='Mary McCusker'>
<Record coActors.name='Reginald VelJohnson'>
<Record coActors.name='David Knell'>
<Record coActors.name='John McIntire'>
<Record coActors.name='Scott Paulin'>
<Record coActors.name='Craig T. Nelson'>
<Record coActors.name='Mare Winningham'>
<Record coActors.name='Cyia Batten'>
<Record coActors.name='Erick Avari'>
<Record coActors.name='Rachel Nichols'>
<Record coActors.name='John Slattery'>
<Record coActors.name='Shiri Appleby'>
<Record coActors.name='Om Puri'>
<Record coActors.name='Amy Adams'>
<Record coActors.name='Julia Roberts'>
<Record coActors.name='Philip Seymour Hoffman'>
<Record coActors.name='John Ford'>
<Record coActors.name='Russ Meyer'>
<Record coActors.name='Stephen Ambrose'>
<Record coActors.name='John McConnell'>
<Record coActors.name='George Wallace'>
<Record coActors.name='Diane Delano'>
<Record coActors.name='Ryan Hurst'>
<Record coActors.name='Tzi Ma'>
<Record coActors.name='J.K. Simmons'>
<Record coActors.name='Marlon Wayans'>
<Record coActors.name='Irma P. Hall'>
<Record coActors.name='Duane Sharp'>
<Record coActors.name='Kurt Naebig'>
<Record coActors.name='Stanley Tucci'>
<Record coActors.name='Jude Law'>
<Record coActors.name='Doug Spinuzza'>
<Record coActors.name='Kevin Chamberlin'>
<Record coActors.name='David Darlow'>
<Record coActors.name='Ciarán Hinds'>
<Record coActors.name='Daniel Craig'>
<Record coActors.name='Paul Newman'>
<Record coActors.name='Liam Aiken'>
<Record coActors.name='Jennifer Jason Leigh'>
<Record coActors.name='Babaloo Mandel'>
<Record coActors.name='Lowell Ganz'>
<Record coActors.name='Howard Morris'>
<Record coActors.name='Bobby Di Cicco'>
<Record coActors.name='Richard B. Shull'>
<Record coActors.name='Shecky Greene'>
<Record coActors.name='Dody Goodman'>
<Record coActors.name='John Candy'>
<Record coActors.name='Eugene Levy'>
<Record coActors.name='Daryl Hannah'>
<Record coActors.name='Robert Stack'>
<Record coActors.name='Barry McGovern'>
<Record coActors.name='Ossie Davis'>
<Record coActors.name='Dan Hedaya'>
<Record coActors.name='Lloyd Bridges'>
<Record coActors.name='Meg Ryan'>
<Record coActors.name='Mercedes Ruehl'>
<Record coActors.name='Jon Lovitz'>
<Record coActors.name='John Heard'>
<Record coActors.name='Robert Loggia'>
<Record coActors.name='Elizabeth Perkins'>
<Record coActors.name='Tim Allen'>
<Record coActors.name='John Morris'>
<Record coActors.name='Wayne Knight'>
<Record coActors.name='Annie Potts'>
<Record coActors.name='John Ratzenberger'>
<Record coActors.name='Wallace Shawn'>
<Record coActors.name='Jim Varney'>
<Record coActors.name='Don Rickles'>
<Record coActors.name='Kelsey Grammer'>
<Record coActors.name='Joan Cusack'>
<Record coActors.name='Sarah Freeman'>
<Record coActors.name='R. Lee Ermey'>
<Record coActors.name='Laurie Metcalf'>
<Record coActors.name='Erik von Detten'>
<Record coActors.name='Annie Potts'>
<Record coActors.name='John Ratzenberger'>
<Record coActors.name='Wallace Shawn'>
<Record coActors.name='Jim Varney'>
<Record coActors.name='Don Rickles'>
<Record coActors.name='John Morris'>
<Record coActors.name='Tim Allen'>
<Record coActors.name='Dana Ivey'>
<Record coActors.name='David Hyde Pierce'>
<Record coActors.name='Carey Lowell'>
<Record coActors.name='Rob Reiner'>
<Record coActors.name='Barbara Garrick'>
<Record coActors.name='Rita Wilson'>
<Record coActors.name='Victor Garber'>
<Record coActors.name='Gaby Hoffmann'>
<Record coActors.name="Rosie O'Donnell">
<Record coActors.name='Ross Malinger'>
<Record coActors.name='Bill Pullman'>
<Record coActors.name='Meg Ryan'>
<Record coActors.name='Paul Giamatti'>
<Record coActors.name='Ted Danson'>
<Record coActors.name='Jeremy Davies'>
<Record coActors.name='Giovanni Ribisi'>
<Record coActors.name='Adam Goldberg'>
<Record coActors.name='Vin Diesel'>
<Record coActors.name='Barry Pepper'>
<Record coActors.name='Edward Burns'>
<Record coActors.name='Matt Damon'>
<Record coActors.name='Max Martini'>
<Record coActors.name='Harve Presnell'>
<Record coActors.name='Joerg Stadler'>
<Record coActors.name='Dennis Farina'>
<Record coActors.name='Tom Sizemore'>
<Record coActors.name='Nathalie Baye'>
<Record coActors.name='Thomas Kopache'>
<Record coActors.name='Candice Azzara'>
<Record coActors.name='Guy Thauvette'>
<Record coActors.name='Elizabeth Banks'>
<Record coActors.name='Ellen Pompeo'>
<Record coActors.name='Nancy Lenehan'>
<Record coActors.name='Jennifer Garner'>
<Record coActors.name='John Finn'>
<Record coActors.name='Chris Ellis'>
<Record coActors.name='Steve Eastin'>
<Record coActors.name='Frank John Hughes'>
<Record coActors.name='Brian Howe'>
<Record coActors.name='James Brolin'>
<Record coActors.name='Amy Adams'>
<Record coActors.name='Martin Sheen'>
<Record coActors.name='Christopher Walken'>
<Record coActors.name='Leonardo DiCaprio'>
<Record coActors.name='Sasha Spielberg'>
<Record coActors.name='Michael Nouri'>
<Record coActors.name='Valeri Nikolayev'>
<Record coActors.name='Stephen Mendel'>
<Record coActors.name='Rini Bell'>
<Record coActors.name='Guillermo Díaz'>
<Record coActors.name='Corey Reynolds'>
<Record coActors.name='Jude Ciccolella'>
<Record coActors.name='Eddie Jones'>
<Record coActors.name='Zoe Saldana'>
<Record coActors.name='Kumar Pallana'>
<Record coActors.name='Barry Shabaka Henley'>
<Record coActors.name='Diego Luna'>
<Record coActors.name='Chi McBride'>
<Record coActors.name='Stanley Tucci'>
<Record coActors.name='Catherine Zeta-Jones'>
<Record coActors.name='Seth Gabel'>
<Record coActors.name='Peter Pedrero'>
<Record coActors.name='Tina Maskell'>
<Record coActors.name='Agathe Natanson'>
<Record coActors.name='Marie-Françoise Audollent'>
<Record coActors.name='Jürgen Prochnow'>
<Record coActors.name='Etienne Chicot'>
<Record coActors.name='Jean-Pierre Marielle'>
<Record coActors.name='Jean-Yves Berteloot'>
<Record coActors.name='Alfred Molina'>
<Record coActors.name='Jean Reno'>
<Record coActors.name='Paul Bettany'>
<Record coActors.name='Ian McKellen'>
<Record coActors.name='Audrey Tautou'>
<Record coActors.name='Joe Mantegna'>
<Record coActors.name='Marcia Wallace'>
<Record coActors.name='Pamela Hayden'>
<Record coActors.name='Maile Flanagan'>
<Record coActors.name='Kelsey Grammer'>
<Record coActors.name='Harry Shearer'>
<Record coActors.name='Hank Azaria'>
<Record coActors.name='Yeardley Smith'>
<Record coActors.name='Nancy Cartwright'>
<Record coActors.name='Julie Kavner'>
<Record coActors.name='Dan Castellaneta'>
<Record coActors.name='Barry Pepper'>
<Record coActors.name='James Cromwell'>
<Record coActors.name='Sam Rockwell'>
<Record coActors.name='Doug Hutchison'>
<Record coActors.name='Gary Sinise'>
<Record coActors.name='Dabbs Greer'>
<Record coActors.name='Patricia Clarkson'>
<Record coActors.name='Graham Greene'>
<Record coActors.name='Michael Jeter'>
<Record coActors.name='David Morse'>
<Record coActors.name='Bonnie Hunt'>
<Record coActors.name='Michael Clarke Duncan'>
<Record coActors.name='Denzel Washington'>
<Record coActors.name='Antonio Banderas'>
<Record coActors.name='Buzz Kilman'>
<Record coActors.name='Roberta Maxwell'>
<Record coActors.name='Roger Corman'>
<Record coActors.name='Xander Berkeley'>
<Record coActors.name='Joe Spano'>
<Record coActors.name='Chris Ellis'>
<Record coActors.name='Michele Little'>
<Record coActors.name='David Andrews'>
<Record coActors.name='Tracy Reiner'>
<Record coActors.name='Jean Speegle Howard'>
<Record coActors.name='Max Elliott Slade'>
<Record coActors.name='Miko Hughes'>
<Record coActors.name='Emily Ann Lloyd'>
<Record coActors.name='Mary Kate Schellhardt'>
<Record coActors.name='Kathleen Quinlan'>
<Record coActors.name='Ed Harris'>
<Record coActors.name='Gary Sinise'>
<Record coActors.name='Kevin Bacon'>
<Record coActors.name='Bill Paxton'>
<Record coActors.name='Julene Renee'>
<Record coActors.name='Leslie Zemeckis'>
<Record coActors.name='Steven Tyler'>
<Record coActors.name='Charles Fleischer'>
<Record coActors.name='Peter Scolari'>
<Record coActors.name='Nona Gaye'>
<Record coActors.name='Chris Coppola'>
<Record coActors.name='Eddie Deezen'>
<Record coActors.name='Michael Jeter'>
<Record coActors.name='Sam Anderson'>
<Record coActors.name='Kevin Mangan'>
<Record coActors.name='Marlena Smalls'>
<Record coActors.name='Kitty K. Green'>
<Record coActors.name='Haley Joel Osment'>
<Record coActors.name='Michael Mattison'>
<Record coActors.name='Nora Dunfee'>
<Record coActors.name='John William Galt'>
<Record coActors.name='Steven Griffith'>
<Record coActors.name='Afemo Omilami'>
<Record coActors.name='Jed Gillin'>
<Record coActors.name='Sonny Shroyer'>
<Record coActors.name='Hanna R. Hall'>
<Record coActors.name='Peter Dobson'>
<Record coActors.name='Michael Conner Humphreys'>
<Record coActors.name='Sally Field'>
<Record coActors.name='Mykelti Williamson'>
<Record coActors.name='Gary Sinise'>
<Record coActors.name='Robin Wright'>
"""

#Q7) How people are related to "Avatar".


result = transaction.run("""
MATCH (people:Person)-[relatedTo]-(:Movie {title:'Avatar'})
RETURN people.name, Type(relatedTo), relatedTo
;""")
for record in result:
    print (record)
"""	
<Record people.name='Dean Knowsley' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=431 start=359 end=345 type='ACTS_IN' properties={'name': 'Samson Pilot'}>>
<Record people.name='Matt Gerald' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=430 start=358 end=345 type='ACTS_IN' properties={'name': 'Lyle Wainfleet'}>>
<Record people.name='Dileep Rao' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=429 start=357 end=345 type='ACTS_IN' properties={'name': 'Dr. Max Patel'}>>
<Record people.name='Wes Studi' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=428 start=356 end=345 type='ACTS_IN' properties={'name': 'Eytukan'}>>
<Record people.name='Laz Alonso' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=427 start=355 end=345 type='ACTS_IN' properties={'name': "Tsu'Tey"}>>
<Record people.name='CCH Pounder' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=426 start=354 end=345 type='ACTS_IN' properties={'name': 'Moha'}>>
<Record people.name='Giovanni Ribisi' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=425 start=353 end=345 type='ACTS_IN' properties={'name': 'Selfridge'}>>
<Record people.name='Joel Moore' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=424 start=352 end=345 type='ACTS_IN' properties={'name': 'Norm Spellman'}>>
<Record people.name='Michelle Rodriguez' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=423 start=351 end=345 type='ACTS_IN' properties={'name': 'Trudy Chacon'}>>
<Record people.name='Stephen Lang' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=422 start=350 end=345 type='ACTS_IN' properties={'name': 'Col. Quaritch'}>>
<Record people.name='Sigourney Weaver' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=421 start=349 end=345 type='ACTS_IN' properties={'name': 'Dr. Grace Augustine'}>>
<Record people.name='Zoe Saldana' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=420 start=348 end=345 type='ACTS_IN' properties={'name': 'Neytiri'}>>
<Record people.name='Sam Worthington' Type(relatedTo)='ACTS_IN' relatedTo=<Relationship id=419 start=347 end=345 type='ACTS_IN' properties={'name': 'Jake Sully'}>>
<Record people.name='James Cameron' Type(relatedTo)='DIRECTED' relatedTo=<Relationship id=418 start=346 end=345 type='DIRECTED' properties={}>>
"""



#Q8) Extend Tom Hanks co-actors, to find co-co-actors who haven't worked with Tom Hanks.


result = transaction.run("""
MATCH (tom:Actor {name:'Tom Hanks'})-[:ACTS_IN]->(m)<-[:ACTS_IN]-(coActors),
(coActors)-[:ACTS_IN]->(m2)<-[:ACTS_IN]-(cocoActors)
WHERE NOT (tom)-[:ACTS_IN]->(m2)
RETURN cocoActors.name AS Recommended, count(*) AS Strength
ORDER BY Strength DESC
;""")
for record in result:
    print (record)


"""
<Record Recommended='Samuel L. Jackson' Strength=50>
<Record Recommended='Bruce Willis' Strength=50>
<Record Recommended='Dan Aykroyd' Strength=50>
<Record Recommended='Alec Baldwin' Strength=39>
<Record Recommended='Steve Buscemi' Strength=38>
<Record Recommended='Ben Affleck' Strength=37>
<Record Recommended='George Clooney' Strength=35>
<Record Recommended='Willem Dafoe' Strength=35>
<Record Recommended='Patrick Warburton' Strength=35>
<Record Recommended='Nicolas Cage' Strength=34>
<Record Recommended='Dennis Quaid' Strength=33>
<Record Recommended="Catherine O'Hara" Strength=32>
<Record Recommended='John Cusack' Strength=32>
<Record Recommended='John Candy' Strength=31>
<Record Recommended='William H. Macy' Strength=31>
<Record Recommended='Brad Pitt' Strength=31>
<Record Recommended='Janeane Garofalo' Strength=31>
<Record Recommended='Sigourney Weaver' Strength=30>
<Record Recommended='Ben Kingsley' Strength=30>
<Record Recommended='Robin Williams' Strength=30>
<Record Recommended='Tony Shalhoub' Strength=29>
<Record Recommended='Kirsten Dunst' Strength=28>
<Record Recommended='Robert De Niro' Strength=28>
<Record Recommended='Steve Martin' Strength=27>
<Record Recommended='Don Cheadle' Strength=27>
<Record Recommended='Kevin Pollak' Strength=27>
<Record Recommended='Stanley Tucci' Strength=27>
<Record Recommended='Michelle Pfeiffer' Strength=27>
<Record Recommended='Nicole Kidman' Strength=26>
<Record Recommended='Anthony Hopkins' Strength=26>
<Record Recommended='Kathy Bates' Strength=26>
<Record Recommended='Andy Garcia' Strength=26>
<Record Recommended='Meryl Streep' Strength=25>
<Record Recommended='Billy Crystal' Strength=25>
<Record Recommended='Chevy Chase' Strength=25>
<Record Recommended='Matthew Broderick' Strength=25>
<Record Recommended='Tim Robbins' Strength=25>
<Record Recommended='Delroy Lindo' Strength=25>
<Record Recommended='Charlize Theron' Strength=24>
<Record Recommended='Val Kilmer' Strength=24>
<Record Recommended='Frank Oz' Strength=24>
<Record Recommended='Gene Hackman' Strength=24>
<Record Recommended='Melanie Griffith' Strength=24>
<Record Recommended='Ving Rhames' Strength=24>
<Record Recommended='Kevin Spacey' Strength=24>
<Record Recommended='Owen Wilson' Strength=23>
<Record Recommended='Harrison Ford' Strength=23>
<Record Recommended='Kevin Costner' Strength=23>
<Record Recommended='Dennis Farina' Strength=23>
<Record Recommended='Demi Moore' Strength=23>
<Record Recommended='William Fichtner' Strength=23>
<Record Recommended='James Belushi' Strength=23>
<Record Recommended='Julia Roberts' Strength=23>
<Record Recommended='Cate Blanchett' Strength=23>
<Record Recommended='Richard Gere' Strength=23>
<Record Recommended='Cameron Diaz' Strength=22>
<Record Recommended='Morgan Freeman' Strength=22>
<Record Recommended='Ian Holm' Strength=22>
<Record Recommended='Christina Ricci' Strength=22>
<Record Recommended='Robin Wright' Strength=22>
<Record Recommended='Angelina Jolie' Strength=22>
<Record Recommended='John Goodman' Strength=22>
<Record Recommended='Johnny Depp' Strength=22>
<Record Recommended='Joan Cusack' Strength=22>
<Record Recommended='Dustin Hoffman' Strength=22>
<Record Recommended='Hank Azaria' Strength=22>
<Record Recommended='Dennis Hopper' Strength=22>
<Record Recommended='Fred Willard' Strength=22>
<Record Recommended='Bill Murray' Strength=22>
<Record Recommended='Emily Mortimer' Strength=21>
<Record Recommended='Michael McKean' Strength=21>
<Record Recommended='John C. Reilly' Strength=21>
<Record Recommended='Ed Harris' Strength=21>
<Record Recommended='James Woods' Strength=21>
<Record Recommended='Donald Sutherland' Strength=21>
<Record Recommended='John Malkovich' Strength=21>
<Record Recommended='Philip Baker Hall' Strength=21>
<Record Recommended='Susan Sarandon' Strength=21>
<Record Recommended='Christopher Lloyd' Strength=21>
<Record Recommended='Martin Short' Strength=20>
<Record Recommended='Bill Nunn' Strength=20>
<Record Recommended='Danny DeVito' Strength=20>
<Record Recommended='Philip Seymour Hoffman' Strength=20>
<Record Recommended='Tom Sizemore' Strength=20>
<Record Recommended='Gwyneth Paltrow' Strength=20>
<Record Recommended='Gary Oldman' Strength=20>
<Record Recommended='Lolita Davidovich' Strength=20>
<Record Recommended='Russell Crowe' Strength=20>
<Record Recommended='Rick Moranis' Strength=20>
<Record Recommended='Greg Kinnear' Strength=20>
<Record Recommended='Michael Madsen' Strength=20>
<Record Recommended='John Travolta' Strength=20>
<Record Recommended='Meg Ryan' Strength=20>
<Record Recommended='Ed Begley Jr.' Strength=19>
<Record Recommended='Matt Damon' Strength=19>
<Record Recommended='Wallace Shawn' Strength=19>
<Record Recommended='Bonnie Hunt' Strength=19>
<Record Recommended='Abigail Breslin' Strength=19>
<Record Recommended='Marisa Tomei' Strength=19>
<Record Recommended='Dylan Baker' Strength=19>
<Record Recommended='Cloris Leachman' Strength=19>
<Record Recommended='Colm Feore' Strength=19>
<Record Recommended='Amanda Peet' Strength=19>
<Record Recommended='James Earl Jones' Strength=19>
<Record Recommended='Christopher Walken' Strength=19>
<Record Recommended='Steve Zahn' Strength=19>
<Record Recommended='Larry Miller' Strength=19>
<Record Recommended='Sean Penn' Strength=19>
<Record Recommended='Cary Elwes' Strength=19>
<Record Recommended='Glenn Close' Strength=18>
<Record Recommended='Jeff Goldblum' Strength=18>
<Record Recommended='Cheech Marin' Strength=18>
<Record Recommended='Jude Law' Strength=18>
<Record Recommended='Patrick Stewart' Strength=18>
<Record Recommended='Adam Sandler' Strength=18>
<Record Recommended='Natalie Portman' Strength=18>
<Record Recommended='Mickey Rourke' Strength=18>
<Record Recommended='Rene Russo' Strength=18>
<Record Recommended='Julianne Moore' Strength=18>
<Record Recommended='Michael Caine' Strength=18>
<Record Recommended='Liev Schreiber' Strength=18>
<Record Recommended='Alan Arkin' Strength=18>
<Record Recommended='Lily Tomlin' Strength=18>
<Record Recommended='Casey Affleck' Strength=17>
<Record Recommended='Patricia Clarkson' Strength=17>
<Record Recommended='William Hurt' Strength=17>
<Record Recommended='Scott Glenn' Strength=17>
<Record Recommended='Elliott Gould' Strength=17>
<Record Recommended='Bruce Campbell' Strength=17>
<Record Recommended='Ray Liotta' Strength=17>
<Record Recommended='Sam Rockwell' Strength=17>
<Record Recommended='Spencer Breslin' Strength=17>
<Record Recommended='J.K. Simmons' Strength=17>
<Record Recommended='Alan Rickman' Strength=17>
<Record Recommended='Giovanni Ribisi' Strength=17>
<Record Recommended='Pat Hingle' Strength=17>
<Record Recommended='Tobey Maguire' Strength=17>
<Record Recommended='Will Smith' Strength=17>
<Record Recommended='James Franco' Strength=17>
<Record Recommended='Rosemary Harris' Strength=17>
<Record Recommended='Timothy Olyphant' Strength=17>
<Record Recommended='Edward Norton' Strength=17>
<Record Recommended='Will Ferrell' Strength=17>
<Record Recommended='Keanu Reeves' Strength=17>
<Record Recommended='Mark Wahlberg' Strength=17>
<Record Recommended='Scott Caan' Strength=17>
<Record Recommended='Danny Glover' Strength=16>
<Record Recommended='Anjelica Huston' Strength=16>
<Record Recommended='Jeff Bridges' Strength=16>
<Record Recommended='Kristen Stewart' Strength=16>
<Record Recommended='Mark Hamill' Strength=16>
<Record Recommended='Mark Ruffalo' Strength=16>
<Record Recommended='Michael Gambon' Strength=16>
<Record Recommended='Viggo Mortensen' Strength=16>
<Record Recommended='Jon Favreau' Strength=16>
<Record Recommended='Robert Duvall' Strength=16>
<Record Recommended='Annette Bening' Strength=16>
<Record Recommended='JoBeth Williams' Strength=16>
<Record Recommended='Danny Trejo' Strength=16>
<Record Recommended='Robert Loggia' Strength=16>
<Record Recommended='Elijah Wood' Strength=16>
<Record Recommended='Frank Langella' Strength=16>
<Record Recommended='John Turturro' Strength=16>
<Record Recommended='Paul Dooley' Strength=16>
<Record Recommended='Woody Allen' Strength=16>
<Record Recommended='Tim Curry' Strength=16>
<Record Recommended='Robert Downey Jr.' Strength=16>
<Record Recommended='Sean Connery' Strength=16>
<Record Recommended='Diane Keaton' Strength=16>
<Record Recommended='Bill Nighy' Strength=16>
<Record Recommended='Luis Guzmán' Strength=16>
<Record Recommended='Renée Zellweger' Strength=16>
<Record Recommended='Tommy Lee Jones' Strength=16>
<Record Recommended='Stanley Anderson' Strength=16>
<Record Recommended='Tim Roth' Strength=16>
<Record Recommended='Josh Hartnett' Strength=16>
<Record Recommended='Jack Nicholson' Strength=16>
<Record Recommended='Catherine Keener' Strength=15>
<Record Recommended='Minnie Driver' Strength=15>
<Record Recommended='Helen Hunt' Strength=15>
<Record Recommended='Tom Cruise' Strength=15>
<Record Recommended='Ron Perlman' Strength=15>
<Record Recommended='Peter Stormare' Strength=15>
<Record Recommended='Tom Arnold' Strength=15>
<Record Recommended='Charlie Sheen' Strength=15>
<Record Recommended='Sharon Stone' Strength=15>
<Record Recommended='Sarah Jessica Parker' Strength=15>
<Record Recommended='Jeff Daniels' Strength=15>
<Record Recommended='Jonathan Pryce' Strength=15>
<Record Recommended='Christopher Plummer' Strength=15>
<Record Recommended='Joe Pesci' Strength=15>
<Record Recommended='Donal Logue' Strength=15>
<Record Recommended='Drew Barrymore' Strength=15>
<Record Recommended='Patricia Arquette' Strength=15>
<Record Recommended='Orlando Bloom' Strength=15>
<Record Recommended='Harris Yulin' Strength=15>
<Record Recommended='Christopher Guest' Strength=15>
<Record Recommended='Michael J. Fox' Strength=15>
<Record Recommended='Ned Beatty' Strength=15>
<Record Recommended='Rip Torn' Strength=15>
<Record Recommended='Cuba Gooding Jr.' Strength=15>
<Record Recommended='John Heard' Strength=15>
<Record Recommended='Harvey Keitel' Strength=15>
<Record Recommended='Judge Reinhold' Strength=15>
<Record Recommended='Tim Matheson' Strength=15>
<Record Recommended='Jason Lee' Strength=15>
<Record Recommended='Geoffrey Rush' Strength=15>
<Record Recommended='Peter Boyle' Strength=15>
<Record Recommended='George Carlin' Strength=15>
<Record Recommended='Kelly Williams' Strength=15>
<Record Recommended='Jennifer Lopez' Strength=15>
<Record Recommended='Eugene Levy' Strength=15>
<Record Recommended='Robert Redford' Strength=15>
<Record Recommended="Vincent D'Onofrio" Strength=15>
<Record Recommended='Christian Bale' Strength=15>
<Record Recommended='Whoopi Goldberg' Strength=15>
<Record Recommended='Phil Hartman' Strength=15>
<Record Recommended='Tom Skerritt' Strength=14>
<Record Recommended='Christopher Lee' Strength=14>
<Record Recommended='Alan Alda' Strength=14>
<Record Recommended='Larry Hankin' Strength=14>
<Record Recommended='Peter Gallagher' Strength=14>
<Record Recommended='Claire Danes' Strength=14>
<Record Recommended='Antonio Banderas' Strength=14>
<Record Recommended='Chris Cooper' Strength=14>
<Record Recommended='Josh Lucas' Strength=14>
<Record Recommended='Clint Eastwood' Strength=14>
<Record Recommended='Alec Guinness' Strength=14>
<Record Recommended='Liam Neeson' Strength=14>
<Record Recommended='Matt Dillon' Strength=14>
<Record Recommended='Jennifer Connelly' Strength=14>
<Record Recommended='Josh Brolin' Strength=14>
<Record Recommended='Clive Owen' Strength=14>
<Record Recommended='Anthony Daniels' Strength=14>
<Record Recommended='Rachel Weisz' Strength=14>
<Record Recommended='Brendan Gleeson' Strength=14>
<Record Recommended='Randy Quaid' Strength=14>
<Record Recommended='Rob Schneider' Strength=14>
<Record Recommended='Martin Lawrence' Strength=14>
<Record Recommended='Paul Newman' Strength=14>
<Record Recommended='Lance Henriksen' Strength=14>
<Record Recommended='Bette Midler' Strength=14>
<Record Recommended='John Belushi' Strength=14>
<Record Recommended='Christian Slater' Strength=14>
<Record Recommended='Rosario Dawson' Strength=14>
<Record Recommended='Rita Wilson' Strength=14>
<Record Recommended='Jack Kehler' Strength=14>
<Record Recommended='Ben Stiller' Strength=14>
<Record Recommended='Selma Blair' Strength=14>
<Record Recommended='Jack Warden' Strength=14>
<Record Recommended='Ray Walston' Strength=14>
<Record Recommended='Nathan Lane' Strength=14>
<Record Recommended='Glenne Headly' Strength=14>
<Record Recommended='Eddie Murphy' Strength=14>
<Record Recommended='Rutger Hauer' Strength=14>
<Record Recommended='Jon Voight' Strength=14>
<Record Recommended='Bill Pullman' Strength=14>
<Record Recommended='Daniel Stern' Strength=14>
<Record Recommended='Burt Reynolds' Strength=14>
<Record Recommended='Michael Keaton' Strength=14>
<Record Recommended='James Caan' Strength=14>
<Record Recommended='Allison Janney' Strength=14>
<Record Recommended='Sean Astin' Strength=13>
<Record Recommended='Ashley Judd' Strength=13>
<Record Recommended='James Coburn' Strength=13>
<Record Recommended='Denzel Washington' Strength=13>
<Record Recommended='Amy Sedaris' Strength=13>
<Record Recommended='Salma Hayek' Strength=13>
<Record Recommended='James Rebhorn' Strength=13>
<Record Recommended='Harry Shearer' Strength=13>
<Record Recommended='Gary Cole' Strength=13>
<Record Recommended='Madeleine Stowe' Strength=13>
<Record Recommended='Michael Rapaport' Strength=13>
<Record Recommended='Lili Taylor' Strength=13>
<Record Recommended='Rob Lowe' Strength=13>
<Record Recommended='Ray Winstone' Strength=13>
<Record Recommended="Kevin J. O'Connor" Strength=13>
<Record Recommended='Stephen Lang' Strength=13>
<Record Recommended='Hilary Swank' Strength=13>
<Record Recommended='Carrie Fisher' Strength=13>
<Record Recommended='Dan Hedaya' Strength=13>
<Record Recommended='Richard Jenkins' Strength=13>
<Record Recommended='Harry Dean Stanton' Strength=13>
<Record Recommended='David Morse' Strength=13>
<Record Recommended='Joe Pantoliano' Strength=13>
<Record Recommended='Al Pacino' Strength=13>
<Record Recommended='Jodie Foster' Strength=13>
<Record Recommended='Elizabeth Banks' Strength=13>
<Record Recommended='Kathy Najimy' Strength=13>
<Record Recommended='Seann William Scott' Strength=13>
<Record Recommended='Kevin Bacon' Strength=13>
<Record Recommended='Colin Farrell' Strength=13>
<Record Recommended='Frances McDormand' Strength=13>
<Record Recommended='Maury Chaykin' Strength=13>
<Record Recommended='Andrea Martin' Strength=13>
<Record Recommended='Oliver Platt' Strength=13>
<Record Recommended='Carla Gugino' Strength=13>
<Record Recommended='Kiefer Sutherland' Strength=13>
<Record Recommended='Kevin Kline' Strength=13>
<Record Recommended='Winona Ryder' Strength=13>
<Record Recommended='Laurence Fishburne' Strength=13>
<Record Recommended='John Hurt' Strength=13>
<Record Recommended='William Lee Scott' Strength=13>
<Record Recommended='Mel Gibson' Strength=13>
<Record Recommended='Brendan Fraser' Strength=13>
<Record Recommended='Juliette Lewis' Strength=13>
<Record Recommended='Brion James' Strength=13>
<Record Recommended='David Arquette' Strength=12>
<Record Recommended='Chris Rock' Strength=12>
<Record Recommended='Will Patton' Strength=12>
<Record Recommended='Edward Asner' Strength=12>
<Record Recommended='Leslie Nielsen' Strength=12>
<Record Recommended='Austin Pendleton' Strength=12>
<Record Recommended='Jeremy Irons' Strength=12>
<Record Recommended='Zooey Deschanel' Strength=12>
<Record Recommended='Ben Foster' Strength=12>
<Record Recommended='Robert Prosky' Strength=12>
<Record Recommended='Natasha Gregson Wagner' Strength=12>
<Record Recommended='Hayden Panettiere' Strength=12>
<Record Recommended='Craig Bierko' Strength=12>
<Record Recommended='Brad Dourif' Strength=12>
<Record Recommended='Parker Posey' Strength=12>
<Record Recommended='Miriam Margolyes' Strength=12>
<Record Recommended='Zeljko Ivanek' Strength=12>
<Record Recommended='Gary Sinise' Strength=12>
<Record Recommended='Macaulay Culkin' Strength=12>
<Record Recommended='Kenneth Branagh' Strength=12>
<Record Recommended='Ted Levine' Strength=12>
<Record Recommended='Radha Mitchell' Strength=12>
<Record Recommended='Andy Serkis' Strength=12>
<Record Recommended='Rade Serbedzija' Strength=12>
<Record Recommended='Celia Weston' Strength=12>
<Record Recommended='Michael Ironside' Strength=12>
<Record Recommended='Naomi Watts' Strength=12>
<Record Recommended='James Gandolfini' Strength=12>
<Record Recommended='Bernie Mac' Strength=12>
<Record Recommended='Charles Grodin' Strength=12>
<Record Recommended='Jennifer Jason Leigh' Strength=12>
<Record Recommended='Kelly Preston' Strength=12>
<Record Recommended='Kim Basinger' Strength=12>
<Record Recommended='Joey Lauren Adams' Strength=12>
<Record Recommended='David Spade' Strength=12>
<Record Recommended='Ruby Dee' Strength=12>
<Record Recommended='Lucy Liu' Strength=12>
<Record Recommended='Sam Neill' Strength=12>
<Record Recommended='Uma Thurman' Strength=12>
<Record Recommended='Scarlett Johansson' Strength=12>
<Record Recommended='Wendy Crewson' Strength=12>
<Record Recommended='Ted Raimi' Strength=12>
<Record Recommended='Justin Long' Strength=12>
<Record Recommended='Stephen Tobolowsky' Strength=12>
<Record Recommended='Kenny Baker' Strength=12>
<Record Recommended='Felicity Huffman' Strength=12>
<Record Recommended='Nick Nolte' Strength=12>
<Record Recommended='Paul Reubens' Strength=12>
<Record Recommended='Holly Hunter' Strength=12>
<Record Recommended='Helen Mirren' Strength=12>
<Record Recommended='Julia Ormond' Strength=12>
<Record Recommended='Arnold Schwarzenegger' Strength=12>
<Record Recommended='Forest Whitaker' Strength=12>
<Record Recommended='Giancarlo Esposito' Strength=12>
<Record Recommended='Brian Cox' Strength=12>
<Record Recommended='Frankie Faison' Strength=12>
<Record Recommended='Jason Isaacs' Strength=12>
<Record Recommended='Benicio Del Toro' Strength=12>
<Record Recommended='Brad Sullivan' Strength=12>
<Record Recommended='Jamie Bell' Strength=12>
<Record Recommended='Peter Dante' Strength=11>
<Record Recommended="Beverly D'Angelo" Strength=11>
<Record Recommended='Bruce Dern' Strength=11>
<Record Recommended='Will Arnett' Strength=11>
<Record Recommended='Ashton Kutcher' Strength=11>
<Record Recommended='Don Knotts' Strength=11>
<Record Recommended='Jennifer Tilly' Strength=11>
<Record Recommended='Aaron Eckhart' Strength=11>
<Record Recommended='Tim Allen' Strength=11>
<Record Recommended='Udo Kier' Strength=11>
<Record Recommended='Ellen Burstyn' Strength=11>
<Record Recommended='Martin Sheen' Strength=11>
<Record Recommended='Cliff Robertson' Strength=11>
<Record Recommended='Walter Matthau' Strength=11>
<Record Recommended='Olympia Dukakis' Strength=11>
<Record Recommended='Fred Ward' Strength=11>
<Record Recommended='Courteney Cox' Strength=11>
<Record Recommended='Jack Davenport' Strength=11>
<Record Recommended='Michael Clarke Duncan' Strength=11>
<Record Recommended='Jane Krakowski' Strength=11>
<Record Recommended='Armin Mueller-Stahl' Strength=11>
<Record Recommended='Matt Frewer' Strength=11>
<Record Recommended='Chloë Sevigny' Strength=11>
<Record Recommended='Laurie Metcalf' Strength=11>
<Record Recommended='Peter Mayhew' Strength=11>
<Record Recommended='Ray McKinnon' Strength=11>
<Record Recommended='Rosanna Arquette' Strength=11>
<Record Recommended='Vera Farmiga' Strength=11>
<Record Recommended='Alfred Molina' Strength=11>
<Record Recommended='Ryan Phillippe' Strength=11>
<Record Recommended='Nick Chinlund' Strength=11>
<Record Recommended='Jeffrey Wright' Strength=11>
<Record Recommended='Gary Busey' Strength=11>
<Record Recommended='Mary Steenburgen' Strength=11>
<Record Recommended="Chris O'Donnell" Strength=11>
<Record Recommended='Jon Lovitz' Strength=11>
<Record Recommended='Dakota Fanning' Strength=11>
<Record Recommended='Ralph Fiennes' Strength=11>
<Record Recommended='M. Emmet Walsh' Strength=11>
<Record Recommended='Ethan Hawke' Strength=11>
<Record Recommended='Sarah Michelle Gellar' Strength=11>
<Record Recommended='George C. Scott' Strength=11>
<Record Recommended='Richard Riehle' Strength=11>
<Record Recommended='Brent Spiner' Strength=11>
<Record Recommended='Alison Lohman' Strength=11>
<Record Recommended='Peter Gerety' Strength=11>
<Record Recommended='Thandie Newton' Strength=11>
<Record Recommended='Brian Doyle-Murray' Strength=11>
<Record Recommended='Bob Balaban' Strength=11>
<Record Recommended='Jack Lemmon' Strength=11>
<Record Recommended='Jared Harris' Strength=11>
<Record Recommended='Patrick Dempsey' Strength=11>
<Record Recommended='Arthur J. Nascarella' Strength=11>
<Record Recommended='Joe Mantegna' Strength=11>
<Record Recommended='Catherine Zeta-Jones' Strength=11>
<Record Recommended='Kelsey Grammer' Strength=11>
<Record Recommended='Chiwetel Ejiofor' Strength=11>
<Record Recommended='Stockard Channing' Strength=11>
<Record Recommended='James Garner' Strength=11>
<Record Recommended='David Prowse' Strength=11>
<Record Recommended='Christopher McDonald' Strength=11>
<Record Recommended='Michael Jeter' Strength=11>
<Record Recommended='Dick Van Patten' Strength=11>
<Record Recommended='Sean Bean' Strength=11>
<Record Recommended='James Cromwell' Strength=11>
<Record Recommended='Leonardo DiCaprio' Strength=11>
<Record Recommended='Crispin Glover' Strength=11>
<Record Recommended='Gaby Hoffmann' Strength=11>
<Record Recommended='Josh Pais' Strength=11>
<Record Recommended='Hector Elizondo' Strength=11>
<Record Recommended='Marcia Gay Harden' Strength=11>
<Record Recommended='Connie Nielsen' Strength=11>
<Record Recommended='David Strathairn' Strength=10>
<Record Recommended='Mel Brooks' Strength=10>
<Record Recommended='Bernard Hill' Strength=10>
<Record Recommended='Laura Linney' Strength=10>
<Record Recommended='Robert Patrick' Strength=10>
<Record Recommended='Bill Paxton' Strength=10>
<Record Recommended='Katie Holmes' Strength=10>
<Record Recommended='Sam Shepard' Strength=10>
<Record Recommended='Billy Dee Williams' Strength=10>
<Record Recommended='Bruce Greenwood' Strength=10>
<Record Recommended='Bruno Kirby' Strength=10>
<Record Recommended='Jason Robards' Strength=10>
<Record Recommended='Katherine Helmond' Strength=10>
<Record Recommended='Seymour Cassel' Strength=10>
<Record Recommended='Michelle Williams' Strength=10>
<Record Recommended='Melanie Lynskey' Strength=10>
<Record Recommended='Billy Bob Thornton' Strength=10>
<Record Recommended='Amanda Plummer' Strength=10>
<Record Recommended='Regina King' Strength=10>
<Record Recommended='Christopher Eccleston' Strength=10>
<Record Recommended='Kevin Smith' Strength=10>
<Record Recommended='Paul Rudd' Strength=10>
<Record Recommended='Hugo Weaving' Strength=10>
<Record Recommended='Thora Birch' Strength=10>
<Record Recommended='John Leguizamo' Strength=10>
<Record Recommended='Paul Giamatti' Strength=10>
<Record Recommended='Marc Blucas' Strength=10>
<Record Recommended='Bruce McGill' Strength=10>
<Record Recommended='Michael Douglas' Strength=10>
<Record Recommended='Kelly Lynch' Strength=10>
<Record Recommended='Mark Harmon' Strength=10>
<Record Recommended='James Gammon' Strength=10>
<Record Recommended='Mark Strong' Strength=10>
<Record Recommended='Chris Penn' Strength=10>
<Record Recommended='Kate Beckinsale' Strength=10>
<Record Recommended='Geena Davis' Strength=10>
<Record Recommended='Halle Berry' Strength=10>
<Record Recommended='John Gielgud' Strength=10>
<Record Recommended='Dennis Haysbert' Strength=10>
<Record Recommended='Milla Jovovich' Strength=10>
<Record Recommended='Tom Wilkinson' Strength=10>
<Record Recommended='Griffin Dunne' Strength=10>
<Record Recommended='Sam Elliott' Strength=10>
<Record Recommended='Mena Suvari' Strength=10>
<Record Recommended='Harold Ramis' Strength=10>
<Record Recommended='Woody Harrelson' Strength=10>
<Record Recommended='Sandra Bullock' Strength=10>
<Record Recommended='Greg Germann' Strength=10>
<Record Recommended='Treat Williams' Strength=10>
<Record Recommended='Michael Shannon' Strength=10>
<Record Recommended='Jennifer Esposito' Strength=10>
<Record Recommended='Pierce Brosnan' Strength=10>
<Record Recommended='Kathleen Turner' Strength=10>
<Record Recommended='Albert Finney' Strength=10>
<Record Recommended='Kris Kristofferson' Strength=10>
<Record Recommended='Toni Collette' Strength=10>
<Record Recommended='Brittany Murphy' Strength=10>
<Record Recommended='Emilio Estevez' Strength=10>
<Record Recommended='Carol Kane' Strength=10>
<Record Recommended='Anna Faris' Strength=10>
<Record Recommended='Jim Broadbent' Strength=10>
<Record Recommended='Matthew McConaughey' Strength=10>
<Record Recommended='Daryl Hannah' Strength=10>
<Record Recommended='Pruitt Taylor Vince' Strength=10>
<Record Recommended='Kurt Russell' Strength=10>
<Record Recommended='Robert Forster' Strength=10>
<Record Recommended='Rachael Leigh Cook' Strength=10>
<Record Recommended='Seth Green' Strength=10>
<Record Recommended='Jennifer Aniston' Strength=10>
<Record Recommended='Lauren Bacall' Strength=10>
<Record Recommended='Hayden Christensen' Strength=10>
<Record Recommended='Debra Messing' Strength=10>
<Record Recommended='Troy Evans' Strength=10>
<Record Recommended='Penelope Cruz' Strength=10>
<Record Recommended='Adam West' Strength=9>
<Record Recommended='John Diehl' Strength=9>
<Record Recommended='Bob Peterson' Strength=9>
<Record Recommended='Jonathan Banks' Strength=9>
<Record Recommended='Jsu Garcia' Strength=9>
<Record Recommended='Luke Wilson' Strength=9>
<Record Recommended='Ashleigh Aston Moore' Strength=9>
<Record Recommended='Daryl Mitchell' Strength=9>
<Record Recommended='Vincent Cassel' Strength=9>
<Record Recommended='Carrie-Anne Moss' Strength=9>
<Record Recommended='Jeff Garlin' Strength=9>
<Record Recommended='Ernie Hudson' Strength=9>
<Record Recommended='Dan Molina' Strength=9>
<Record Recommended='Rhea Perlman' Strength=9>
<Record Recommended='Barry Pepper' Strength=9>
<Record Recommended='Steven Wright' Strength=9>
<Record Recommended='David Duchovny' Strength=9>
<Record Recommended='Kyle MacLachlan' Strength=9>
<Record Recommended='Jeffrey Jones' Strength=9>
<Record Recommended='Téa Leoni' Strength=9>
<Record Recommended='Sissy Spacek' Strength=9>
<Record Recommended='Danny Mann' Strength=9>
<Record Recommended='Jeremy Piven' Strength=9>
<Record Recommended='Richard Schiff' Strength=9>
<Record Recommended='Lauren Tom' Strength=9>
<Record Recommended='Keith David' Strength=9>
<Record Recommended='Diane Lane' Strength=9>
<Record Recommended='Miguel Ferrer' Strength=9>
<Record Recommended='Kim Dickens' Strength=9>
<Record Recommended='Clifton Collins Jr.' Strength=9>
<Record Recommended='Tom Noonan' Strength=9>
<Record Recommended='Chi McBride' Strength=9>
<Record Recommended='Bobby Cannavale' Strength=9>
<Record Recommended='Michael Papajohn' Strength=9>
<Record Recommended='Sylvester Stallone' Strength=9>
<Record Recommended='Joaquin Phoenix' Strength=9>
<Record Recommended='Vince Vaughn' Strength=9>
<Record Recommended='Kenneth McMillan' Strength=9>
<Record Recommended='Ewan McGregor' Strength=9>
<Record Recommended='John Michael Higgins' Strength=9>
<Record Recommended='Sean Elmore' Strength=9>
<Record Recommended='J.T. Walsh' Strength=9>
<Record Recommended='Donnie Wahlberg' Strength=9>
<Record Recommended='Viola Davis' Strength=9>
<Record Recommended='Eric Lloyd' Strength=9>
<Record Recommended='Michael Wincott' Strength=9>
<Record Recommended='Jamie Kennedy' Strength=9>
<Record Recommended='Tim Blake Nelson' Strength=9>
<Record Recommended='Madison Davenport' Strength=9>
<Record Recommended="Rosie O'Donnell" Strength=9>
<Record Recommended='Larry The Cable Guy' Strength=9>
<Record Recommended='Mary McCormack' Strength=9>
<Record Recommended='Mary Lynn Rajskub' Strength=9>
<Record Recommended='Leelee Sobieski' Strength=9>
<Record Recommended='William Shatner' Strength=9>
<Record Recommended='Rhys Ifans' Strength=9>
<Record Recommended='Evan Dunn' Strength=9>
<Record Recommended='Jake Busey' Strength=9>
<Record Recommended='Zach Braff' Strength=9>
<Record Recommended='Valeria Golino' Strength=9>
<Record Recommended='Brinke Stevens' Strength=9>
<Record Recommended='Miranda Richardson' Strength=9>
<Record Recommended='Bernadette Peters' Strength=9>
<Record Recommended='Devon Sawa' Strength=9>
<Record Recommended='Michael Wallis' Strength=9>
<Record Recommended='Grace Zabriskie' Strength=9>
<Record Recommended='Alyssa Milano' Strength=9>
<Record Recommended='Amy Adams' Strength=9>
<Record Recommended='Mark Dindal' Strength=9>
<Record Recommended='Gérard Depardieu' Strength=9>
<Record Recommended='Kevin Chapman' Strength=9>
<Record Recommended='Taylor Negron' Strength=9>
<Record Recommended='Joe Whyte' Strength=9>
<Record Recommended='Cole Hauser' Strength=9>
<Record Recommended='Dom DeLuise' Strength=9>
<Record Recommended='Michael Lerner' Strength=9>
<Record Recommended='Kate Winslet' Strength=9>
<Record Recommended='Matthew Josten' Strength=9>
<Record Recommended='Michael Moore' Strength=9>
<Record Recommended='M.C. Gainey' Strength=9>
<Record Recommended='Jenifer Lewis' Strength=9>
<Record Recommended='Mark Walton' Strength=9>
<Record Recommended='Jean Reno' Strength=9>
<Record Recommended='Thomas Haden Church' Strength=9>
<Record Recommended='Piper Perabo' Strength=9>
<Record Recommended='Charles Durning' Strength=9>
<Record Recommended='Clark Gregg' Strength=9>
<Record Recommended='John Lithgow' Strength=9>
<Record Recommended='Eva Mendes' Strength=9>
<Record Recommended='David Ogden Stiers' Strength=9>
<Record Recommended='Kevin Nealon' Strength=9>
<Record Recommended='Dianne Wiest' Strength=9>
<Record Recommended='Anne Archer' Strength=9>
<Record Recommended='Jason Mewes' Strength=9>
<Record Recommended='Walter Sparrow' Strength=9>
<Record Recommended='Raymond J. Barry' Strength=9>
<Record Recommended='Ian McNeice' Strength=9>
<Record Recommended='Stephen King' Strength=9>
<Record Recommended='Lisa Jane Persky' Strength=9>
<Record Recommended='Breckin Meyer' Strength=9>
<Record Recommended='Brian Dennehy' Strength=9>
<Record Recommended='Kerry Washington' Strength=9>
<Record Recommended='Jane Curtin' Strength=9>
<Record Recommended='Mark Margolis' Strength=8>
<Record Recommended='Bryce Dallas Howard' Strength=8>
<Record Recommended='Billy Crudup' Strength=8>
<Record Recommended='Mageina Tovah' Strength=8>
<Record Recommended='Ellen Barkin' Strength=8>
<Record Recommended='Betty White' Strength=8>
<Record Recommended='Frank Welker' Strength=8>
<Record Recommended='Jason Alexander' Strength=8>
<Record Recommended='Chris Klein' Strength=8>
<Record Recommended='Daniel Baldwin' Strength=8>
<Record Recommended='Queen Latifah' Strength=8>
<Record Recommended='LL Cool J' Strength=8>
<Record Recommended='Jay Mohr' Strength=8>
<Record Recommended='Arija Bareikis' Strength=8>
<Record Recommended='Jonah Hill' Strength=8>
<Record Recommended='Charles Napier' Strength=8>
<Record Recommended='Rupert Everett' Strength=8>
<Record Recommended='Rory Culkin' Strength=8>
<Record Recommended='Laura San Giacomo' Strength=8>
<Record Recommended='Mia Farrow' Strength=8>
<Record Recommended='Keira Knightley' Strength=8>
<Record Recommended='Debra Monk' Strength=8>
<Record Recommended='Madonna Louise Veronica Ciccone' Strength=8>
<Record Recommended='Jennifer Beals' Strength=8>
<Record Recommended='Allen Covert' Strength=8>
<Record Recommended='Wayne Knight' Strength=8>
<Record Recommended='Henry Gibson' Strength=8>
<Record Recommended='Peter Coyote' Strength=8>
<Record Recommended='Neal McDonough' Strength=8>
<Record Recommended='Tilda Swinton' Strength=8>
<Record Recommended='Corin Nemec' Strength=8>
<Record Recommended='Shannon Elizabeth' Strength=8>
<Record Recommended='Elizabeth Perkins' Strength=8>
<Record Recommended='John Larroquette' Strength=8>
<Record Recommended='Max Thieriot' Strength=8>
<Record Recommended='Mos Def' Strength=8>
<Record Recommended='Matthew Modine' Strength=8>
<Record Recommended='Elizabeth Hurley' Strength=8>
<Record Recommended='Albert Brooks' Strength=8>
<Record Recommended='Quentin Tarantino' Strength=8>
<Record Recommended='Louise Fletcher' Strength=8>
<Record Recommended='Thomas Jane' Strength=8>
<Record Recommended='Peter Dinklage' Strength=8>
<Record Recommended='Tony Plana' Strength=8>
<Record Recommended='Ray Garvey' Strength=8>
<Record Recommended='William Atherton' Strength=8>
<Record Recommended='Matt Craven' Strength=8>
<Record Recommended='John Cleese' Strength=8>
<Record Recommended='Jonny Lee Miller' Strength=8>
<Record Recommended='Emily Watson' Strength=8>
<Record Recommended='Elya Baskin' Strength=8>
<Record Recommended='Chelcie Ross' Strength=8>
<Record Recommended='Paul Walker' Strength=8>
<Record Recommended='Jamie Lee Curtis' Strength=8>
<Record Recommended='Bob Hoskins' Strength=8>
<Record Recommended='Paul Reiser' Strength=8>
<Record Recommended='Jamey Sheridan' Strength=8>
<Record Recommended='Clint Howard' Strength=8>
<Record Recommended='Diedrich Bader' Strength=8>
<Record Recommended='Brad Garrett' Strength=8>
<Record Recommended='John Rhys-Davies' Strength=8>
<Record Recommended='Nia Long' Strength=8>
<Record Recommended='Tom Poston' Strength=8>
<Record Recommended='Marshall Bell' Strength=8>
<Record Recommended='Missi Pyle' Strength=8>
<Record Recommended='Jane Lynch' Strength=8>
<Record Recommended='John Ratzenberger' Strength=8>
<Record Recommended='Anthony Anderson' Strength=8>
<Record Recommended='Marcel Iures' Strength=8>
<Record Recommended='Regina Hall' Strength=8>
<Record Recommended='Julia Stiles' Strength=8>
<Record Recommended='Marley Shelton' Strength=8>
<Record Recommended='Kareem Abdul-Jabbar' Strength=8>
<Record Recommended='Laura Dern' Strength=8>
<Record Recommended='Dorian Harewood' Strength=8>
<Record Recommended='Daniel Gillies' Strength=8>
<Record Recommended='John C. McGinley' Strength=8>
<Record Recommended='Danny Nucci' Strength=8>
<Record Recommended='Jason Bateman' Strength=8>
<Record Recommended='Jason Biggs' Strength=8>
<Record Recommended='Kevin McCarthy' Strength=8>
<Record Recommended='Anna Paquin' Strength=8>
<Record Recommended='Lois Smith' Strength=8>
<Record Recommended='Gregory Sporleder' Strength=8>
<Record Recommended='James Duval' Strength=8>
<Record Recommended='Tim Thomerson' Strength=8>
<Record Recommended='Remak Ramsay' Strength=8>
<Record Recommended='Hal Holbrook' Strength=8>
<Record Recommended='Jean-Marc Barr' Strength=8>
<Record Recommended='Norbert Weisser' Strength=8>
<Record Recommended='Trevor Morgan' Strength=8>
<Record Recommended='Garry Marshall' Strength=8>
<Record Recommended='Stellan Skarsgård' Strength=8>
<Record Recommended="Jerry O'Connell" Strength=8>
<Record Recommended='Piper Laurie' Strength=8>
<Record Recommended='Max von Sydow' Strength=8>
<Record Recommended='James Caviezel' Strength=8>
<Record Recommended='Patrick Breen' Strength=8>
<Record Recommended='Kirstie Alley' Strength=8>
<Record Recommended='Ewen Bremner' Strength=8>
<Record Recommended='Jonathan Hyde' Strength=8>
<Record Recommended='Roger Rees' Strength=8>
<Record Recommended='Zach Grenier' Strength=8>
<Record Recommended='Don Stroud' Strength=8>
<Record Recommended='Eddie Izzard' Strength=8>
<Record Recommended='Kim Coates' Strength=8>
<Record Recommended='Sandra Taylor' Strength=8>
<Record Recommended='Dermot Mulroney' Strength=8>
<Record Recommended='David Warner' Strength=8>
<Record Recommended='Corey Haim' Strength=8>
<Record Recommended='Eddie Jemison' Strength=8>
<Record Recommended='Timothy Hutton' Strength=8>
<Record Recommended='Richard Herd' Strength=8>
<Record Recommended='Lauren Graham' Strength=8>
<Record Recommended='Linda Hamilton' Strength=8>
<Record Recommended='John Landis' Strength=8>
<Record Recommended='Pete Postlethwaite' Strength=8>
<Record Recommended='Steve Carell' Strength=8>
<Record Recommended='Jon Gries' Strength=8>
<Record Recommended='Robbie Coltrane' Strength=8>
<Record Recommended='Steve Railsback' Strength=8>
<Record Recommended='Virginia Madsen' Strength=8>
<Record Recommended='David Krumholtz' Strength=8>
<Record Recommended='Siobhan Fallon' Strength=8>
<Record Recommended='G.D. Spradlin' Strength=8>
<Record Recommended='Michael Biehn' Strength=8>
<Record Recommended='January Jones' Strength=8>
<Record Recommended='Jeremy Davies' Strength=8>
<Record Recommended='Brian Markinson' Strength=8>
<Record Recommended='Maggie Smith' Strength=8>
<Record Recommended='Sela Ward' Strength=8>
<Record Recommended='Jon Bernthal' Strength=8>
<Record Recommended='Peter Ustinov' Strength=8>
<Record Recommended='John Slattery' Strength=8>
<Record Recommended='Joel Moore' Strength=8>
<Record Recommended='Richard Dreyfuss' Strength=8>
<Record Recommended='Stephen Bishop' Strength=8>
<Record Recommended='Michael Moriarty' Strength=8>
<Record Recommended='D.B. Sweeney' Strength=8>
<Record Recommended='Kevin Dunn' Strength=8>
<Record Recommended='Sarah Paulson' Strength=8>
<Record Recommended='Lynn Cohen' Strength=8>
<Record Recommended='Vanessa Redgrave' Strength=7>
<Record Recommended='Patty Duke' Strength=7>
<Record Recommended='Bud Cort' Strength=7>
<Record Recommended='Vin Diesel' Strength=7>
<Record Recommended='Neve Campbell' Strength=7>
<Record Recommended='Kelli Garner' Strength=7>
<Record Recommended='Michael Weston' Strength=7>
<Record Recommended='Willow Smith' Strength=7>
<Record Recommended='Johnny Knoxville' Strength=7>
<Record Recommended='Patrick Kilpatrick' Strength=7>
<Record Recommended='Faye Dunaway' Strength=7>
<Record Recommended='Tracy Morgan' Strength=7>
<Record Recommended='Bebe Neuwirth' Strength=7>
<Record Recommended='Ned Bellamy' Strength=7>
<Record Recommended='Ron Rifkin' Strength=7>
<Record Recommended='Michael Sheen' Strength=7>
<Record Recommended='William Forsythe' Strength=7>
<Record Recommended='Simon McBurney' Strength=7>
<Record Recommended='Mackenzie Crook' Strength=7>
<Record Recommended='Karl Urban' Strength=7>
<Record Recommended='Christina Applegate' Strength=7>
<Record Recommended='Edie McClurg' Strength=7>
<Record Recommended='Jason Gray-Stanford' Strength=7>
<Record Recommended='Judy Davis' Strength=7>
<Record Recommended='Herb Lovelle' Strength=7>
<Record Recommended='Jim Carrey' Strength=7>
<Record Recommended='Michelle Rodriguez' Strength=7>
<Record Recommended='Bruce Davison' Strength=7>
<Record Recommended='Jamie Foxx' Strength=7>
<Record Recommended='Carel Struycken' Strength=7>
<Record Recommended='Rachel Dratch' Strength=7>
<Record Recommended='Julie Hagerty' Strength=7>
<Record Recommended='Embeth Davidtz' Strength=7>
<Record Recommended='Alyson Hannigan' Strength=7>
<Record Recommended='Aisha Tyler' Strength=7>
<Record Recommended='Dennis Franz' Strength=7>
<Record Recommended='Michael Gough' Strength=7>
<Record Recommended='Jim Haynie' Strength=7>
<Record Recommended='Zoe Saldana' Strength=7>
<Record Recommended='Hugh Jackman' Strength=7>
<Record Recommended='Skeet Ulrich' Strength=7>
<Record Recommended='Spencer Treat Clark' Strength=7>
<Record Recommended='David Koechner' Strength=7>
<Record Recommended='Lisa Kudrow' Strength=7>
<Record Recommended='Amy Madigan' Strength=7>
<Record Recommended='Sophie Okonedo' Strength=7>
<Record Recommended='Ian McShane' Strength=7>
<Record Recommended='Billy Burke' Strength=7>
<Record Recommended='Christine Ebersole' Strength=7>
<Record Recommended='Aasif Mandvi' Strength=7>
<Record Recommended='Angela Lansbury' Strength=7>
<Record Recommended='Robert Davi' Strength=7>
<Record Recommended='Rick Rossovich' Strength=7>
<Record Recommended='Courtney Love' Strength=7>
<Record Recommended='Stephen Furst' Strength=7>
<Record Recommended='Mark Boone Junior' Strength=7>
<Record Recommended='Rachel McAdams' Strength=7>
<Record Recommended='Richard Lineback' Strength=7>
<Record Recommended='Sherman Howard' Strength=7>
<Record Recommended='Alessandro Nivola' Strength=7>
<Record Recommended='Carmen Electra' Strength=7>
<Record Recommended='Julie Andrews' Strength=7>
<Record Recommended='Casey Siemaszko' Strength=7>
<Record Recommended='Gary Houston' Strength=7>
<Record Recommended='Scott Terra' Strength=7>
<Record Recommended='Paul Bettany' Strength=7>
<Record Recommended='Kathleen Freeman' Strength=7>
<Record Recommended='Nick Cannon' Strength=7>
<Record Recommended='Penelope Ann Miller' Strength=7>
<Record Recommended='Rob Reiner' Strength=7>
<Record Recommended='Clea DuVall' Strength=7>
<Record Recommended='Alfre Woodard' Strength=7>
<Record Recommended='Omid Djalili' Strength=7>
<Record Recommended='Tina Majorino' Strength=7>
<Record Recommended='Elle Fanning' Strength=7>
<Record Recommended='Judd Nelson' Strength=7>
<Record Recommended='Paul Guilfoyle' Strength=7>
<Record Recommended='Tippi Hedren' Strength=7>
<Record Recommended='Miranda Otto' Strength=7>
<Record Recommended='Kathy Baker' Strength=7>
<Record Recommended='Dana Carvey' Strength=7>
<Record Recommended='Kevin Conway' Strength=7>
<Record Recommended='Elizabeth Berkley' Strength=7>
<Record Recommended='Debra Winger' Strength=7>
<Record Recommended='Anthony Edwards' Strength=7>
<Record Recommended='Robert Stanton' Strength=7>
<Record Recommended='Jackie Burroughs' Strength=7>
<Record Recommended='Ian McDiarmid' Strength=7>
<Record Recommended='Fiona Shaw' Strength=7>
<Record Recommended='Robert Stack' Strength=7>
<Record Recommended='Ed Lauter' Strength=7>
<Record Recommended='Cedric the Entertainer' Strength=7>
<Record Recommended='Emily Blunt' Strength=7>
<Record Recommended='Lauren Holly' Strength=7>
<Record Recommended="David O'Hara" Strength=7>
<Record Recommended='Jaime King' Strength=7>
<Record Recommended="Carroll O'Connor" Strength=7>
<Record Recommended='Mako' Strength=7>
<Record Recommended='Marc Lawrence' Strength=7>
<Record Recommended='Tom Berenger' Strength=7>
<Record Recommended='Kavan Smith' Strength=7>
<Record Recommended='Rick Aviles' Strength=7>
<Record Recommended='Ronny Cox' Strength=7>
<Record Recommended='Murray Hamilton' Strength=7>
<Record Recommended='Zak Orth' Strength=7>
<Record Recommended='Adam Storke' Strength=7>
<Record Recommended='Hope Davis' Strength=7>
<Record Recommended='Richard Council' Strength=7>
<Record Recommended='Christopher Meloni' Strength=7>
<Record Recommended='Steven Ford' Strength=7>
<Record Recommended='K.K. Dodds' Strength=7>
<Record Recommended='Joe Morton' Strength=7>
<Record Recommended='Patrick Swayze' Strength=7>
<Record Recommended='Kim Cattrall' Strength=7>
<Record Recommended='Mykelti Williamson' Strength=7>
<Record Recommended='Jonathan Tucker' Strength=7>
<Record Recommended='Bridget Fonda' Strength=7>
<Record Recommended='David Hyde Pierce' Strength=7>
<Record Recommended='Zach Mills' Strength=7>
<Record Recommended='Robert Pastorelli' Strength=7>
<Record Recommended='John Schuck' Strength=7>
<Record Recommended='Carl Reiner' Strength=7>
<Record Recommended='Charles S. Dutton' Strength=7>
<Record Recommended='Jeff Fahey' Strength=7>
<Record Recommended='Chris Sarandon' Strength=7>
<Record Recommended='Billy Boyd' Strength=7>
<Record Recommended='Gary Dourdan' Strength=7>
<Record Recommended='Hugh Grant' Strength=7>
<Record Recommended='Diane Venora' Strength=7>
<Record Recommended='Greg Ellis' Strength=7>
<Record Recommended='Fred Savage' Strength=7>
<Record Recommended='F. Murray Abraham' Strength=7>
<Record Recommended='Judd Hirsch' Strength=7>
<Record Recommended='John Carroll Lynch' Strength=7>
<Record Recommended='Michael Lonsdale' Strength=7>
<Record Recommended='April Grace' Strength=7>
<Record Recommended='Shaobo Qin' Strength=7>
<Record Recommended='Dylan McDermott' Strength=7>
<Record Recommended='Caroline Goodall' Strength=7>
<Record Recommended='Evan Handler' Strength=7>
<Record Recommended='Guy Pearce' Strength=7>
<Record Recommended='Anne Bancroft' Strength=7>
<Record Recommended='Richard Pryor' Strength=7>
<Record Recommended='Pamela Reed' Strength=7>
<Record Recommended='Eric Roberts' Strength=6>
<Record Recommended='Heather Graham' Strength=6>
<Record Recommended='David Wenham' Strength=6>
<Record Recommended='Irwin Corey' Strength=6>
<Record Recommended='Howard Alden' Strength=6>
<Record Recommended='Orlando Jones' Strength=6>
<Record Recommended='Adam Baldwin' Strength=6>
<Record Recommended='Scott Coffey' Strength=6>
<Record Recommended='Perla Haney-Jardine' Strength=6>
<Record Recommended='Kai Wulff' Strength=6>
<Record Recommended='Alonzo Atkins' Strength=6>
<Record Recommended='Sydney Walker' Strength=6>
<Record Recommended='Bob Dorian' Strength=6>
<Record Recommended='Tom Erhart' Strength=6>
<Record Recommended='Guy Boyd' Strength=6>
<Record Recommended='Elizabeth Hoy' Strength=6>
<Record Recommended='Lawrence Feldman' Strength=6>
<Record Recommended='Isaac Hayes' Strength=6>
<Record Recommended='Isaach De Bankole' Strength=6>
<Record Recommended='Tina Sloan' Strength=6>
<Record Recommended='Jeremy Sisto' Strength=6>
<Record Recommended='James Frain' Strength=6>
<Record Recommended='Gwen Banta' Strength=6>
<Record Recommended='Mike Myers' Strength=6>
<Record Recommended='Eric Keenleyside' Strength=6>
<Record Recommended='Valerie Perrine' Strength=6>
<Record Recommended='Kris Lemche' Strength=6>
<Record Recommended='Joy Bryant' Strength=6>
<Record Recommended='Jerry Orbach' Strength=6>
<Record Recommended='Nicky Katt' Strength=6>
<Record Recommended='Joan Plowright' Strength=6>
<Record Recommended='Hope Marie Carlton' Strength=6>
<Record Recommended='Vince Giordano' Strength=6>
<Record Recommended='Shia LaBeouf' Strength=6>
<Record Recommended='Tom Holland' Strength=6>
<Record Recommended='Julio Oscar Mechoso' Strength=6>
<Record Recommended='Paul Calderon' Strength=6>
<Record Recommended='Michael Massee' Strength=6>
<Record Recommended='Geoffrey Lewis' Strength=6>
<Record Recommended='Eddie Griffin' Strength=6>
<Record Recommended='Billy Zane' Strength=6>
<Record Recommended='Philip Levy' Strength=6>
<Record Recommended='Ryan Reynolds' Strength=6>
<Record Recommended='Matt Keeslar' Strength=6>
<Record Recommended='Conchata Ferrell' Strength=6>
<Record Recommended='Jacquie Barnbrook' Strength=6>
<Record Recommended='Adrian Grenier' Strength=6>
<Record Recommended='Kate Mara' Strength=6>
<Record Recommended='Balthazar Getty' Strength=6>
<Record Recommended='Kellie Overbey' Strength=6>
<Record Recommended='James Brown' Strength=6>
<Record Recommended='David Brannen' Strength=6>
<Record Recommended='Julia Louis-Dreyfus' Strength=6>
<Record Recommended='Dave Chappelle' Strength=6>
<Record Recommended='Kevin Cahoon' Strength=6>
<Record Recommended='Joseph Gordon-Levitt' Strength=6>
<Record Recommended='Mick Garris' Strength=6>
<Record Recommended='Brian Haley' Strength=6>
<Record Recommended='Bob Gunton' Strength=6>
<Record Recommended='Mink Stole' Strength=6>
<Record Recommended='Kristen Bell' Strength=6>
<Record Recommended='F. William Parker' Strength=6>
<Record Recommended='Reese Witherspoon' Strength=6>
<Record Recommended='Malcolm McDowell' Strength=6>
<Record Recommended='Mary-Louise Parker' Strength=6>
<Record Recommended='Patrick Horgan' Strength=6>
<Record Recommended='Luca Bercovici' Strength=6>
<Record Recommended='Scott Thomson' Strength=6>
<Record Recommended='José Zúñiga' Strength=6>
<Record Recommended='Murphy Dunne' Strength=6>
<Record Recommended='Elmore James' Strength=6>
<Record Recommended='Andy Dick' Strength=6>
<Record Recommended='Tony M. Conde' Strength=6>
<Record Recommended='Josef Sommer' Strength=6>
<Record Recommended='Eric Bana' Strength=6>
<Record Recommended='Peter Sarsgaard' Strength=6>
<Record Recommended='Stark Sands' Strength=6>
<Record Recommended='Cindy Fisher' Strength=6>
<Record Recommended='Lari Taylor' Strength=6>
<Record Recommended='Stephen Dorff' Strength=6>
<Record Recommended='Max Minghella' Strength=6>
<Record Recommended='Daniel von Bargen' Strength=6>
<Record Recommended='Chuck Wilson' Strength=6>
<Record Recommended='Paul Gleason' Strength=6>
<Record Recommended='Randy Sandke' Strength=6>
<Record Recommended='Jake Gyllenhaal' Strength=6>
<Record Recommended='Rae Dawn Chong' Strength=6>
<Record Recommended='Melora Walters' Strength=6>
<Record Recommended='Justin Timberlake' Strength=6>
<Record Recommended='Dov Tiefenbach' Strength=6>
<Record Recommended='Aretha Franklin' Strength=6>
<Record Recommended='Jonathan Loughran' Strength=6>
<Record Recommended='John Hollis' Strength=6>
<Record Recommended='John Doumanian' Strength=6>
<Record Recommended='John Randolph Jones' Strength=6>
<Record Recommended='Rocky Carroll' Strength=6>
<Record Recommended='Jennifer Coolidge' Strength=6>
<Record Recommended='Sam Raimi' Strength=6>
<Record Recommended='Rosie Shuster' Strength=6>
<Record Recommended='Jada Pinkett Smith' Strength=6>
<Record Recommended='Makenzie Vega' Strength=6>
<Record Recommended='Joanna Going' Strength=6>
<Record Recommended='Ben Piazza' Strength=6>
<Record Recommended='Carmen' Strength=6>
<Record Recommended='David Andrews' Strength=6>
<Record Recommended='Jack McGee' Strength=6>
<Record Recommended='Andre Braugher' Strength=6>
<Record Recommended='Steven Williams' Strength=6>
<Record Recommended='Nancy Travis' Strength=6>
<Record Recommended='Rainn Wilson' Strength=6>
<Record Recommended='Sebastian Roché' Strength=6>
<Record Recommended='Leonard Termo' Strength=6>
<Record Recommended='Dick Hyman' Strength=6>
<Record Recommended='Frances Fisher' Strength=6>
<Record Recommended='Ray Charles' Strength=6>
<Record Recommended='Evan Rachel Wood' Strength=6>
<Record Recommended='Kristi Oleson' Strength=6>
<Record Recommended='Ted Sommer' Strength=6>
<Record Recommended='Vanessa Ferlito' Strength=6>
<Record Recommended='Vivica A. Fox' Strength=6>
<Record Recommended='Armand Cerami' Strength=6>
<Record Recommended='Raymond Beckenstein' Strength=6>
<Record Recommended='Cynthia Garris' Strength=6>
<Record Recommended='Kurt Fuller' Strength=6>
<Record Recommended='Gary McLarty' Strength=6>
<Record Recommended='Bill Fagerbakke' Strength=6>
<Record Recommended='Glenn Walker Harris Jr.' Strength=6>
<Record Recommended='James Remar' Strength=6>
<Record Recommended='Colin Firth' Strength=6>
<Record Recommended='Isabella Rossellini' Strength=6>
<Record Recommended='Michael Richards' Strength=6>
<Record Recommended='William Petersen' Strength=6>
<Record Recommended='John Lee Hooker' Strength=6>
<Record Recommended='Leo Geter' Strength=6>
<Record Recommended='Denis Leary' Strength=6>
<Record Recommended='Kevin Zegers' Strength=6>
<Record Recommended='Richard Kind' Strength=6>
<Record Recommended='Olivia Williams' Strength=6>
<Record Recommended='John Farley' Strength=6>
<Record Recommended='Alfonso Arau' Strength=6>
<Record Recommended='Bonnie Bedelia' Strength=6>
<Record Recommended='Nastassja Kinski' Strength=6>
<Record Recommended='Ken Peplowski' Strength=6>
<Record Recommended='Chazz Palminteri' Strength=6>
<Record Recommended='Sam Worthington' Strength=6>
<Record Recommended='Dean Hill' Strength=6>
<Record Recommended='Elias Koteas' Strength=6>
<Record Recommended='Judith Belushi-Pisano' Strength=6>
<Record Recommended='Jeremy Bulloch' Strength=6>
<Record Recommended='Molly Ringwald' Strength=6>
<Record Recommended='Tracey Ullman' Strength=6>
<Record Recommended='Cab Calloway' Strength=6>
<Record Recommended='Michael Dorn' Strength=6>
<Record Recommended='Brian McConnachie' Strength=6>
<Record Recommended='Shane West' Strength=6>
<Record Recommended='John Tormey' Strength=6>
<Record Recommended='Jay O. Sanders' Strength=6>
<Record Recommended='Theresa Russell' Strength=6>
<Record Recommended='Jessica Tandy' Strength=6>
<Record Recommended='Ramsey Faragallah' Strength=6>
<Record Recommended='Channing Tatum' Strength=6>
<Record Recommended='Nick Swardson' Strength=6>
<Record Recommended='Michael Angarano' Strength=6>
<Record Recommended='Willie Hall' Strength=6>
<Record Recommended='Gerald Walling' Strength=6>
<Record Recommended='Charles Mountain' Strength=6>
<Record Recommended='Peter MacNicol' Strength=6>
<Record Recommended='Steve Cropper' Strength=6>
<Record Recommended='George Wyner' Strength=6>
<Record Recommended='Ciarán Hinds' Strength=6>
<Record Recommended='Kristin Davis' Strength=6>
<Record Recommended='Gerry Bamman' Strength=6>
<Record Recommended='Diana Scarwid' Strength=6>
<Record Recommended='John Paxton' Strength=6>
<Record Recommended='Sonia Braga' Strength=6>
<Record Recommended='Dan Moran' Strength=6>
<Record Recommended='Guido Quaroni' Strength=6>
<Record Recommended='Elizabeth Mitchell' Strength=6>
<Record Recommended='Stan Shaw' Strength=6>
<Record Recommended='Devon Aoki' Strength=6>
<Record Recommended='Loren Dean' Strength=6>
<Record Recommended='Toni Fleming' Strength=6>
<Record Recommended='Eugene J. Anthony' Strength=6>
<Record Recommended='Dominic Monaghan' Strength=6>
<Record Recommended='Elizabeth Wilson' Strength=6>
<Record Recommended='David Carradine' Strength=6>
<Record Recommended='Kevin Corrigan' Strength=6>
<Record Recommended='Daniel Craig' Strength=6>
<Record Recommended='Natasha Henstridge' Strength=6>
<Record Recommended='Lisa Boyle' Strength=6>
<Record Recommended='Matt Murphy' Strength=6>
<Record Recommended='Eric Christian Olsen' Strength=6>
<Record Recommended='Terry Crews' Strength=6>
<Record Recommended='Patton Oswalt' Strength=6>
<Record Recommended='Nancy Allen' Strength=6>
<Record Recommended='Robert Englund' Strength=6>
<Record Recommended='Maurice Sonnenberg' Strength=6>
<Record Recommended='Tia Carrere' Strength=6>
<Record Recommended='Vanessa Williams' Strength=6>
<Record Recommended='Jack Thompson' Strength=6>
<Record Recommended='Mary McDonnell' Strength=6>
<Record Recommended='R. Lee Ermey' Strength=6>
<Record Recommended='Peter Riegert' Strength=6>
<Record Recommended='Rebecca Ferratti' Strength=6>
<Record Recommended='Juliette Binoche' Strength=6>
<Record Recommended='Ossie Davis' Strength=6>
<Record Recommended='Donna Murphy' Strength=6>
<Record Recommended='Ian McKellen' Strength=6>
<Record Recommended='Jed Rees' Strength=6>
<Record Recommended='Robert Wisdom' Strength=6>
<Record Recommended='Frank Whaley' Strength=6>
<Record Recommended='Joe Cuttone' Strength=6>
<Record Recommended='Timothy Spall' Strength=6>
<Record Recommended='Richard Masur' Strength=6>
<Record Recommended='Howard Erskine' Strength=6>
<Record Recommended='Hume Cronyn' Strength=6>
<Record Recommended='Brian Thompson' Strength=6>
<Record Recommended='Holland Taylor' Strength=6>
<Record Recommended='Joel Helleny' Strength=6>
<Record Recommended='Tim Meadows' Strength=6>
<Record Recommended='Ling Bai' Strength=6>
<Record Recommended='Hanns Zischler' Strength=6>
<Record Recommended='Aidan Quinn' Strength=6>
<Record Recommended='Maria Bamford' Strength=6>
<Record Recommended='Joe Grifasi' Strength=6>
<Record Recommended='Nick Jameson' Strength=6>
<Record Recommended='Lou Marini' Strength=6>
<Record Recommended='Bernard Fox' Strength=6>
<Record Recommended='Ira Wheeler' Strength=6>
<Record Recommended='Lucinda Jenney' Strength=6>
<Record Recommended='Iraida Polanco' Strength=6>
<Record Recommended='Charles Hallahan' Strength=6>
<Record Recommended='Harvey Korman' Strength=6>
<Record Recommended='Tchéky Karyo' Strength=6>
<Record Recommended='Kaili Vernoff' Strength=6>
<Record Recommended='Heath Ledger' Strength=6>
<Record Recommended='Jami Gertz' Strength=6>
<Record Recommended='Tom Malone' Strength=6>
<Record Recommended='David Huddleston' Strength=6>
<Record Recommended='John Bloom' Strength=6>
<Record Recommended='Martin Ferrero' Strength=6>
<Record Recommended='Hugh Laurie' Strength=6>
<Record Recommended='John Spencer' Strength=6>
<Record Recommended='Trude Klein' Strength=6>
<Record Recommended='Joe Manganiello' Strength=6>
<Record Recommended='Joseph Cross' Strength=6>
<Record Recommended='Walter Levine' Strength=6>
<Record Recommended='Bruce Brown' Strength=6>
<Record Recommended='Freddie Highmore' Strength=6>
<Record Recommended='Hilary Duff' Strength=6>
<Record Recommended='Chaka Khan' Strength=6>
<Record Recommended='Kenneth Edelson' Strength=6>
<Record Recommended='Layne Britton' Strength=6>
<Record Recommended='Barbara Hershey' Strength=6>
<Record Recommended='Peter Outerbridge' Strength=6>
<Record Recommended='David Margulies' Strength=6>
<Record Recommended='Andie MacDowell' Strength=6>
<Record Recommended='Kathryn Hahn' Strength=6>
<Record Recommended='Stephen Collins' Strength=6>
<Record Recommended='John Ashton' Strength=6>
<Record Recommended='Scott Wilson' Strength=6>
<Record Recommended='Alan Rubin' Strength=6>
<Record Recommended='Michael Mulheren' Strength=6>
<Record Recommended='Warren Frost' Strength=6>
<Record Recommended='Donald Dunn' Strength=6>
<Record Recommended='Judy Gold' Strength=6>
<Record Recommended='Rob Paulsen' Strength=6>
<Record Recommended='Henry Jones' Strength=6>
<Record Recommended='Anthony Quinn' Strength=6>
<Record Recommended='Melinda Dillon' Strength=6>
<Record Recommended='Ryan Gosling' Strength=6>
<Record Recommended='Lynn Redgrave' Strength=6>
<Record Recommended='Gene Schuldt' Strength=6>
<Record Recommended='Jeff Conaway' Strength=6>
<Record Recommended='Wes Studi' Strength=6>
<Record Recommended='Julian Glover' Strength=6>
<Record Recommended='Lou Diamond Phillips' Strength=6>
<Record Recommended='John Mahoney' Strength=6>
<Record Recommended='Peter Ecklund' Strength=6>
<Record Recommended='Anne Hathaway' Strength=6>
<Record Recommended='Simon Baker' Strength=6>
<Record Recommended='Lily Rabe' Strength=6>
<Record Recommended='Hart Bochner' Strength=6>
<Record Recommended='Ron Eldard' Strength=6>
<Record Recommended='Jack Nance' Strength=6>
<Record Recommended='Ian Roberts' Strength=6>
<Record Recommended='Dale Dye' Strength=6>
<Record Recommended='Lee Van Cleef' Strength=6>
<Record Recommended='Emma Thompson' Strength=6>
<Record Recommended='Wanda Sykes' Strength=6>
<Record Recommended='Shawnee Smith' Strength=6>
<Record Recommended='Maggie Gyllenhaal' Strength=6>
<Record Recommended='Courtney B. Vance' Strength=6>
<Record Recommended='Candice Bergen' Strength=6>
<Record Recommended='Carole Bayeux' Strength=6>
<Record Recommended='James Marsden' Strength=6>
<Record Recommended='Christopher Knights' Strength=6>
<Record Recommended='Keri Russell' Strength=6>
<Record Recommended='Jack Orend' Strength=6>
<Record Recommended='Peter Linari' Strength=6>
<Record Recommended='Tom Waits' Strength=5>
<Record Recommended='Helena Bonham Carter' Strength=5>
<Record Recommended='Michael Murphy' Strength=5>
<Record Recommended='Malcolm Danare' Strength=5>
<Record Recommended='Toby Huss' Strength=5>
<Record Recommended='Tom Welling' Strength=5>
<Record Recommended='Samuel Lord Black' Strength=5>
<Record Recommended='Chris Coppola' Strength=5>
<Record Recommended='Jessica Lange' Strength=5>
<Record Recommended='Ed Gale' Strength=5>
<Record Recommended='Lambert Wilson' Strength=5>
<Record Recommended='Patrice Martinez' Strength=5>
<Record Recommended='Cheri Oteri' Strength=5>
<Record Recommended='Robert Picardo' Strength=5>
<Record Recommended='Michael Rooker' Strength=5>
<Record Recommended='Cherry Jones' Strength=5>
<Record Recommended='Jason Kravits' Strength=5>
<Record Recommended='Dean Stockwell' Strength=5>
<Record Recommended='Jonathan Frakes' Strength=5>
<Record Recommended='Danny Bonaduce' Strength=5>
<Record Recommended='John Di Maggio' Strength=5>
<Record Recommended='Lee Evans' Strength=5>
<Record Recommended='Greg Travis' Strength=5>
<Record Recommended='Ronee Blakley' Strength=5>
<Record Recommended='Laraine Newman' Strength=5>
<Record Recommended='Lucy Butler' Strength=5>
<Record Recommended='Lee Wilkof' Strength=5>
<Record Recommended='Steve Susskind' Strength=5>
<Record Recommended='Alanna Ubach' Strength=5>
<Record Recommended='Mandy Moore' Strength=5>
<Record Recommended='Naveen Andrews' Strength=5>
<Record Recommended='Eric Idle' Strength=5>
<Record Recommended='Henry Rollins' Strength=5>
<Record Recommended='Sam Anderson' Strength=5>
<Record Recommended='Jon Hamm' Strength=5>
<Record Recommended='Djimon Hounsou' Strength=5>
<Record Recommended='Peter Falk' Strength=5>
<Record Recommended='Poppy Montgomery' Strength=5>
<Record Recommended='Vinny Vella' Strength=5>
<Record Recommended='Erinn Bartlett' Strength=5>
<Record Recommended='Chris Owen' Strength=5>
<Record Recommended='Julie Bowen' Strength=5>
<Record Recommended='Patrick Macnee' Strength=5>
<Record Recommended='Joseph Fiennes' Strength=5>
<Record Recommended='Adam Goldberg' Strength=5>
<Record Recommended='Eileen Atkins' Strength=5>
<Record Recommended='Denise Richards' Strength=5>
<Record Recommended='Dyan Cannon' Strength=5>
<Record Recommended='Lou Jacobi' Strength=5>
<Record Recommended='Daniel D. McGrew' Strength=5>
<Record Recommended='Jenna Maetlind' Strength=5>
<Record Recommended='Jill Talley' Strength=5>
<Record Recommended='Michael Shamus Wiles' Strength=5>
<Record Recommended='Roselyn Sanchez' Strength=5>
<Record Recommended='Topher Grace' Strength=5>
<Record Recommended='Blake Heron' Strength=5>
<Record Recommended='Christopher Reeve' Strength=5>
<Record Recommended='Art LaFleur' Strength=5>
<Record Recommended='Kevin Olson' Strength=5>
<Record Recommended='Matt Sigloch' Strength=5>
<Record Recommended='David Proval' Strength=5>
<Record Recommended='Roger Bart' Strength=5>
<Record Recommended='Ulrich Thomsen' Strength=5>
<Record Recommended='Laz Alonso' Strength=5>
<Record Recommended='Michael Winslow' Strength=5>
<Record Recommended='Rik Young' Strength=5>
<Record Recommended='Joanna Cassidy' Strength=5>
<Record Recommended='Marsha Mason' Strength=5>
<Record Recommended='Jason Patric' Strength=5>
<Record Recommended='Mary Wickes' Strength=5>
<Record Recommended='Brooke Shields' Strength=5>
<Record Recommended='Jack Elam' Strength=5>
<Record Recommended='Craig Kilborn' Strength=5>
<Record Recommended='Des Webb' Strength=5>
<Record Recommended='Nicole Sullivan' Strength=5>
<Record Recommended='Albert Hall' Strength=5>
<Record Recommended='Julio Cedillo' Strength=5>
<Record Recommended='Robert Blake' Strength=5>
<Record Recommended='Colm Meaney' Strength=5>
<Record Recommended='Shawn Wayans' Strength=5>
<Record Recommended='Reba McEntire' Strength=5>
<Record Recommended='Jeroen Krabbé' Strength=5>
<Record Recommended='Amy Brenneman' Strength=5>
<Record Recommended='Marilu Henner' Strength=5>
<Record Recommended='Dee Wallace' Strength=5>
<Record Recommended='David Byrd' Strength=5>
<Record Recommended='Gilbert B. Combs' Strength=5>
<Record Recommended='Elizabeth Peña' Strength=5>
<Record Recommended='John Roselius' Strength=5>
<Record Recommended='Richard Portnow' Strength=5>
<Record Recommended='Liv Tyler' Strength=5>
<Record Recommended='Terence Stamp' Strength=5>
<Record Recommended='Alan Ruck' Strength=5>
<Record Recommended='Terrence Howard' Strength=5>
<Record Recommended='Andrew McCarthy' Strength=5>
<Record Recommended='Amanda Anka' Strength=5>
<Record Recommended='Tom Selleck' Strength=5>
<Record Recommended='Jean Smart' Strength=5>
<Record Recommended='Tom Kenny' Strength=5>
<Record Recommended='Shelley Duvall' Strength=5>
<Record Recommended='Tom Guiry' Strength=5>
<Record Recommended='Louis Eppolito' Strength=5>
<Record Recommended='Tom Bower' Strength=5>
<Record Recommended="Tommy 'Tiny' Lister" Strength=5>
<Record Recommended='Stephen Baldwin' Strength=5>
<Record Recommended='Christopher Evan Welch' Strength=5>
<Record Recommended='Dave Foley' Strength=5>
<Record Recommended='Dwayne Johnson' Strength=5>
<Record Recommended='Shay Duffin' Strength=5>
<Record Recommended='Sam Huntington' Strength=5>
<Record Recommended='Lisa Ann Walter' Strength=5>
<Record Recommended='Tony Goldwyn' Strength=5>
<Record Recommended='Jennifer Schwalbach Smith' Strength=5>
<Record Recommended='Trevor Howard' Strength=5>
<Record Recommended='Meredith Salenger' Strength=5>
<Record Recommended='J.C. MacKenzie' Strength=5>
<Record Recommended='Blair Underwood' Strength=5>
<Record Recommended='Blythe Danner' Strength=5>
<Record Recommended='Jane Seymour' Strength=5>
<Record Recommended='Heather Stephens' Strength=5>
<Record Recommended='Jack' Strength=5>
<Record Recommended='Jon Abrahams' Strength=5>
<Record Recommended='Rubén Blades' Strength=5>
<Record Recommended='Lorraine Gary' Strength=5>
<Record Recommended='Jennifer Garner' Strength=5>
<Record Recommended='Mark Webber' Strength=5>
<Record Recommended='Keith Allen' Strength=5>
<Record Recommended='Saffron Burrows' Strength=5>
<Record Recommended='Sean Whalen' Strength=5>
<Record Recommended='Enrico Colantoni' Strength=5>
<Record Recommended='Forrest J Ackerman' Strength=5>
<Record Recommended='Debi Mazar' Strength=5>
<Record Recommended='Dash Mihok' Strength=5>
<Record Recommended='Tress MacNeille' Strength=5>
<Record Recommended='David Keith' Strength=5>
<Record Recommended='Jack Purvis' Strength=5>
<Record Recommended='Judi Dench' Strength=5>
<Record Recommended='Gailard Sartain' Strength=5>
<Record Recommended='Samantha Mathis' Strength=5>
<Record Recommended='Joe Flaherty' Strength=5>
<Record Recommended='Shawn Hatosy' Strength=5>
<Record Recommended='Linden Ashby' Strength=5>
<Record Recommended='Billy Connolly' Strength=5>
<Record Recommended='Brad Renfro' Strength=5>
<Record Recommended='Cody Cameron' Strength=5>
<Record Recommended='Mary Kay Place' Strength=5>
<Record Recommended='Alan Jones Silva' Strength=5>
<Record Recommended='Eric Stoltz' Strength=5>
<Record Recommended='Charlotte Salt' Strength=5>
<Record Recommended='Dominic West' Strength=5>
<Record Recommended='Ernest Borgnine' Strength=5>
<Record Recommended='Shea Whigham' Strength=5>
<Record Recommended='Dax Shepard' Strength=5>
<Record Recommended='Jocelyn Quivrin' Strength=5>
<Record Recommended='Bobby Slayton' Strength=5>
<Record Recommended='Ann-Margret' Strength=5>
<Record Recommended='David Cross' Strength=5>
<Record Recommended='Nora Dunn' Strength=5>
<Record Recommended='Mía Maestro' Strength=5>
<Record Recommended='Matthew Perry' Strength=5>
<Record Recommended='Gabriel Byrne' Strength=5>
<Record Recommended='Stefania Rocca' Strength=5>
<Record Recommended='Anthony Perkins' Strength=5>
<Record Recommended='Stephen Root' Strength=5>
<Record Recommended='Marton Csokas' Strength=5>
<Record Recommended='Clive Revill' Strength=5>
<Record Recommended='Alicia Witt' Strength=5>
<Record Recommended='Heather Matarazzo' Strength=5>
<Record Recommended='Roshan Seth' Strength=5>
<Record Recommended='Madeline Kahn' Strength=5>
<Record Recommended='Paprika Steen' Strength=5>
<Record Recommended='Alexander Folk' Strength=5>
<Record Recommended='John Savage' Strength=5>
<Record Recommended='David Caruso' Strength=5>
<Record Recommended='Jesse James' Strength=5>
<Record Recommended='Philip Bosco' Strength=5>
<Record Recommended='Clayne Crawford' Strength=5>
<Record Recommended='Charlotte Rampling' Strength=5>
<Record Recommended='Michael Peña' Strength=5>
<Record Recommended='Saoirse Ronan' Strength=5>
<Record Recommended='André Benjamin' Strength=5>
<Record Recommended='Jayce Bartok' Strength=5>
<Record Recommended='Patrick Malahide' Strength=5>
<Record Recommended='Thomas Kretschmann' Strength=5>
<Record Recommended='Freddy Rodríguez' Strength=5>
<Record Recommended='Samantha Morton' Strength=5>
<Record Recommended='Jennifer Syme' Strength=5>
<Record Recommended='James Whitmore' Strength=5>
<Record Recommended='Anna Levine' Strength=5>
<Record Recommended='Akosua Busia' Strength=5>
<Record Recommended='Ivory Ocean' Strength=5>
<Record Recommended='Kevin Tighe' Strength=5>
<Record Recommended='Robert Knott' Strength=5>
<Record Recommended='Christian Clavier' Strength=5>
<Record Recommended='Wendy Makkena' Strength=5>
<Record Recommended='Brian Van Holt' Strength=5>
<Record Recommended='Sara Foster' Strength=5>
<Record Recommended='James Marshall' Strength=5>
<Record Recommended='Leo Burmester' Strength=5>
<Record Recommended='Elise Neal' Strength=5>
<Record Recommended='Ioan Gruffudd' Strength=5>
<Record Recommended='Mary Gibbs' Strength=5>
<Record Recommended='Jena Malone' Strength=5>
<Record Recommended='Julia Sweeney' Strength=5>
<Record Recommended='Romola Garai' Strength=5>
<Record Recommended='Guy Siner' Strength=5>
<Record Recommended='Brooke Smith' Strength=5>
<Record Recommended='Pepe Serna' Strength=5>
<Record Recommended='Sharisse Baker-Bernard' Strength=5>
<Record Recommended='Michael Nouri' Strength=5>
<Record Recommended='Alexis Arquette' Strength=5>
<Record Recommended='Dane Cook' Strength=5>
<Record Recommended='Cliff Curtis' Strength=5>
<Record Recommended='Carl Sundstrom' Strength=5>
<Record Recommended='Margaret Colin' Strength=5>
<Record Recommended='Marc Anthony' Strength=5>
<Record Recommended='Michelle Nicastro' Strength=5>
<Record Recommended='Damian Lewis' Strength=5>
<Record Recommended='Seth Rogen' Strength=5>
<Record Recommended='Teri Garr' Strength=5>
<Record Recommended='Costas Mandylor' Strength=5>
<Record Recommended='Blair Brown' Strength=5>
<Record Recommended='Ricky Gervais' Strength=5>
<Record Recommended='Maria Thayer' Strength=5>
<Record Recommended='Michael Cera' Strength=5>
<Record Recommended='Dyana Ortelli' Strength=5>
<Record Recommended='Tim Daly' Strength=5>
<Record Recommended='Jeff Bennett' Strength=5>
<Record Recommended='Suzy Amis' Strength=5>
<Record Recommended='Jimmy Smits' Strength=5>
<Record Recommended='Ewan Stewart' Strength=5>
<Record Recommended='Fredrik Hiller' Strength=5>
<Record Recommended='Omar Epps' Strength=5>
<Record Recommended='Timothy Dalton' Strength=5>
<Record Recommended='Adam Carolla' Strength=5>
<Record Recommended='Julie Delpy' Strength=5>
<Record Recommended='Laurence Olivier' Strength=5>
<Record Recommended='Robert Carlyle' Strength=5>
<Record Recommended='Philip Gordon' Strength=5>
<Record Recommended='Woody Schultz' Strength=5>
<Record Recommended='Phil Proctor' Strength=5>
<Record Recommended='Haley Joel Osment' Strength=5>
<Record Recommended='Sherilyn Fenn' Strength=5>
<Record Recommended='Tracey Walter' Strength=5>
<Record Recommended="Michael O'Neill" Strength=5>
<Record Recommended='Chris Farley' Strength=5>
<Record Recommended='Robin Bartlett' Strength=5>
<Record Recommended="Peter O'Toole" Strength=5>
<Record Recommended='Leslie Bega' Strength=5>
<Record Recommended='Dominic Keating' Strength=5>
<Record Recommended='Peter Horton' Strength=5>
<Record Recommended='Richard Crenna' Strength=5>
<Record Recommended='Justin Theroux' Strength=5>
<Record Recommended='Tom Hardy' Strength=5>
<Record Recommended='Michelle Monaghan' Strength=5>
<Record Recommended="Brian O'Halloran" Strength=5>
<Record Recommended='Al Garrett' Strength=5>
<Record Recommended='Steve Coogan' Strength=5>
<Record Recommended='Sonje Fortag' Strength=5>
<Record Recommended='Joe Don Baker' Strength=5>
<Record Recommended='Jessica Alba' Strength=5>
<Record Recommended='Sinbad' Strength=5>
<Record Recommended='Daniel Sunjata' Strength=5>
<Record Recommended='Jacinda Barrett' Strength=5>
<Record Recommended='Amy Ryan' Strength=5>
<Record Recommended='GQ' Strength=5>
<Record Recommended='Gene Ross' Strength=5>
<Record Recommended='Dylan Walsh' Strength=5>
<Record Recommended='John Vernon' Strength=5>
<Record Recommended='Angela Goethals' Strength=5>
<Record Recommended='Sheryl Lee Ralph' Strength=5>
<Record Recommended='Bill Irwin' Strength=5>
<Record Recommended='Burt Lancaster' Strength=5>
<Record Recommended='Saul Rubinek' Strength=5>
<Record Recommended='Kathleen Gati' Strength=5>
<Record Recommended='Édgar Ramírez' Strength=5>
<Record Recommended='Diego Luna' Strength=5>
<Record Recommended='Ben Gazzara' Strength=5>
<Record Recommended='Jeremy Howard' Strength=5>
<Record Recommended='Joan Rivers' Strength=5>
<Record Recommended='Liliana Mumy' Strength=5>
<Record Recommended='Raul Julia' Strength=5>
<Record Recommended='Mads Mikkelsen' Strength=5>
<Record Recommended='Xander Berkeley' Strength=5>
<Record Recommended='Orson Bean' Strength=5>
<Record Recommended='Jeff Pidgeon' Strength=5>
<Record Recommended='Rodney Dangerfield' Strength=5>
<Record Recommended='John Solari' Strength=5>
<Record Recommended='Rachel Miner' Strength=5>
<Record Recommended='Kenneth Colley' Strength=5>
<Record Recommended='Jeordie White' Strength=5>
<Record Recommended='Alex D. Linz' Strength=5>
<Record Recommended='Roscoe Lee Browne' Strength=5>
<Record Recommended='Kristin Scott Thomas' Strength=5>
<Record Recommended='Eli Wallach' Strength=5>
<Record Recommended='Marilyn Manson' Strength=5>
<Record Recommended='Margot Kidder' Strength=5>
<Record Recommended='Alice Braga' Strength=5>
<Record Recommended='Campbell Scott' Strength=5>
<Record Recommended='Mischa Barton' Strength=5>
<Record Recommended='Richard Roundtree' Strength=5>
<Record Recommended='Monica Keena' Strength=5>
<Record Recommended='Tyler Steelman' Strength=5>
<Record Recommended='Swoosie Kurtz' Strength=5>
<Record Recommended='Kirk Douglas' Strength=5>
<Record Recommended='Shirley Henderson' Strength=5>
<Record Recommended='Robert Joy' Strength=5>
<Record Recommended='Jason Spevack' Strength=5>
<Record Recommended='James Spader' Strength=5>
<Record Recommended='John Terry' Strength=5>
<Record Recommended='Derek Jacobi' Strength=5>
<Record Recommended='Colin Hanks' Strength=5>
<Record Recommended="Brian F. O'Byrne" Strength=5>
<Record Recommended='Erika Alexander' Strength=5>
<Record Recommended='Ally Sheedy' Strength=5>
<Record Recommended='Devin Ratray' Strength=5>
<Record Recommended='Fred Delmare' Strength=5>
<Record Recommended='Malin Åkerman' Strength=5>
<Record Recommended='Joe Spinell' Strength=5>
<Record Recommended='Michael Gaston' Strength=5>
<Record Recommended='Matt Salinger' Strength=5>
<Record Recommended='Matt Servitto' Strength=5>
<Record Recommended='Obba Babatundé' Strength=5>
<Record Recommended='Casey Boersma' Strength=4>
<Record Recommended='Emmanuel Lewis' Strength=4>
<Record Recommended='Adam Scott' Strength=4>
<Record Recommended='Yigal Naor' Strength=4>
<Record Recommended='Steve Valentine' Strength=4>
<Record Recommended='Strother Martin' Strength=4>
<Record Recommended='Telly Savalas' Strength=4>
<Record Recommended='Robin Sachs' Strength=4>
<Record Recommended='Chris Bauer' Strength=4>
<Record Recommended='John Blaylock' Strength=4>
<Record Recommended='Annabeth Gish' Strength=4>
<Record Recommended='Shawn Doyle' Strength=4>
<Record Recommended='Brandon de Paul' Strength=4>
<Record Recommended='Colleen Rennison' Strength=4>
<Record Recommended='Hal Sparks' Strength=4>
<Record Recommended='Jeff Anderson' Strength=4>
<Record Recommended='Frank Adamson' Strength=4>
<Record Recommended='David B. Allen' Strength=4>
<Record Recommended='William Baldwin' Strength=4>
<Record Recommended='Alex Neuberger' Strength=4>
<Record Recommended='Angela Bassett' Strength=4>
<Record Recommended='Stephanie Roth Haberle' Strength=4>
<Record Recommended='Adam Brody' Strength=4>
<Record Recommended='Mike Epps' Strength=4>
<Record Recommended='Katharine Isabelle' Strength=4>
<Record Recommended='Leslie Caron' Strength=4>
<Record Recommended='Simon Pegg' Strength=4>
<Record Recommended='Jane Kaczmarek' Strength=4>
<Record Recommended='Michael Emerson' Strength=4>
<Record Recommended='Jean Louisa Kelly' Strength=4>
<Record Recommended='Camilla Belle' Strength=4>
<Record Recommended='Sam Waterston' Strength=4>
<Record Recommended='Florence Henderson' Strength=4>
<Record Recommended='Joey Diaz' Strength=4>
<Record Recommended='Monica Potter' Strength=4>
<Record Recommended='Artie Lange' Strength=4>
<Record Recommended='Jackie Earle Haley' Strength=4>
<Record Recommended='Colin Stinton' Strength=4>
<Record Recommended='Vernon Wells' Strength=4>
<Record Recommended='Alexander D. Slanger' Strength=4>
<Record Recommended='Adam Rich' Strength=4>
<Record Recommended='Lillian Lehman' Strength=4>
<Record Recommended='Adrian Pasdar' Strength=4>
<Record Recommended='Brad William Henke' Strength=4>
<Record Recommended='Carl Lumbly' Strength=4>
<Record Recommended='Zach Galifianakis' Strength=4>
<Record Recommended='Tupac Shakur' Strength=4>
<Record Recommended='Francesca Neri' Strength=4>
<Record Recommended='Richard Davalos' Strength=4>
<Record Recommended='Jim Garrison' Strength=4>
<Record Recommended='Kevin McNally' Strength=4>
<Record Recommended='Kate del Castillo' Strength=4>
<Record Recommended='George Kennedy' Strength=4>
<Record Recommended='Randall Batinkoff' Strength=4>
<Record Recommended='Cynthia Stevenson' Strength=4>
<Record Recommended='Art Carney' Strength=4>
<Record Recommended='Desmond Harrington' Strength=4>
<Record Recommended='Alan Blumenfeld' Strength=4>
<Record Recommended='Fay Masterson' Strength=4>
<Record Recommended='Margaret Avery' Strength=4>
<Record Recommended='Kate Hudson' Strength=4>
<Record Recommended='Renée Estevez' Strength=4>
<Record Recommended='Portia Dawson' Strength=4>
<Record Recommended='Blair Breard' Strength=4>
<Record Recommended='Anna Hoelck' Strength=4>
<Record Recommended='John Kavanagh' Strength=4>
<Record Recommended='Jack Noseworthy' Strength=4>
<Record Recommended='Danny Aiello' Strength=4>
<Record Recommended='Michelle Burke' Strength=4>
<Record Recommended='Scoot McNairy' Strength=4>
<Record Recommended='Wentworth Miller' Strength=4>
<Record Recommended='Sally Field' Strength=4>
<Record Recommended='Lou Taylor Pucci' Strength=4>
<Record Recommended='Geraldine James' Strength=4>
<Record Recommended='Ashley Hoelck' Strength=4>
<Record Recommended='Rupert Friend' Strength=4>
<Record Recommended='Ethan Suplee' Strength=4>
<Record Recommended='Kevin Grevioux' Strength=4>
<Record Recommended='Jess Harnell' Strength=4>
<Record Recommended='Retta' Strength=4>
<Record Recommended='Malcolm Stewart' Strength=4>
<Record Recommended='Drew Carey' Strength=4>
<Record Recommended='Louis Gossett Jr.' Strength=4>
<Record Recommended='Joey Slotnick' Strength=4>
<Record Recommended='Stephen Pearlman' Strength=4>
<Record Recommended='Tom Dugan' Strength=4>
<Record Recommended='Emilie de Ravin' Strength=4>
<Record Recommended='Gloria Stuart' Strength=4>
<Record Recommended='Kevin Neil McCready' Strength=4>
<Record Recommended='Arsenio Hall' Strength=4>
<Record Recommended='Ivano Marescotti' Strength=4>
<Record Recommended='Jeremy Miller' Strength=4>
<Record Recommended='Edward James Olmos' Strength=4>
<Record Recommended='Oliver Kindred' Strength=4>
<Record Recommended='Garette Ratliff Henson' Strength=4>
<Record Recommended='Eliza Dushku' Strength=4>
<Record Recommended='Kenneth Welsh' Strength=4>
<Record Recommended='Barbara Harris' Strength=4>
<Record Recommended='Steve Harris' Strength=4>
<Record Recommended='Mark Blankfield' Strength=4>
<Record Recommended='Janet Margolin' Strength=4>
<Record Recommended='Julie Gonzalo' Strength=4>
<Record Recommended='Miriam Flynn' Strength=4>
<Record Recommended='Benjamin Bratt' Strength=4>
<Record Recommended='Abraham Benrubi' Strength=4>
<Record Recommended='Kelly Macdonald' Strength=4>
<Record Recommended='Juliet Mills' Strength=4>
<Record Recommended='Ernest Harden Jr.' Strength=4>
<Record Recommended='Jill Teed' Strength=4>
<Record Recommended='Ellen Page' Strength=4>
<Record Recommended='Peter Firth' Strength=4>
<Record Recommended='Nancy Ticotin' Strength=4>
<Record Recommended='Hal Fishman' Strength=4>
<Record Recommended='Glenn Morshower' Strength=4>
<Record Recommended='Wayde Preston' Strength=4>
<Record Recommended='Richard E. Grant' Strength=4>
<Record Recommended='Kyra Sedgwick' Strength=4>
<Record Recommended='Anne Heche' Strength=4>
<Record Recommended='Anne Cullimore Decker' Strength=4>
<Record Recommended="Patrick Thomas O'Brien" Strength=4>
<Record Recommended='Bill Duke' Strength=4>
<Record Recommended='Dolly Parton' Strength=4>
<Record Recommended='Ana Claudia Talancón' Strength=4>
<Record Recommended='Tara Reid' Strength=4>
<Record Recommended='François Chau' Strength=4>
<Record Recommended='Ray Park' Strength=4>
<Record Recommended='Harry Lennix' Strength=4>
<Record Recommended='Ashley Edner' Strength=4>
<Record Recommended='Paul Lombardi' Strength=4>
<Record Recommended='Martin Freeman' Strength=4>
<Record Recommended='Anthony Easton' Strength=4>
<Record Recommended='Robert Wahlberg' Strength=4>
<Record Recommended='C. Thomas Howell' Strength=4>
<Record Recommended='Tate Donovan' Strength=4>
<Record Recommended='Tracie Thoms' Strength=4>
<Record Recommended='Vicki Lewis' Strength=4>
<Record Recommended='Roger Guenveur Smith' Strength=4>
<Record Recommended='Steve Guttenberg' Strength=4>
<Record Recommended='River Phoenix' Strength=4>
<Record Recommended='Cynthia Nixon' Strength=4>
<Record Recommended='Marion Cotillard' Strength=4>
<Record Recommended='Karen Black' Strength=4>
<Record Recommended='Duong Don' Strength=4>
<Record Recommended='Paul Petersen' Strength=4>
<Record Recommended='Ernest Thomas' Strength=4>
<Record Recommended='Ellen DeGeneres' Strength=4>
<Record Recommended='Sasha Mitchell' Strength=4>
<Record Recommended='Erik MacArthur' Strength=4>
<Record Recommended='Sarah Polley' Strength=4>
<Record Recommended='Ray LePere' Strength=4>
<Record Recommended='Tony Dow' Strength=4>
<Record Recommended='Erik Per Sullivan' Strength=4>
<Record Recommended='Monica Bellucci' Strength=4>
<Record Recommended='Nicolas Bro' Strength=4>
<Record Recommended='Vincent Schiavelli' Strength=4>
<Record Recommended='Kate Shindle' Strength=4>
<Record Recommended='Chris Evans' Strength=4>
<Record Recommended="Alexander 'Alex' Garde" Strength=4>
<Record Recommended='Marc McClure' Strength=4>
<Record Recommended='Gary Coleman' Strength=4>
<Record Recommended='Sean Pertwee' Strength=4>
<Record Recommended='David Harbour' Strength=4>
<Record Recommended='Richard Dysart' Strength=4>
<Record Recommended='Pat Healy' Strength=4>
<Record Recommended='Jordan Nagai' Strength=4>
<Record Recommended='Kim Delaney' Strength=4>
<Record Recommended='Martin McDougall' Strength=4>
<Record Recommended='Harvey Miller' Strength=4>
<Record Recommended='Thomas Curtis' Strength=4>
<Record Recommended='Todd Field' Strength=4>
<Record Recommended='Leif Garrett' Strength=4>
<Record Recommended='Arnold Vosloo' Strength=4>
<Record Recommended='Ryan Simpkins' Strength=4>
<Record Recommended='Emily Browning' Strength=4>
<Record Recommended='Edward Burns' Strength=4>
<Record Recommended='Hillary Wolf' Strength=4>
<Record Recommended='Maureen McCormick' Strength=4>
<Record Recommended='David Ellison' Strength=4>
<Record Recommended="Ed O'Neill" Strength=4>
<Record Recommended='Don McKellar' Strength=4>
<Record Recommended='Nigel Bennett' Strength=4>
<Record Recommended='John de Lancie' Strength=4>
<Record Recommended='Lawrence Makoare' Strength=4>
<Record Recommended='Gerard Butler' Strength=4>
<Record Recommended='Joe Flanigan' Strength=4>
<Record Recommended='Eric Balfour' Strength=4>
<Record Recommended='Christopher Jacot' Strength=4>
<Record Recommended='Massimilio Massimi' Strength=4>
<Record Recommended='Ron Palillo' Strength=4>
<Record Recommended='Elizabeth Taylor' Strength=4>
<Record Recommended='Bill Mumy' Strength=4>
<Record Recommended='Matthew Lillard' Strength=4>
<Record Recommended='Mickie McGowan' Strength=4>
<Record Recommended='Jesse Doran' Strength=4>
<Record Recommended='John Mills' Strength=4>
<Record Recommended='Perry Benson' Strength=4>
<Record Recommended='Kirk Acevedo' Strength=4>
<Record Recommended='Mathieu Kassovitz' Strength=4>
<Record Recommended='Lanny Flaherty' Strength=4>
<Record Recommended='Shauna Shim' Strength=4>
<Record Recommended='John Ortiz' Strength=4>
<Record Recommended='Charlton Heston' Strength=4>
<Record Recommended='Paul Wesley' Strength=4>
<Record Recommended='Colin Ryan' Strength=4>
<Record Recommended='Becky Ann Baker' Strength=4>
<Record Recommended='Andy Davoli' Strength=4>
<Record Recommended='Sofia Coppola' Strength=4>
<Record Recommended='Jonathan Jackson' Strength=4>
<Record Recommended='Justus von Dohnanyi' Strength=4>
<Record Recommended='Jennifer Echols' Strength=4>
<Record Recommended='Anton Yelchin' Strength=4>
<Record Recommended='Lisa Jakub' Strength=4>
<Record Recommended='Nobu McCarthy' Strength=4>
<Record Recommended='Tanya Clarke' Strength=4>
<Record Recommended='Annie Potts' Strength=4>
<Record Recommended='Micole Mercurio' Strength=4>
<Record Recommended='Wilhelm von Homburg' Strength=4>
<Record Recommended='Scott Paulin' Strength=4>
<Record Recommended='Caroline Rhea' Strength=4>
<Record Recommended='Heidi Klum' Strength=4>
<Record Recommended='Gerry Wolff' Strength=4>
<Record Recommended='Peter Jacobson' Strength=4>
<Record Recommended='Richard Moll' Strength=4>
<Record Recommended='Lara Harris' Strength=4>
<Record Recommended='Anna Brobeck' Strength=4>
<Record Recommended='Sidney Poitier' Strength=4>
<Record Recommended='Frank Vincent' Strength=4>
<Record Recommended='Bates Wilder' Strength=4>
<Record Recommended='Virginia Capers' Strength=4>
<Record Recommended='Christopher Johnson' Strength=4>
<Record Recommended='Keith Loneker' Strength=4>
<Record Recommended='Margo Martindale' Strength=4>
<Record Recommended='Corey Feldman' Strength=4>
<Record Recommended='William Windom' Strength=4>
<Record Recommended='Hope Alexander-Willis' Strength=4>
<Record Recommended='Frank Adonis' Strength=4>
<Record Recommended='Jerome Ranft' Strength=4>
<Record Recommended='Vik Sahay' Strength=4>
<Record Recommended='Erin Moran' Strength=4>
<Record Recommended='Alex Rocco' Strength=4>
<Record Recommended='Julie Christie' Strength=4>
<Record Recommended='Dana Ivey' Strength=4>
<Record Recommended='Mandy Patinkin' Strength=4>
<Record Recommended='Jordan Ladd' Strength=4>
<Record Recommended='Jason Statham' Strength=4>
<Record Recommended='Scott Foley' Strength=4>
<Record Recommended='J.C. Quinn' Strength=4>
<Record Recommended='Mira Sorvino' Strength=4>
<Record Recommended='Fred Berry' Strength=4>
<Record Recommended='Andrew Garfield' Strength=4>
<Record Recommended='Ian Gomez' Strength=4>
<Record Recommended='Freddie Prinze Jr.' Strength=4>
<Record Recommended='Powers Boothe' Strength=4>
<Record Recommended='Jake Sandvig' Strength=4>
<Record Recommended='Jillie Simon' Strength=4>
<Record Recommended='Andrew Francis' Strength=4>
<Record Recommended='Jay North' Strength=4>
<Record Recommended='Kevin Dillon' Strength=4>
<Record Recommended='Marvin Braverman' Strength=4>
<Record Recommended='Terence Kelly' Strength=4>
<Record Recommended='Tamala Jones' Strength=4>
<Record Recommended='Lewis Black' Strength=4>
<Record Recommended='Heather Litteer' Strength=4>
<Record Recommended='Emma Stone' Strength=4>
<Record Recommended='Haywood Nelson' Strength=4>
<Record Recommended='Anthony Michael Hall' Strength=4>
<Record Recommended='Kathy Griffin' Strength=4>
<Record Recommended='David Eigenberg' Strength=4>
<Record Recommended='Rachel Ticotin' Strength=4>
<Record Recommended='Kent Cassella' Strength=4>
<Record Recommended='John Wayne' Strength=4>
<Record Recommended='Linda Thorson' Strength=4>
<Record Recommended='Jann Carl' Strength=4>
<Record Recommended='Craig Parker' Strength=4>
<Record Recommended='Adam Beach' Strength=4>
<Record Recommended='Christian Clemenson' Strength=4>
<Record Recommended='Sophia Myles' Strength=4>
<Record Recommended='Jayne Meadows' Strength=4>
<Record Recommended='Clive Russell' Strength=4>
<Record Recommended='Afemo Omilami' Strength=4>
<Record Recommended='Flora Martínez' Strength=4>
<Record Recommended='Kaitlin Cullum' Strength=4>
<Record Recommended='Liam Aiken' Strength=4>
<Record Recommended='Vivien Cardone' Strength=4>
<Record Recommended='Otto Sander' Strength=4>
<Record Recommended='Sally Kirkland' Strength=4>
<Record Recommended='Dustin Diamond' Strength=4>
<Record Recommended='Cleo King' Strength=4>
<Record Recommended='Eriq Ebouaney' Strength=4>
<Record Recommended='Nick Stahl' Strength=4>
<Record Recommended='Robert John Burke' Strength=4>
<Record Recommended='Patrick Bauchau' Strength=4>
<Record Recommended='Avery Brooks' Strength=4>
<Record Recommended='Stuart Townsend' Strength=4>
<Record Recommended='Bronson Pinchot' Strength=4>
<Record Recommended='Lisa Blades' Strength=4>
<Record Recommended='Sean Young' Strength=4>
<Record Recommended='Mindy Burbano' Strength=4>
<Record Recommended='Carla Cassola' Strength=4>
<Record Recommended='Elie Docter' Strength=4>
<Record Recommended='Julie Walters' Strength=4>
<Record Recommended='Jason Ritter' Strength=4>
<Record Recommended='John Kirk' Strength=4>
<Record Recommended='Barry Tubb' Strength=4>
<Record Recommended='Jenna Boyd' Strength=4>
<Record Recommended='Wyatt Smith' Strength=4>
<Record Recommended='Caroline Aaron' Strength=4>
<Record Recommended='Maria Bello' Strength=4>
<Record Recommended='David Arkin' Strength=4>
<Record Recommended='Kevin P. Farley' Strength=4>
<Record Recommended='David Selby' Strength=4>
<Record Recommended='Lorene Yarnell' Strength=4>
<Record Recommended='Frank Ridley' Strength=4>
<Record Recommended='Taylor Momsen' Strength=4>
<Record Recommended='Victor Steinbach' Strength=4>
<Record Recommended='Donald Fullilove' Strength=4>
<Record Recommended='Roy Thinnes' Strength=4>
<Record Recommended='Larry Vigus' Strength=4>
<Record Recommended='Rex Linn' Strength=4>
<Record Recommended='Mike Lookinland' Strength=4>
<Record Recommended='Michael Parks' Strength=4>
<Record Recommended='Joan Allen' Strength=4>
<Record Recommended='James McAvoy' Strength=4>
<Record Recommended='Evan Lee Dahl' Strength=4>
<Record Recommended='Marc John Jefferies' Strength=4>
<Record Recommended='Richard Attenborough' Strength=4>
<Record Recommended='Thom Hoffman' Strength=4>
<Record Recommended='Emily Harrison' Strength=4>
<Record Recommended='Edward Herrmann' Strength=4>
<Record Recommended='Eddie Kaye Thomas' Strength=4>
<Record Recommended='Lisa Joyner' Strength=4>
<Record Recommended='Howard Hesseman' Strength=4>
<Record Recommended='Burt Young' Strength=4>
<Record Recommended='Darren McGavin' Strength=4>
<Record Recommended='Rebecca Romijn' Strength=4>
<Record Recommended='Beth Grant' Strength=4>
<Record Recommended='Mimi Rogers' Strength=4>
<Record Recommended='Allen Bernstein' Strength=4>
<Record Recommended='Mae Whitman' Strength=4>
<Record Recommended='Peter Dobson' Strength=4>
<Record Recommended='Wesley Snipes' Strength=4>
<Record Recommended='Anthony Rapp' Strength=4>
<Record Recommended='Jonathan Lipnicki' Strength=4>
<Record Recommended='Tom Howard' Strength=4>
<Record Recommended='Kieran Culkin' Strength=4>
<Record Recommended='Peggy Mannix' Strength=4>
<Record Recommended='Adam Fogerty' Strength=4>
<Record Recommended='Erwin Geschonneck' Strength=4>
<Record Recommended='Keith Carradine' Strength=4>
<Record Recommended='Daphne Zuniga' Strength=4>
<Record Recommended='Naomie Harris' Strength=4>
<Record Recommended='Jake Chapman' Strength=4>
<Record Recommended='Bill Raymond' Strength=4>
<Record Recommended='Mario Cantone' Strength=4>
<Record Recommended='Rodney Allen Rippy' Strength=4>
<Record Recommended='Elisabeth Shue' Strength=4>
<Record Recommended='Robert Bagnell' Strength=4>
<Record Recommended='André the Giant' Strength=4>
<Record Recommended='Justin Chatwin' Strength=4>
<Record Recommended='Kelly Reilly' Strength=4>
<Record Recommended='Richard Edson' Strength=4>
<Record Recommended='Julie Benz' Strength=4>
<Record Recommended='Harland Williams' Strength=4>
<Record Recommended='José Ferrer' Strength=4>
<Record Recommended='Diane Kruger' Strength=4>
<Record Recommended='Willie Aames' Strength=4>
<Record Recommended='Miko C. Brando' Strength=4>
<Record Recommended='Spencer Garrett' Strength=4>
<Record Recommended='Arielle Kebbel' Strength=4>
<Record Recommended='Tilde Lindgren' Strength=4>
<Record Recommended='Marie-Josée Croze' Strength=4>
<Record Recommended='Jesse Bradford' Strength=4>
<Record Recommended='Matt Ross' Strength=4>
<Record Recommended='Paul Benedict' Strength=4>
<Record Recommended='Harvey Fierstein' Strength=4>
<Record Recommended='Gregg Henry' Strength=4>
<Record Recommended='Peter Egan' Strength=4>
<Record Recommended='Daniel Day-Lewis' Strength=4>
<Record Recommended='John Stockwell' Strength=4>
<Record Recommended='René Lavan' Strength=4>
<Record Recommended='Gregg Edelman' Strength=4>
<Record Recommended='Rowan Atkinson' Strength=4>
<Record Recommended='Donald Pleasence' Strength=4>
<Record Recommended='Maureen Stapleton' Strength=4>
<Record Recommended='David Lansbury' Strength=4>
<Record Recommended='Daniel Brühl' Strength=4>
<Record Recommended='Marion Ross' Strength=4>
<Record Recommended='Martin Balsam' Strength=4>
<Record Recommended='Doris Roberts' Strength=4>
<Record Recommended='Terry Loughlin' Strength=4>
<Record Recommended='Ron Silver' Strength=4>
<Record Recommended='Frances Bay' Strength=4>
<Record Recommended='Chris Pratt' Strength=4>
<Record Recommended='Mary Elizabeth Mastrantonio' Strength=4>
<Record Recommended='Jackie Sandler' Strength=4>
<Record Recommended='Jon Heder' Strength=4>
<Record Recommended='Miles Purinton' Strength=4>
<Record Recommended='Nicholle Tom' Strength=4>
<Record Recommended='Bert Remsen' Strength=4>
<Record Recommended='Pat Skipper' Strength=4>
<Record Recommended='Josh Cooley' Strength=4>
<Record Recommended='John Liddle' Strength=4>
<Record Recommended='Sergei Virovlianski' Strength=4>
<Record Recommended='Isla Fisher' Strength=4>
<Record Recommended='Thomas McCarthy' Strength=4>
<Record Recommended='Amelia Campbell' Strength=4>
<Record Recommended='Bill Hader' Strength=4>
<Record Recommended='Kim Gillingham' Strength=4>
<Record Recommended='Donna Dixon' Strength=4>
<Record Recommended='Wendle Josepher' Strength=4>
<Record Recommended='Garrett M. Brown' Strength=4>
<Record Recommended='Eddie Marsan' Strength=4>
<Record Recommended='William Sanderson' Strength=4>
<Record Recommended='Scott G. Anderson' Strength=4>
<Record Recommended='Agnes Bruckner' Strength=4>
<Record Recommended='David Marshall Grant' Strength=4>
<Record Recommended='Derek Luke' Strength=4>
<Record Recommended='Corey Johnson' Strength=4>
<Record Recommended='Stan Lee' Strength=4>
<Record Recommended='Theresa Randle' Strength=4>
<Record Recommended='Leslie Mann' Strength=4>
<Record Recommended='Michael McDonald' Strength=4>
<Record Recommended='Michael Ensign' Strength=4>
<Record Recommended='Michael Esper' Strength=4>
<Record Recommended='Mel Smith' Strength=4>
<Record Recommended='James Russo' Strength=4>
<Record Recommended='Dwight Yoakam' Strength=4>
<Record Recommended='Barry Livingston' Strength=4>
<Record Recommended='Zoe Kazan' Strength=4>
<Record Recommended='Valri Bromfield' Strength=4>
<Record Recommended='Nicki Aycox' Strength=4>
<Record Recommended='Valeria Bruni Tedeschi' Strength=4>
<Record Recommended='Leslie Zemeckis' Strength=4>
<Record Recommended='Elaine Bromka' Strength=4>
<Record Recommended='David Hunt' Strength=4>
<Record Recommended='Victor Wong' Strength=4>
<Record Recommended='Steven Bauer' Strength=4>
<Record Recommended='Gordon Tootoosis' Strength=4>
<Record Recommended='Sheila McCarthy' Strength=4>
<Record Recommended='Steven Weber' Strength=4>
<Record Recommended='Lucy Gordon' Strength=4>
<Record Recommended='Avril Lavigne' Strength=4>
<Record Recommended='Red Buttons' Strength=4>
<Record Recommended='Busta Rhymes' Strength=4>
<Record Recommended='Deborah Kara Unger' Strength=4>
<Record Recommended='Marlon Brando' Strength=4>
<Record Recommended='Victor Argo' Strength=4>
<Record Recommended='Goldie Hawn' Strength=4>
<Record Recommended='Maura Tierney' Strength=4>
<Record Recommended='John Hawkes' Strength=4>
<Record Recommended='Rob Elk' Strength=4>
<Record Recommended='Brawley Nolte' Strength=4>
<Record Recommended='Jacqueline Bisset' Strength=4>
<Record Recommended='Sybil Danning' Strength=4>
<Record Recommended='Jared Leto' Strength=4>
<Record Recommended='Ryan Hurst' Strength=4>
<Record Recommended='Steve Forrest' Strength=4>
<Record Recommended='Harold Gould' Strength=4>
<Record Recommended='Lara Flynn Boyle' Strength=4>
<Record Recommended='Stephen Dillane' Strength=4>
<Record Recommended='Julian Sands' Strength=4>
<Record Recommended='Leslie Bibb' Strength=4>
<Record Recommended='Todd Bridges' Strength=4>
<Record Recommended='Heather Locklear' Strength=4>
<Record Recommended='Kevin Heffernan' Strength=4>
<Record Recommended='Evelina Lundqvist' Strength=4>
<Record Recommended='Evelina Brinkemo' Strength=4>
<Record Recommended='Michelle Ruben' Strength=4>
<Record Recommended='Peter Friedman' Strength=4>
<Record Recommended='Mark McCracken' Strength=4>
<Record Recommended='Chris Tucker' Strength=4>
<Record Recommended='John Benjamin Hickey' Strength=4>
<Record Recommended='Nicholas Pasco' Strength=4>
<Record Recommended='Jake Steinfeld' Strength=4>
<Record Recommended='John Wood' Strength=4>
<Record Recommended='Roberts Blossom' Strength=4>
<Record Recommended='Meagan Good' Strength=4>
<Record Recommended='Maria Pitillo' Strength=4>
<Record Recommended='Dominique Pinon' Strength=4>
<Record Recommended='Razaaq Adoti' Strength=4>
<Record Recommended='Josh Daugherty' Strength=4>
<Record Recommended='Willie Garson' Strength=4>
<Record Recommended='Isaiah Washington' Strength=4>
<Record Recommended='Michael Buffer' Strength=4>
<Record Recommended='Jay Baruchel' Strength=4>
<Record Recommended='Rufus Sewell' Strength=4>
<Record Recommended='David Kaye' Strength=4>
<Record Recommended='Alison Eastwood' Strength=4>
<Record Recommended='Pedro Armendáriz Jr.' Strength=4>
<Record Recommended='Mark DeCarlo' Strength=4>
<Record Recommended='Jon Polito' Strength=4>
<Record Recommended='Eva Marie Saint' Strength=4>
<Record Recommended='Patrick Blindauer' Strength=4>
<Record Recommended='Rachael Harris' Strength=4>
<Record Recommended='Jedidiah Cohen' Strength=4>
<Record Recommended='Sienna Miller' Strength=4>
<Record Recommended='Joss Ackland' Strength=4>
<Record Recommended='Eddie Mekka' Strength=4>
<Record Recommended='Kath Soucie' Strength=4>
<Record Recommended='Jeremy Leary' Strength=4>
<Record Recommended='Elizabeth Franz' Strength=4>
<Record Recommended='Helga Olofsson' Strength=4>
<Record Recommended='Harriet Andersson' Strength=4>
<Record Recommended='Meghan Faye Gallagher' Strength=4>
<Record Recommended='Joaquim de Almeida' Strength=4>
<Record Recommended='Michelle Trachtenberg' Strength=4>
<Record Recommended='Steve Pemberton' Strength=4>
<Record Recommended='Paddy Considine' Strength=4>
<Record Recommended='Mark Rolston' Strength=4>
<Record Recommended='Butch Patrick' Strength=4>
<Record Recommended='Nick Damici' Strength=4>
<Record Recommended='William Sadler' Strength=4>
<Record Recommended='Enrique Castillo' Strength=4>
<Record Recommended='Doug Savant' Strength=4>
<Record Recommended='Mischa Hausserman' Strength=4>
<Record Recommended='Allen Garfield' Strength=4>
<Record Recommended='Rosamund Pike' Strength=4>
<Record Recommended='Graham Beckel' Strength=4>
<Record Recommended='Jonathan Feyer' Strength=4>
<Record Recommended='Lindsey Dann' Strength=4>
<Record Recommended='Ambyr Childers' Strength=4>
<Record Recommended='Jay Underwood' Strength=4>
<Record Recommended='Kevin Gage' Strength=4>
<Record Recommended='Cillian Murphy' Strength=4>
<Record Recommended='Alison Folland' Strength=4>
<Record Recommended='Mare Winningham' Strength=4>
<Record Recommended='Julene Renee' Strength=4>
<Record Recommended='Nicholas Schwerin' Strength=4>
<Record Recommended='Jimmy Bennett' Strength=4>
<Record Recommended='Cheryl Howard' Strength=4>
<Record Recommended='Glenn Fitzgerald' Strength=4>
<Record Recommended='Kathryn Erbe' Strength=4>
<Record Recommended='James Staley' Strength=4>
<Record Recommended='Françoise Yip' Strength=4>
<Record Recommended='Brian Clark' Strength=4>
<Record Recommended='Christopher Gorham' Strength=4>
<Record Recommended='Roger Ashton-Griffiths' Strength=4>
<Record Recommended='Maria Conchita Alonso' Strength=4>
<Record Recommended='Cara Seymour' Strength=4>
<Record Recommended='Kathleen Randazzo' Strength=4>
<Record Recommended='Candy Samples' Strength=4>
<Record Recommended='Anthony Mackie' Strength=4>
<Record Recommended='Emile Hirsch' Strength=4>
<Record Recommended='Nesbitt Blaisdell' Strength=4>
<Record Recommended='Mathieu Amalric' Strength=4>
<Record Recommended='Robin Tunney' Strength=4>
<Record Recommended='Rose Byrne' Strength=4>
<Record Recommended='Stephanie Faracy' Strength=4>
<Record Recommended='Thomas F. Walsh' Strength=4>
<Record Recommended='Almayvonne' Strength=4>
<Record Recommended='Charlene Tilton' Strength=4>
<Record Recommended='Sinéad Cusack' Strength=4>
<Record Recommended='Moritz Bleibtreu' Strength=4>
<Record Recommended='Clifton Powell' Strength=4>
<Record Recommended='Fred Wolf' Strength=4>
<Record Recommended='Nancy Pimental' Strength=4>
<Record Recommended='Erin Murphy' Strength=4>
<Record Recommended='Vinnie Jones' Strength=4>
<Record Recommended='Paul Bates' Strength=4>
<Record Recommended='Dan Fogler' Strength=4>
<Record Recommended='Kevin McNulty' Strength=3>
<Record Recommended='Geneviève Bujold' Strength=3>
<Record Recommended='Eva-Maria Hagen' Strength=3>
<Record Recommended='R.G. Armstrong' Strength=3>
<Record Recommended='Paul Benjamin' Strength=3>
<Record Recommended='Blake Lively' Strength=3>
<Record Recommended='Tony Danza' Strength=3>
<Record Recommended='Charlayne Woodard' Strength=3>
<Record Recommended='Daphne Alexander' Strength=3>
<Record Recommended='Brad Oscar' Strength=3>
<Record Recommended='Hagan Beggs' Strength=3>
<Record Recommended='Angelique Fernandez' Strength=3>
<Record Recommended='Dennis Hayden' Strength=3>
<Record Recommended='Rachelle Lefevre' Strength=3>
<Record Recommended='Anna Botting' Strength=3>
<Record Recommended='Molly Parker' Strength=3>
<Record Recommended='Lisa Arturo' Strength=3>
<Record Recommended='Tim Preece' Strength=3>
<Record Recommended='Edwin Marian' Strength=3>
<Record Recommended='Nina Siemaszko' Strength=3>
<Record Recommended='Dale Dickey' Strength=3>
<Record Recommended='Joseph Mazzello' Strength=3>
<Record Recommended='Shishir Kurup' Strength=3>
<Record Recommended='Ulrich Thein' Strength=3>
<Record Recommended='Bill McCutcheon' Strength=3>
<Record Recommended='Hal Buckley' Strength=3>
<Record Recommended='Matt Gerald' Strength=3>
<Record Recommended='Frankie Muniz' Strength=3>
<Record Recommended='Robbie Williams' Strength=3>
<Record Recommended='Aidan Devine' Strength=3>
<Record Recommended='Ione Skye' Strength=3>
<Record Recommended='Jennifer Carpenter' Strength=3>
<Record Recommended='Kristin Minter' Strength=3>
<Record Recommended='Steve Burns' Strength=3>
<Record Recommended='Michael Cristofer' Strength=3>
<Record Recommended='Joel Grey' Strength=3>
<Record Recommended='Lawrence Bender' Strength=3>
<Record Recommended='Janne Mortil' Strength=3>
<Record Recommended='Bruno Ganz' Strength=3>
<Record Recommended='Victor Garber' Strength=3>
<Record Recommended='Jenny McCarthy' Strength=3>
<Record Recommended='Vincent Perez' Strength=3>
<Record Recommended='Steve Eastin' Strength=3>
<Record Recommended='Robert Powell' Strength=3>
<Record Recommended='Henry Winkler' Strength=3>
<Record Recommended='Linda Bassett' Strength=3>
<Record Recommended='István Bálint' Strength=3>
<Record Recommended='Michael Brunner' Strength=3>
<Record Recommended='Peter Aykroyd' Strength=3>
<Record Recommended='Rose McGowan' Strength=3>
<Record Recommended='Robbie Bulloch' Strength=3>
<Record Recommended='Traylor Howard' Strength=3>
<Record Recommended='Billy Gallo' Strength=3>
<Record Recommended='Harry Belafonte' Strength=3>
<Record Recommended='Jack Plotnick' Strength=3>
<Record Recommended='John Turner' Strength=3>
<Record Recommended='Alexandrea Owens' Strength=3>
<Record Recommended='Clarice Taylor' Strength=3>
<Record Recommended='Amber Valletta' Strength=3>
<Record Recommended='Chris Elliott' Strength=3>
<Record Recommended='Erika Eleniak' Strength=3>
<Record Recommended='Andy Romano' Strength=3>
<Record Recommended='Gillian Barber' Strength=3>
<Record Recommended='Malik Yoba' Strength=3>
<Record Recommended='Conrad Roberts' Strength=3>
<Record Recommended='Kimberly Blair' Strength=3>
<Record Recommended='Rhonda Dotson' Strength=3>
<Record Recommended='Betsy Brantley' Strength=3>
<Record Recommended='Billy Merasty' Strength=3>
<Record Recommended='Reiley McClendon' Strength=3>
<Record Recommended='Natalie Canerday' Strength=3>
<Record Recommended='Amanda Swisten' Strength=3>
<Record Recommended='Danny Verduzco' Strength=3>
<Record Recommended='Jackie Cooper' Strength=3>
<Record Recommended='Kriangsak Ming-olo' Strength=3>
<Record Recommended='Richard Gleason' Strength=3>
<Record Recommended='Jonathan Silverman' Strength=3>
<Record Recommended='Renoly Santiago' Strength=3>
<Record Recommended='Ray Baker' Strength=3>
<Record Recommended='Paula Garcés' Strength=3>
<Record Recommended='Sharon Washington' Strength=3>
<Record Recommended='Joseph Cortese' Strength=3>
<Record Recommended='Omar Sharif' Strength=3>
<Record Recommended='Lew Palter' Strength=3>
<Record Recommended='Kenneth Mars' Strength=3>
<Record Recommended='David Thewlis' Strength=3>
<Record Recommended='Jeffrey Tambor' Strength=3>
<Record Recommended='Janie Woods-Morris' Strength=3>
<Record Recommended='Gillian Anderson' Strength=3>
<Record Recommended='Tom Riis Farrell' Strength=3>
<Record Recommended='Tony Denman' Strength=3>
<Record Recommended='Phoebe Cates' Strength=3>
<Record Recommended='Meret Becker' Strength=3>
<Record Recommended='Thomas Gottschalk' Strength=3>
<Record Recommended='Adewale Akinnuoye-Agbaje' Strength=3>
<Record Recommended='Rodger Halston' Strength=3>
<Record Recommended='Peter Facinelli' Strength=3>
<Record Recommended='Dominique Swain' Strength=3>
<Record Recommended='Alessandro Fabrizi' Strength=3>
<Record Recommended='Fairuza Balk' Strength=3>
<Record Recommended='Gabrielle Lazure' Strength=3>
<Record Recommended='Harley Jane Kozak' Strength=3>
<Record Recommended='Terry Kinney' Strength=3>
<Record Recommended='Ludacris' Strength=3>
<Record Recommended='Valentina Vargas' Strength=3>
<Record Recommended='Lena Olin' Strength=3>
<Record Recommended='Bob Sapp' Strength=3>
<Record Recommended='Cindy Girling' Strength=3>
<Record Recommended='Jean-François Balmer' Strength=3>
<Record Recommended='Will Sasso' Strength=3>
<Record Recommended='B.B. King' Strength=3>
<Record Recommended='Jeff Morris' Strength=3>
<Record Recommended='Jenna Elfman' Strength=3>
<Record Recommended='Sean McGinley' Strength=3>
<Record Recommended='Peter Mullan' Strength=3>
<Record Recommended='Catherine McCormack' Strength=3>
<Record Recommended='Tamlyn Tomita' Strength=3>
<Record Recommended='Gila Almagor' Strength=3>
<Record Recommended='Paula Patton' Strength=3>
<Record Recommended='Tara Strong' Strength=3>
<Record Recommended='George Fargo' Strength=3>
<Record Recommended='Kerri Green' Strength=3>
<Record Recommended='Manfred Krug' Strength=3>
<Record Recommended='Michael Laskin' Strength=3>
<Record Recommended='Peter Capaldi' Strength=3>
<Record Recommended='Carol Bruce' Strength=3>
<Record Recommended='Frank C. Turner' Strength=3>
<Record Recommended='Jake La Botz' Strength=3>
<Record Recommended='Randy Stripling' Strength=3>
<Record Recommended='Craig Robinson' Strength=3>
<Record Recommended='Richard T. Jones' Strength=3>
<Record Recommended='Cecil Zilla Mamanzi' Strength=3>
<Record Recommended='Jeffrey Daniel Phillips' Strength=3>
<Record Recommended='George Dzundza' Strength=3>
<Record Recommended='Leslie Wing' Strength=3>
<Record Recommended='Monique Gabrielle' Strength=3>
<Record Recommended='Nick Cassavetes' Strength=3>
<Record Recommended='Sammi Davis' Strength=3>
<Record Recommended='Steve Rankin' Strength=3>
<Record Recommended='Jaymes Butler' Strength=3>
<Record Recommended='Stephen Rea' Strength=3>
<Record Recommended='Alexander Siddig' Strength=3>
<Record Recommended='Robin Driscoll' Strength=3>
<Record Recommended='Jonathan Winters' Strength=3>
<Record Recommended='Donald Trump' Strength=3>
<Record Recommended='Estella Warren' Strength=3>
<Record Recommended='Nicole Fugere' Strength=3>
<Record Recommended='Chris Pine' Strength=3>
<Record Recommended='Dean Cain' Strength=3>
<Record Recommended='Sonsee Neu' Strength=3>
<Record Recommended='John Getz' Strength=3>
<Record Recommended='Patricia Belcher' Strength=3>
<Record Recommended='John Astin' Strength=3>
<Record Recommended='Jody Thompson' Strength=3>
<Record Recommended='Sarah Silverman' Strength=3>
<Record Recommended='Andy Borowitz' Strength=3>
<Record Recommended='Tommy Chong' Strength=3>
<Record Recommended='Slim Pickens' Strength=3>
<Record Recommended='Adam Rodriguez' Strength=3>
<Record Recommended="Mo'Nique" Strength=3>
<Record Recommended='Amaury Nolasco' Strength=3>
<Record Recommended='Hannjo Hasse' Strength=3>
<Record Recommended='Chorn Solyda' Strength=3>
<Record Recommended='Lauryn Hill' Strength=3>
<Record Recommended='August Schellenberg' Strength=3>
<Record Recommended='Jessica Lundy' Strength=3>
<Record Recommended='Rafi Gavron' Strength=3>
<Record Recommended='Romain Duris' Strength=3>
<Record Recommended='Larry Bryggman' Strength=3>
<Record Recommended='Elizabeth Hawthorne' Strength=3>
<Record Recommended='Talia Shire' Strength=3>
<Record Recommended='John Witherspoon' Strength=3>
<Record Recommended='David Alexander' Strength=3>
<Record Recommended='Julie Kavner' Strength=3>
<Record Recommended='Mike Judge' Strength=3>
<Record Recommended='Gemma Arterton' Strength=3>
<Record Recommended='Elizabeth McGovern' Strength=3>
<Record Recommended='Joe Sheridan' Strength=3>
<Record Recommended='Brian Brophy' Strength=3>
<Record Recommended='Julieta Serrano' Strength=3>
<Record Recommended='Alisa Christensen' Strength=3>
<Record Recommended='Willie Nelson' Strength=3>
<Record Recommended='Dee Pollock' Strength=3>
<Record Recommended='Sung Kang' Strength=3>
<Record Recommended='Brian Kimmet' Strength=3>
<Record Recommended='Brad Carr' Strength=3>
<Record Recommended='Shirley MacLaine' Strength=3>
<Record Recommended='Jimmy Carr' Strength=3>
<Record Recommended='Alice Krige' Strength=3>
<Record Recommended='Sergio Rubini' Strength=3>
<Record Recommended='John Furlong' Strength=3>
<Record Recommended='Walter Robles' Strength=3>
<Record Recommended='Clark Gable' Strength=3>
<Record Recommended='James Keane' Strength=3>
<Record Recommended='Miguel Sandoval' Strength=3>
<Record Recommended='John Shrapnel' Strength=3>
<Record Recommended='Lisa Gay Hamilton' Strength=3>
<Record Recommended='Martin Henderson' Strength=3>
<Record Recommended='David Cronenberg' Strength=3>
<Record Recommended='Laura Bell Bundy' Strength=3>
<Record Recommended='McNally Sagal' Strength=3>
<Record Recommended='Callum Keith Rennie' Strength=3>
<Record Recommended='Benoît Magimel' Strength=3>
<Record Recommended='Famke Janssen' Strength=3>
<Record Recommended='Alexis Bledel' Strength=3>
<Record Recommended='Brendan Deary' Strength=3>
<Record Recommended='Dileep Rao' Strength=3>
<Record Recommended='James Hong' Strength=3>
<Record Recommended='Greg Zola' Strength=3>
<Record Recommended='Reginald VelJohnson' Strength=3>
<Record Recommended='Pasquale Cajano' Strength=3>
<Record Recommended='Gene Collins' Strength=3>
<Record Recommended='Sara Rue' Strength=3>
<Record Recommended='Thomas Lennon' Strength=3>
<Record Recommended='Todd Susman' Strength=3>
<Record Recommended='Lachlan Murdoch' Strength=3>
<Record Recommended='Tamsin Kelsey' Strength=3>
<Record Recommended='Dick Van Dyke' Strength=3>
<Record Recommended='Justin Mentell' Strength=3>
<Record Recommended='Jason Segel' Strength=3>
<Record Recommended='Peter Sellers' Strength=3>
<Record Recommended='Joshua Leonard' Strength=3>
<Record Recommended='Marie Bunel' Strength=3>
<Record Recommended='Joan Copeland' Strength=3>
<Record Recommended='Gerry Quigley' Strength=3>
<Record Recommended='Kristen Dalton' Strength=3>
<Record Recommended='Lupe Ontiveros' Strength=3>
<Record Recommended='Matt Malloy' Strength=3>
<Record Recommended='Jeremy Suarez' Strength=3>
<Record Recommended='Holmes Osborne' Strength=3>
<Record Recommended='Eva Mattes' Strength=3>
<Record Recommended='David Rasche' Strength=3>
<Record Recommended='James Doohan' Strength=3>
<Record Recommended='George Savalas' Strength=3>
<Record Recommended='Lyle Lovett' Strength=3>
<Record Recommended='Neil Pepe' Strength=3>
<Record Recommended='Peter Sohn' Strength=3>
<Record Recommended='Agatha Hurle' Strength=3>
<Record Recommended='Angel Tompkins' Strength=3>
<Record Recommended='Robert Seeliger' Strength=3>
<Record Recommended='Nigel Gibbs' Strength=3>
<Record Recommended='Michael Rispoli' Strength=3>
<Record Recommended='Ryan Pelton' Strength=3>
<Record Recommended='Jeremy Renner' Strength=3>
<Record Recommended='Lee Arenberg' Strength=3>
<Record Recommended='Mark Ivanir' Strength=3>
<Record Recommended='Estelle Harris' Strength=3>
<Record Recommended='William Smith Yelton' Strength=3>
<Record Recommended='Gavin MacLeod' Strength=3>
<Record Recommended='Gretchen Mol' Strength=3>
<Record Recommended='Tom Troupe' Strength=3>
<Record Recommended='John G. Heller' Strength=3>
<Record Recommended='Colleen Dewhurst' Strength=3>
<Record Recommended="Michael O'Hagan" Strength=3>
<Record Recommended='Michael Cassidy' Strength=3>
<Record Recommended='Connor Paolo' Strength=3>
<Record Recommended='Vincent Spano' Strength=3>
<Record Recommended='Kyle Chandler' Strength=3>
<Record Recommended='Barnard Hughes' Strength=3>
<Record Recommended='Alan King' Strength=3>
<Record Recommended='Raven-Symoné' Strength=3>
<Record Recommended='Olivia Burnette' Strength=3>
<Record Recommended='Ken Stott' Strength=3>
<Record Recommended='Amy Yasbeck' Strength=3>
<Record Recommended='Fergal Reilly' Strength=3>
<Record Recommended='Panchito Gómez' Strength=3>
<Record Recommended='François Berléand' Strength=3>
<Record Recommended='David Dwyer' Strength=3>
<Record Recommended='Roma Maffia' Strength=3>
<Record Recommended='Anson Mount' Strength=3>
<Record Recommended='Brigitte Fossey' Strength=3>
<Record Recommended="Somkuan 'Kuan' Siroon" Strength=3>
<Record Recommended='Montel Williams' Strength=3>
<Record Recommended='Dean McDermott' Strength=3>
<Record Recommended='Elissa Knight' Strength=3>
<Record Recommended='Jaid Barrymore' Strength=3>
<Record Recommended='Pat Corley' Strength=3>
<Record Recommended="Cyril O'Reilly" Strength=3>
<Record Recommended='Jacqueline Kim' Strength=3>
<Record Recommended='Graham Stark' Strength=3>
<Record Recommended='Chris Young' Strength=3>
<Record Recommended='John Lone' Strength=3>
<Record Recommended='Sergej Trifunović' Strength=3>
<Record Recommended='Gena Rowlands' Strength=3>
<Record Recommended='Steven Hill' Strength=3>
<Record Recommended='Tim Guinee' Strength=3>
<Record Recommended='Mario Van Peebles' Strength=3>
<Record Recommended='Tina Fiorda' Strength=3>
<Record Recommended='Colleen Fitzpatrick' Strength=3>
<Record Recommended='Warren Beatty' Strength=3>
<Record Recommended='Gina Hecht' Strength=3>
<Record Recommended='Graham Greene' Strength=3>
<Record Recommended='Michael C. Maronna' Strength=3>
<Record Recommended='Lee Tergesen' Strength=3>
<Record Recommended='Richard Joseph Paul' Strength=3>
<Record Recommended='Katharine Ross' Strength=3>
<Record Recommended='Steve Allen' Strength=3>
<Record Recommended='Ed Beeten' Strength=3>
<Record Recommended='Laila Robins' Strength=3>
<Record Recommended='Barry Del Sherman' Strength=3>
<Record Recommended='Faith Hill' Strength=3>
<Record Recommended='Octavia Spencer' Strength=3>
<Record Recommended='David Paymer' Strength=3>
<Record Recommended='Rik Mayall' Strength=3>
<Record Recommended='Lee Oakes' Strength=3>
<Record Recommended='Jessica Hecht' Strength=3>
<Record Recommended='Len Lesser' Strength=3>
<Record Recommended='Helen Slater' Strength=3>
<Record Recommended='Scott Miles' Strength=3>
<Record Recommended='Jane Adams' Strength=3>
<Record Recommended='Edwin Louis' Strength=3>
<Record Recommended='Felicity Waterman' Strength=3>
<Record Recommended='Mark Addy' Strength=3>
<Record Recommended='Walter Koenig' Strength=3>
<Record Recommended='Lynn Whitfield' Strength=3>
<Record Recommended='Garry Shandling' Strength=3>
<Record Recommended='MacInTalk' Strength=3>
<Record Recommended='Bertila Damas' Strength=3>
<Record Recommended='Dale Wilson' Strength=3>
<Record Recommended='Jason Davis' Strength=3>
<Record Recommended='Temuera Morrison' Strength=3>
<Record Recommended='Leonard Nimoy' Strength=3>
<Record Recommended='David Lewis' Strength=3>
<Record Recommended='Lee Pace' Strength=3>
<Record Recommended='Jihmi Kennedy' Strength=3>
<Record Recommended='Wilmer Calderon' Strength=3>
<Record Recommended='Sarah Dampf' Strength=3>
<Record Recommended='Kareena Kapoor' Strength=3>
<Record Recommended='Marcus Thomas' Strength=3>
<Record Recommended='Aleksa Palladino' Strength=3>
<Record Recommended='Eve Jeffers' Strength=3>
<Record Recommended='Nikolaj Coster-Waldau' Strength=3>
<Record Recommended='Julius Callahan' Strength=3>
<Record Recommended='Jerry Messing' Strength=3>
<Record Recommended='Henry Thomas' Strength=3>
<Record Recommended='John Bedford Lloyd' Strength=3>
<Record Recommended='Florencia Lozano' Strength=3>
<Record Recommended='Leon Rippy' Strength=3>
<Record Recommended='A.J. Cook' Strength=3>
<Record Recommended='John Capodice' Strength=3>
<Record Recommended='James Stewart' Strength=3>
<Record Recommended='Robert Easton' Strength=3>
<Record Recommended='Koji Kataoka' Strength=3>
<Record Recommended='Irrfan Khan' Strength=3>
<Record Recommended='Laura Harrington' Strength=3>
<Record Recommended='Lisa Nicole Carson' Strength=3>
<Record Recommended="Maureen O'Hara" Strength=3>
<Record Recommended='Heather Langenkamp' Strength=3>
<Record Recommended='Pauley Perrette' Strength=3>
<Record Recommended='Karl-Otto Alberty' Strength=3>
<Record Recommended='Éva Igó' Strength=3>
<Record Recommended='Rob Corddry' Strength=3>
<Record Recommended='Nadim Sawalha' Strength=3>
<Record Recommended='Scott Hylands' Strength=3>
<Record Recommended='Amy Poehler' Strength=3>
<Record Recommended='Michael Michele' Strength=3>
<Record Recommended='Jeff Perry' Strength=3>
<Record Recommended='Dylan Hartigan' Strength=3>
<Record Recommended='Michael Imperioli' Strength=3>
<Record Recommended='Jill Ritchie' Strength=3>
<Record Recommended='Amy Locane' Strength=3>
<Record Recommended='Joan Hackett' Strength=3>
<Record Recommended='Thomas Mitchell' Strength=3>
<Record Recommended='Gavin Craig' Strength=3>
<Record Recommended='Patrick Thomas' Strength=3>
<Record Recommended='Andy Richter' Strength=3>
<Record Recommended='Ashley Olsen' Strength=3>
<Record Recommended='Galen Yuen' Strength=3>
<Record Recommended='Michaela Mann' Strength=3>
<Record Recommended='Jeff Harding' Strength=3>
<Record Recommended='Levan Uchaneishvili' Strength=3>
<Record Recommended='Alexa Vega' Strength=3>
<Record Recommended='Hugh M. Hefner' Strength=3>
<Record Recommended='Jonathan Phillips' Strength=3>
<Record Recommended='Jon Stewart' Strength=3>
<Record Recommended='Steven Randazzo' Strength=3>
<Record Recommended='Nyasha Hatendi' Strength=3>
<Record Recommended='Sandy Helberg' Strength=3>
<Record Recommended='Don Johnson' Strength=3>
<Record Recommended='Nick Mazzola' Strength=3>
<Record Recommended='Emmanuelle Chriqui' Strength=3>
<Record Recommended='Rick Gonzalez' Strength=3>
<Record Recommended='Trini Alvarado' Strength=3>
<Record Recommended='Bernard Cuffling' Strength=3>
<Record Recommended='Linda Hunt' Strength=3>
<Record Recommended='Paul Rodriguez' Strength=3>
<Record Recommended='Clancy Brown' Strength=3>
<Record Recommended='Rob Campbell' Strength=3>
<Record Recommended='Rob Brown' Strength=3>
<Record Recommended='Pauly Shore' Strength=3>
<Record Recommended='Theresa Merritt' Strength=3>
<Record Recommended='Jean-Pierre Cassel' Strength=3>
<Record Recommended='Cristina Raines' Strength=3>
<Record Recommended='Winston Mangwarara' Strength=3>
<Record Recommended='Philippe Bergeron' Strength=3>
<Record Recommended='Hilary Gordon' Strength=3>
<Record Recommended='Peter Rnic' Strength=3>
<Record Recommended='Robert Schwartzman' Strength=3>
<Record Recommended='Peter Greene' Strength=3>
<Record Recommended='Austin Crim' Strength=3>
<Record Recommended='Rumer Willis' Strength=3>
<Record Recommended='Nicholas Cascone' Strength=3>
<Record Recommended='Daryl Sabara' Strength=3>
<Record Recommended='Rossy de Palma' Strength=3>
<Record Recommended='Thomas Ian Nicholas' Strength=3>
<Record Recommended='Joel Gretsch' Strength=3>
<Record Recommended='Nicholas Art' Strength=3>
<Record Recommended='Lennie James' Strength=3>
<Record Recommended='Michael K. Williams' Strength=3>
<Record Recommended='Colin Cunningham' Strength=3>
<Record Recommended='Mario Adorf' Strength=3>
<Record Recommended='Hilary Shepard' Strength=3>
<Record Recommended="Frances O'Connor" Strength=3>
<Record Recommended='Carrie Preston' Strength=3>
<Record Recommended='Saichia Wongwiroj' Strength=3>
<Record Recommended='Loudon Wainwright III' Strength=3>
<Record Recommended='Rich Hutchman' Strength=3>
<Record Recommended='Edward Furlong' Strength=3>
<Record Recommended='Alan Cumming' Strength=3>
<Record Recommended='Ben Johnson' Strength=3>
<Record Recommended='Michael Clark' Strength=3>
<Record Recommended='Tyler Patrick Jones' Strength=3>
<Record Recommended='Sally Hawkins' Strength=3>
<Record Recommended='Crystal Verge' Strength=3>
<Record Recommended='Lew Temple' Strength=3>
<Record Recommended='Domenick Lombardozzi' Strength=3>
<Record Recommended='Kailie Hollister' Strength=3>
<Record Recommended='Myles Jeffrey' Strength=3>
<Record Recommended='Peter Graves' Strength=3>
<Record Recommended='Andy Samberg' Strength=3>
<Record Recommended='Piper Mackenzie Harris' Strength=3>
<Record Recommended='Jaime Pressly' Strength=3>
<Record Recommended='Greta Scacchi' Strength=3>
<Record Recommended='Illeana Douglas' Strength=3>
<Record Recommended='Helen McCrory' Strength=3>
<Record Recommended='Paul Tingay' Strength=3>
<Record Recommended='Richard Lautsch' Strength=3>
<Record Recommended='Ben Burtt' Strength=3>
<Record Recommended='Roger Lloyd-Pack' Strength=3>
<Record Recommended='Perry Lopez' Strength=3>
<Record Recommended='Timothy Stack' Strength=3>
<Record Recommended='George Wendt' Strength=3>
<Record Recommended='Shane Baumel' Strength=3>
<Record Recommended='Bridget Hall' Strength=3>
<Record Recommended='Ed Helms' Strength=3>
<Record Recommended='Lexi Randall' Strength=3>
<Record Recommended='Parker Stevenson' Strength=3>
<Record Recommended='Jake Johnson' Strength=3>
<Record Recommended='Anthony James' Strength=3>
<Record Recommended='Saïd Taghmaoui' Strength=3>
<Record Recommended='E.G. Marshall' Strength=3>
<Record Recommended='Dieter Laser' Strength=3>
<Record Recommended='Franco Nero' Strength=3>
<Record Recommended='Bridget Moynahan' Strength=3>
<Record Recommended='Bruce A. Young' Strength=3>
<Record Recommended='Elisha Cuthbert' Strength=3>
<Record Recommended='Gregory Cooke' Strength=3>
<Record Recommended='Jim Parsons' Strength=3>
<Record Recommended='Ole Thestrup' Strength=3>
<Record Recommended='T.J. Cross' Strength=3>
<Record Recommended='Bess Wohl' Strength=3>
<Record Recommended='Marg Helgenberger' Strength=3>
<Record Recommended='Tim DeKay' Strength=3>
<Record Recommended='Alan Howard' Strength=3>
<Record Recommended='Jeanette Brox' Strength=3>
<Record Recommended='Eric Schneider' Strength=3>
<Record Recommended='Lindsay Lohan' Strength=3>
<Record Recommended='Debby Davison' Strength=3>
<Record Recommended='Vincent Pastore' Strength=3>
<Record Recommended='Lorri Bagley' Strength=3>
<Record Recommended='Peter A. DeCenzie' Strength=3>
<Record Recommended='Susan Dalian' Strength=3>
<Record Recommended='Gerard Plunkett' Strength=3>
<Record Recommended='Anthony LaPaglia' Strength=3>
<Record Recommended='John Amos' Strength=3>
<Record Recommended='Javier Bardem' Strength=3>
<Record Recommended='Gerry Vichi' Strength=3>
<Record Recommended='Paul Bartel' Strength=3>
<Record Recommended='Spalding Gray' Strength=3>
<Record Recommended='Richard Libertini' Strength=3>
<Record Recommended='Maggie Q' Strength=3>
<Record Recommended='Dann Florek' Strength=3>
<Record Recommended='Silas Carson' Strength=3>
<Record Recommended="Abhijati 'Meuk' Jusakul" Strength=3>
<Record Recommended='Annie Parisse' Strength=3>
<Record Recommended='Michael Constantine' Strength=3>
<Record Recommended='Anthony DeSimone' Strength=3>
<Record Recommended='Brittany Snow' Strength=3>
<Record Recommended='Aaron Pearl' Strength=3>
<Record Recommended='W. Earl Brown' Strength=3>
<Record Recommended='Richard Jordan' Strength=3>
<Record Recommended='Rob Krausz' Strength=3>
<Record Recommended='Georgia Engel' Strength=3>
<Record Recommended='Phil Fondacaro' Strength=3>
<Record Recommended='Jane Alexander' Strength=3>
<Record Recommended='Nicholas Turturro' Strength=3>
<Record Recommended='Wendell Wellman' Strength=3>
<Record Recommended='Larry Pine' Strength=3>
<Record Recommended='Timothy Busfield' Strength=3>
<Record Recommended='Oprah Winfrey' Strength=3>
<Record Recommended='Heidi Lenhart' Strength=3>
<Record Recommended='Helena Mattsson' Strength=3>
<Record Recommended='Chris Spencer' Strength=3>
<Record Recommended='Mr. Yuttana Muenwaja' Strength=3>
<Record Recommended='Chopper Bernet' Strength=3>
<Record Recommended='Corki Corman' Strength=3>
<Record Recommended='Claire Forlani' Strength=3>
<Record Recommended='Armando Hernández' Strength=3>
<Record Recommended='Colleen Camp' Strength=3>
<Record Recommended='Giuseppe Andrews' Strength=3>
<Record Recommended='Robert Knepper' Strength=3>
<Record Recommended='William Mapother' Strength=3>
<Record Recommended='John Finn' Strength=3>
<Record Recommended='Joely Richardson' Strength=3>
<Record Recommended='Nicholas Wyman' Strength=3>
<Record Recommended='Shahrukh Khan' Strength=3>
<Record Recommended='John Gallagher Jr.' Strength=3>
<Record Recommended='Sam Phillips' Strength=3>
<Record Recommended='Stephen Colbert' Strength=3>
<Record Recommended='Melinda Clarke' Strength=3>
<Record Recommended='Dick Hughes' Strength=3>
<Record Recommended='Sacha Baron Cohen' Strength=3>
<Record Recommended='Nick Searcy' Strength=3>
<Record Recommended='Kelly McGillis' Strength=3>
<Record Recommended='Jill Scott' Strength=3>
<Record Recommended='Matt Hill' Strength=3>
<Record Recommended='Richard Benjamin' Strength=3>
<Record Recommended='Michael McShane' Strength=3>
<Record Recommended='Kim Bodnia' Strength=3>
<Record Recommended='Saeed Jaffrey' Strength=3>
<Record Recommended='Stephanie Berry' Strength=3>
<Record Recommended='Omar Benson Miller' Strength=3>
<Record Recommended='John Tench' Strength=3>
<Record Recommended='Jerry Weintraub' Strength=3>
<Record Recommended='Colleen Dunn' Strength=3>
<Record Recommended='Billy West' Strength=3>
<Record Recommended='Rory Cochrane' Strength=3>
<Record Recommended='Raf Vallone' Strength=3>
<Record Recommended='Jeffrey DeMunn' Strength=3>
<Record Recommended='Leigh Taylor-Young' Strength=3>
<Record Recommended='Christina Cole' Strength=3>
<Record Recommended='Jean-François Stévenin' Strength=3>
<Record Recommended='Diane Salinger' Strength=3>
<Record Recommended='Warren Oates' Strength=3>
<Record Recommended='Roberto Benigni' Strength=3>
<Record Recommended='Kim Kondrashoff' Strength=3>
<Record Recommended='Marina Sirtis' Strength=3>
<Record Recommended='Jon Seda' Strength=3>
<Record Recommended='Winston Ntshona' Strength=3>
<Record Recommended='Chris Hemsworth' Strength=3>
<Record Recommended='Timm Sharp' Strength=3>
<Record Recommended='Adam Hann-Byrd' Strength=3>
<Record Recommended='Anthony Peck' Strength=3>
<Record Recommended='Jessica Biel' Strength=3>
<Record Recommended='Josh Janowicz' Strength=3>
<Record Recommended='French Stewart' Strength=3>
<Record Recommended='Christoph Sanders' Strength=3>
<Record Recommended='Zoaunne LeRoy' Strength=3>
<Record Recommended='Frank Gorshin' Strength=3>
<Record Recommended='Lou Romano' Strength=3>
<Record Recommended='Nobu Matsuhisa' Strength=3>
<Record Recommended='Jeremiah Mnisi' Strength=3>
<Record Recommended='Reece Thompson' Strength=3>
<Record Recommended='James Farentino' Strength=3>
<Record Recommended='Kevin Michael Richardson' Strength=3>
<Record Recommended='Margarita Sanz' Strength=3>
<Record Recommended='Sergio Castellitto' Strength=3>
<Record Recommended='Jarrad Paul' Strength=3>
<Record Recommended='Michael S. Ruscheinsky' Strength=3>
<Record Recommended='Russi Taylor' Strength=3>
<Record Recommended='Earl Boen' Strength=3>
<Record Recommended='Kate Reid' Strength=3>
<Record Recommended='Clare Clifford' Strength=3>
<Record Recommended='Kelly Hu' Strength=3>
<Record Recommended='Nicole Ari Parker' Strength=3>
<Record Recommended='Mercedes Ruehl' Strength=3>
<Record Recommended='Sophie Thompson' Strength=3>
<Record Recommended='Milo Ventimiglia' Strength=3>
<Record Recommended='Britney Spears' Strength=3>
<Record Recommended='Margaret Cho' Strength=3>
<Record Recommended='Jeffrey Vincent Parise' Strength=3>
<Record Recommended='Chris Mulkey' Strength=3>
<Record Recommended='Joey Travolta' Strength=3>
<Record Recommended='Björk' Strength=3>
<Record Recommended='Hailey Noelle Johnson' Strength=3>
<Record Recommended='Dick Balduzzi' Strength=3>
<Record Recommended='Donna W. Scott' Strength=3>
<Record Recommended='CCH Pounder' Strength=3>
<Record Recommended='Robert Thomas Reed' Strength=3>
<Record Recommended='Stephen Dimopoulos' Strength=3>
<Record Recommended='Garrett Hedlund' Strength=3>
<Record Recommended='Chris Humphreys' Strength=3>
<Record Recommended='Frank Bruynbroek' Strength=3>
<Record Recommended="Ryan O'Neal" Strength=3>
<Record Recommended='Shaina Tianne Unger' Strength=3>
<Record Recommended='Elden Henson' Strength=3>
<Record Recommended='Mehdi Nebbou' Strength=3>
<Record Recommended='Oliver Clayton-Luce' Strength=3>
<Record Recommended='Richard Hamilton' Strength=3>
<Record Recommended='Dick Miller' Strength=3>
<Record Recommended='Ray Wise' Strength=3>
<Record Recommended='Billy Wirth' Strength=3>
<Record Recommended='Jesper Christensen' Strength=3>
<Record Recommended='Kate Capshaw' Strength=3>
<Record Recommended='Catherine Deneuve' Strength=3>
<Record Recommended='Nomadlozi Kubheka' Strength=3>
<Record Recommended='Ron Halder' Strength=3>
<Record Recommended='Don Creech' Strength=3>
<Record Recommended="Shaquille O'Neal" Strength=3>
<Record Recommended='Jordana Brewster' Strength=3>
<Record Recommended='Shirley Knight' Strength=3>
<Record Recommended='Scott Speedman' Strength=3>
<Record Recommended='Erika von Tagen' Strength=3>
<Record Recommended='Liz Torres' Strength=3>
<Record Recommended='Tomas Villum Jensen' Strength=3>
<Record Recommended='Wood Harris' Strength=3>
<Record Recommended='Gordon Arnell' Strength=3>
<Record Recommended='Bruce Altman' Strength=3>
<Record Recommended='Isabelle Fuhrman' Strength=3>
<Record Recommended='Serena Scott Thomas' Strength=3>
<Record Recommended='Paul Winfield' Strength=3>
<Record Recommended='Cheryl Carter' Strength=3>
<Record Recommended='Tobin Bell' Strength=3>
<Record Recommended='Patricia Reyes Spíndola' Strength=3>
<Record Recommended='Lynn Collins' Strength=3>
<Record Recommended='Paul Scofield' Strength=3>
<Record Recommended='Kevin Cooney' Strength=3>
<Record Recommended='Geraldine Chaplin' Strength=3>
<Record Recommended='Cheryl Hines' Strength=3>
<Record Recommended='Jernard Burks' Strength=3>
<Record Recommended='Jens Albinus' Strength=3>
<Record Recommended="Laurie O'Brien" Strength=3>
<Record Recommended='Lisa Masters' Strength=3>
<Record Recommended='Catherine Kellner' Strength=3>
<Record Recommended='Susan Kellermann' Strength=3>
<Record Recommended='Joanne Whalley' Strength=3>
<Record Recommended='George Hamilton' Strength=3>
<Record Recommended='Hugo Stanger' Strength=3>
<Record Recommended='David Spielberg' Strength=3>
<Record Recommended='James Shigeta' Strength=3>
<Record Recommended='Ian Giatti' Strength=3>
<Record Recommended='Zakes Mokae' Strength=3>
<Record Recommended='Alice Ghostley' Strength=3>
<Record Recommended='Lana McKissack' Strength=3>
<Record Recommended='Jean Bouise' Strength=3>
<Record Recommended='Stuart Devenie' Strength=3>
<Record Recommended='Iman' Strength=3>
<Record Recommended='Fiona Lewis' Strength=3>
<Record Recommended='Carlos Andrés Gómez' Strength=3>
<Record Recommended="Randall 'Tex' Cobb" Strength=3>
<Record Recommended='Ben Bray' Strength=3>
<Record Recommended='Sam Jaeger' Strength=3>
<Record Recommended='Lee Kagan' Strength=3>
<Record Recommended='Michael Alexander Jackson' Strength=3>
<Record Recommended='Eric Jungmann' Strength=3>
<Record Recommended='August Diehl' Strength=3>
<Record Recommended='Maria Ford' Strength=3>
<Record Recommended='Lesley Ann Warren' Strength=3>
<Record Recommended='Kathleen Chalfant' Strength=3>
<Record Recommended='Mel Rodriguez' Strength=3>
<Record Recommended='Nika Futterman' Strength=3>
<Record Recommended='Chad Lindberg' Strength=3>
<Record Recommended='Ellen Albertini Dow' Strength=3>
<Record Recommended='Steven Michael Quezada' Strength=3>
<Record Recommended='Jeanne Tripplehorn' Strength=3>
<Record Recommended='Art Hindle' Strength=3>
<Record Recommended='Mike McGlone' Strength=3>
<Record Recommended='Larry Gilliard Jr.' Strength=3>
<Record Recommended='Snoop Dogg' Strength=3>
<Record Recommended='Spike Lee' Strength=3>
<Record Recommended='Brett Kelley' Strength=3>
<Record Recommended='Patricia Vonne' Strength=3>
<Record Recommended='Kathleen Robertson' Strength=3>
<Record Recommended='Arabella Field' Strength=3>
<Record Recommended='Angie Harmon' Strength=3>
<Record Recommended='Michael Young' Strength=3>
<Record Recommended='Lorry Goldman' Strength=3>
<Record Recommended='Antone Pagan' Strength=3>
<Record Recommended='Paul McGillion' Strength=3>
<Record Recommended='Rajpal Yadav' Strength=3>
<Record Recommended='Jeremy Crutchley' Strength=3>
<Record Recommended='Gisele Bündchen' Strength=3>
<Record Recommended='Stuart Margolin' Strength=3>
<Record Recommended='Linda Hart' Strength=3>
<Record Recommended='Elvis Presley' Strength=3>
<Record Recommended='Reed Diamond' Strength=3>
<Record Recommended='Carmen Maura' Strength=3>
<Record Recommended='Martin East' Strength=3>
<Record Recommended='Diana Douglas' Strength=3>
<Record Recommended='Tracy Brooks Swope' Strength=3>
<Record Recommended='Isabelle Huppert' Strength=3>
<Record Recommended='Kate Nelligan' Strength=3>
<Record Recommended='Nigel Ivy' Strength=3>
<Record Recommended='Natasha Richardson' Strength=3>
<Record Recommended='Lewis Abernathy' Strength=3>
<Record Recommended='Ice Cube' Strength=3>
<Record Recommended='Tom Everett Scott' Strength=3>
<Record Recommended='Leonardo Nam' Strength=3>
<Record Recommended='Robin Gammell' Strength=3>
<Record Recommended='Matthew Walker' Strength=3>
<Record Recommended='Johnny Galecki' Strength=3>
<Record Recommended='Suzanne Solari' Strength=3>
<Record Recommended='Joanna Gleason' Strength=3>
<Record Recommended='John Pankow' Strength=3>
<Record Recommended='Mark Simich' Strength=3>
<Record Recommended='Mary Beth Hurt' Strength=3>
<Record Recommended='Dave Thomas' Strength=3>
<Record Recommended='James Karen' Strength=3>
<Record Recommended='Deborah Rush' Strength=3>
<Record Recommended='Ty Olsson' Strength=3>
<Record Recommended='Mekhi Phifer' Strength=3>
<Record Recommended='Billy Burnette' Strength=3>
<Record Recommended='Paul Adelstein' Strength=3>
<Record Recommended='Ryan Newman' Strength=3>
<Record Recommended='Mel Harris' Strength=3>
<Record Recommended='Barry Shabaka Henley' Strength=3>
<Record Recommended='Don MacKay' Strength=3>
<Record Recommended="Jack O'Halloran" Strength=3>
<Record Recommended='Roy Francis' Strength=3>
<Record Recommended='Linus Roache' Strength=3>
<Record Recommended='Fallon Brooking' Strength=3>
<Record Recommended='Sterling Hayden' Strength=3>
<Record Recommended='Jack McBrayer' Strength=3>
<Record Recommended='Paul E. Short' Strength=3>
<Record Recommended='Marcus Aurelius' Strength=3>
<Record Recommended='Kirsten Johnson' Strength=3>
<Record Recommended='Shawn Pyfrom' Strength=3>
<Record Recommended='Brent Briscoe' Strength=3>
<Record Recommended='Micah Lavette' Strength=3>
<Record Recommended='Julianna McCarthy' Strength=3>
<Record Recommended='Cristián de la Fuente' Strength=3>
<Record Recommended='Ernie Lively' Strength=3>
<Record Recommended='Fred Pearlman' Strength=3>
<Record Recommended='Patricia Charbonneau' Strength=3>
<Record Recommended='Jonathan Bennett' Strength=3>
<Record Recommended='Mila Kunis' Strength=3>
<Record Recommended='John Fujioka' Strength=3>
<Record Recommended='Deon Richmond' Strength=3>
<Record Recommended='Brett Rickaby' Strength=3>
<Record Recommended="James D'Arcy" Strength=3>
<Record Recommended='Ralph Seymour' Strength=3>
<Record Recommended='Eben Young' Strength=3>
<Record Recommended='Haylie Duff' Strength=3>
<Record Recommended='Simon Fenton' Strength=3>
<Record Recommended='Martin Evans' Strength=3>
<Record Recommended='Lorrie Bess Crumley' Strength=3>
<Record Recommended='Allison Siko' Strength=3>
<Record Recommended='John Franklin' Strength=3>
<Record Recommended='Rebecca De Mornay' Strength=3>
<Record Recommended='Tony Siragusa' Strength=3>
<Record Recommended='Ute Lemper' Strength=3>
<Record Recommended='Amanda De Cadenet' Strength=3>
<Record Recommended='Gabriel Casseus' Strength=3>
<Record Recommended='Allison Mack' Strength=3>
<Record Recommended='Beverly Todd' Strength=3>
<Record Recommended='Aldis Hodge' Strength=3>
<Record Recommended='Ivana Milicevic' Strength=3>
<Record Recommended='Guy Witcher' Strength=3>
<Record Recommended='Taylor Nichols' Strength=3>
<Record Recommended='Gregory Hines' Strength=3>
<Record Recommended='Jackie Gleason' Strength=3>
<Record Recommended='Martin Landau' Strength=3>
<Record Recommended='Linda Tomassone' Strength=3>
<Record Recommended='Casey Sander' Strength=3>
<Record Recommended='Jared Lavette' Strength=3>
<Record Recommended='Irwin Keyes' Strength=3>
<Record Recommended='Shepherd Sanders' Strength=3>
<Record Recommended='Ami Weinberg' Strength=3>
<Record Recommended='Charlie Korsmo' Strength=3>
<Record Recommended="Maureen O'Sullivan" Strength=3>
<Record Recommended='Nicholas Pryor' Strength=3>
<Record Recommended='Gabriel Macht' Strength=3>
<Record Recommended='Zena Grey' Strength=3>
<Record Recommended='Steven Berkoff' Strength=3>
<Record Recommended='Lonette McKee' Strength=3>
<Record Recommended='Luke Bigham' Strength=3>
<Record Recommended='Tyrese Gibson' Strength=3>
<Record Recommended='Cynthia Gibb' Strength=3>
<Record Recommended='Maria de Medeiros' Strength=3>
<Record Recommended='Frederick Strother' Strength=3>
<Record Recommended='James Lally' Strength=3>
<Record Recommended='Michelle Murdocca' Strength=3>
<Record Recommended='Basil Hoffman' Strength=3>
<Record Recommended='Gabrielle Rose' Strength=3>
<Record Recommended='Mike Doyle' Strength=3>
<Record Recommended='Dominic Walker' Strength=3>
<Record Recommended='Ali Larter' Strength=3>
<Record Recommended='Judith Scott' Strength=3>
<Record Recommended='Hugh Dancy' Strength=3>
<Record Recommended='Conrad Janis' Strength=3>
<Record Recommended='Landry Allbright' Strength=3>
<Record Recommended='Christopher Neame' Strength=3>
<Record Recommended='Boris Kodjoe' Strength=3>
<Record Recommended='Hywell Williams' Strength=3>
<Record Recommended='Keenan Wynn' Strength=3>
<Record Recommended='Stacey Dash' Strength=3>
<Record Recommended='Michael Bowen' Strength=3>
<Record Recommended='Judy Greer' Strength=3>
<Record Recommended='James Badge Dale' Strength=3>
<Record Recommended='Eileen Ryan' Strength=3>
<Record Recommended='Sam Robards' Strength=3>
<Record Recommended='Hannah Taylor-Gordon' Strength=3>
<Record Recommended='Arsinée Khanjian' Strength=3>
<Record Recommended='Bokeem Woodbine' Strength=3>
<Record Recommended='Max Van Ville' Strength=3>
<Record Recommended='Annabella Piugattuk' Strength=3>
<Record Recommended='Peter Haworth' Strength=3>
<Record Recommended='Damon Wayans' Strength=3>
<Record Recommended='Anna Longhi' Strength=3>
<Record Recommended='Louis Zorich' Strength=3>
<Record Recommended='Bill Romanowski' Strength=3>
<Record Recommended='Jonathan Whittaker' Strength=3>
<Record Recommended='Jeffrey Combs' Strength=3>
<Record Recommended='Doug Abrahams' Strength=3>
<Record Recommended='Kat Dennings' Strength=3>
<Record Recommended='Elpidia Carrillo' Strength=3>
<Record Recommended='John McLaughlin' Strength=3>
<Record Recommended='Kasi Lemmons' Strength=3>
<Record Recommended='William Devane' Strength=3>
<Record Recommended='Lek Chaiyan Chunsuttiwat' Strength=3>
<Record Recommended='Allan F. Nicholls' Strength=3>
<Record Recommended='Gert Van Niekirk' Strength=3>
<Record Recommended='Anne Dudek' Strength=3>
<Record Recommended='Brenda Blethyn' Strength=3>
<Record Recommended='Christian Aubert' Strength=3>
<Record Recommended='Marc Macaulay' Strength=3>
<Record Recommended='Jim Carter' Strength=3>
<Record Recommended='Dean Knowsley' Strength=3>
<Record Recommended='Kimberly Elise' Strength=3>
<Record Recommended='Mary-Kate Olsen' Strength=3>
<Record Recommended='Tuesday Weld' Strength=3>
<Record Recommended='Devon Hoholuk' Strength=3>
<Record Recommended='Rich Sommer' Strength=3>
<Record Recommended='Courtland Mead' Strength=3>
<Record Recommended='Glynn Turman' Strength=3>
<Record Recommended='Jane Horrocks' Strength=3>
<Record Recommended='Steve Byers' Strength=3>
<Record Recommended='Jay Thomas' Strength=3>
<Record Recommended='John D. King' Strength=3>
<Record Recommended='Rick Fox' Strength=3>
<Record Recommended='Michel Piccoli' Strength=3>
<Record Recommended='Oscar Goodman' Strength=3>
<Record Recommended='George Harris' Strength=3>
<Record Recommended='Omar Rodríguez' Strength=3>
<Record Recommended='Alan Tudyk' Strength=3>
<Record Recommended='Adam McKay' Strength=3>
<Record Recommended='Courtney Cole-Fendley' Strength=3>
<Record Recommended='Ron Prather' Strength=3>
<Record Recommended='Rolf Hoppe' Strength=3>
<Record Recommended='John Huston' Strength=3>
<Record Recommended='Natassia Malthe' Strength=3>
<Record Recommended='Kate Blumberg' Strength=3>
<Record Recommended='Robert Miranda' Strength=3>
<Record Recommended='Til Schweiger' Strength=3>
<Record Recommended='Sydney Pollack' Strength=3>
<Record Recommended='David Hurst' Strength=3>
<Record Recommended='Paul Greenberg' Strength=3>
<Record Recommended='Alessandro Mastrobuono' Strength=3>
<Record Recommended='Byron Lucas' Strength=3>
<Record Recommended='Frank McRae' Strength=3>
<Record Recommended='Teerawat Mulvilai' Strength=3>
<Record Recommended='Peter Law' Strength=3>
<Record Recommended='Jürgen Prochnow' Strength=3>
<Record Recommended='Robert Hays' Strength=3>
<Record Recommended='Mark Phinney' Strength=3>
<Record Recommended='Stephen Rannazzisi' Strength=3>
<Record Recommended='Niecy Nash' Strength=3>
<Record Recommended='Joanna Merlin' Strength=3>
<Record Recommended='Laura Shanahan' Strength=3>
<Record Recommended='Mark Blum' Strength=3>
<Record Recommended='Anna Maria Horsford' Strength=3>
<Record Recommended='Michael J. Farina' Strength=3>
<Record Recommended='Juan Fernández' Strength=3>
<Record Recommended='Fiorello' Strength=3>
<Record Recommended='Charles Bronson' Strength=3>
<Record Recommended='Ken Jeong' Strength=3>
<Record Recommended='Jerry Stiller' Strength=3>
<Record Recommended="De'voreaux White" Strength=3>
<Record Recommended='Chelse Swain' Strength=3>
<Record Recommended='Robert Romanus' Strength=3>
<Record Recommended='Lea Thompson' Strength=3>
<Record Recommended='Vicellous Reon Shannon' Strength=3>
<Record Recommended='Amrish Puri' Strength=3>
<Record Recommended='Gil Bellows' Strength=3>
<Record Recommended='Rhea Seehorn' Strength=3>
<Record Recommended='Lukas Haas' Strength=3>
<Record Recommended='Agustín Almodóvar' Strength=3>
<Record Recommended='Ken Garito' Strength=3>
<Record Recommended='Edi Gathegi' Strength=3>
<Record Recommended='Jason Flemyng' Strength=3>
<Record Recommended='Edward Fletcher' Strength=3>
<Record Recommended='Tim Rossovich' Strength=3>
<Record Recommended='Marianne Graffam' Strength=3>
<Record Recommended='Natascha McElhone' Strength=3>
<Record Recommended='Jim Fyfe' Strength=3>
<Record Recommended='Tonderai Masenda' Strength=3>
<Record Recommended='Sarah Lilly' Strength=3>
<Record Recommended='Juanita Moore' Strength=3>
<Record Recommended='Skipp Sudduth' Strength=3>
<Record Recommended='Robert Smigel' Strength=3>
<Record Recommended='Sandra Oh' Strength=3>
<Record Recommended='Brent Stait' Strength=3>
<Record Recommended='Jack Palance' Strength=3>
<Record Recommended='Frank Hoyt Taylor' Strength=3>
<Record Recommended='Tom Hollander' Strength=3>
<Record Recommended='Yvan Attal' Strength=3>
<Record Recommended='Kathy Ireland' Strength=3>
<Record Recommended='Susan Hegarty' Strength=3>
<Record Recommended='Walter Brennan' Strength=3>
<Record Recommended='Jack Betts' Strength=3>
<Record Recommended='Stephanie Szostak' Strength=3>
<Record Recommended='Rebecca Gordon' Strength=3>
<Record Recommended='Norm MacDonald' Strength=3>
<Record Recommended='Whip Hubley' Strength=3>
<Record Recommended='Seth Adkins' Strength=3>
<Record Recommended='Eric Braeden' Strength=3>
<Record Recommended='Kathi Copeland' Strength=3>
<Record Recommended='Michael Paré' Strength=3>
<Record Recommended='Brian Howe' Strength=3>
<Record Recommended='Lisa Kaplan' Strength=3>
<Record Recommended='Stacy Keach' Strength=3>
<Record Recommended='Thomas Rosales Jr.' Strength=3>
<Record Recommended='Jonathan Rhys Meyers' Strength=3>
<Record Recommended='Larenz Tate' Strength=3>
<Record Recommended='Cary-Hiroyuki Tagawa' Strength=3>
<Record Recommended='Nita Talbot' Strength=3>
<Record Recommended='Nigel Hawthorne' Strength=3>
<Record Recommended='Adrien Brody' Strength=3>
<Record Recommended='Romany Malco' Strength=3>
<Record Recommended='Becky Gonzalez' Strength=3>
<Record Recommended='Damien Dante Wayans' Strength=3>
<Record Recommended='Jason Barry' Strength=3>
<Record Recommended='James Oliver' Strength=3>
<Record Recommended='Ralf Moeller' Strength=3>
<Record Recommended='Lily Knight' Strength=3>
<Record Recommended='Richard Bohringer' Strength=3>
<Record Recommended='Thomas B. Duffy' Strength=3>
<Record Recommended='Robert Carradine' Strength=3>
<Record Recommended='Blake Clark' Strength=3>
<Record Recommended='Fran Drescher' Strength=3>
<Record Recommended='Ron Cook' Strength=3>
<Record Recommended='Cody Hanford' Strength=3>
<Record Recommended='Scott Spiro' Strength=3>
<Record Recommended='Leslie Hayman' Strength=3>
<Record Recommended='Annabelle Gurwitch' Strength=3>
<Record Recommended='Scott Bakula' Strength=3>
<Record Recommended='Paige Tamada' Strength=3>
<Record Recommended='Matthew Lawrence' Strength=3>
<Record Recommended='Daniel Kash' Strength=3>
<Record Recommended='Greg Proops' Strength=2>
<Record Recommended='Claude Woolman' Strength=2>
<Record Recommended='Takayo Fischer' Strength=2>
<Record Recommended='Arly Jover' Strength=2>
<Record Recommended='Jaden Smith' Strength=2>
<Record Recommended='Anthony Starke' Strength=2>
<Record Recommended='Joann Havrilla' Strength=2>
<Record Recommended='Bill Gerber' Strength=2>
<Record Recommended='Vera Miles' Strength=2>
<Record Recommended="Lou D'Amato" Strength=2>
<Record Recommended='LeVar Burton' Strength=2>
<Record Recommended='Mark Frost' Strength=2>
<Record Recommended='Bijou Phillips' Strength=2>
<Record Recommended='Toby Jones' Strength=2>
<Record Recommended='John Patrick White' Strength=2>
<Record Recommended='Lori Heuring' Strength=2>
<Record Recommended='Kiele Sanchez' Strength=2>
<Record Recommended='Sonnell Dadral' Strength=2>
<Record Recommended='Gwen Welles' Strength=2>
<Record Recommended='Sonja Smits' Strength=2>
<Record Recommended='Paterson Joseph' Strength=2>
<Record Recommended='Marco Sanchez' Strength=2>
<Record Recommended='Azucena Medina' Strength=2>
<Record Recommended='Ivan Malré' Strength=2>
<Record Recommended='Brandon Wood' Strength=2>
<Record Recommended='Elizabeth Jagger' Strength=2>
<Record Recommended='Malgorzata Zajaczkowska' Strength=2>
<Record Recommended='Rob Lynds' Strength=2>
<Record Recommended='Maggie Grace' Strength=2>
<Record Recommended='David Marciano' Strength=2>
<Record Recommended='Noelle Parker' Strength=2>
<Record Recommended='David House' Strength=2>
<Record Recommended='Alexandra Berardi' Strength=2>
<Record Recommended='Kent Harper' Strength=2>
<Record Recommended='Amanda Peterson' Strength=2>
<Record Recommended='Nathan Fillion' Strength=2>
<Record Recommended='Harry Connick Jr.' Strength=2>
<Record Recommended='Andrea Bendewald' Strength=2>
<Record Recommended='Maxwell Caulfield' Strength=2>
<Record Recommended='Patrick Fugit' Strength=2>
<Record Recommended='Philip Bruns' Strength=2>
<Record Recommended='Jon DeVries' Strength=2>
<Record Recommended='Noel Gugliemi' Strength=2>
<Record Recommended='Mark Lambert' Strength=2>
<Record Recommended='Coolio' Strength=2>
<Record Recommended='Valerie Richards' Strength=2>
<Record Recommended="Kimberly 'Lil' Kim' Jones" Strength=2>
<Record Recommended='David Hemblen' Strength=2>
<Record Recommended='Peri Gilpin' Strength=2>
<Record Recommended='Ted Danson' Strength=2>
<Record Recommended='Eric Morgan Stuart' Strength=2>
<Record Recommended='Diahann Carroll' Strength=2>
<Record Recommended='Rekha Sharma' Strength=2>
<Record Recommended='Carlos A. Cabarcas' Strength=2>
<Record Recommended='Lee Garlington' Strength=2>
<Record Recommended='Marshall Fallwell Jr.' Strength=2>
<Record Recommended='Molly Shannon' Strength=2>
<Record Recommended='Norm Crosby' Strength=2>
<Record Recommended='Gerald R. Molen' Strength=2>
<Record Recommended='Harry Hamlin' Strength=2>
<Record Recommended='Carlos Cobos' Strength=2>
<Record Recommended='Robert J. Wilke' Strength=2>
<Record Recommended='Dorothy Malone' Strength=2>
<Record Recommended='Jerry Nelson' Strength=2>
<Record Recommended='Joseph Marcus' Strength=2>
<Record Recommended='Enrique Murciano' Strength=2>
<Record Recommended='Timothy Paul Perez' Strength=2>
<Record Recommended='Ramon Alvarez' Strength=2>
<Record Recommended='Christopher Shyer' Strength=2>
<Record Recommended='Alexandra Stewart' Strength=2>
<Record Recommended='B.J. Harrison' Strength=2>
<Record Recommended='Meredith Baxter' Strength=2>
<Record Recommended='Lev Mailer' Strength=2>
<Record Recommended='James Fox' Strength=2>
<Record Recommended='Tristan Rogers' Strength=2>
<Record Recommended='Ron Masak' Strength=2>
<Record Recommended='Lachele Carl' Strength=2>
<Record Recommended='Gary Beach' Strength=2>
<Record Recommended='Eric Epstein' Strength=2>
<Record Recommended='John Carradine' Strength=2>
<Record Recommended='June Carryl' Strength=2>
<Record Recommended='Jordana Spiro' Strength=2>
<Record Recommended='Jochen Diestelmann' Strength=2>
<Record Recommended='Aviva' Strength=2>
<Record Recommended='Joe Pontillo' Strength=2>
<Record Recommended='Vyacheslav Vinnik' Strength=2>
<Record Recommended='Troels Lyby' Strength=2>
<Record Recommended='Vince Desiderio' Strength=2>
<Record Recommended='Dallas Roberts' Strength=2>
<Record Recommended='Günter Naumann' Strength=2>
<Record Recommended='Sophia Loren' Strength=2>
<Record Recommended='James Cosmo' Strength=2>
<Record Recommended='Oliver Robins' Strength=2>
<Record Recommended='Kevin Breznahan' Strength=2>
<Record Recommended='Charlie Hofheimer' Strength=2>
<Record Recommended='Anna McNeely' Strength=2>
<Record Recommended='P.J. Soles' Strength=2>
<Record Recommended='Daniel Farber' Strength=2>
<Record Recommended='Mayim Bialik' Strength=2>
<Record Recommended='John Corbett' Strength=2>
<Record Recommended='Tina Holmes' Strength=2>
<Record Recommended='Enid Nelmes' Strength=2>
<Record Recommended='J. Anthony Brown' Strength=2>
<Record Recommended='Onalee Ames' Strength=2>
<Record Recommended='John Cariani' Strength=2>
<Record Recommended='Ice-T' Strength=2>
<Record Recommended='Gabriel Thomson' Strength=2>
<Record Recommended='Sheila Kelley' Strength=2>
<Record Recommended='Chris Kattan' Strength=2>
<Record Recommended='Joakim Nätterqvist' Strength=2>
<Record Recommended='Marsha Warfield' Strength=2>
<Record Recommended='Emilia Fox' Strength=2>
<Record Recommended='Paul Dinello' Strength=2>
<Record Recommended='Millie Perkins' Strength=2>
<Record Recommended='Michael Jai White' Strength=2>
<Record Recommended='Nacho Martínez' Strength=2>
<Record Recommended='Lucas Black' Strength=2>
<Record Recommended='Richard Harris' Strength=2>
<Record Recommended='Alex Datcher' Strength=2>
<Record Recommended='Bruce Nelson' Strength=2>
<Record Recommended='Badja Djola' Strength=2>
<Record Recommended='Deanna Oliver' Strength=2>
<Record Recommended='June Chadwick' Strength=2>
<Record Recommended='Sami Kirkpatrick' Strength=2>
<Record Recommended='Catalina Sandino Moreno' Strength=2>
<Record Recommended='Darryl Quon' Strength=2>
<Record Recommended='Michael Greene' Strength=2>
<Record Recommended='Dave Mallow' Strength=2>
<Record Recommended='Tony Hendra' Strength=2>
<Record Recommended='Frida Betrani' Strength=2>
<Record Recommended='Lorraine Bracco' Strength=2>
<Record Recommended='Kate Hardie' Strength=2>
<Record Recommended='James Coco' Strength=2>
<Record Recommended='Clovis Cornillac' Strength=2>
<Record Recommended='Rachel Covey' Strength=2>
<Record Recommended='Blake Woodruff' Strength=2>
<Record Recommended='Mark Christopher Lawrence' Strength=2>
<Record Recommended='Andrew Greenough' Strength=2>
<Record Recommended='Tony Randall' Strength=2>
<Record Recommended='Marcia Bennett' Strength=2>
<Record Recommended='Herbert Köfer' Strength=2>
<Record Recommended='Gates McFadden' Strength=2>
<Record Recommended='Josh Mostel' Strength=2>
<Record Recommended='John Nelles' Strength=2>
<Record Recommended='Lennie Huhtala' Strength=2>
<Record Recommended='Ernes Borgnine' Strength=2>
<Record Recommended='Maurice LaMarche' Strength=2>
<Record Recommended='Stephen McHattie' Strength=2>
<Record Recommended='Raquel Gavia' Strength=2>
<Record Recommended='Akbar Kurtha' Strength=2>
<Record Recommended='Rafael Osorio' Strength=2>
<Record Recommended='Sarah Thompson' Strength=2>
<Record Recommended='Tina Nguyen' Strength=2>
<Record Recommended='Danielle Harris' Strength=2>
<Record Recommended='Julie Halston' Strength=2>
<Record Recommended='Caroline Gray' Strength=2>
<Record Recommended='Bob Odenkirk' Strength=2>
<Record Recommended='Christina Milian' Strength=2>
<Record Recommended='Muriel Moore' Strength=2>
<Record Recommended="Austin O'Brien" Strength=2>
<Record Recommended='Rosemary Dunsmore' Strength=2>
<Record Recommended='Sarah Parish' Strength=2>
<Record Recommended='David Freiberg' Strength=2>
<Record Recommended="Patrick O'Neal" Strength=2>
<Record Recommended="Kel O'Neill" Strength=2>
<Record Recommended='Royce D. Applegate' Strength=2>
<Record Recommended='Daikon' Strength=2>
<Record Recommended='Zachary Mabry' Strength=2>
<Record Recommended='Jan Munroe' Strength=2>
<Record Recommended='Amanda Bynes' Strength=2>
<Record Recommended='Emma Campbell' Strength=2>
<Record Recommended='Andrew J. Lederer' Strength=2>
<Record Recommended='Mark Camacho' Strength=2>
<Record Recommended='Oleg Taktarov' Strength=2>
<Record Recommended='Sam Saletta' Strength=2>
<Record Recommended='Kristen Ruhlin' Strength=2>
<Record Recommended='Jan Niklas' Strength=2>
<Record Recommended='Antonio Zavala' Strength=2>
<Record Recommended='Peter Banks' Strength=2>
<Record Recommended='Aleta Barthell' Strength=2>
<Record Recommended='Isaac C. Singleton Jr.' Strength=2>
<Record Recommended='Brian Keith Gamble' Strength=2>
<Record Recommended='Victor Colicchio' Strength=2>
<Record Recommended='Nichole Hiltz' Strength=2>
<Record Recommended='Blackie Lawless' Strength=2>
<Record Recommended='Clark Sanchez' Strength=2>
<Record Recommended='Fred Armisen' Strength=2>
<Record Recommended='Harold Sylvester' Strength=2>
<Record Recommended='Robert Brown' Strength=2>
<Record Recommended='Daniel Gerroll' Strength=2>
<Record Recommended='Sara Botsford' Strength=2>
<Record Recommended='Robert Guillaume' Strength=2>
<Record Recommended='Jason Lewis' Strength=2>
<Record Recommended='William Hall Jr.' Strength=2>
<Record Recommended='David Hayward' Strength=2>
<Record Recommended='Tone Loc' Strength=2>
<Record Recommended='Kelly Bishop' Strength=2>
<Record Recommended='Sean Hayes' Strength=2>
<Record Recommended='Joshua Jackson' Strength=2>
<Record Recommended='David Gane' Strength=2>
<Record Recommended='Manoj Joshi' Strength=2>
<Record Recommended='Michael Hayden' Strength=2>
<Record Recommended='Alberto Reyes' Strength=2>
<Record Recommended='Vassar Clements' Strength=2>
<Record Recommended='Nona Gaye' Strength=2>
<Record Recommended='Nigel Linden' Strength=2>
<Record Recommended='Tyrone Henry' Strength=2>
<Record Recommended='Jase Blankfort' Strength=2>
<Record Recommended='Aaron Fors' Strength=2>
<Record Recommended='Jim Thorburn' Strength=2>
<Record Recommended='Wendy Phillips' Strength=2>
<Record Recommended='Michael Tucker' Strength=2>
<Record Recommended='Dominique Jackson' Strength=2>
<Record Recommended="Mike O'Malley" Strength=2>
<Record Recommended='George Takei' Strength=2>
<Record Recommended='Monika Ramnath' Strength=2>
<Record Recommended='Brooke Adams' Strength=2>
<Record Recommended='Norah Jones' Strength=2>
<Record Recommended='Stéphane Audran' Strength=2>
<Record Recommended='Andrew Secombe' Strength=2>
<Record Recommended='Jenny Agutter' Strength=2>
<Record Recommended='Declan Donnelly' Strength=2>
<Record Recommended='Jeffrey Broadhurst' Strength=2>
<Record Recommended='Erika Pelikowsky' Strength=2>
<Record Recommended="Keir O'Donnell" Strength=2>
<Record Recommended='John White' Strength=2>
<Record Recommended='Ian Charleson' Strength=2>
<Record Recommended='Gary Anthony Williams' Strength=2>
<Record Recommended='Yvonne Zima' Strength=2>
<Record Recommended='Sara Ramirez' Strength=2>
<Record Recommended='Eileen Essell' Strength=2>
<Record Recommended='Michael Potter' Strength=2>
<Record Recommended='Jean Champion' Strength=2>
<Record Recommended='Hannah Higgins' Strength=2>
<Record Recommended='Garth Pillsbury' Strength=2>
<Record Recommended='Jack Ong' Strength=2>
<Record Recommended='Vernon Chapman' Strength=2>
<Record Recommended='Valente Rodriguez' Strength=2>
<Record Recommended='Aunjanue Ellis' Strength=2>
<Record Recommended='Jason Hildebrandt' Strength=2>
<Record Recommended='Crystal Field' Strength=2>
<Record Recommended='Eva Blaylock' Strength=2>
<Record Recommended='Pell James' Strength=2>
<Record Recommended='Ben Walker' Strength=2>
<Record Recommended='Billy Ray Sharkey' Strength=2>
<Record Recommended='Bryn Dowling' Strength=2>
<Record Recommended='André Penvern' Strength=2>
<Record Recommended='John Doucette' Strength=2>
<Record Recommended='Sunny Johnson' Strength=2>
<Record Recommended='Mpho Koaho' Strength=2>
<Record Recommended="John F. O'Donohue" Strength=2>
<Record Recommended='Mel Winkler' Strength=2>
<Record Recommended='Irineo Alvarez' Strength=2>
<Record Recommended='Mariska Hargitay' Strength=2>
<Record Recommended='Malcolm-Jamal Warner' Strength=2>
<Record Recommended='Kurtwood Smith' Strength=2>
<Record Recommended='Rosel Zech' Strength=2>
<Record Recommended='Dato Bakhtadze' Strength=2>
<Record Recommended='Derek Kellock' Strength=2>
<Record Recommended='Philip Winchester' Strength=2>
<Record Recommended='Jorge Dallinger' Strength=2>
<Record Recommended='Sam Douglas' Strength=2>
<Record Recommended='Shelagh Fraser' Strength=2>
<Record Recommended='Angela Bettis' Strength=2>
<Record Recommended='Monica Liljistrand' Strength=2>
<Record Recommended='Sakina Jaffrey' Strength=2>
<Record Recommended='James Dan Calvert' Strength=2>
<Record Recommended='Billy Drago' Strength=2>
<Record Recommended='Yuriy Kutsenko' Strength=2>
<Record Recommended='Dakota Blue Richards' Strength=2>
<Record Recommended='Mia Kirshner' Strength=2>
<Record Recommended='Tony Lip' Strength=2>
<Record Recommended='Nestor Serrano' Strength=2>
<Record Recommended='Mary Crosby' Strength=2>
<Record Recommended='Badria Timimi' Strength=2>
<Record Recommended='Leonard Roberts' Strength=2>
<Record Recommended='Bob McDivitt' Strength=2>
<Record Recommended="Harry O'Reilly" Strength=2>
<Record Recommended='Jodi Benson' Strength=2>
<Record Recommended='Alex Borstein' Strength=2>
<Record Recommended='Jason London' Strength=2>
<Record Recommended='Michael Badalucco' Strength=2>
<Record Recommended='Robert Page' Strength=2>
<Record Recommended='Ashley Walters' Strength=2>
<Record Recommended='Warren Takeuchi' Strength=2>
<Record Recommended='Jackie Mason' Strength=2>
<Record Recommended='Kathleen Barr' Strength=2>
<Record Recommended='Tony Curtis' Strength=2>
<Record Recommended='Katt Williams' Strength=2>
<Record Recommended='Kylie Minogue' Strength=2>
<Record Recommended='David McIlwraith' Strength=2>
<Record Recommended='Katarina Witt' Strength=2>
<Record Recommended='Jake T. Roberts' Strength=2>
<Record Recommended='Monet Mazur' Strength=2>
<Record Recommended='Stevie Parry' Strength=2>
<Record Recommended='Kate Bosworth' Strength=2>
<Record Recommended='Gael García Bernal' Strength=2>
<Record Recommended='Martin Klebba' Strength=2>
<Record Recommended='Jay Brazeau' Strength=2>
<Record Recommended='Dey Young' Strength=2>
<Record Recommended='Diane Delano' Strength=2>
<Record Recommended='Gary Stevens' Strength=2>
<Record Recommended='Terence Alexander' Strength=2>
<Record Recommended='Paris Hilton' Strength=2>
<Record Recommended='Maya Zapata' Strength=2>
<Record Recommended='Titus Welliver' Strength=2>
<Record Recommended='Craig March' Strength=2>
<Record Recommended='Daniel Clark' Strength=2>
<Record Recommended='Remo Girone' Strength=2>
<Record Recommended='Christian Berkel' Strength=2>
<Record Recommended='Tom Amandes' Strength=2>
<Record Recommended='Stacey Pickren' Strength=2>
<Record Recommended="Charles 'Tatoo' Jensen" Strength=2>
<Record Recommended='Jill Ireland' Strength=2>
<Record Recommended='Kazuyoshi Minamimagoe' Strength=2>
<Record Recommended='Ed Stoppard' Strength=2>
<Record Recommended='India Ennenga' Strength=2>
<Record Recommended='Asia Argento' Strength=2>
<Record Recommended='Tamara Hope' Strength=2>
<Record Recommended='Isabelle Adjani' Strength=2>
<Record Recommended='Nestor Carbonell' Strength=2>
<Record Recommended='Todd Allen' Strength=2>
<Record Recommended='Ben Shenkman' Strength=2>
<Record Recommended='Ticky Holgado' Strength=2>
<Record Recommended='Keke Palmer' Strength=2>
<Record Recommended='Tina Fey' Strength=2>
<Record Recommended='Dan van Husen' Strength=2>
<Record Recommended='Joel Leffert' Strength=2>
<Record Recommended='Peter Gunn' Strength=2>
<Record Recommended='Yancy Butler' Strength=2>
<Record Recommended='Richard Briers' Strength=2>
<Record Recommended='Tresa Hughes' Strength=2>
<Record Recommended='Priyanka Chopra' Strength=2>
<Record Recommended='Brent Barrett' Strength=2>
<Record Recommended='Patty Maloney' Strength=2>
<Record Recommended='Orville Hallberg' Strength=2>
<Record Recommended='Rebecca Pidgeon' Strength=2>
<Record Recommended='Catherine Dent' Strength=2>
<Record Recommended='Arlin Miller' Strength=2>
<Record Recommended='Matthias Hues' Strength=2>
<Record Recommended='Hugh Ross' Strength=2>
<Record Recommended='Douglas Brian Martin' Strength=2>
<Record Recommended='Roberta Leighton' Strength=2>
<Record Recommended='Colette Brown' Strength=2>
<Record Recommended='Lubomir Mykytiuk' Strength=2>
<Record Recommended='Ronald Lacey' Strength=2>
<Record Recommended='Patrika Darbo' Strength=2>
<Record Recommended='Elizabeth Ann Feeley' Strength=2>
<Record Recommended='Norbert Christian' Strength=2>
<Record Recommended='Geraldine Fitzgerald' Strength=2>
<Record Recommended='Bob Newhart' Strength=2>
<Record Recommended='Tapp Watkins' Strength=2>
<Record Recommended='Spencer Wilding' Strength=2>
<Record Recommended='Stephen Mendillo' Strength=2>
<Record Recommended='Fred Dalton Thompson' Strength=2>
<Record Recommended='Trieu Tran' Strength=2>
<Record Recommended='Joseph Whipp' Strength=2>
<Record Recommended='Harry Basil' Strength=2>
<Record Recommended='Vladica Kostic' Strength=2>
<Record Recommended='David Alpay' Strength=2>
<Record Recommended='Jack Murdock' Strength=2>
<Record Recommended='Nancy Anne Ridder' Strength=2>
<Record Recommended='Mimi Craven' Strength=2>
<Record Recommended='Glynis Johns' Strength=2>
<Record Recommended='James LeGros' Strength=2>
<Record Recommended='Tony Lo Bianco' Strength=2>
<Record Recommended='Mike Schank' Strength=2>
<Record Recommended='Stephan Jones' Strength=2>
<Record Recommended='Paz de la Huerta' Strength=2>
<Record Recommended='Niklas Konowal' Strength=2>
<Record Recommended='John Ireland' Strength=2>
<Record Recommended='Todd Sherry' Strength=2>
<Record Recommended='Barry Flatman' Strength=2>
<Record Recommended='Lonny Price' Strength=2>
<Record Recommended='Aidan Gould' Strength=2>
<Record Recommended='Sean Salisbury' Strength=2>
<Record Recommended='Cindy Carver' Strength=2>
<Record Recommended='Alexis Dziena' Strength=2>
<Record Recommended='David La Haye' Strength=2>
<Record Recommended='Kerry Fox' Strength=2>
<Record Recommended='Miko Hughes' Strength=2>
<Record Recommended='Carolyn Horwitz' Strength=2>
<Record Recommended='Mark Engelhardt' Strength=2>
<Record Recommended='Adam Garcia' Strength=2>
<Record Recommended='Helen Merino' Strength=2>
<Record Recommended='Roberto Sosa' Strength=2>
<Record Recommended='Terry Chen' Strength=2>
<Record Recommended='Hale Appleman' Strength=2>
<Record Recommended='Faizon Love' Strength=2>
<Record Recommended='Rosanna DeSoto' Strength=2>
<Record Recommended='Bruno Cremer' Strength=2>
<Record Recommended='Carla Meyer' Strength=2>
<Record Recommended='Dolph Lundgren' Strength=2>
<Record Recommended='Brittany Ashton Holmes' Strength=2>
<Record Recommended='Cécile De France' Strength=2>
<Record Recommended='Scott L. Schwartz' Strength=2>
<Record Recommended='Lauren Hasson' Strength=2>
<Record Recommended='Creagen Dow' Strength=2>
<Record Recommended='Christopher Castile' Strength=2>
<Record Recommended='Philip Granger' Strength=2>
<Record Recommended='Nichelle Nichols' Strength=2>
<Record Recommended='Domenic Bove' Strength=2>
<Record Recommended='Jimmi Simpson' Strength=2>
<Record Recommended='Ali Suliman' Strength=2>
<Record Recommended='Tony Darrow' Strength=2>
<Record Recommended='Kimberly Stringer' Strength=2>
<Record Recommended='Julie Gawkowski' Strength=2>
<Record Recommended='Sharon Barr' Strength=2>
<Record Recommended='Kathryn Meisle' Strength=2>
<Record Recommended='Meat Loaf' Strength=2>
<Record Recommended='Sophie Rois' Strength=2>
<Record Recommended='Ena Cohen' Strength=2>
<Record Recommended='Aaron Himelstein' Strength=2>
<Record Recommended='Roy Costley' Strength=2>
<Record Recommended='Colin Salmon' Strength=2>
<Record Recommended='Sala Baker' Strength=2>
<Record Recommended='Lisa De Leeuw' Strength=2>
<Record Recommended='Robert Wagner' Strength=2>
<Record Recommended='Aonghus Og McAnally' Strength=2>
<Record Recommended='Jonnie Barnett' Strength=2>
<Record Recommended='Micheline Presle' Strength=2>
<Record Recommended='David Soul' Strength=2>
<Record Recommended='Tory Ross' Strength=2>
<Record Recommended='G.W. Bailey' Strength=2>
<Record Recommended='Barbara Hamilton' Strength=2>
<Record Recommended='Chelsea Field' Strength=2>
<Record Recommended='Elizabeth Rodriguez' Strength=2>
<Record Recommended='Tim Conway' Strength=2>
<Record Recommended='Giacomo Baessato' Strength=2>
<Record Recommended='Graham Jarvis' Strength=2>
<Record Recommended='Sal Viscuso' Strength=2>
<Record Recommended='Chynna Phillips' Strength=2>
<Record Recommended='Kathy Burke' Strength=2>
<Record Recommended='Michael Patrick Carter' Strength=2>
<Record Recommended='Duke Stroud' Strength=2>
<Record Recommended='Burgess Meredith' Strength=2>
<Record Recommended='Erik Stolhanske' Strength=2>
<Record Recommended='Bradley Lavelle' Strength=2>
<Record Recommended='Götz Otto' Strength=2>
<Record Recommended='Michael Cochrane' Strength=2>
<Record Recommended='Mark Pellegrino' Strength=2>
<Record Recommended='Peter Appel' Strength=2>
<Record Recommended='Kazuko Shibata' Strength=2>
<Record Recommended='Bryon P. Caunar' Strength=2>
<Record Recommended='Denholm Elliott' Strength=2>
<Record Recommended='Jessica Bowman' Strength=2>
<Record Recommended='Solbjørg Højfeldt' Strength=2>
<Record Recommended='Heathcote Williams' Strength=2>
<Record Recommended='Joe Unger' Strength=2>
<Record Recommended='Jenna Stern' Strength=2>
<Record Recommended='Cristina Piaget' Strength=2>
<Record Recommended='Kristy Swanson' Strength=2>
<Record Recommended="Jay Laga'aia" Strength=2>
<Record Recommended='Ray Wills' Strength=2>
<Record Recommended='Daniel Butler' Strength=2>
<Record Recommended='Mark Hall' Strength=2>
<Record Recommended='Walter Lendrich' Strength=2>
<Record Recommended='Montgomery John' Strength=2>
<Record Recommended='Robert Haley' Strength=2>
<Record Recommended='Lily Cole' Strength=2>
<Record Recommended='Marlon Wayans' Strength=2>
<Record Recommended='Don Harvey' Strength=2>
<Record Recommended='Steve Reevis' Strength=2>
<Record Recommended='Sabine Karsenti' Strength=2>
<Record Recommended='Carol McGinnis' Strength=2>
<Record Recommended='Juliette Brewer' Strength=2>
<Record Recommended='Ron Livingston' Strength=2>
<Record Recommended='Evangeline Lilly' Strength=2>
<Record Recommended='Lee Ingleby' Strength=2>
<Record Recommended='Bill McKinney' Strength=2>
<Record Recommended='Rick Ravanello' Strength=2>
<Record Recommended='Jimmy Noonan' Strength=2>
<Record Recommended='Aaron Stanford' Strength=2>
<Record Recommended='Lou Hancock' Strength=2>
<Record Recommended='Gert Fröbe' Strength=2>
<Record Recommended='Paul Birchard' Strength=2>
<Record Recommended='Ivette Soler' Strength=2>
<Record Recommended='Alexandra Fong' Strength=2>
<Record Recommended='Gill Gayle' Strength=2>
<Record Recommended='Hannah Mazodier' Strength=2>
<Record Recommended='Franka Potente' Strength=2>
<Record Recommended='Eddie J. Fernandez' Strength=2>
<Record Recommended='Izabella Scorupco' Strength=2>
<Record Recommended='Kristen Bone' Strength=2>
<Record Recommended='Peter Anthony Tambakis' Strength=2>
<Record Recommended='Louis Lombardi' Strength=2>
<Record Recommended='Jimi Mistry' Strength=2>
<Record Recommended='Fritz Wepper' Strength=2>
<Record Recommended='Zoë Kravitz' Strength=2>
<Record Recommended='Andy Beckwith' Strength=2>
<Record Recommended='Claire Stansfield' Strength=2>
<Record Recommended='Patrick Wilson' Strength=2>
<Record Recommended='Mickey Rooney' Strength=2>
<Record Recommended='Miguel Nino' Strength=2>
<Record Recommended='Andrea Shawcross' Strength=2>
<Record Recommended='Marie-Anne Chazel' Strength=2>
<Record Recommended='Sarah Lafleur' Strength=2>
<Record Recommended='Callie Anne Morgan' Strength=2>
<Record Recommended='Ben Savage' Strength=2>
<Record Recommended='Robert Shaw' Strength=2>
<Record Recommended='Conrad Vernon' Strength=2>
<Record Recommended='Ricki Lake' Strength=2>
<Record Recommended='Russ Meyer' Strength=2>
<Record Recommended='John Corvello' Strength=2>
<Record Recommended='Robert Pugh' Strength=2>
<Record Recommended='Treva Etienne' Strength=2>
<Record Recommended='Stephanie Sawyer' Strength=2>
<Record Recommended='Paul Gale' Strength=2>
<Record Recommended='Dan Washington' Strength=2>
<Record Recommended='Rhiana Griffith' Strength=2>
<Record Recommended='Fumihiro Hayashi' Strength=2>
<Record Recommended='Anton Rodgers' Strength=2>
<Record Recommended='Bill McGough' Strength=2>
<Record Recommended='John Cho' Strength=2>
<Record Recommended='Denis Conway' Strength=2>
<Record Recommended='A.J. Balance' Strength=2>
<Record Recommended='Jay Hernandez' Strength=2>
<Record Recommended='Ray Harryhausen' Strength=2>
<Record Recommended='Matt Clark' Strength=2>
<Record Recommended='Archie Panjabi' Strength=2>
<Record Recommended='David Zayas' Strength=2>
<Record Recommended='Eddie Jones' Strength=2>
<Record Recommended='Daniel Zacapa' Strength=2>
<Record Recommended='Stefan Gierasch' Strength=2>
<Record Recommended='Susannah York' Strength=2>
<Record Recommended='Shelby Hoffman' Strength=2>
<Record Recommended='Ky-Mani Marley' Strength=2>
<Record Recommended='Andrew Jackson' Strength=2>
<Record Recommended='Ulf Pilgaard' Strength=2>
<Record Recommended='Gary Cervantes' Strength=2>
<Record Recommended='Mark McConchie' Strength=2>
<Record Recommended='Daeg Faerch' Strength=2>
<Record Recommended='Hubert Saint-Macary' Strength=2>
<Record Recommended='Rawle D. Lewis' Strength=2>
<Record Recommended='Sharon Clark' Strength=2>
<Record Recommended='Grant Gelt' Strength=2>
<Record Recommended='Kyle Secor' Strength=2>
<Record Recommended='Thomas F. Wilson' Strength=2>
<Record Recommended='Loretta Devine' Strength=2>
<Record Recommended='Ina Barron' Strength=2>
<Record Recommended='Janet McTeer' Strength=2>
<Record Recommended='Edward Entero Chey' Strength=2>
<Record Recommended='William Hootkins' Strength=2>
<Record Recommended='Georges Claisse' Strength=2>
<Record Recommended='Michael Beattie' Strength=2>
<Record Recommended='Oscar Nuñez' Strength=2>
<Record Recommended='Joyce Hyser' Strength=2>
<Record Recommended='Christopher Murray' Strength=2>
<Record Recommended='Eric Bogosian' Strength=2>
<Record Recommended='Gillian Goodman' Strength=2>
<Record Recommended='James Ransone' Strength=2>
<Record Recommended='Myke R. Mueller' Strength=2>
<Record Recommended='Rachel Mittelman' Strength=2>
<Record Recommended='Walter Burke' Strength=2>
<Record Recommended='Travis Champagne' Strength=2>
<Record Recommended='Carolyn Saxon' Strength=2>
<Record Recommended='Bryan Genesse' Strength=2>
<Record Recommended='Brandon Smith' Strength=2>
<Record Recommended='Mariel Hemingway' Strength=2>
<Record Recommended='Peter Lawford' Strength=2>
<Record Recommended='Michael Ian Black' Strength=2>
<Record Recommended='Forrest Fyre' Strength=2>
<Record Recommended='Joseph McKenna' Strength=2>
<Record Recommended='Diane Bradley' Strength=2>
<Record Recommended='Rachel Ward' Strength=2>
<Record Recommended='Jon Stafford' Strength=2>
<Record Recommended='David Bowie' Strength=2>
<Record Recommended='Lochlyn Munro' Strength=2>
<Record Recommended='Julia Bridgeman' Strength=2>
<Record Recommended='Toby Kebbell' Strength=2>
<Record Recommended='Jonah Blechman' Strength=2>
<Record Recommended='Christine Taylor' Strength=2>
<Record Recommended='Princess Livingston' Strength=2>
<Record Recommended='Gérard Desarthe' Strength=2>
<Record Recommended='Kelly Sheridan' Strength=2>
<Record Recommended='David Gwillim' Strength=2>
<Record Recommended='Jorge Robles' Strength=2>
<Record Recommended='Stephanie Belding' Strength=2>
<Record Recommended='Daniel Dae Kim' Strength=2>
<Record Recommended='Darlene Hunt' Strength=2>
<Record Recommended='Di Quon' Strength=2>
<Record Recommended='Chris McCarron' Strength=2>
<Record Recommended='J. Michael Moncrief' Strength=2>
<Record Recommended='Jared Padalecki' Strength=2>
<Record Recommended='James Rothenberg' Strength=2>
<Record Recommended='Daniel Enright' Strength=2>
<Record Recommended='Bert Matias' Strength=2>
<Record Recommended='Herbert Lom' Strength=2>
<Record Recommended='Malcolm Cousins' Strength=2>
<Record Recommended='Richard Lintern' Strength=2>
<Record Recommended='George Cole' Strength=2>
<Record Recommended='Denise Faye' Strength=2>
<Record Recommended='Dee Bradley Baker' Strength=2>
<Record Recommended='Malachi Pearson' Strength=2>
<Record Recommended='Elizabeth Daily' Strength=2>
<Record Recommended='Line Kruse' Strength=2>
<Record Recommended='Cyril Couton' Strength=2>
<Record Recommended='Rachel York' Strength=2>
<Record Recommended='Laurine Towler' Strength=2>
<Record Recommended='Ian Tracey' Strength=2>
<Record Recommended='Diego Sieres' Strength=2>
<Record Recommended='María Barranco' Strength=2>
<Record Recommended='Morgan Alling' Strength=2>
<Record Recommended='Zaide Silvia Gutiérrez' Strength=2>
<Record Recommended='T. Robert Pigott' Strength=2>
<Record Recommended='Everett McGill' Strength=2>
<Record Recommended='Jason Weaver' Strength=2>
<Record Recommended='Victoria Abril' Strength=2>
<Record Recommended='Jeffrey Donovan' Strength=2>
<Record Recommended='William B. Davis' Strength=2>
<Record Recommended='Sarah Douglas' Strength=2>
<Record Recommended='Grace Kelly' Strength=2>
<Record Recommended='Alan Autry' Strength=2>
<Record Recommended='Derrick Bridgeman' Strength=2>
<Record Recommended='Rufus' Strength=2>
<Record Recommended='Christian Mills' Strength=2>
<Record Recommended='Andrea Bogart' Strength=2>
<Record Recommended='Kim Robillard' Strength=2>
<Record Recommended='Michael Rosenbaum' Strength=2>
<Record Recommended='André Maranne' Strength=2>
<Record Recommended='Dominic Scott Kay' Strength=2>
<Record Recommended='Grant Monohon' Strength=2>
<Record Recommended='Wilmer Valderrama' Strength=2>
<Record Recommended="Rodney 'Bear' Jackson" Strength=2>
<Record Recommended='Adrian Alonso' Strength=2>
<Record Recommended='Luce Rains' Strength=2>
<Record Recommended='Frank B. Moore' Strength=2>
<Record Recommended='Taso Papadakis' Strength=2>
<Record Recommended='Ted Monte' Strength=2>
<Record Recommended='Dina Merrill' Strength=2>
<Record Recommended='Karl Geary' Strength=2>
<Record Recommended='Leonard Jackson' Strength=2>
<Record Recommended='Rosa Blasi' Strength=2>
<Record Recommended='Eric Allan Kramer' Strength=2>
<Record Recommended='François Cluzet' Strength=2>
<Record Recommended='Bobby Di Cicco' Strength=2>
<Record Recommended='Nicholas Ballas' Strength=2>
<Record Recommended='Brian Murray' Strength=2>
<Record Recommended='Rochelle Kennedy' Strength=2>
<Record Recommended='Gloria Reuben' Strength=2>
<Record Recommended='Joey Ansah' Strength=2>
<Record Recommended='Richard S. Brummer' Strength=2>
<Record Recommended='Lake Bell' Strength=2>
<Record Recommended='Angela Elayne Gibbs' Strength=2>
<Record Recommended='Robin Soans' Strength=2>
<Record Recommended='Clarice F. Geigerman' Strength=2>
<Record Recommended='Ralph Bellamy' Strength=2>
<Record Recommended="Sean O'Bryan" Strength=2>
<Record Recommended='Stephanie Stromer' Strength=2>
<Record Recommended='Shaun Phillips' Strength=2>
<Record Recommended='Jackie Chan' Strength=2>
<Record Recommended='Colin Mochrie' Strength=2>
<Record Recommended='Ray Stevenson' Strength=2>
<Record Recommended='Olivia Hayman' Strength=2>
<Record Recommended='André Dussollier' Strength=2>
<Record Recommended='Larry Thomas' Strength=2>
<Record Recommended='Daisy Tormé' Strength=2>
<Record Recommended='Russell Wong' Strength=2>
<Record Recommended='Anna Chlumsky' Strength=2>
<Record Recommended='Karen Austin' Strength=2>
<Record Recommended='David Ferguson' Strength=2>
<Record Recommended='Bret Loehr' Strength=2>
<Record Recommended='Naima Belkhiati' Strength=2>
<Record Recommended='Joanne Rodriguez' Strength=2>
<Record Recommended='Lynne Cormack' Strength=2>
<Record Recommended='Sharon Brathwaite-Sanders' Strength=2>
<Record Recommended='Tyler Perry' Strength=2>
<Record Recommended='Takako Fuji' Strength=2>
<Record Recommended='Christine Cavanaugh' Strength=2>
<Record Recommended='Phil Brown' Strength=2>
<Record Recommended='David Oyelowo' Strength=2>
<Record Recommended='James Mason' Strength=2>
<Record Recommended='Johnny Simmons' Strength=2>
<Record Recommended='Claude Dauphin' Strength=2>
<Record Recommended='Sarah-Jane Potts' Strength=2>
<Record Recommended='Terence Bernie Hines' Strength=2>
<Record Recommended='Annie McEnroe' Strength=2>
<Record Recommended='Ryan Miranda' Strength=2>
<Record Recommended='Ellen Greene' Strength=2>
<Record Recommended='Jimmy Workman' Strength=2>
<Record Recommended='Maya Angelou' Strength=2>
<Record Recommended='Teala Dunn' Strength=2>
<Record Recommended='Ornella Muti' Strength=2>
<Record Recommended='Shan Omar Huey' Strength=2>
<Record Recommended='Steve Kahan' Strength=2>
<Record Recommended='Marty Balin' Strength=2>
<Record Recommended='Lee Majors' Strength=2>
<Record Recommended='Helen Slayton-Hughes' Strength=2>
<Record Recommended='Carolyn Dando' Strength=2>
<Record Recommended='Fernando Guillén' Strength=2>
<Record Recommended='Shari Hall' Strength=2>
<Record Recommended='Woodrow Parfrey' Strength=2>
<Record Recommended='Donald Sumpter' Strength=2>
<Record Recommended='Adoni Maropis' Strength=2>
<Record Recommended='Ellen Pompeo' Strength=2>
<Record Recommended='Dolores Duffy' Strength=2>
<Record Recommended='Althea Currier' Strength=2>
<Record Recommended='Park Bench' Strength=2>
<Record Recommended='Darko Cesar' Strength=2>
<Record Recommended='Sarah Lord' Strength=2>
<Record Recommended='Fisher Stevens' Strength=2>
<Record Recommended='Lars Michael Dinesen' Strength=2>
<Record Recommended='Jonathan Coy' Strength=2>
<Record Recommended='Angie Dickinson' Strength=2>
<Record Recommended='Ariel Waller' Strength=2>
<Record Recommended='Emma Rose Lima' Strength=2>
<Record Recommended='Heather Burns' Strength=2>
<Record Recommended='Sam McMurray' Strength=2>
<Record Recommended='Kevin G. Schmidt' Strength=2>
<Record Recommended='Cat Power' Strength=2>
<Record Recommended="Heather O'Rourke" Strength=2>
<Record Recommended='Max Casella' Strength=2>
<Record Recommended='Bruce Boa' Strength=2>
<Record Recommended='Katrine Falkenberg' Strength=2>
<Record Recommended='Elle Macpherson' Strength=2>
<Record Recommended='Tim Halligan' Strength=2>
<Record Recommended='James Coleman' Strength=2>
<Record Recommended='Kellie Waymire' Strength=2>
<Record Recommended='Robert Miano' Strength=2>
<Record Recommended='Chad Everett' Strength=2>
<Record Recommended='Daniel Studi' Strength=2>
<Record Recommended='Jim Jarmusch' Strength=2>
<Record Recommended='Alyson Stoner' Strength=2>
<Record Recommended='Bryan Brown' Strength=2>
<Record Recommended='Grant Shaud' Strength=2>
<Record Recommended='Chandra Wilson' Strength=2>
<Record Recommended='Jerry Minor' Strength=2>
<Record Recommended='Jake T. Austin' Strength=2>
<Record Recommended='Janie Draper' Strength=2>
<Record Recommended='Zelda Rubinstein' Strength=2>
<Record Recommended='Jean Dasté' Strength=2>
<Record Recommended='Ian Richardson' Strength=2>
<Record Recommended='David Schwimmer' Strength=2>
<Record Recommended='Bent Mejding' Strength=2>
<Record Recommended='Meg Gillentine' Strength=2>
<Record Recommended='Sam Josepher' Strength=2>
<Record Recommended='Desreta Jackson' Strength=2>
<Record Recommended='Dave Peel' Strength=2>
<Record Recommended='Roger Corman' Strength=2>
<Record Recommended='Waris Ahluwalia' Strength=2>
<Record Recommended='Diane Baker' Strength=2>
<Record Recommended='Anthony Jordan Atler' Strength=2>
<Record Recommended='Morgan Woodward' Strength=2>
<Record Recommended='Phyllida Law' Strength=2>
<Record Recommended='Lyle Alzado' Strength=2>
<Record Recommended='Brendan Sexton III' Strength=2>
<Record Recommended='Katy Jurado' Strength=2>
<Record Recommended='Jeff Altman' Strength=2>
<Record Recommended='Gregory Jbara' Strength=2>
<Record Recommended='Michael D. Roberts' Strength=2>
<Record Recommended='Paul Sorvino' Strength=2>
<Record Recommended='John Burton Jr.' Strength=2>
<Record Recommended='Henry Cavill' Strength=2>
<Record Recommended='Take' Strength=2>
<Record Recommended='Rockets Redglare' Strength=2>
<Record Recommended='Josh Strait' Strength=2>
<Record Recommended='Desmond Dube' Strength=2>
<Record Recommended='Jim McKrell' Strength=2>
<Record Recommended='Kaitlin Hopkins' Strength=2>
<Record Recommended='Jenny Seagrove' Strength=2>
<Record Recommended='Joe Hart' Strength=2>
<Record Recommended='Benedict Wong' Strength=2>
<Record Recommended='Lorna Patterson' Strength=2>
<Record Recommended='Phil Collins' Strength=2>
<Record Recommended='Bobby Coleman' Strength=2>
<Record Recommended='Jason Miller' Strength=2>
<Record Recommended='Matt Weinberg' Strength=2>
<Record Recommended='Leo Fuchs' Strength=2>
<Record Recommended='Ray Nicholson' Strength=2>
<Record Recommended='Uwe Ochsenknecht' Strength=2>
<Record Recommended='Angus Barnett' Strength=2>
<Record Recommended='Alexander Godunov' Strength=2>
<Record Recommended='Eileen Pedde' Strength=2>
<Record Recommended='Bikram Singh Bhamra' Strength=2>
<Record Recommended='Christian Tessier' Strength=2>
<Record Recommended='Bumper Robinson' Strength=2>
<Record Recommended='Vincent Laresca' Strength=2>
<Record Recommended='Moira Harris' Strength=2>
<Record Recommended='Vyto Ruginis' Strength=2>
<Record Recommended='Carmen Argenziano' Strength=2>
<Record Recommended='Dave Sheridan' Strength=2>
<Record Recommended='Michael Edwards' Strength=2>
<Record Recommended='Deena Fontaine' Strength=2>
<Record Recommended='Forrest Landis' Strength=2>
<Record Recommended='Stephen Fry' Strength=2>
<Record Recommended='Troy Beyer' Strength=2>
<Record Recommended='Michael Flessas' Strength=2>
<Record Recommended='Benjamin Mouton' Strength=2>
<Record Recommended='Brian Posehn' Strength=2>
<Record Recommended='Ed Westwick' Strength=2>
<Record Recommended='Dana Tyler' Strength=2>
<Record Recommended="Matt O'Toole" Strength=2>
<Record Recommended='Larry Gilman' Strength=2>
<Record Recommended='Richard Lee-Sung' Strength=2>
<Record Recommended='Val Avery' Strength=2>
<Record Recommended='Paul Frees' Strength=2>
<Record Recommended='Steve Kroft' Strength=2>
<Record Recommended='Paul Schneider' Strength=2>
<Record Recommended='Anita Gillette' Strength=2>
<Record Recommended='Andrew Weems' Strength=2>
<Record Recommended='Richard Lawson' Strength=2>
<Record Recommended='George Coe' Strength=2>
<Record Recommended='Keri Lynn Pratt' Strength=2>
<Record Recommended='Adriana Yanez' Strength=2>
<Record Recommended='Cassandra Freeman' Strength=2>
<Record Recommended='Kate Jackson' Strength=2>
<Record Recommended='Zach Tyler' Strength=2>
<Record Recommended='Jeff LeBeau' Strength=2>
<Record Recommended='Caroline Dhavernas' Strength=2>
<Record Recommended='Mac Miller' Strength=2>
<Record Recommended='Spencer Fox' Strength=2>
<Record Recommended='Hector Atreyu Ruiz' Strength=2>
<Record Recommended='Victor Pagan' Strength=2>
<Record Recommended='Stephen Graham' Strength=2>
<Record Recommended='Haing S. Ngor' Strength=2>
<Record Recommended='Alan North' Strength=2>
<Record Recommended='E.R. Davies' Strength=2>
<Record Recommended='Shay Roundtree' Strength=2>
<Record Recommended='Billy Barty' Strength=2>
<Record Recommended='Brittany Robertson' Strength=2>
<Record Recommended='Melina Kanakaredes' Strength=2>
<Record Recommended='Richard Baskin' Strength=2>
<Record Recommended='Ned Dennehy' Strength=2>
<Record Recommended='Aaron Abrams' Strength=2>
<Record Recommended='Mark Brandon Read' Strength=2>
<Record Recommended='Bibi Andersson' Strength=2>
<Record Recommended='Beau Bridges' Strength=2>
<Record Recommended='David Threlfall' Strength=2>
<Record Recommended='Geoffrey Blake' Strength=2>
<Record Recommended='Jennifer Pisana' Strength=2>
<Record Recommended='Ruth Lawlor' Strength=2>
<Record Recommended='Marcus Powell' Strength=2>
<Record Recommended='Charles Q. Murphy' Strength=2>
<Record Recommended='Skyler Gisondo' Strength=2>
<Record Recommended='Alan Fawcett' Strength=2>
<Record Recommended='Michael Mosley' Strength=2>
<Record Recommended='Don Francks' Strength=2>
<Record Recommended='Augustin Legrand' Strength=2>
<Record Recommended='Rosie Perez' Strength=2>
<Record Recommended='Christina Souza' Strength=2>
<Record Recommended='Steve Speirs' Strength=2>
<Record Recommended='Sam Bottoms' Strength=2>
<Record Recommended='Rick Overton' Strength=2>
<Record Recommended='Annekathrin Bürger' Strength=2>
<Record Recommended='Hugo Perez' Strength=2>
<Record Recommended='Jamie Foreman' Strength=2>
<Record Recommended='Penn Jillette' Strength=2>
<Record Recommended='Judith Malina' Strength=2>
<Record Recommended='Jonathan Harris' Strength=2>
<Record Recommended='Carmine Giovinazzo' Strength=2>
<Record Recommended='Nathan Lee Chasing His Horse' Strength=2>
<Record Recommended='Jurnee Smollett' Strength=2>
<Record Recommended='Jennifer Clement' Strength=2>
<Record Recommended='Anthony Russell' Strength=2>
<Record Recommended='Barbara Baxley' Strength=2>
<Record Recommended='Jean-Pierre Kalfon' Strength=2>
<Record Recommended='Michele Mariana' Strength=2>
<Record Recommended='Gwen Verdon' Strength=2>
<Record Recommended='Edward Bunker' Strength=2>
<Record Recommended='Karina Arroyave' Strength=2>
<Record Recommended='Michael Colyar' Strength=2>
<Record Recommended='Peter Jackson' Strength=2>
<Record Recommended='Danny Goldring' Strength=2>
<Record Recommended='Poppy Rogers' Strength=2>
<Record Recommended='Angeline Ball' Strength=2>
<Record Recommended='Andrew Dougherty' Strength=2>
<Record Recommended='Patrick Bergin' Strength=2>
<Record Recommended='Joe Anderson' Strength=2>
<Record Recommended='Benita Ha' Strength=2>
<Record Recommended='Jack Rader' Strength=2>
<Record Recommended='David Call' Strength=2>
<Record Recommended='Yûichi Sugiyama' Strength=2>
<Record Recommended='Melora Hardin' Strength=2>
<Record Recommended='Lisa K. Wyatt' Strength=2>
<Record Recommended='Wazzan Troupe' Strength=2>
<Record Recommended='Mike Blakeley' Strength=2>
<Record Recommended='David Herlihy' Strength=2>
<Record Recommended='Ken Jenkins' Strength=2>
<Record Recommended='Paul Shenar' Strength=2>
<Record Recommended='Suzi Hofrichter' Strength=2>
<Record Recommended='Dave Colon' Strength=2>
<Record Recommended='Sheila Rosenthal' Strength=2>
<Record Recommended='Chris Ellis' Strength=2>
<Record Recommended='Jim Zulevic' Strength=2>
<Record Recommended='Barclay Hope' Strength=2>
<Record Recommended='Jean-Pierre Castaldi' Strength=2>
<Record Recommended='Ajay Naidu' Strength=2>
<Record Recommended='Kimberly Beck' Strength=2>
<Record Recommended='Kent Nolan' Strength=2>
<Record Recommended='Christine Schorn' Strength=2>
<Record Recommended='Lenn Kudrjawizki' Strength=2>
<Record Recommended='Anthony Heald' Strength=2>
<Record Recommended='Shahid Kapur' Strength=2>
<Record Recommended='Karen Allen' Strength=2>
<Record Recommended='Victor Rasuk' Strength=2>
<Record Recommended='Tony Curran' Strength=2>
<Record Recommended='Lady Chablis' Strength=2>
<Record Recommended='Deborah Harry' Strength=2>
<Record Recommended='Elisabeth Harnois' Strength=2>
<Record Recommended='Joe Viterelli' Strength=2>
<Record Recommended='Shohreh Aghdashloo' Strength=2>
<Record Recommended='Sanaa Lathan' Strength=2>
<Record Recommended='Esai Morales' Strength=2>
<Record Recommended='Adriano Giannini' Strength=2>
<Record Recommended='Stephen Boyd' Strength=2>
<Record Recommended='James Biberi' Strength=2>
<Record Recommended='Johnny Vegas' Strength=2>
<Record Recommended='RZA' Strength=2>
<Record Recommended='Tyreese Burnett' Strength=2>
<Record Recommended='Wendy Westerwelle' Strength=2>
<Record Recommended='Eve Gordon' Strength=2>
<Record Recommended='Jean Dujardin' Strength=2>
<Record Recommended='Nicholas Guest' Strength=2>
<Record Recommended='Paula Marshall' Strength=2>
<Record Recommended='Denis Mercier' Strength=2>
<Record Recommended='Jonathan Brandis' Strength=2>
<Record Recommended='Jim Abrahams' Strength=2>
<Record Recommended='Tony Hale' Strength=2>
<Record Recommended='Alexa Benedetti' Strength=2>
<Record Recommended='Yul Brynner' Strength=2>
<Record Recommended='Mark Polish' Strength=2>
<Record Recommended='Joe Lando' Strength=2>
<Record Recommended='Paul Kaye' Strength=2>
<Record Recommended='Robin Taylor' Strength=2>
<Record Recommended='John Saxon' Strength=2>
<Record Recommended='Jim Jackman' Strength=2>
<Record Recommended='Shaun Toub' Strength=2>
<Record Recommended='Jeffrey Carlson' Strength=2>
<Record Recommended='Cherilyn Hayres' Strength=2>
<Record Recommended='Louise Lombard' Strength=2>
<Record Recommended='Greg Bryk' Strength=2>
<Record Recommended='Paul Borghese' Strength=2>
<Record Recommended='Susan Norfleet' Strength=2>
<Record Recommended='Lisa Roberts Gillan' Strength=2>
<Record Recommended='Cameron Bright' Strength=2>
<Record Recommended='John Sayles' Strength=2>
<Record Recommended='Yasmin Paige' Strength=2>
<Record Recommended='Connor Fox' Strength=2>
<Record Recommended='Andrew Lawrence' Strength=2>
<Record Recommended='Cesar Flores' Strength=2>
<Record Recommended='Hiroko Kawasaki' Strength=2>
<Record Recommended='Matthew Blakeley' Strength=2>
<Record Recommended='Peter Strauss' Strength=2>
<Record Recommended='Ralph Richardson' Strength=2>
<Record Recommended='Claude Rich' Strength=2>
<Record Recommended='Harry Shannon' Strength=2>
<Record Recommended='Ron White' Strength=2>
<Record Recommended='Fionnula Flanagan' Strength=2>
<Record Recommended='David Brown' Strength=2>
<Record Recommended='Georg Marischka' Strength=2>
<Record Recommended='Mari Gorman' Strength=2>
<Record Recommended='Michael Berresse' Strength=2>
<Record Recommended='David Alan Grier' Strength=2>
<Record Recommended='Morgan York' Strength=2>
<Record Recommended='Sarah Thyre' Strength=2>
<Record Recommended='Sebastian Tillinger' Strength=2>
<Record Recommended='Guy Leverton' Strength=2>
<Record Recommended='Melonie Diaz' Strength=2>
<Record Recommended='Willis Bouchey' Strength=2>
<Record Recommended='Michael Hirsch' Strength=2>
<Record Recommended='Richard C. Sarafian' Strength=2>
<Record Recommended='Adrian Lester' Strength=2>
<Record Recommended='Annabella Sciorra' Strength=2>
<Record Recommended='Caroline Chikezie' Strength=2>
<Record Recommended='Geno Silva' Strength=2>
<Record Recommended='Tina Benko' Strength=2>
<Record Recommended='Moira Deady' Strength=2>
<Record Recommended='Stephen Young' Strength=2>
<Record Recommended='Christoph Bayertt' Strength=2>
<Record Recommended='Birgitte Hjort Sørensen' Strength=2>
<Record Recommended='Leo Rossi' Strength=2>
<Record Recommended='Rose Abdoo' Strength=2>
<Record Recommended='Tom Green' Strength=2>
<Record Recommended='Athol Fugard' Strength=2>
<Record Recommended='J. Evan Bonifant' Strength=2>
<Record Recommended='Jenette Goldstein' Strength=2>
<Record Recommended='Tyra Banks' Strength=2>
<Record Recommended='Clifton James' Strength=2>
<Record Recommended='Brian Part' Strength=2>
<Record Recommended='Roger Avary' Strength=2>
<Record Recommended='Meagen Fay' Strength=2>
<Record Recommended='Mette Berggreen' Strength=2>
<Record Recommended='Sandy Baron' Strength=2>
<Record Recommended='Sophie Marceau' Strength=2>
<Record Recommended='Nick Bakay' Strength=2>
<Record Recommended='Tane McClure' Strength=2>
<Record Recommended='Art Bonilla' Strength=2>
<Record Recommended='Lobo Sebastian' Strength=2>
<Record Recommended='Gabrielle Anwar' Strength=2>
<Record Recommended='Joseph Lawrence' Strength=2>
<Record Recommended='Cicely Tyson' Strength=2>
<Record Recommended='Gillian Jacobs' Strength=2>
<Record Recommended='Mark Hildreth' Strength=2>
<Record Recommended='Stacy Hogue' Strength=2>
<Record Recommended='Julien Frison' Strength=2>
<Record Recommended='Amr Waked' Strength=2>
<Record Recommended='Brian Tochi' Strength=2>
<Record Recommended='Ralph Riach' Strength=2>
<Record Recommended='Daniel J. Travanti' Strength=2>
<Record Recommended='Tom Courtenay' Strength=2>
<Record Recommended='Sid Haig' Strength=2>
<Record Recommended='Ron Carey' Strength=2>
<Record Recommended='Andrew Bryniarski' Strength=2>
<Record Recommended='Jerry Springer' Strength=2>
<Record Recommended='Dominic Cooper' Strength=2>
<Record Recommended='Dean Jones' Strength=2>
<Record Recommended='Raquel Welch' Strength=2>
<Record Recommended='Gerald Lenton-Young' Strength=2>
<Record Recommended='Julian Rhind-Tutt' Strength=2>
<Record Recommended='Rick Negron' Strength=2>
<Record Recommended='Idina Menzel' Strength=2>
<Record Recommended='Monte Landis' Strength=2>
<Record Recommended='Sheb Wooley' Strength=2>
<Record Recommended='Amanda Wyss' Strength=2>
<Record Recommended='Alexis Smith' Strength=2>
<Record Recommended='Luz Maria Molina' Strength=2>
<Record Recommended='Justin Bartha' Strength=2>
<Record Recommended='Leland Orser' Strength=2>
<Record Recommended='David Bowe' Strength=2>
<Record Recommended='Jenny Wade' Strength=2>
<Record Recommended='Christine Baranski' Strength=2>
<Record Recommended='Gary Cooper' Strength=2>
<Record Recommended='John Noble' Strength=2>
<Record Recommended='Eve McVeagh' Strength=2>
<Record Recommended='Gad Elmaleh' Strength=2>
<Record Recommended='Lawrence Howard Levy' Strength=2>
<Record Recommended='Guillaume Canet' Strength=2>
<Record Recommended='Kent McCord' Strength=2>
<Record Recommended='Colette Stevenson' Strength=2>
<Record Recommended='Keri Claussen' Strength=2>
<Record Recommended='Günther Maria Halmer' Strength=2>
<Record Recommended='Angayuqaq Oscar Kawagley' Strength=2>
<Record Recommended='Dee Snider' Strength=2>
<Record Recommended='Marga Legal' Strength=2>
<Record Recommended='Valentina Cortese' Strength=2>
<Record Recommended='Alison Pill' Strength=2>
<Record Recommended='Gloria Gifford' Strength=2>
<Record Recommended='Shane Rimmer' Strength=2>
<Record Recommended='Jason Bushman' Strength=2>
<Record Recommended='Jessie Flower' Strength=2>
<Record Recommended='Olivia Thirlby' Strength=2>
<Record Recommended='Yves Beneyton' Strength=2>
<Record Recommended='Charles G. Schelling' Strength=2>
<Record Recommended='Doug E. Doug' Strength=2>
<Record Recommended='John Cassini' Strength=2>
<Record Recommended='Helen Shaver' Strength=2>
<Record Recommended='Jose Pablo Cantillo' Strength=2>
<Record Recommended='Evan Sabara' Strength=2>
<Record Recommended='Allison McAtee' Strength=2>
<Record Recommended='Donald E. Jones' Strength=2>
<Record Recommended='Denis Lavant' Strength=2>
<Record Recommended='Jerry Reed' Strength=2>
<Record Recommended='John Robinson' Strength=2>
<Record Recommended='Hark Bohm' Strength=2>
<Record Recommended='Sue Barton' Strength=2>
<Record Recommended='Gregory Itzin' Strength=2>
<Record Recommended='Mike Binder' Strength=2>
<Record Recommended='Diana Salvatore' Strength=2>
<Record Recommended='Willard E. Pugh' Strength=2>
<Record Recommended='Angela Paton' Strength=2>
<Record Recommended='Tom Wright' Strength=2>
<Record Recommended='Nick Frost' Strength=2>
<Record Recommended='Rúaidhrí Conroy' Strength=2>
<Record Recommended='Patti LuPone' Strength=2>
<Record Recommended='Kelly Ward' Strength=2>
<Record Recommended='Uwe Boll' Strength=2>
<Record Recommended='Maggie Lawson' Strength=2>
<Record Recommended='Virginie Ledoyen' Strength=2>
<Record Recommended='Loles León' Strength=2>
<Record Recommended='Joseph Pupo' Strength=2>
<Record Recommended='Ebon Moss-Bachrach' Strength=2>
<Record Recommended='Paul Mazursky' Strength=2>
<Record Recommended='Giovanna Zacarías' Strength=2>
<Record Recommended='Miguel Angel Plaza' Strength=2>
<Record Recommended='Gannon Forrester' Strength=2>
<Record Recommended='Germaine Delbat' Strength=2>
<Record Recommended='Jaimz Woolvett' Strength=2>
<Record Recommended='Jean-Hugues Anglade' Strength=2>
<Record Recommended='Elaine May' Strength=2>
<Record Recommended='Jake Dengel' Strength=2>
<Record Recommended='Teresa Gilmore' Strength=2>
<Record Recommended='Lon Chaney Jr.' Strength=2>
<Record Recommended='Marc Duret' Strength=2>
<Record Recommended='Brenda Fricker' Strength=2>
<Record Recommended='Jeff Kober' Strength=2>
<Record Recommended='Laura Regan' Strength=2>
<Record Recommended='Robert Douglas Washington' Strength=2>
<Record Recommended='Guillermo Ruiz' Strength=2>
<Record Recommended='Richard Bradford' Strength=2>
<Record Recommended='Casey Kasem' Strength=2>
<Record Recommended='Robert Weems' Strength=2>
<Record Recommended='Arliss Howard' Strength=2>
<Record Recommended='Jet Li' Strength=2>
<Record Recommended='Doug Hutchison' Strength=2>
<Record Recommended='Juan Diego Botto' Strength=2>
<Record Recommended='Kate Burton' Strength=2>
<Record Recommended='David Kaff' Strength=2>
<Record Recommended='Catherine Tayrien' Strength=2>
<Record Recommended='John Norman' Strength=2>
<Record Recommended='Brian McNamara' Strength=2>
<Record Recommended='Kelly Carlson' Strength=2>
<Record Recommended='George Segal' Strength=2>
<Record Recommended='Richard Coyle' Strength=2>
<Record Recommended='Sandra De Sousa' Strength=2>
<Record Recommended='Glenn Ford' Strength=2>
<Record Recommended='Andrew Kevin Walker' Strength=2>
<Record Recommended='Esther Rolle' Strength=2>
<Record Recommended='Gary Kohn' Strength=2>
<Record Recommended='S. Scott Bullock' Strength=2>
<Record Recommended='R.D. Call' Strength=2>
<Record Recommended='Thomas Robins' Strength=2>
<Record Recommended='David Leary' Strength=2>
<Record Recommended='Darlanne Fluegel' Strength=2>
<Record Recommended='Edwin Starr' Strength=2>
<Record Recommended='Louise Hopkins' Strength=2>
<Record Recommended='Menna Trussler' Strength=2>
<Record Recommended='Sacha Pitoëff' Strength=2>
<Record Recommended='Josh Flitter' Strength=2>
<Record Recommended='Terri Coulter' Strength=2>
<Record Recommended='Robin Dunne' Strength=2>
<Record Recommended='Rachel Majorowski' Strength=2>
<Record Recommended='Christopher Heyerdahl' Strength=2>
<Record Recommended='Imogene Coca' Strength=2>
<Record Recommended='Teresa Hill' Strength=2>
<Record Recommended='Zlatko Buric' Strength=2>
<Record Recommended='Todd Louiso' Strength=2>
<Record Recommended='Gastón Manuel Peterson' Strength=2>
<Record Recommended='Paul Coeur' Strength=2>
<Record Recommended='Andrew Divoff' Strength=2>
<Record Recommended='Sean Patrick Flanery' Strength=2>
<Record Recommended='Kelly Blatz' Strength=2>
<Record Recommended='Nancy Sherburne' Strength=2>
<Record Recommended='Sue Ane Langdon' Strength=2>
<Record Recommended='Stan Stennet' Strength=2>
<Record Recommended='Jack Rovello' Strength=2>
<Record Recommended='Noelle Harling' Strength=2>
<Record Recommended='Michelle Chadwick' Strength=2>
<Record Recommended='Bruce Norris' Strength=2>
<Record Recommended='Ron Perkins' Strength=2>
<Record Recommended='William Hickey' Strength=2>
<Record Recommended='Don Cochran' Strength=2>
<Record Recommended='Mary Elizabeth Winstead' Strength=2>
<Record Recommended='Harold Perrineau' Strength=2>
<Record Recommended='Renate Blume' Strength=2>
<Record Recommended='Linda Fiorentino' Strength=2>
<Record Recommended='Michael B. Silver' Strength=2>
<Record Recommended='Rodger Bumpass' Strength=2>
<Record Recommended='Joe Santos' Strength=2>
<Record Recommended='Vernon Dobtcheff' Strength=2>
<Record Recommended='Boman Irani' Strength=2>
<Record Recommended='Francesca Annis' Strength=2>
<Record Recommended='Verna Bloom' Strength=2>
<Record Recommended='Richard Hunt' Strength=2>
<Record Recommended='Annie Corley' Strength=2>
<Record Recommended='Hallie Kate Eisenberg' Strength=2>
<Record Recommended='Danso Gordon' Strength=2>
<Record Recommended='Iben Hjejle' Strength=2>
<Record Recommended='William Holden' Strength=2>
<Record Recommended='Raven Goodwin' Strength=2>
<Record Recommended='Jean-Pierre Léaud' Strength=2>
<Record Recommended='Brent Kinsman' Strength=2>
<Record Recommended='Søren Pilmark' Strength=2>
<Record Recommended='Skandar Keynes' Strength=2>
<Record Recommended='Sarah Alexander' Strength=2>
<Record Recommended='Jim Nabors' Strength=2>
<Record Recommended='Lance LeGault' Strength=2>
<Record Recommended='Nick Hobbs' Strength=2>
<Record Recommended='Padrig Owen Jones' Strength=2>
<Record Recommended='Trevor Peacock' Strength=2>
<Record Recommended='Denise Dowse' Strength=2>
<Record Recommended='Mary Stuart Masterson' Strength=2>
<Record Recommended='Russell Sams' Strength=2>
<Record Recommended='John Di Benedetto' Strength=2>
<Record Recommended='Haji' Strength=2>
<Record Recommended='Anthony Mockus Sr.' Strength=2>
<Record Recommended='June Brown' Strength=2>
<Record Recommended='Scott Michael Campbell' Strength=2>
<Record Recommended='Jordan Warkol' Strength=2>
<Record Recommended='Eric Hines' Strength=2>
<Record Recommended='David Yip' Strength=2>
<Record Recommended='Lloyd Nolan' Strength=2>
<Record Recommended='Vittorio Mezzogiorno' Strength=2>
<Record Recommended='E. Roger Mitchell' Strength=2>
<Record Recommended='Jamison Newlander' Strength=2>
<Record Recommended='Duane Whitaker' Strength=2>
<Record Recommended='Cher' Strength=2>
<Record Recommended='Jean-Claude La Marre' Strength=2>
<Record Recommended='Ashley Johnson' Strength=2>
<Record Recommended='Roberta Maxwell' Strength=2>
<Record Recommended='John Patrick Amedori' Strength=2>
<Record Recommended='André Falcon' Strength=2>
<Record Recommended="Bobb'e J. Thompson" Strength=2>
<Record Recommended='Patrick Pinney' Strength=2>
<Record Recommended='Gore Vidal' Strength=2>
<Record Recommended='Balázs Koós' Strength=2>
<Record Recommended='Abe Vigoda' Strength=2>
<Record Recommended='Danny Mastrogiorgio' Strength=2>
<Record Recommended='David Hayman' Strength=2>
<Record Recommended='Brent Jennings' Strength=2>
<Record Recommended='Lewis Smith' Strength=2>
<Record Recommended='Christopher Hart' Strength=2>
<Record Recommended='KaDee Strickland' Strength=2>
<Record Recommended='Vaughn Taylor' Strength=2>
<Record Recommended='John DiSanti' Strength=2>
<Record Recommended='David Wayne' Strength=2>
<Record Recommended='Gerry Becker' Strength=2>
<Record Recommended='Tom Ewell' Strength=2>
<Record Recommended='Nick Wolcuff' Strength=2>
<Record Recommended='Venus Terzo' Strength=2>
<Record Recommended='Michael FitzGerald' Strength=2>
<Record Recommended='Debrah Farentino' Strength=2>
<Record Recommended='Columbus Short' Strength=2>
<Record Recommended='Ricardo Montalban' Strength=2>
<Record Recommended='Daniel Lapaine' Strength=2>
<Record Recommended='David Wolos-Fonteno' Strength=2>
<Record Recommended='Elizabeth Ashley' Strength=2>
<Record Recommended='Leila Kenzle' Strength=2>
<Record Recommended='Viktor Avdyushko' Strength=2>
<Record Recommended='Gennadi Vengerov' Strength=2>
<Record Recommended='Angela Lamarsh' Strength=2>
<Record Recommended='Brittany Daniel' Strength=2>
<Record Recommended='Jonathan Higgins' Strength=2>
<Record Recommended='Wilfrid Bray' Strength=2>
<Record Recommended='Leslie Easterbrook' Strength=2>
<Record Recommended='John Alexander' Strength=2>
<Record Recommended='Amanda Detmer' Strength=2>
<Record Recommended='Julianna Margulies' Strength=2>
<Record Recommended='Ashton Holmes' Strength=2>
<Record Recommended='Jesse Catlien' Strength=2>
<Record Recommended='Ty Wood' Strength=2>
<Record Recommended='Rick Borgia' Strength=2>
<Record Recommended='Benjamin McKenzie' Strength=2>
<Record Recommended='Bennet Guillory' Strength=2>
<Record Recommended='Ross Bagley' Strength=2>
<Record Recommended='Darlene Cates' Strength=2>
<Record Recommended='Jillian Armenante' Strength=2>
<Record Recommended='Rory McCann' Strength=2>
<Record Recommended='Douglas Seale' Strength=2>
<Record Recommended='Kevin Sussman' Strength=2>
<Record Recommended='Winston Thomas' Strength=2>
<Record Recommended='Anna Deavere Smith' Strength=2>
<Record Recommended='Erica Leerhsen' Strength=2>
<Record Recommended='Vondie Curtis-Hall' Strength=2>
<Record Recommended='Harry Morgan' Strength=2>
<Record Recommended='Paul Reynolds' Strength=2>
<Record Recommended='Stuart McQuarrie' Strength=2>
<Record Recommended='Brenda Bakke' Strength=2>
<Record Recommended='Trio Los Rivera' Strength=2>
<Record Recommended='Shelley Long' Strength=2>
<Record Recommended='Meg Tilly' Strength=2>
<Record Recommended='Bethany Butler' Strength=2>
<Record Recommended='Leo Fitzpatrick' Strength=2>
<Record Recommended='Donna J. Dickson' Strength=2>
<Record Recommended='Benito Martinez' Strength=2>
<Record Recommended='Tony Azito' Strength=2>
<Record Recommended='Rena Sofer' Strength=2>
<Record Recommended='Yuki Matsuzaki' Strength=2>
<Record Recommended='DeRay Davis' Strength=2>
<Record Recommended='Donna Denton' Strength=2>
<Record Recommended='Bonita Hall' Strength=2>
<Record Recommended='Mason Gamble' Strength=2>
<Record Recommended='Ashlyn Sanchez' Strength=2>
<Record Recommended='Larry Cohen' Strength=2>
<Record Recommended='Jeremy Blackman' Strength=2>
<Record Recommended='Ray Santilli' Strength=2>
<Record Recommended='Joe Ranft' Strength=2>
<Record Recommended='Desmond Llewelyn' Strength=2>
<Record Recommended='Heather Wahlquist' Strength=2>
<Record Recommended='David Patrick Kelly' Strength=2>
<Record Recommended='Larry Drake' Strength=2>
<Record Recommended='Alyque Padamsee' Strength=2>
<Record Recommended='Elizabeth Reaser' Strength=2>
<Record Recommended='Adam LaVorgna' Strength=2>
<Record Recommended='Harrison Page' Strength=2>
<Record Recommended='Bob Dishy' Strength=2>
<Record Recommended='Michael Ontkean' Strength=2>
<Record Recommended='Oscar Hsu' Strength=2>
<Record Recommended='Roseanne' Strength=2>
<Record Recommended='Sophia Ellis' Strength=2>
<Record Recommended='Ariel Winter' Strength=2>
<Record Recommended='Robert Kerman' Strength=2>
<Record Recommended='Matthias Habich' Strength=2>
<Record Recommended='Angela Little' Strength=2>
<Record Recommended='Luke Brandon Field' Strength=2>
<Record Recommended='Michael Bailey Smith' Strength=2>
<Record Recommended='Peter Youngblood Hills' Strength=2>
<Record Recommended='Kara Hoffman' Strength=2>
<Record Recommended='Leon' Strength=2>
<Record Recommended='Andrzej Seweryn' Strength=2>
<Record Recommended='Kevin McKidd' Strength=2>
<Record Recommended='Oliver Hudson' Strength=2>
<Record Recommended='Wen Yann Shih' Strength=2>
<Record Recommended='Mort Mills' Strength=2>
<Record Recommended='Greg Wood' Strength=2>
<Record Recommended='Randy Savage' Strength=2>
<Record Recommended='Lainie Kazan' Strength=2>
<Record Recommended='David Conrad' Strength=2>
<Record Recommended='Peter Frechette' Strength=2>
<Record Recommended='Glenn Shadix' Strength=2>
<Record Recommended='Vincent Kartheiser' Strength=2>
<Record Recommended='Kylie Bax' Strength=2>
<Record Recommended='Daphne Korol' Strength=2>
<Record Recommended='Brendan Coyle' Strength=2>
<Record Recommended='Lili Haydn' Strength=2>
<Record Recommended='Kevin Anderson' Strength=2>
<Record Recommended='Kevin Chamberlin' Strength=2>
<Record Recommended='Melanie Mayron' Strength=2>
<Record Recommended='Linda Darlow' Strength=2>
<Record Recommended='Diane Amos' Strength=2>
<Record Recommended='Eva Gabor' Strength=2>
<Record Recommended='Rachel True' Strength=2>
<Record Recommended='Morgan Farley' Strength=2>
<Record Recommended='Jean-Pierre Aumont' Strength=2>
<Record Recommended='Lisa Thornhill' Strength=2>
<Record Recommended='Claudia Black' Strength=2>
<Record Recommended='Jacob Smith' Strength=2>
<Record Recommended='Gustavo Sanchez-Parra' Strength=2>
<Record Recommended='Jo Ann Soto' Strength=2>
<Record Recommended='Charley Lau' Strength=2>
<Record Recommended='Jon Cryer' Strength=2>
<Record Recommended='Hawthorne James' Strength=2>
<Record Recommended='Art James' Strength=2>
<Record Recommended='Patrick McGoohan' Strength=2>
<Record Recommended='Rene Auberjonois' Strength=2>
<Record Recommended='Nick Phalen' Strength=2>
<Record Recommended='Chuck Connors' Strength=2>
<Record Recommended='Jacqueline Obradors' Strength=2>
<Record Recommended='Anthony McPartlin' Strength=2>
<Record Recommended='Warwick Davis' Strength=2>
<Record Recommended='Melissa George' Strength=2>
<Record Recommended='Parley Baer' Strength=2>
<Record Recommended='Sonja Bennett' Strength=2>
<Record Recommended='Alun Armstrong' Strength=2>
<Record Recommended='Todd Graff' Strength=2>
<Record Recommended='Kevin Lima' Strength=2>
<Record Recommended='Genie Francis' Strength=2>
<Record Recommended='Alexander Gould' Strength=2>
<Record Recommended='Dan Warry-Smith' Strength=2>
<Record Recommended='Keith Gordon' Strength=2>
<Record Recommended='Pandora Peaks' Strength=2>
<Record Recommended='Nina Mazodier' Strength=2>
<Record Recommended='Peggy Mason' Strength=2>
<Record Recommended='Pam Grier' Strength=2>
<Record Recommended='Kimberly Scott' Strength=2>
<Record Recommended='Tony Luke Jr.' Strength=2>
<Record Recommended='Verne Troyer' Strength=2>
<Record Recommended='Katie Cassidy' Strength=2>
<Record Recommended='Mark Dacascos' Strength=2>
<Record Recommended='Tim Dixon' Strength=2>
<Record Recommended='Tom Gallop' Strength=2>
<Record Recommended='Brian Austin Green' Strength=2>
<Record Recommended='Fanda Nikic' Strength=2>
<Record Recommended='François Truffaut' Strength=2>
<Record Recommended='Mum Brothers' Strength=2>
<Record Recommended='Eanna MacLiam' Strength=2>
<Record Recommended='Steven Hinkle' Strength=2>
<Record Recommended='Beverly Hotsprings' Strength=2>
<Record Recommended='Paul Kantner' Strength=2>
<Record Recommended='Olivia Colman' Strength=2>
<Record Recommended='Robert Gossett' Strength=2>
<Record Recommended='Niels Olsen' Strength=2>
<Record Recommended='Marek Vasut' Strength=2>
<Record Recommended='Maurice Page' Strength=2>
<Record Recommended='Timothy Webber' Strength=2>
<Record Recommended='Joe Gnoffo' Strength=2>
<Record Recommended='Melissa Leo' Strength=2>
<Record Recommended='Bruno Lastra' Strength=2>
<Record Recommended='Jay Robert Inslee' Strength=2>
<Record Recommended='Leonardo Cimino' Strength=2>
<Record Recommended='Maggs Harries' Strength=2>
<Record Recommended='Mia Wasikowska' Strength=2>
<Record Recommended='Richard Holden' Strength=2>
<Record Recommended='Dylan Moran' Strength=2>
<Record Recommended='Colleen McCauley' Strength=2>
<Record Recommended='Michael Rouse' Strength=2>
<Record Recommended='Brandon T. Jackson' Strength=2>
<Record Recommended='Brigitte Bako' Strength=2>
<Record Recommended='Noel Williams' Strength=2>
<Record Recommended='Alexander Schwan' Strength=2>
<Record Recommended='Gary Werntz' Strength=2>
<Record Recommended='Jillian Bach' Strength=2>
<Record Recommended='Yaphet Kotto' Strength=2>
<Record Recommended='Noah Wyle' Strength=2>
<Record Recommended='Keye Luke' Strength=2>
<Record Recommended='Hunter Parrish' Strength=2>
<Record Recommended='Denzel Whitaker' Strength=2>
<Record Recommended='SaRenna Lee' Strength=2>
<Record Recommended='Thomas Dekker' Strength=2>
<Record Recommended='Michael Pitt' Strength=2>
<Record Recommended='David Sinaiko' Strength=2>
<Record Recommended='Cathy Belton' Strength=2>
<Record Recommended='Melissa Sagemiller' Strength=2>
<Record Recommended='Madeleine Moffat' Strength=2>
<Record Recommended='Eugene Byrd' Strength=2>
<Record Recommended='Macy Gray' Strength=2>
<Record Recommended='Andy Milonakis' Strength=2>
<Record Recommended='Greg Donaldson' Strength=2>
<Record Recommended='Ted Stanhope' Strength=2>
<Record Recommended='Antoni Corone' Strength=2>
<Record Recommended='Wayne Robson' Strength=2>
<Record Recommended='James Kirchner' Strength=2>
<Record Recommended='Edward Fox' Strength=2>
<Record Recommended='Kelvin Han Yee' Strength=2>
<Record Recommended='Adolph Caesar' Strength=2>
<Record Recommended='Chris Sigurdson' Strength=2>
<Record Recommended='Chris Wilson' Strength=2>
<Record Recommended='Craig Chaquico' Strength=2>
<Record Recommended='Molly Sims' Strength=2>
<Record Recommended='Danny Pino' Strength=2>
<Record Recommended='Paul Soter' Strength=2>
<Record Recommended='Rachel Nichols' Strength=2>
<Record Recommended='Mamie Gummer' Strength=2>
<Record Recommended='Gilles Marini' Strength=2>
<Record Recommended='Wes Craven' Strength=2>
<Record Recommended='Joshua Jenkins' Strength=2>
<Record Recommended='Noble Willingham' Strength=2>
<Record Recommended='Brett Davern' Strength=2>
<Record Recommended='Dragan Mićanović' Strength=2>
<Record Recommended='J.J. Cohen' Strength=2>
<Record Recommended='Cathy Tyson' Strength=2>
<Record Recommended='Marin Hinkle' Strength=2>
<Record Recommended='Scott Mosier' Strength=2>
<Record Recommended='Jonathan Ke Quan' Strength=2>
<Record Recommended='Monirak Sisowath' Strength=2>
<Record Recommended='John Voldstad' Strength=2>
<Record Recommended='James Foley' Strength=2>
<Record Recommended='Frank Collison' Strength=2>
<Record Recommended='Dick Peabody' Strength=2>
<Record Recommended='Nicollette Sheridan' Strength=2>
<Record Recommended='Michael Bell' Strength=2>
<Record Recommended='Travis Tedford' Strength=2>
<Record Recommended='Shelley Morrison' Strength=2>
<Record Recommended='Todd M. Camhe' Strength=2>
<Record Recommended='Ernie Lee Banks' Strength=2>
<Record Recommended='Mary Ann Hay' Strength=2>
<Record Recommended='Susan Messing' Strength=2>
<Record Recommended='Lauren Birkell' Strength=2>
<Record Recommended='Brent Hinkley' Strength=2>
<Record Recommended='Anita Morris' Strength=2>
<Record Recommended='Gaspard Ulliel' Strength=2>
<Record Recommended='James Haven' Strength=2>
<Record Recommended='Kerry Bishé' Strength=2>
<Record Recommended='Kristoffer Cooper' Strength=2>
<Record Recommended='Jeremy Sheffield' Strength=2>
<Record Recommended='Paul Urcioli' Strength=2>
<Record Recommended='Peter Jason' Strength=2>
<Record Recommended='Michael J. Pollard' Strength=2>
<Record Recommended='Alan Hale Jr.' Strength=2>
<Record Recommended='Tracy Reiner' Strength=2>
<Record Recommended='Mark Holton' Strength=2>
<Record Recommended='Alan Stanford' Strength=2>
<Record Recommended='Stanley Townsend' Strength=2>
<Record Recommended='Howell Evans' Strength=2>
<Record Recommended='Mike Starr' Strength=2>
<Record Recommended='Miguel A. Gaetan' Strength=2>
<Record Recommended='Ian D. Clark' Strength=2>
<Record Recommended='David McCullough' Strength=2>
<Record Recommended='Truman Capote' Strength=2>
<Record Recommended='Santiago Cabrera' Strength=2>
<Record Recommended='Arthur Rowton' Strength=2>
<Record Recommended='Michael Cerveris' Strength=2>
<Record Recommended='Israel Rubinek' Strength=2>
<Record Recommended='Luis Soto' Strength=2>
<Record Recommended='Bernie Rachelle' Strength=2>
<Record Recommended='Joel McCrary' Strength=2>
<Record Recommended='Stuart M. Besser' Strength=2>
<Record Recommended='Kristin Kreuk' Strength=2>
<Record Recommended='Michel Galabru' Strength=2>
<Record Recommended='Calista Flockhart' Strength=2>
<Record Recommended='Linda Larkin' Strength=2>
<Record Recommended="Terry O'Quinn" Strength=2>
<Record Recommended='Loretta Wendt Jolivette' Strength=2>
<Record Recommended='Stuart Wilson' Strength=2>
<Record Recommended='Jeremy Guskin' Strength=2>
<Record Recommended='Raúl Méndez' Strength=2>
<Record Recommended='David Hasselhoff' Strength=2>
<Record Recommended='Malik Sealy' Strength=2>
<Record Recommended='Common' Strength=2>
<Record Recommended='Michael Buscemi' Strength=2>
<Record Recommended='Rose McIver' Strength=2>
<Record Recommended='David Sparrow' Strength=2>
<Record Recommended='Elina Löwensohn' Strength=2>
<Record Recommended='John Beasley' Strength=2>
<Record Recommended='Julianne Nicholson' Strength=2>
<Record Recommended='Shondrella Avery' Strength=2>
<Record Recommended='Kevin Jamal Woods' Strength=2>
<Record Recommended='Peter Hall' Strength=2>
<Record Recommended='Emmy Rossum' Strength=2>
<Record Recommended='Kyle Gallner' Strength=2>
<Record Recommended='Anna Chancellor' Strength=2>
<Record Recommended='Ron Canada' Strength=2>
<Record Recommended='Adriana Cordova' Strength=2>
<Record Recommended='Jamie Campbell Bower' Strength=2>
<Record Recommended='Musetta Vander' Strength=2>
<Record Recommended='Veronica Ferres' Strength=2>
<Record Recommended='Chus Lampreave' Strength=2>
<Record Recommended='Jayne Brook' Strength=2>
<Record Recommended='Rod Steiger' Strength=2>
<Record Recommended='Desmond Askew' Strength=2>
<Record Recommended='Andrew Robb' Strength=2>
<Record Recommended='Jill Clayburgh' Strength=2>
<Record Recommended='Amanda Seyfried' Strength=2>
<Record Recommended='Tyler Posey' Strength=2>
<Record Recommended='Bodil Jørgensen' Strength=2>
<Record Recommended='Conrad Dunn' Strength=2>
<Record Recommended='Ian Porter' Strength=2>
<Record Recommended='Grey DeLisle' Strength=2>
<Record Recommended='David Fine' Strength=2>
<Record Recommended='Marina Stephenson Kerr' Strength=2>
<Record Recommended='Maury Sterling' Strength=2>
<Record Recommended='William Daniels' Strength=2>
<Record Recommended='Walter High' Strength=2>
<Record Recommended='Biff Yeager' Strength=2>
<Record Recommended='Stephanie Metcalfe' Strength=2>
<Record Recommended='Curd Jürgens' Strength=2>
<Record Recommended='Wiley Wiggins' Strength=2>
<Record Recommended='Sushma Reddy' Strength=2>
<Record Recommended='John Mighton' Strength=2>
<Record Recommended='Hilmar Thate' Strength=2>
<Record Recommended='Ronald Hamilton' Strength=2>
<Record Recommended='Rohini Hattangadi' Strength=2>
<Record Recommended='Josh Stamberg' Strength=2>
<Record Recommended='Sheila Bailey' Strength=2>
<Record Recommended='Reggie Jackson' Strength=2>
<Record Recommended='Barbara Babcock' Strength=2>
<Record Recommended="Franc D'Ambrosio" Strength=2>
<Record Recommended='James Purefoy' Strength=2>
<Record Recommended='Byung-hun Lee' Strength=2>
<Record Recommended='Catherine Fitch' Strength=2>
<Record Recommended='Pete Hamill' Strength=2>
<Record Recommended='Bea Arthur' Strength=2>
<Record Recommended='Armand Assante' Strength=2>
<Record Recommended="Dylan O'Sullivan Farrow" Strength=2>
<Record Recommended='Paul Dano' Strength=2>
<Record Recommended='Donald Faison' Strength=2>
<Record Recommended='Lee Richardson' Strength=2>
<Record Recommended='Don Thompson' Strength=2>
<Record Recommended='Sarah DeVincentis' Strength=2>
<Record Recommended='Dawn Pritchard' Strength=2>
<Record Recommended='Charlie Hewson' Strength=2>
<Record Recommended='Wil Wheaton' Strength=2>
<Record Recommended='Franco Columbu' Strength=2>
<Record Recommended="Glynnis O'Connor" Strength=2>
<Record Recommended='Devorah Rose' Strength=2>
<Record Recommended='Matt Mercier' Strength=2>
<Record Recommended='Graham Norton' Strength=2>
<Record Recommended='Michael Benyaer' Strength=2>
<Record Recommended='Eliza Roberts' Strength=2>
<Record Recommended='Tim Pigott-Smith' Strength=2>
<Record Recommended='Valentina Cervi' Strength=2>
<Record Recommended='Mauralea Austin' Strength=2>
<Record Recommended='Ashley Scott' Strength=2>
<Record Recommended='Shane Kinsman' Strength=2>
<Record Recommended='Worthie Meacham' Strength=2>
<Record Recommended="Ed O'Ross" Strength=2>
<Record Recommended='Ed Gilbert' Strength=2>
<Record Recommended='Sarah Bolger' Strength=2>
<Record Recommended='Kevin Carroll' Strength=2>
<Record Recommended='Shiloh Fernandez' Strength=2>
<Record Recommended="Denis O'Hare" Strength=2>
<Record Recommended='Patrick Dougherty' Strength=2>
<Record Recommended='Jennifer Rae Beck' Strength=2>
<Record Recommended='Werner Kirsch' Strength=2>
<Record Recommended='Petrea Burchard' Strength=2>
<Record Recommended='Chris Bell' Strength=2>
<Record Recommended='Patti Bryant' Strength=2>
<Record Recommended='Judy Parfitt' Strength=2>
<Record Recommended='Bruno Bichir' Strength=2>
<Record Recommended='Mary Seibel' Strength=2>
<Record Recommended='Stephen Spinella' Strength=2>
<Record Recommended='Carlo Alban' Strength=2>
<Record Recommended='Rachel Schwartz' Strength=2>
<Record Recommended='Blake Jeremy Collins' Strength=2>
<Record Recommended='Wilbur Fitzgerald' Strength=2>
<Record Recommended='Michel Duchaussoy' Strength=2>
<Record Recommended='Alicia Silverstone' Strength=2>
<Record Recommended='Woody Watson' Strength=2>
<Record Recommended='Lora Schroeder' Strength=2>
<Record Recommended='Jim Henson' Strength=2>
<Record Recommended='Paul Herman' Strength=2>
<Record Recommended='Candy Clark' Strength=2>
<Record Recommended='Erick Avari' Strength=2>
<Record Recommended='Joe Nunez' Strength=2>
<Record Recommended='Tamer Hassan' Strength=2>
<Record Recommended='Reathel Bean' Strength=2>
<Record Recommended='Luke de Woolfson' Strength=2>
<Record Recommended='Lucy Lawless' Strength=2>
<Record Recommended='Sisqó' Strength=2>
<Record Recommended='Blake McIver Ewing' Strength=2>
<Record Recommended='Katherine Krapum Chey' Strength=2>
<Record Recommended='Gérard Lanvin' Strength=2>
<Record Recommended='Garfield Wilson' Strength=2>
<Record Recommended='Kayvan Novak' Strength=2>
<Record Recommended='Richard Lynch' Strength=2>
<Record Recommended='Jennifer Hudson' Strength=2>
<Record Recommended='Magda Szubanski' Strength=2>
<Record Recommended='Chance Michael Corbitt' Strength=2>
<Record Recommended='DeForest Kelley' Strength=2>
<Record Recommended='Shannyn Sossamon' Strength=2>
<Record Recommended='Amy Hill' Strength=2>
<Record Recommended='Ralph Macchio' Strength=2>
<Record Recommended='Sarah Carter' Strength=2>
<Record Recommended='Ed Herlihy' Strength=2>
<Record Recommended='Isaac Laskin' Strength=2>
<Record Recommended='Jackie Tohn' Strength=2>
<Record Recommended='Frederick Coffin' Strength=2>
<Record Recommended='Linda Kash' Strength=2>
<Record Recommended='Ian Ziering' Strength=2>
<Record Recommended='Matthew Fox' Strength=2>
<Record Recommended='Jared Sandler' Strength=2>
<Record Recommended='Jason Behr' Strength=2>
<Record Recommended='Danny Huston' Strength=2>
<Record Recommended='Gene Evans' Strength=2>
<Record Recommended='Reiko Aylesworth' Strength=2>
<Record Recommended='Brandon Hirsch' Strength=2>
<Record Recommended='Mike Dopud' Strength=2>
<Record Recommended='Sarah Badel' Strength=2>
<Record Recommended='Ray Romano' Strength=2>
<Record Recommended='Ayelet Zurer' Strength=2>
<Record Recommended='Sally Kellerman' Strength=2>
<Record Recommended='Marshall Dougherty' Strength=2>
<Record Recommended='Alice Taglioni' Strength=2>
<Record Recommended='Rosemary Murphy' Strength=2>
<Record Recommended='Molly Cheek' Strength=2>
<Record Recommended='Catherine Mangan' Strength=2>
<Record Recommended='Eric Thal' Strength=2>
<Record Recommended='Barry Corbin' Strength=2>
<Record Recommended='Bill Cable' Strength=2>
<Record Recommended='Peter Greenwood' Strength=2>
<Record Recommended='Frederic Forrest' Strength=2>
<Record Recommended='Don Ameche' Strength=2>
<Record Recommended='Dafydd Wyn Roberts' Strength=2>
<Record Recommended='Robert DoQui' Strength=2>
<Record Recommended='Laird Macintosh' Strength=2>
<Record Recommended='Chiara Mastroianni' Strength=2>
<Record Recommended='Michael Taliferro' Strength=2>
<Record Recommended='Brad Hunt' Strength=2>
<Record Recommended='Jenna Fischer' Strength=2>
<Record Recommended='Julie Payne' Strength=2>
<Record Recommended='Cory Hodges' Strength=2>
<Record Recommended='Brian Patterson' Strength=2>
<Record Recommended='Eric Silver' Strength=2>
<Record Recommended="Madeline O'Brien" Strength=2>
<Record Recommended='Nicky Henson' Strength=2>
<Record Recommended='Jim Staahl' Strength=2>
<Record Recommended='Anthony Zerbe' Strength=2>
<Record Recommended='Chris Messina' Strength=2>
<Record Recommended='Paolo Bonacelli' Strength=2>
<Record Recommended='Signe Egholm Olsen' Strength=2>
<Record Recommended='Dexter Fletcher' Strength=2>
<Record Recommended='Rachel Sweet' Strength=2>
<Record Recommended='Brenda McDonald' Strength=2>
<Record Recommended='Derek Cecil' Strength=2>
<Record Recommended='Jonah Bobo' Strength=2>
<Record Recommended='Leslie Phillips' Strength=2>
<Record Recommended='Rob Benedict' Strength=2>
<Record Recommended='Pierre Dherte' Strength=2>
<Record Recommended='Eva Green' Strength=2>
<Record Recommended='Stephen Stucker' Strength=2>
<Record Recommended='Bruce Ramsay' Strength=2>
<Record Recommended='Brian Gleeson' Strength=2>
<Record Recommended='Claude Vernier' Strength=2>
<Record Recommended='Werner Herzog' Strength=2>
<Record Recommended='Mickey Morton' Strength=2>
<Record Recommended='Jack Shepherd' Strength=2>
<Record Recommended='Frank Ashmore' Strength=2>
<Record Recommended='Gary Gober' Strength=2>
<Record Recommended='Emmanuel Johnson' Strength=2>
<Record Recommended='Dewey Weber' Strength=2>
<Record Recommended='William Hope' Strength=2>
<Record Recommended='Kristen Wiig' Strength=2>
<Record Recommended='R.J. Parnell' Strength=2>
<Record Recommended='John Cazale' Strength=2>
<Record Recommended='Peter James' Strength=2>
<Record Recommended='Christopher Denham' Strength=2>
<Record Recommended='Mick Jagger' Strength=2>
<Record Recommended='Claudia Cardinale' Strength=2>
<Record Recommended='Gordon Currie' Strength=2>
<Record Recommended='Sylvain Landry' Strength=2>
<Record Recommended='Lin Shaye' Strength=2>
<Record Recommended='Merle Kilgore' Strength=2>
<Record Recommended='Chris Marquette' Strength=2>
<Record Recommended='Steve Talley' Strength=2>
<Record Recommended='Steven Elder' Strength=2>
<Record Recommended='Allan Graf' Strength=2>
<Record Recommended='Kelly Rowan' Strength=2>
<Record Recommended='Jeremy Northam' Strength=2>
<Record Recommended='Paz Vega' Strength=2>
<Record Recommended='Pat Kane' Strength=2>
<Record Recommended='David Mucci' Strength=2>
<Record Recommended='Gina Gershon' Strength=2>
<Record Recommended='Kevin Ligon' Strength=2>
<Record Recommended='Pam Shaw' Strength=2>
<Record Recommended='Bernard Cribbins' Strength=2>
<Record Recommended='Tisha Campbell' Strength=2>
<Record Recommended='Cristi Conaway' Strength=2>
<Record Recommended='Orson Welles' Strength=2>
<Record Recommended='John Cater' Strength=2>
<Record Recommended='Juan Carlos Serrán' Strength=2>
<Record Recommended="Peter O'Meara" Strength=2>
<Record Recommended='Elvis Costello' Strength=2>
<Record Recommended='Jeanie Calleja' Strength=2>
<Record Recommended='Sebastian Shaw' Strength=2>
<Record Recommended='Candace Carey' Strength=2>
<Record Recommended='Pernilla August' Strength=2>
<Record Recommended='Sterling Beaumon' Strength=2>
<Record Recommended='Christine Lippa' Strength=2>
<Record Recommended='Sienna Guillory' Strength=2>
<Record Recommended='Matt Letscher' Strength=2>
<Record Recommended='Ben Cross' Strength=2>
<Record Recommended='Faith Prince' Strength=2>
<Record Recommended='Craig T. Nelson' Strength=2>
<Record Recommended='Jeremy Swift' Strength=2>
<Record Recommended='Yeardley Smith' Strength=2>
<Record Recommended='Kim Hunter' Strength=2>
<Record Recommended='Lloyd Bridges' Strength=2>
<Record Recommended='Will Forte' Strength=2>
<Record Recommended='Nancy Casemore' Strength=2>
<Record Recommended='Roy Scheider' Strength=2>
<Record Recommended='David Mitchell' Strength=2>
<Record Recommended='Isabelle Carré' Strength=2>
<Record Recommended='Julie Lott' Strength=2>
<Record Recommended='Anita Smith' Strength=2>
<Record Recommended='Féodor Atkine' Strength=2>
<Record Recommended='Charlie Newmark' Strength=2>
<Record Recommended='John Sharian' Strength=2>
<Record Recommended='Shannon Jardine' Strength=2>
<Record Recommended='Don Brockett' Strength=2>
<Record Recommended='Carlos Gallardo' Strength=2>
<Record Recommended='Luke Kirby' Strength=2>
<Record Recommended='Bill Bailey' Strength=2>
<Record Recommended='Ed Byrne' Strength=2>
<Record Recommended='Riz Abbasi' Strength=2>
<Record Recommended='Kristen Johnston' Strength=2>
<Record Recommended='Noah Taylor' Strength=2>
<Record Recommended='Jane Fonda' Strength=2>
<Record Recommended='Shannon Lawson' Strength=2>
<Record Recommended='Heather Ashleigh' Strength=2>
<Record Recommended='Phyllis Diller' Strength=2>
<Record Recommended='Joel Palmer' Strength=2>
<Record Recommended='Joe Piscopo' Strength=2>
<Record Recommended='Paul Norell' Strength=2>
<Record Recommended='Leslie Schofield' Strength=2>
<Record Recommended='Douglas Anderson' Strength=2>
<Record Recommended='Peter Dougherty' Strength=2>
<Record Recommended='Chad Bannon' Strength=2>
<Record Recommended='Chia Hui Liu' Strength=2>
<Record Recommended='Dejan Cukic' Strength=2>
<Record Recommended='Dalip Tahil' Strength=2>
<Record Recommended='Kim Myers' Strength=2>
<Record Recommended='Tasha de Vasconcelos' Strength=2>
<Record Recommended='Elsa Lanchester' Strength=2>
<Record Recommended='Sean Markey' Strength=2>
<Record Recommended='Gérard Buhr' Strength=2>
<Record Recommended='Albie Woodington' Strength=2>
<Record Recommended='John Salley' Strength=2>
<Record Recommended='Robert A. Silverman' Strength=2>
<Record Recommended='Dolan Dougherty' Strength=2>
<Record Recommended='Graham McGrath' Strength=2>
<Record Recommended='Terry Baker' Strength=2>
<Record Recommended='Hannes Messemer' Strength=2>
<Record Recommended='Lothaire Bluteau' Strength=2>
<Record Recommended='Austin Stout' Strength=2>
<Record Recommended='Sid Caesar' Strength=2>
<Record Recommended='Sylvia Kaler' Strength=2>
<Record Recommended='Judith Benezra' Strength=2>
<Record Recommended='Marilyn Sokol' Strength=2>
<Record Recommended='Steve Oedekerk' Strength=2>
<Record Recommended='Laura Harring' Strength=2>
<Record Recommended='Robert Katims' Strength=2>
<Record Recommended='Jon Bon Jovi' Strength=2>
<Record Recommended='Christian Hecq' Strength=2>
<Record Recommended='Israel Tellez' Strength=2>
<Record Recommended='Robert Foxworth' Strength=2>
<Record Recommended='Jake Siegel' Strength=2>
<Record Recommended='Jonah Meyerson' Strength=2>
<Record Recommended='Abby Brammell' Strength=2>
<Record Recommended='Hanna R. Hall' Strength=2>
<Record Recommended='Mikey Holekamp' Strength=2>
<Record Recommended='Paul Perri' Strength=2>
<Record Recommended='Roger Yuan' Strength=2>
<Record Recommended='Freddie Jones' Strength=2>
<Record Recommended='Leonor Varela' Strength=2>
<Record Recommended='Sadie Frost' Strength=2>
<Record Recommended='Horacio Garcia Rojas' Strength=2>
<Record Recommended='Jason Raize' Strength=2>
<Record Recommended='Chazz Dominguez' Strength=2>
<Record Recommended='Grace Jones' Strength=2>
<Record Recommended='Kimberly J. Brown' Strength=2>
<Record Recommended='Stephen Geoffreys' Strength=2>
<Record Recommended='Timothy Brown' Strength=2>
<Record Recommended='Dwight Ewell' Strength=2>
<Record Recommended='Jean Effron' Strength=2>
<Record Recommended='Wiveca Bonerais' Strength=2>
<Record Recommended='Talisa Soto' Strength=2>
<Record Recommended='Hugh Dillon' Strength=2>
<Record Recommended='John Bekavac' Strength=2>
<Record Recommended='Eusebio Poncela' Strength=2>
<Record Recommended='Mitch Baker' Strength=2>
<Record Recommended='Paul Christie' Strength=2>
<Record Recommended='Vincent Paterson' Strength=2>
<Record Recommended='Morwenna Banks' Strength=2>
<Record Recommended='Ian MacDonald' Strength=2>
<Record Recommended='Jake Thomas' Strength=2>
<Record Recommended='Lynne Thigpen' Strength=2>
<Record Recommended='Jay Whittaker' Strength=2>
<Record Recommended='Taraji P. Henson' Strength=2>
<Record Recommended='Imelda Staunton' Strength=2>
<Record Recommended='Karen Kruper' Strength=2>
<Record Recommended='Harry Meyen' Strength=2>
<Record Recommended='Chris Noth' Strength=2>
<Record Recommended='Clare Higgins' Strength=2>
<Record Recommended='Ben Whishaw' Strength=2>
<Record Recommended='Grant Heslov' Strength=2>
<Record Recommended='Jay Chandrasekhar' Strength=2>
<Record Recommended='Shelley Winters' Strength=2>
<Record Recommended='Steven Mackintosh' Strength=2>
<Record Recommended='John Friedrich' Strength=2>
<Record Recommended='Earl Poitier' Strength=2>
<Record Recommended='Roger Dumas' Strength=2>
<Record Recommended='Dean Reed' Strength=2>
<Record Recommended='Johnny Strong' Strength=2>
<Record Recommended='Justin Shilton' Strength=2>
<Record Recommended='Anne Meara' Strength=2>
<Record Recommended='Joey Chin' Strength=2>
<Record Recommended='Brian Geraghty' Strength=2>
<Record Recommended='Joe Dante' Strength=2>
<Record Recommended='Aishwarya Rai' Strength=2>
<Record Recommended='Susan Wooldridge' Strength=2>
<Record Recommended='Dafydd Hywel' Strength=2>
<Record Recommended='Elizabeth Berrington' Strength=2>
<Record Recommended='Bradley Cooper' Strength=2>
<Record Recommended='Jason Beghe' Strength=2>
<Record Recommended='Ty Burrell' Strength=2>
<Record Recommended='Dale Place' Strength=2>
<Record Recommended='Joe Lo Truglio' Strength=2>
<Record Recommended='Caroline Proust' Strength=2>
<Record Recommended='Arthur Kennedy' Strength=2>
<Record Recommended="Ron O'Neal" Strength=2>
<Record Recommended='Flor Kent' Strength=2>
<Record Recommended='Maggie Wheeler' Strength=2>
<Record Recommended='Tessa Richarde' Strength=2>
<Record Recommended='Hayley Mills' Strength=2>
<Record Recommended='Tavia Schwartz' Strength=2>
<Record Recommended='Rhona Mitra' Strength=2>
<Record Recommended='Richard Griffiths' Strength=2>
<Record Recommended='Adam Ryen' Strength=2>
<Record Recommended='Brock Peters' Strength=2>
<Record Recommended='Tad Hilgenbrink' Strength=2>
<Record Recommended="Annette O'Toole" Strength=2>
<Record Recommended='Bria Roberts' Strength=2>
<Record Recommended='Tom Adams' Strength=2>
<Record Recommended='Burt Kwouk' Strength=2>
<Record Recommended='Sebastian Stan' Strength=2>
<Record Recommended='Helga Liné' Strength=2>
<Record Recommended='Victoria Racimo' Strength=2>
<Record Recommended='Azura Skye' Strength=2>
<Record Recommended='Peter Willcock' Strength=2>
<Record Recommended='Sofía Vergara' Strength=2>
<Record Recommended='Ralph St. George' Strength=2>
<Record Recommended='Richmond Arquette' Strength=2>
<Record Recommended='Sarah Rose Karr' Strength=2>
<Record Recommended='Greg Hollimon' Strength=2>
<Record Recommended='Liane Balaban' Strength=2>
<Record Recommended='Candy Ford' Strength=2>
<Record Recommended='Lenka Peterson' Strength=2>
<Record Recommended='Nahtasha Budhi' Strength=2>
<Record Recommended='Simon Callow' Strength=2>
<Record Recommended='Elisabeth Volkmann' Strength=2>
<Record Recommended='Marla Sucharetza' Strength=2>
<Record Recommended='Matthew Marsden' Strength=2>
<Record Recommended='William Dennis Hunt' Strength=2>
<Record Recommended='Dianne Reeves' Strength=2>
<Record Recommended='Alec Mapa' Strength=2>
<Record Recommended='Eion Bailey' Strength=2>
<Record Recommended='Jimmy Nail' Strength=2>
<Record Recommended='Lou Hirsch' Strength=2>
<Record Recommended='Suzy Joachim' Strength=2>
<Record Recommended='Tony Alcantar' Strength=2>
<Record Recommended='Leonard L. Thomas' Strength=2>
<Record Recommended='Winfried Glatzeder' Strength=2>
<Record Recommended='Jeffrey Zubernis' Strength=2>
<Record Recommended='Leonid Swjetlow' Strength=2>
<Record Recommended='Richard Leacock' Strength=2>
<Record Recommended='Jon Robin Baitz' Strength=2>
<Record Recommended='Michele Lee' Strength=2>
<Record Recommended='Oliver Ford Davies' Strength=2>
<Record Recommended='Peter Cushing' Strength=2>
<Record Recommended='Sean McCann' Strength=2>
<Record Recommended='Kim Director' Strength=2>
<Record Recommended='Marceline Hugot' Strength=2>
<Record Recommended='Gurudarshan' Strength=2>
<Record Recommended='Cybill Shepherd' Strength=2>
<Record Recommended='David Bailie' Strength=2>
<Record Recommended='Chelsea Lagos' Strength=2>
<Record Recommended='Barry Humphries' Strength=2>
<Record Recommended='Steve Rosen' Strength=2>
<Record Recommended='Miriam Karlin' Strength=2>
<Record Recommended='Akiko Takeshita' Strength=2>
<Record Recommended='Steven Pasquale' Strength=2>
<Record Recommended='Dabney Coleman' Strength=2>
<Record Recommended='Alex Winter' Strength=2>
<Record Recommended='Laura Lovelace' Strength=2>
<Record Recommended='Gary Shoefield' Strength=2>
<Record Recommended='Zack Ward' Strength=2>
<Record Recommended='Ralph J. Alderman' Strength=2>
<Record Recommended='Victor Mohica' Strength=2>
<Record Recommended='Tony Amendola' Strength=2>
<Record Recommended='Otto Kruger' Strength=2>
<Record Recommended='Bill Bixby' Strength=2>
<Record Recommended='Holly Aird' Strength=2>
<Record Recommended='Tom Signorelli' Strength=2>
<Record Recommended='Angela Featherstone' Strength=2>
<Record Recommended='Jacob Vargas' Strength=2>
<Record Recommended='Shahid Ahmed' Strength=2>
<Record Recommended='Oliver Pierpaoli' Strength=2>
<Record Recommended='Dave Goelz' Strength=2>
<Record Recommended='Paul Hipp' Strength=2>
<Record Recommended='Adrian Scarborough' Strength=2>
<Record Recommended='Lacey Chabert' Strength=2>
<Record Recommended='Mazhar Munir' Strength=2>
<Record Recommended='John Rubano' Strength=2>
<Record Recommended='Keith Charles' Strength=2>
<Record Recommended='Tony Haygarth' Strength=1>
<Record Recommended='Tanya Lopert' Strength=1>
<Record Recommended='Harriet Sansom Harris' Strength=1>
<Record Recommended='Ryan Alosio' Strength=1>
<Record Recommended='Miles Meadows' Strength=1>
<Record Recommended='Amandah Reyne' Strength=1>
<Record Recommended='Casper Van Dien' Strength=1>
<Record Recommended='Harvey Virdi' Strength=1>
<Record Recommended='Daryn Jones' Strength=1>
<Record Recommended='Benno Fürmann' Strength=1>
<Record Recommended='Frank Ertl' Strength=1>
<Record Recommended='Will MacMillan' Strength=1>
<Record Recommended='Janet Henfrey' Strength=1>
<Record Recommended='Tyson Ritter' Strength=1>
<Record Recommended='Darrian McClanahan' Strength=1>
<Record Recommended='Scott Michael Morgan' Strength=1>
<Record Recommended='Ross McCall' Strength=1>
<Record Recommended='Roy Jenson' Strength=1>
<Record Recommended='Mary Lynn Owen' Strength=1>
<Record Recommended='Bonnie Root' Strength=1>
<Record Recommended='Floyd Levine' Strength=1>
<Record Recommended='William Converse-Roberts' Strength=1>
<Record Recommended='Mhairi Steenbock' Strength=1>
<Record Recommended='Tanay Chheda' Strength=1>
<Record Recommended='Patrick Taylor' Strength=1>
<Record Recommended='Maude Eburne' Strength=1>
<Record Recommended='Gregory Forstner' Strength=1>
<Record Recommended='Ben Cardinal' Strength=1>
<Record Recommended='Alexei Sayle' Strength=1>
<Record Recommended='Macia Zapata' Strength=1>
<Record Recommended='Olegar Fedoro' Strength=1>
<Record Recommended='Sean Gunn' Strength=1>
<Record Recommended='Mablean Ephriam' Strength=1>
<Record Recommended='Scott Porter' Strength=1>
<Record Recommended='DeVone Lawson Jr.' Strength=1>
<Record Recommended='Michael Wildman' Strength=1>
<Record Recommended='Dimple Sharma' Strength=1>
<Record Recommended='Conrad Bergschneider' Strength=1>
<Record Recommended='Tony Armatrading' Strength=1>
<Record Recommended='Robert Oliveri' Strength=1>
<Record Recommended='Pam Gail' Strength=1>
<Record Recommended='India de Beaufort' Strength=1>
<Record Recommended='Richard Anderson' Strength=1>
<Record Recommended='Jalal Nuriddin' Strength=1>
<Record Recommended='Jeremy Sumpter' Strength=1>
<Record Recommended='Gina Torres' Strength=1>
<Record Recommended='Omar J. Dorsey' Strength=1>
<Record Recommended='Robert Littman' Strength=1>
<Record Recommended='Renato Rascel' Strength=1>
<Record Recommended='Salli Richardson-Whitfield' Strength=1>
<Record Recommended='Fernando Hilbeck' Strength=1>
<Record Recommended='Peter Cockett' Strength=1>
<Record Recommended='Antonio Muñiz' Strength=1>
<Record Recommended='Chuck Cooper' Strength=1>
<Record Recommended='Alan Kaplan' Strength=1>
<Record Recommended='Christian Pikes' Strength=1>
<Record Recommended='Sebastien Roberts' Strength=1>
<Record Recommended='Joanne Linville' Strength=1>
<Record Recommended='Romolo Di Biasi' Strength=1>
<Record Recommended='Deborah Van Valkenburgh' Strength=1>
<Record Recommended='Sheila Paterson' Strength=1>
<Record Recommended='Kelle Kipp' Strength=1>
<Record Recommended='Arnoldo Foà' Strength=1>
<Record Recommended='Anne Haney' Strength=1>
<Record Recommended='John Womack Jr.' Strength=1>
<Record Recommended='Francis De Wolff' Strength=1>
<Record Recommended='Terry Gilliam' Strength=1>
<Record Recommended='Judith Baldwin' Strength=1>
<Record Recommended='Kevin Jubinville' Strength=1>
<Record Recommended='Ariana Richards' Strength=1>
<Record Recommended='James Bulleit' Strength=1>
<Record Recommended='Mario Joyner' Strength=1>
<Record Recommended='John Neville' Strength=1>
<Record Recommended='Peter Looney' Strength=1>
<Record Recommended='Jean-Marie Winling' Strength=1>
<Record Recommended='Katja Riemann' Strength=1>
<Record Recommended='Rishikesh Sharma' Strength=1>
<Record Recommended='Patrick Gallagher' Strength=1>
<Record Recommended='Anthony Ruiz' Strength=1>
<Record Recommended='Amber Heard' Strength=1>
<Record Recommended='Franz Kutschera' Strength=1>
<Record Recommended='Ric Sarabia' Strength=1>
<Record Recommended='Bob Clark' Strength=1>
<Record Recommended='Robert Klein' Strength=1>
<Record Recommended='Jayson Therrien' Strength=1>
<Record Recommended='Alisan Porter' Strength=1>
<Record Recommended='Tony Theng' Strength=1>
<Record Recommended='Murray Langston' Strength=1>
<Record Recommended='Victor McGuire' Strength=1>
<Record Recommended='Steve Sandor' Strength=1>
<Record Recommended='Bitty Schram' Strength=1>
<Record Recommended='Adam Harrington' Strength=1>
<Record Recommended='Mike Weinberg' Strength=1>
<Record Recommended='Andy Luotto' Strength=1>
<Record Recommended='Mike Figgis' Strength=1>
<Record Recommended='Dr. Richard Lutz' Strength=1>
<Record Recommended='Bernd Tauber' Strength=1>
<Record Recommended='Georgia Allen' Strength=1>
<Record Recommended='David Wohl' Strength=1>
<Record Recommended='Billy Morton' Strength=1>
<Record Recommended='Sumalee Montano' Strength=1>
<Record Recommended='Stephi Lineburg' Strength=1>
<Record Recommended='Harry Andrews' Strength=1>
<Record Recommended='Ingeborga Dapkunaite' Strength=1>
<Record Recommended='Dillon Freasier' Strength=1>
<Record Recommended='Zach Galligan' Strength=1>
<Record Recommended='Joe Alaskey' Strength=1>
<Record Recommended='Jacqueline Beer' Strength=1>
<Record Recommended='Peter Williamson' Strength=1>
<Record Recommended='José Taitano' Strength=1>
<Record Recommended='Loyd Catlett' Strength=1>
<Record Recommended='Oliver Tobias' Strength=1>
<Record Recommended='Marge Redmond' Strength=1>
<Record Recommended="Michael O'Sullivan" Strength=1>
<Record Recommended='Alexis von Hagemeister' Strength=1>
<Record Recommended='Irene Olga López' Strength=1>
<Record Recommended='Dennis Boutsikaris' Strength=1>
<Record Recommended='Cécile Henry' Strength=1>
<Record Recommended='Scott Williamson' Strength=1>
<Record Recommended='Sharon Ziman' Strength=1>
<Record Recommended='Joseph Shiloach' Strength=1>
<Record Recommended='Anna Perrier' Strength=1>
<Record Recommended='Mickey Fleddermann' Strength=1>
<Record Recommended='Lindy Booth' Strength=1>
<Record Recommended='Richard Foronjy' Strength=1>
<Record Recommended='William Peter Blatty' Strength=1>
<Record Recommended='Emily Woof' Strength=1>
<Record Recommended="Linda O'Neil" Strength=1>
<Record Recommended='John Damler' Strength=1>
<Record Recommended='Simon Oakland' Strength=1>
<Record Recommended='James Daughton' Strength=1>
<Record Recommended='Tre Rogers' Strength=1>
<Record Recommended='Frank Cassavetes' Strength=1>
<Record Recommended='John Bobek' Strength=1>
<Record Recommended='Samantha Ivers' Strength=1>
<Record Recommended='Enoch King' Strength=1>
<Record Recommended='Brandon Routh' Strength=1>
<Record Recommended='Martin McCann' Strength=1>
<Record Recommended='Foxy Lae' Strength=1>
<Record Recommended='John Lilla' Strength=1>
<Record Recommended='Axel Triebel' Strength=1>
<Record Recommended='Alonzo Millsap' Strength=1>
<Record Recommended='Sidney Blackmer' Strength=1>
<Record Recommended='Shelby Young' Strength=1>
<Record Recommended='Alana Locke' Strength=1>
<Record Recommended='Robbie Kay' Strength=1>
<Record Recommended='Robert Plunket' Strength=1>
<Record Recommended='Tobias Mehler' Strength=1>
<Record Recommended='Patrick Cranshaw' Strength=1>
<Record Recommended='Joachim Dietmar Mues' Strength=1>
<Record Recommended='José Pérez' Strength=1>
<Record Recommended='James DePaul' Strength=1>
<Record Recommended='Teresa Celli' Strength=1>
<Record Recommended='Frank Murray' Strength=1>
<Record Recommended='Jeff Doucette' Strength=1>
<Record Recommended='Stephanie Dawn Wood' Strength=1>
<Record Recommended='Martin Herdman' Strength=1>
<Record Recommended='Peter Gantzler' Strength=1>
<Record Recommended='Ben Miller' Strength=1>
<Record Recommended='Castulo Guerra' Strength=1>
<Record Recommended='Mathabo Pieterson' Strength=1>
<Record Recommended='Stan Egi' Strength=1>
<Record Recommended='Robin Chalk' Strength=1>
<Record Recommended='Dominique Bettenfeld' Strength=1>
<Record Recommended='Steve Stransman' Strength=1>
<Record Recommended='Gordon Thomson' Strength=1>
<Record Recommended='William Haze' Strength=1>
<Record Recommended='Marianne Basler' Strength=1>
<Record Recommended='Ron Crawford' Strength=1>
<Record Recommended='Betsy Palmer' Strength=1>
<Record Recommended='Ron Insana' Strength=1>
<Record Recommended='Joshua Daniel' Strength=1>
<Record Recommended='Jessica Booker' Strength=1>
<Record Recommended='Manuel Bandera' Strength=1>
<Record Recommended='Titos Vandis' Strength=1>
<Record Recommended='Zsuzsa Gordon' Strength=1>
<Record Recommended='Joey Hazinsky' Strength=1>
<Record Recommended='Royston Innes' Strength=1>
<Record Recommended='Peter Sturm' Strength=1>
<Record Recommended='Friedrich Richter' Strength=1>
<Record Recommended='Therese Bradley' Strength=1>
<Record Recommended='John Howard' Strength=1>
<Record Recommended='Jason Sudeikis' Strength=1>
<Record Recommended='Cynthia Alvarado' Strength=1>
<Record Recommended='Anne Parillaud' Strength=1>
<Record Recommended='Tino Mewes' Strength=1>
<Record Recommended='Janet Jackson' Strength=1>
<Record Recommended='Ray Milland' Strength=1>
<Record Recommended='Art Malik' Strength=1>
<Record Recommended='Michael Finn' Strength=1>
<Record Recommended='Rie Rasmussen' Strength=1>
<Record Recommended='Alfred Barker Jr.' Strength=1>
<Record Recommended='Philippa Fordham' Strength=1>
<Record Recommended='Maria Simon' Strength=1>
<Record Recommended='Vincent Grass' Strength=1>
<Record Recommended="Brooke D'Orsay" Strength=1>
<Record Recommended='Steve Buck' Strength=1>
<Record Recommended='Eddie Alderson' Strength=1>
<Record Recommended='Isabel Mestres' Strength=1>
<Record Recommended='James Carpinello' Strength=1>
<Record Recommended='Keith Nobbs' Strength=1>
<Record Recommended='Steven Beckingham' Strength=1>
<Record Recommended='Roxana Guttman' Strength=1>
<Record Recommended='Nick Wilkinson' Strength=1>
<Record Recommended='Kiowa Gordon' Strength=1>
<Record Recommended='Natima Bradley' Strength=1>
<Record Recommended='Jordy Benattar' Strength=1>
<Record Recommended="Caroline O'Connor" Strength=1>
<Record Recommended='Eric Schildkraut' Strength=1>
<Record Recommended='Ashley Greene' Strength=1>
<Record Recommended='Charlie Bewley' Strength=1>
<Record Recommended='Annabelle Weenick' Strength=1>
<Record Recommended='John Dehner' Strength=1>
<Record Recommended='Michael Hitchcock' Strength=1>
<Record Recommended='Austin Friel' Strength=1>
<Record Recommended='Anna Friel' Strength=1>
<Record Recommended='Jessica Williams' Strength=1>
<Record Recommended='Michelle Krusiec' Strength=1>
<Record Recommended='Richard Kiel' Strength=1>
<Record Recommended='Louis Turenne' Strength=1>
<Record Recommended='Tyler Mane' Strength=1>
<Record Recommended='Alex McArthur' Strength=1>
<Record Recommended='Joey Kramer' Strength=1>
<Record Recommended='Laurie Murdoch' Strength=1>
<Record Recommended='Terence Harvey' Strength=1>
<Record Recommended='Claus Riis Østergaard' Strength=1>
<Record Recommended='Neville Brand' Strength=1>
<Record Recommended='Miguel A. Núñez Jr.' Strength=1>
<Record Recommended='Rose Thiéry' Strength=1>
<Record Recommended='Giancarlo Giannini' Strength=1>
<Record Recommended='Ernie Reyes Jr.' Strength=1>
<Record Recommended='Claudia Christian' Strength=1>
<Record Recommended="Michael O'Keefe" Strength=1>
<Record Recommended='Jonah Rooney' Strength=1>
<Record Recommended='Vanity' Strength=1>
<Record Recommended='Marina Bouras' Strength=1>
<Record Recommended='Richard Boone' Strength=1>
<Record Recommended='Samuel Ball' Strength=1>
<Record Recommended='Rick Warden' Strength=1>
<Record Recommended='Otis Day' Strength=1>
<Record Recommended='Jan Sinclair' Strength=1>
<Record Recommended='Leif Erickson' Strength=1>
<Record Recommended='Jordan Lund' Strength=1>
<Record Recommended='Corey Page' Strength=1>
<Record Recommended='Lori Singer' Strength=1>
<Record Recommended='Richard Lewis' Strength=1>
<Record Recommended='Noel Fisher' Strength=1>
<Record Recommended='Cliff De Young' Strength=1>
<Record Recommended='Donald Saiontz' Strength=1>
<Record Recommended='Riccardo Scamarcio' Strength=1>
<Record Recommended='Matthew Whittet' Strength=1>
<Record Recommended='Kathleen York' Strength=1>
<Record Recommended='Kristyn Mae-Anne Lao' Strength=1>
<Record Recommended='Harry Crosby' Strength=1>
<Record Recommended='Najwa Nimri' Strength=1>
<Record Recommended='Charlie Cox' Strength=1>
<Record Recommended='Maia Campbell' Strength=1>
<Record Recommended='Peggy Gormley' Strength=1>
<Record Recommended='Farrah Fawcett' Strength=1>
<Record Recommended='Charles McGraw' Strength=1>
<Record Recommended='Dr. Dre' Strength=1>
<Record Recommended='Joe Inscoe' Strength=1>
<Record Recommended='John Duttine' Strength=1>
<Record Recommended='Susan Tyrrell' Strength=1>
<Record Recommended='Sherry Knight' Strength=1>
<Record Recommended='Ron Dean' Strength=1>
<Record Recommended='Paula Jai Parker' Strength=1>
<Record Recommended='Michael Shanks' Strength=1>
<Record Recommended='Michel Voletti' Strength=1>
<Record Recommended='Barry Bostwick' Strength=1>
<Record Recommended='Eric Benjamin' Strength=1>
<Record Recommended='Anna Mucha' Strength=1>
<Record Recommended='Waris Hussein' Strength=1>
<Record Recommended='Tony Todd' Strength=1>
<Record Recommended='Max Cantor' Strength=1>
<Record Recommended='Zoltan Butuc' Strength=1>
<Record Recommended='Scali Delpeyrat' Strength=1>
<Record Recommended='Zander Schloss' Strength=1>
<Record Recommended='Zoe Bell' Strength=1>
<Record Recommended='Jackson Bond' Strength=1>
<Record Recommended='Jack Hill' Strength=1>
<Record Recommended='Phoebe Nicholls' Strength=1>
<Record Recommended='Keir Dullea' Strength=1>
<Record Recommended='James Carville' Strength=1>
<Record Recommended='Craig Archibald' Strength=1>
<Record Recommended='Trevor Gagnon' Strength=1>
<Record Recommended='Yul Vazquez' Strength=1>
<Record Recommended='Eileen Nicholas' Strength=1>
<Record Recommended='Camryn Manheim' Strength=1>
<Record Recommended='Joe Turkel' Strength=1>
<Record Recommended='Rosemarie DeWitt' Strength=1>
<Record Recommended='Gerold Noelli' Strength=1>
<Record Recommended='Gig Morton' Strength=1>
<Record Recommended='Rebecca Løgstrup' Strength=1>
<Record Recommended='Max Baker' Strength=1>
<Record Recommended='Tommy Flanagan' Strength=1>
<Record Recommended='Matthew Lewis' Strength=1>
<Record Recommended='Kellee Stewart' Strength=1>
<Record Recommended='Ayesha Dharker' Strength=1>
<Record Recommended='Alan Ruscoe' Strength=1>
<Record Recommended="Peter O'Brien" Strength=1>
<Record Recommended='Sô Yamamura' Strength=1>
<Record Recommended='Paul Stewart' Strength=1>
<Record Recommended='Julianne Grossman' Strength=1>
<Record Recommended='Khleo Thomas' Strength=1>
<Record Recommended='Aya Cash' Strength=1>
<Record Recommended='Carl Irwin' Strength=1>
<Record Recommended='Conleth Hill' Strength=1>
<Record Recommended='Helena Kallianiotes' Strength=1>
<Record Recommended='Maurice Orozco' Strength=1>
<Record Recommended='Anthony Dilio' Strength=1>
<Record Recommended='Danielia L. Cotton' Strength=1>
<Record Recommended='Wally Welch' Strength=1>
<Record Recommended='Rosie Shaw' Strength=1>
<Record Recommended='Tom Bell' Strength=1>
<Record Recommended='Ben Chaplin' Strength=1>
<Record Recommended='Geneviève Fontanel' Strength=1>
<Record Recommended='Sylvia Earle' Strength=1>
<Record Recommended='Andrea Bruschi' Strength=1>
<Record Recommended='Lou Antonio' Strength=1>
<Record Recommended='Jennifer Lyons' Strength=1>
<Record Recommended='Grant Cramer' Strength=1>
<Record Recommended='Janine Benyus' Strength=1>
<Record Recommended='Michael James Ford' Strength=1>
<Record Recommended='Stefan Kalipha' Strength=1>
<Record Recommended='Jerry Tondo' Strength=1>
<Record Recommended='Alan C. Peterson' Strength=1>
<Record Recommended='Matt King' Strength=1>
<Record Recommended='Pascal Rollin' Strength=1>
<Record Recommended='Alex Solowitz' Strength=1>
<Record Recommended='Horst Buchholz' Strength=1>
<Record Recommended='Michel Muller' Strength=1>
<Record Recommended='Gianmarco Tognazzi' Strength=1>
<Record Recommended='Carla Bessey' Strength=1>
<Record Recommended='Jon Glaser' Strength=1>
<Record Recommended='Kevin McAfee' Strength=1>
<Record Recommended='Lindsay Wagner' Strength=1>
<Record Recommended='Peter Carpenter' Strength=1>
<Record Recommended='Gary Riley' Strength=1>
<Record Recommended='Whitney Cummings' Strength=1>
<Record Recommended='Julie Bishop' Strength=1>
<Record Recommended='Roger Hammond' Strength=1>
<Record Recommended='Tusshar Kapoor' Strength=1>
<Record Recommended='Valeria Marian' Strength=1>
<Record Recommended='Phil McCall' Strength=1>
<Record Recommended='Mark Kassen' Strength=1>
<Record Recommended='Kerry Skalsky' Strength=1>
<Record Recommended='Jimmy Fallon' Strength=1>
<Record Recommended='Nina Van Pallandt' Strength=1>
<Record Recommended='Louise Mieritz' Strength=1>
<Record Recommended='Matthew Marsh' Strength=1>
<Record Recommended='Gary L. Mack' Strength=1>
<Record Recommended='Mizan Ayers' Strength=1>
<Record Recommended='Simone von Zglinicki' Strength=1>
<Record Recommended='Jessica Mas' Strength=1>
<Record Recommended='Warren J. Kemmerling' Strength=1>
<Record Recommended='Michelle Yeoh' Strength=1>
<Record Recommended='Atticus Shaffer' Strength=1>
<Record Recommended="Ted D'Arms" Strength=1>
<Record Recommended='Emmbre Perry' Strength=1>
<Record Recommended='Kristen Miller' Strength=1>
<Record Recommended='Brett Harrelson' Strength=1>
<Record Recommended='Claudine Baschet' Strength=1>
<Record Recommended='David Belle' Strength=1>
<Record Recommended='F. Valentino Morales' Strength=1>
<Record Recommended='Vanessa Lengies' Strength=1>
<Record Recommended='Welker White' Strength=1>
<Record Recommended='Bob Holt' Strength=1>
<Record Recommended='Robert Douglas' Strength=1>
<Record Recommended='Marc Warren' Strength=1>
<Record Recommended='Paresh Rawal' Strength=1>
<Record Recommended='Frank Brown Jr.' Strength=1>
<Record Recommended='Madeleine Cheminat' Strength=1>
<Record Recommended='Alexander Beyer' Strength=1>
<Record Recommended='James Dreyfus' Strength=1>
<Record Recommended='Soledad St. Hilaire' Strength=1>
<Record Recommended='D.A. Pauley' Strength=1>
<Record Recommended='Bob Amaral' Strength=1>
<Record Recommended='Ray Jeffries' Strength=1>
<Record Recommended='Lauren Lorbeck' Strength=1>
<Record Recommended='Anthony Eisley' Strength=1>
<Record Recommended='Paul Mercurio' Strength=1>
<Record Recommended='Chris Barrie' Strength=1>
<Record Recommended='Chandra West' Strength=1>
<Record Recommended='Christine Kan' Strength=1>
<Record Recommended='Stoney Westmoreland' Strength=1>
<Record Recommended='Morgan Walters' Strength=1>
<Record Recommended='Peter Aylward' Strength=1>
<Record Recommended='Neil Jackson' Strength=1>
<Record Recommended='Keenen Ivory Wayans' Strength=1>
<Record Recommended='Julia Montgomery' Strength=1>
<Record Recommended='Simon Bernstein' Strength=1>
<Record Recommended='Maria Canals-Barrera' Strength=1>
<Record Recommended='Roberta Eaton' Strength=1>
<Record Recommended='Howard George' Strength=1>
<Record Recommended='David Hanson' Strength=1>
<Record Recommended='Craig Susser' Strength=1>
<Record Recommended='Daniel Davin' Strength=1>
<Record Recommended='Pete Sepenuk' Strength=1>
<Record Recommended='Joan Freeman' Strength=1>
<Record Recommended='Michael Roof' Strength=1>
<Record Recommended='Jo Prestia' Strength=1>
<Record Recommended='Mary Portser' Strength=1>
<Record Recommended='William Allen Young' Strength=1>
<Record Recommended='Jack Daniel Wells' Strength=1>
<Record Recommended='Russell Hicks' Strength=1>
<Record Recommended='Leleti Khumalo' Strength=1>
<Record Recommended='Billy McColl' Strength=1>
<Record Recommended='Rodrigo Santoro' Strength=1>
<Record Recommended='Richard Strange' Strength=1>
<Record Recommended='Christopher Daniel Barnes' Strength=1>
<Record Recommended='Brad Calcaterra' Strength=1>
<Record Recommended='Kathryn Howell' Strength=1>
<Record Recommended='Homie Doroodian' Strength=1>
<Record Recommended='Evan Parke' Strength=1>
<Record Recommended='Carin Abicht' Strength=1>
<Record Recommended='Gundula Hofer' Strength=1>
<Record Recommended='Amanda' Strength=1>
<Record Recommended='Dominique Sanda' Strength=1>
<Record Recommended='Marie Jones' Strength=1>
<Record Recommended='George Pilgrim' Strength=1>
<Record Recommended='Alan McQueen' Strength=1>
<Record Recommended='Neha Dhupia' Strength=1>
<Record Recommended='Ian Christopher Scott' Strength=1>
<Record Recommended='Paula Devicq' Strength=1>
<Record Recommended='Huey Lewis' Strength=1>
<Record Recommended='Mario Davignon' Strength=1>
<Record Recommended='Jesse Falcon' Strength=1>
<Record Recommended='Katharine McPhee' Strength=1>
<Record Recommended='Rico Bueno' Strength=1>
<Record Recommended='Jay Tarses' Strength=1>
<Record Recommended='Udo Samel' Strength=1>
<Record Recommended='Kumar Pallana' Strength=1>
<Record Recommended='Anupam Kher' Strength=1>
<Record Recommended='Michael Irvin' Strength=1>
<Record Recommended='Daniel E. Smith' Strength=1>
<Record Recommended='Jay Villiers' Strength=1>
<Record Recommended='Maureen McGovern' Strength=1>
<Record Recommended='John Gavin' Strength=1>
<Record Recommended='Gregory Paul Martin' Strength=1>
<Record Recommended='Brian Delate' Strength=1>
<Record Recommended='Carl T. Evans' Strength=1>
<Record Recommended='Brian Hutchison' Strength=1>
<Record Recommended='James Saito' Strength=1>
<Record Recommended='Maggie Wellman' Strength=1>
<Record Recommended='Steve Smith' Strength=1>
<Record Recommended='Tony Ganios' Strength=1>
<Record Recommended='Maria Giovanna Donzelli' Strength=1>
<Record Recommended='Alexander Pollock' Strength=1>
<Record Recommended='John Martinus' Strength=1>
<Record Recommended='Maria Arcé' Strength=1>
<Record Recommended='Uschi Digard' Strength=1>
<Record Recommended='Christian Friis' Strength=1>
<Record Recommended='Bernard Fresson' Strength=1>
<Record Recommended='Calvin Levels' Strength=1>
<Record Recommended='Phillip Vaden' Strength=1>
<Record Recommended='Greg Cipes' Strength=1>
<Record Recommended='Ebbe Roe Smith' Strength=1>
<Record Recommended='Gabriel Malema' Strength=1>
<Record Recommended='Noah Emmerich' Strength=1>
<Record Recommended='Danielle Darrieux' Strength=1>
<Record Recommended='Angelika Hillebrecht' Strength=1>
<Record Recommended='Lynette Walden' Strength=1>
<Record Recommended='Erika Dunkelmann' Strength=1>
<Record Recommended='Yvonne Bryceland' Strength=1>
<Record Recommended='Gordon Michaels' Strength=1>
<Record Recommended='Jennifer Savidge' Strength=1>
<Record Recommended='Rodney A. Grant' Strength=1>
<Record Recommended='Jeff Tarpley' Strength=1>
<Record Recommended='Adam Alexi-Malle' Strength=1>
<Record Recommended='Kelly Overton' Strength=1>
<Record Recommended='Beth Ehlers' Strength=1>
<Record Recommended='William Duff-Griffin' Strength=1>
<Record Recommended='Jonathan Adams' Strength=1>
<Record Recommended='Burt Bulos' Strength=1>
<Record Recommended='Stephen Walters' Strength=1>
<Record Recommended='James Franciscus' Strength=1>
<Record Recommended='Geovanny Corvera' Strength=1>
<Record Recommended='Angus Sutherland' Strength=1>
<Record Recommended='Gaston Joly' Strength=1>
<Record Recommended='Chuck McCann' Strength=1>
<Record Recommended='Emma Lockhart' Strength=1>
<Record Recommended='Peter Iacangelo' Strength=1>
<Record Recommended='Parisa Fitz-Henley' Strength=1>
<Record Recommended='Yolande Moreau' Strength=1>
<Record Recommended='Liza Minnelli' Strength=1>
<Record Recommended='Melissa Greenspan' Strength=1>
<Record Recommended='Sean Wei Mah' Strength=1>
<Record Recommended='Carys Eleri' Strength=1>
<Record Recommended='Tom Burke' Strength=1>
<Record Recommended='Stefanie Stappenbeck' Strength=1>
<Record Recommended='Brandon Firla' Strength=1>
<Record Recommended='Daniel Cudmore' Strength=1>
<Record Recommended='Tim McMullan' Strength=1>
<Record Recommended='Kandyse McClure' Strength=1>
<Record Recommended='Carrie Aizley' Strength=1>
<Record Recommended='Matt McCoy' Strength=1>
<Record Recommended='Emie Hudson' Strength=1>
<Record Recommended='Daniel Olbrychski' Strength=1>
<Record Recommended='Maurice Roëves' Strength=1>
<Record Recommended="Pascal N'Zonzi" Strength=1>
<Record Recommended='Laura Nativo' Strength=1>
<Record Recommended='Alice Evans' Strength=1>
<Record Recommended='Eija Vilpas' Strength=1>
<Record Recommended='Anny Chasson' Strength=1>
<Record Recommended='Dean Hawes' Strength=1>
<Record Recommended='Susan May Pratt' Strength=1>
<Record Recommended='Gabrielle Brennan' Strength=1>
<Record Recommended='Don Goodwin' Strength=1>
<Record Recommended='Mike Pniewski' Strength=1>
<Record Recommended='Rolf Becker' Strength=1>
<Record Recommended='Mya' Strength=1>
<Record Recommended='Michel Blanc' Strength=1>
<Record Recommended='Joanne Baron' Strength=1>
<Record Recommended='Charles Halton' Strength=1>
<Record Recommended='Michael Alaimo' Strength=1>
<Record Recommended='Christopher Kubheka' Strength=1>
<Record Recommended='Robert McLane' Strength=1>
<Record Recommended='Ron Brice' Strength=1>
<Record Recommended='Gene Reynolds' Strength=1>
<Record Recommended='Patrick Baladi' Strength=1>
<Record Recommended='Rebel Rodriguez' Strength=1>
<Record Recommended="Edward Saint Pe'" Strength=1>
<Record Recommended='Kunal Khemu' Strength=1>
<Record Recommended='Zoie Palmer' Strength=1>
<Record Recommended='Annabel Brooks' Strength=1>
<Record Recommended='Donna Spangler' Strength=1>
<Record Recommended='Kelsey Lansdowne' Strength=1>
<Record Recommended='Lena Headey' Strength=1>
<Record Recommended='F. Rufus Owens' Strength=1>
<Record Recommended='Ruth Bradley' Strength=1>
<Record Recommended='Jordan Tesfay' Strength=1>
<Record Recommended='Michael Webber' Strength=1>
<Record Recommended='Daniela Golz' Strength=1>
<Record Recommended='Alessandro Serra' Strength=1>
<Record Recommended='Steffie Spira' Strength=1>
<Record Recommended='Stephen Dunham' Strength=1>
<Record Recommended='David Floyd' Strength=1>
<Record Recommended='Kevan Ohtsji' Strength=1>
<Record Recommended='Allisa Boardley' Strength=1>
<Record Recommended='Dmitry Chepovetsky' Strength=1>
<Record Recommended='Martine Demaret' Strength=1>
<Record Recommended='Becca Gardner' Strength=1>
<Record Recommended='T.J. Hoban' Strength=1>
<Record Recommended='Ana Leza' Strength=1>
<Record Recommended='Matteo Angius' Strength=1>
<Record Recommended='Amy Stewart' Strength=1>
<Record Recommended='Dimitri Andreas' Strength=1>
<Record Recommended='Judith Hoag' Strength=1>
<Record Recommended='Patricia Kalember' Strength=1>
<Record Recommended='Kenneth Tobey' Strength=1>
<Record Recommended='Jan Sterling' Strength=1>
<Record Recommended='J. Adam Glover' Strength=1>
<Record Recommended='Martin Semmelrogge' Strength=1>
<Record Recommended='Neil Patrick Harris' Strength=1>
<Record Recommended='Jim Barbour' Strength=1>
<Record Recommended='Agnes Moorehead' Strength=1>
<Record Recommended='Christina Orchid' Strength=1>
<Record Recommended='Bernard Menez' Strength=1>
<Record Recommended='Alex Carter' Strength=1>
<Record Recommended='Reggie Johnson' Strength=1>
<Record Recommended='Eglantine Rembauville-Nicolle' Strength=1>
<Record Recommended='James Handy' Strength=1>
<Record Recommended='Bill Camp' Strength=1>
<Record Recommended='Ivan Desny' Strength=1>
<Record Recommended='Sergio Nicolai' Strength=1>
<Record Recommended='Franziska Walser' Strength=1>
<Record Recommended='Jordan Charney' Strength=1>
<Record Recommended='Rif Hutton' Strength=1>
<Record Recommended='Scott Benjaminson' Strength=1>
<Record Recommended='Ty Panitz' Strength=1>
<Record Recommended='Leif Tilden' Strength=1>
<Record Recommended='Joe Strummer' Strength=1>
<Record Recommended='Neil Ross' Strength=1>
<Record Recommended='Taylor Parks' Strength=1>
<Record Recommended='Tessa Ia' Strength=1>
<Record Recommended='Cameron Mathison' Strength=1>
<Record Recommended='Olivia Newton-John' Strength=1>
<Record Recommended='Ted Roisum' Strength=1>
<Record Recommended='Rick Bramucci' Strength=1>
<Record Recommended='Billy Jayne' Strength=1>
<Record Recommended='Jeff Sanders' Strength=1>
<Record Recommended='Jennifer Love Hewitt' Strength=1>
<Record Recommended='Steffan Rhodri' Strength=1>
<Record Recommended='Danièle Lebrun' Strength=1>
<Record Recommended='Christine Kaufmann' Strength=1>
<Record Recommended='Cynthia Rhodes' Strength=1>
<Record Recommended='Didier Flamand' Strength=1>
<Record Recommended='Kevin Rice' Strength=1>
<Record Recommended='Cascy Beddow' Strength=1>
<Record Recommended='Don Hood' Strength=1>
<Record Recommended='Kyle Schmid' Strength=1>
<Record Recommended='Christopher Martin' Strength=1>
<Record Recommended='Nike Arrighi' Strength=1>
<Record Recommended='DJ Pooh' Strength=1>
<Record Recommended='Anthony-James Ryan' Strength=1>
<Record Recommended='Manfred Inger' Strength=1>
<Record Recommended='Everett Quinton' Strength=1>
<Record Recommended='Gulshan Grover' Strength=1>
<Record Recommended='Bianca Jagger' Strength=1>
<Record Recommended='Jan Elle' Strength=1>
<Record Recommended='Caroline Blakiston' Strength=1>
<Record Recommended='Isabel Allende' Strength=1>
<Record Recommended='Klaus Löwitsch' Strength=1>
<Record Recommended='Hannelore Hoger' Strength=1>
<Record Recommended='Andrea Savage' Strength=1>
<Record Recommended='Caroline Kava' Strength=1>
<Record Recommended='Larry Gates' Strength=1>
<Record Recommended='Aurelien Parent Koenig' Strength=1>
<Record Recommended='Brooke Lyons' Strength=1>
<Record Recommended='Tony Sirico' Strength=1>
<Record Recommended='Bonita Granville' Strength=1>
<Record Recommended='Carmine DiBenedetto' Strength=1>
<Record Recommended='Jeremia Ramasita' Strength=1>
<Record Recommended='Peter Johansen' Strength=1>
<Record Recommended='Andrew Rubin' Strength=1>
<Record Recommended='Harald Juhnke' Strength=1>
<Record Recommended='Hans-Michael Rehberg' Strength=1>
<Record Recommended='Sean Cory' Strength=1>
<Record Recommended='Steve Miller' Strength=1>
<Record Recommended='Jamie Sives' Strength=1>
<Record Recommended='Annie Ross' Strength=1>
<Record Recommended='Gesine Cukrowski' Strength=1>
<Record Recommended='Stefano Ambrogi' Strength=1>
<Record Recommended='Loris Loddi' Strength=1>
<Record Recommended='Jacob Kogan' Strength=1>
<Record Recommended='Dominique Blanc' Strength=1>
<Record Recommended='Ross Bagdasarian Jr.' Strength=1>
<Record Recommended='Erika Christensen' Strength=1>
<Record Recommended='Philip Glenister' Strength=1>
<Record Recommended='Audrey Christie' Strength=1>
<Record Recommended='Ralf Richter' Strength=1>
<Record Recommended='Jane Leeves' Strength=1>
<Record Recommended='Andrew Tombes' Strength=1>
<Record Recommended='Jude Ciccolella' Strength=1>
<Record Recommended='Cole Sprouse' Strength=1>
<Record Recommended='Shanna McCullough' Strength=1>
<Record Recommended='Gregory Harrison' Strength=1>
<Record Recommended='Eva Coutts' Strength=1>
<Record Recommended='Justine Waddell' Strength=1>
<Record Recommended='Billy Sands' Strength=1>
<Record Recommended='Lee Case' Strength=1>
<Record Recommended='Kate Beahan' Strength=1>
<Record Recommended='Russell Means' Strength=1>
<Record Recommended='Jane Brucker' Strength=1>
<Record Recommended='Dawn Didawick' Strength=1>
<Record Recommended='Cheryl Hawker' Strength=1>
<Record Recommended='Leslie Aldredge' Strength=1>
<Record Recommended='Woon Young Park' Strength=1>
<Record Recommended='David McCurley' Strength=1>
<Record Recommended='Giuseppe Battiston' Strength=1>
<Record Recommended='Drake Bell' Strength=1>
<Record Recommended='Thelma Louise Carter' Strength=1>
<Record Recommended='Enrique Iglesias' Strength=1>
<Record Recommended='Charles Dance' Strength=1>
<Record Recommended='Ben Wilson' Strength=1>
<Record Recommended='Rab Affleck' Strength=1>
<Record Recommended='Larissa Gomes' Strength=1>
<Record Recommended='Allan Hawco' Strength=1>
<Record Recommended='Judith Light' Strength=1>
<Record Recommended='Abdel Kechiche' Strength=1>
<Record Recommended='Robin Duke' Strength=1>
<Record Recommended='Ngoc Le' Strength=1>
<Record Recommended='Pierre Dux' Strength=1>
<Record Recommended='Kris Pope' Strength=1>
<Record Recommended='Corin  Redgrave' Strength=1>
<Record Recommended='Bud Spencer' Strength=1>
<Record Recommended='John Mariano' Strength=1>
<Record Recommended='Matthias Fuchs' Strength=1>
<Record Recommended='Marisa Coughlan' Strength=1>
<Record Recommended='Henry Hübchen' Strength=1>
<Record Recommended='Johnny Hallyday' Strength=1>
<Record Recommended='Rick Ducommun' Strength=1>
<Record Recommended='Sabine Glaser' Strength=1>
<Record Recommended='Penny Fuller' Strength=1>
<Record Recommended='Joyce Van Patten' Strength=1>
<Record Recommended='Justine Wachsberger' Strength=1>
<Record Recommended='Kenneth Choi' Strength=1>
<Record Recommended='Lars Arentz-Hansen' Strength=1>
<Record Recommended='Cornelia Guest' Strength=1>
<Record Recommended='Charles C. Stevenson Jr.' Strength=1>
<Record Recommended='Susan Ursitti' Strength=1>
<Record Recommended='Jonathan Sagall' Strength=1>
<Record Recommended='Mark Herrier' Strength=1>
<Record Recommended='Idan Alterman' Strength=1>
<Record Recommended='Buzz Aldrin' Strength=1>
<Record Recommended='Kevin Eshelman' Strength=1>
<Record Recommended='Stefano Abbati' Strength=1>
<Record Recommended='Anders Hove' Strength=1>
<Record Recommended='Chelah Horsdal' Strength=1>
<Record Recommended='Lorraine Farris' Strength=1>
<Record Recommended='Aemilia Robinson' Strength=1>
<Record Recommended='K.C. Collins' Strength=1>
<Record Recommended='Fabio Scarpa' Strength=1>
<Record Recommended='Vanessa del Rio' Strength=1>
<Record Recommended='Eric Yellin' Strength=1>
<Record Recommended='Rachel Singer' Strength=1>
<Record Recommended='Jerry Strivelli' Strength=1>
<Record Recommended='Klaus-Jürgen Tews' Strength=1>
<Record Recommended='Sylvia Miles' Strength=1>
<Record Recommended='Barbara Stanwyck' Strength=1>
<Record Recommended='Reginald Farmer' Strength=1>
<Record Recommended='Rüdiger Klink' Strength=1>
<Record Recommended='Tom Townsend' Strength=1>
<Record Recommended='Alexandra Maria Lara' Strength=1>
<Record Recommended='Ray Proscia' Strength=1>
<Record Recommended='Marlène Jobert' Strength=1>
<Record Recommended='Torri Higginson' Strength=1>
<Record Recommended='Chiaki Kuriyama' Strength=1>
<Record Recommended='Joss Stone' Strength=1>
<Record Recommended='Steven Schub' Strength=1>
<Record Recommended='Nathalie Lunghi' Strength=1>
<Record Recommended='Lejla Hadzimuratovic' Strength=1>
<Record Recommended='Steve Howey' Strength=1>
<Record Recommended='Serge Feuillard' Strength=1>
<Record Recommended='Robert Rusler' Strength=1>
<Record Recommended='Joel Brooks' Strength=1>
<Record Recommended='Sarah Juel Werner' Strength=1>
<Record Recommended='Ezra Buzzington' Strength=1>
<Record Recommended='David Herman' Strength=1>
<Record Recommended='Eric Freeman' Strength=1>
<Record Recommended='William Beck' Strength=1>
<Record Recommended='Keeley Hawes' Strength=1>
<Record Recommended='Alexandra Wentworth' Strength=1>
<Record Recommended='Jack Gilford' Strength=1>
<Record Recommended='Steve Maye' Strength=1>
<Record Recommended='Kazuki Kitamura' Strength=1>
<Record Recommended='Jay Jacobus' Strength=1>
<Record Recommended='Edward M. Kelahan' Strength=1>
<Record Recommended='Steve Franken' Strength=1>
<Record Recommended='Todd Robert Anderson' Strength=1>
<Record Recommended='Shiri Appleby' Strength=1>
<Record Recommended='Frits Helmuth' Strength=1>
<Record Recommended='Kristina Wayborn' Strength=1>
<Record Recommended='Catharine Bolz' Strength=1>
<Record Recommended='Nancy Baldwin' Strength=1>
<Record Recommended='Firmine Richard' Strength=1>
<Record Recommended='Karl Heinz Vosgerau' Strength=1>
<Record Recommended='Amber Scott' Strength=1>
<Record Recommended='Jeremy Kemp' Strength=1>
<Record Recommended='Tom Virtue' Strength=1>
<Record Recommended='Shannan Click' Strength=1>
<Record Recommended='Patricio Castillo' Strength=1>
<Record Recommended='John Anderson' Strength=1>
<Record Recommended='Lisa Kreuzer' Strength=1>
<Record Recommended='Jason Marsden' Strength=1>
<Record Recommended='John David Carson' Strength=1>
<Record Recommended='Virgil Warner' Strength=1>
<Record Recommended='Jim Wynorski' Strength=1>
<Record Recommended='Joachim Król' Strength=1>
<Record Recommended='Christine Estabrook' Strength=1>
<Record Recommended='Sam Hanna' Strength=1>
<Record Recommended='Sasha Jenson' Strength=1>
<Record Recommended='Janet Wood' Strength=1>
<Record Recommended='Daniel Logan' Strength=1>
<Record Recommended='Conrad Goode' Strength=1>
<Record Recommended='Kristi Frank' Strength=1>
<Record Recommended="Fiona O'Shaughnessy" Strength=1>
<Record Recommended='Matt McKenzie' Strength=1>
<Record Recommended='D.L. Hughley' Strength=1>
<Record Recommended='William Schallert' Strength=1>
<Record Recommended='Benoît Poelvoorde' Strength=1>
<Record Recommended='James G. Hoosier' Strength=1>
<Record Recommended='Frank Pietrangolare' Strength=1>
<Record Recommended='Jason Acuña' Strength=1>
<Record Recommended='Blandine Pélissier' Strength=1>
<Record Recommended='Wolfgang Preiss' Strength=1>
<Record Recommended='John Woodvine' Strength=1>
<Record Recommended='Cheryl Freeman' Strength=1>
<Record Recommended='Wolfram Handel' Strength=1>
<Record Recommended='Sarah Steele' Strength=1>
<Record Recommended='Andrea Renzi' Strength=1>
<Record Recommended='Heiner Lauterbach' Strength=1>
<Record Recommended='MacIntyre Dixon' Strength=1>
<Record Recommended='Denis Arndt' Strength=1>
<Record Recommended='John Ingle' Strength=1>
<Record Recommended='Vanessa Angel' Strength=1>
<Record Recommended='Michael Eklund' Strength=1>
<Record Recommended='Jasper Polish' Strength=1>
<Record Recommended='Eugene Lipinski' Strength=1>
<Record Recommended='Sonya Salomaa' Strength=1>
<Record Recommended='Sarah Holcomb' Strength=1>
<Record Recommended='Martin Mull' Strength=1>
<Record Recommended='Douglas Wilmer' Strength=1>
<Record Recommended='Roger Allam' Strength=1>
<Record Recommended='Leah Pinsent' Strength=1>
<Record Recommended='Staffan Kihlbom' Strength=1>
<Record Recommended='Toby Keith' Strength=1>
<Record Recommended='Alma Beltran' Strength=1>
<Record Recommended='Serge Rousseau' Strength=1>
<Record Recommended='Joris Gratwohl' Strength=1>
<Record Recommended='Mario Pilar' Strength=1>
<Record Recommended='Barbara Auer' Strength=1>
<Record Recommended='Michael Panes' Strength=1>
<Record Recommended='John Taylor' Strength=1>
<Record Recommended='Gary Trousdale' Strength=1>
<Record Recommended='Ken Watanabe' Strength=1>
<Record Recommended='Ryun Yu' Strength=1>
<Record Recommended='Leos Carax' Strength=1>
<Record Recommended='Darius McCrary' Strength=1>
<Record Recommended='Anne De Salvo' Strength=1>
<Record Recommended='Lutz Stückrath' Strength=1>
<Record Recommended='Derek Greene' Strength=1>
<Record Recommended='Rick Zumwalt' Strength=1>
<Record Recommended='Ritch Brinkley' Strength=1>
<Record Recommended='Timothy Peach' Strength=1>
<Record Recommended='Michael Habeck' Strength=1>
<Record Recommended='Mark Rydell' Strength=1>
<Record Recommended='Bernard Hocke' Strength=1>
<Record Recommended='Bjorn Johnson' Strength=1>
<Record Recommended='Robert V. Greene' Strength=1>
<Record Recommended='Alberta Watson' Strength=1>
<Record Recommended='Vincene Wallace' Strength=1>
<Record Recommended='Josh Richman' Strength=1>
<Record Recommended='Doris Belack' Strength=1>
<Record Recommended='Michael Polish' Strength=1>
<Record Recommended='Lara Steinick' Strength=1>
<Record Recommended='Zuleikha Robinson' Strength=1>
<Record Recommended='Edward Saxon' Strength=1>
<Record Recommended='Dawn Ressy' Strength=1>
<Record Recommended='Christy Hartburg' Strength=1>
<Record Recommended='Skip Ward' Strength=1>
<Record Recommended='Ross Shafer' Strength=1>
<Record Recommended='Dana Davis' Strength=1>
<Record Recommended='Lucia Rijker' Strength=1>
<Record Recommended='Sarah Backhous' Strength=1>
<Record Recommended='Noah Gray-Cabey' Strength=1>
<Record Recommended='Simon Reynolds' Strength=1>
<Record Recommended='James Cada' Strength=1>
<Record Recommended='Katharina Tanner' Strength=1>
<Record Recommended='Jon Lormer' Strength=1>
<Record Recommended='Linda Blair' Strength=1>
<Record Recommended='Bruce Jarchow' Strength=1>
<Record Recommended='Mélanie Doutey' Strength=1>
<Record Recommended='Louis K. Sher' Strength=1>
<Record Recommended='Edith Atwater' Strength=1>
<Record Recommended='Christopher Reed' Strength=1>
<Record Recommended='James Roday' Strength=1>
<Record Recommended='Matt Stone' Strength=1>
<Record Recommended='Larry B. Scott' Strength=1>
<Record Recommended='Deuandra T. Brown' Strength=1>
<Record Recommended='Jennifer Jostyn' Strength=1>
<Record Recommended='Blue' Strength=1>
<Record Recommended='Bruce Scott' Strength=1>
<Record Recommended='Salvador Sánchez' Strength=1>
<Record Recommended='Henry Fonda' Strength=1>
<Record Recommended='Milo Addica' Strength=1>
<Record Recommended='Ralf Wolter' Strength=1>
<Record Recommended='Margaret Field' Strength=1>
<Record Recommended='Kathy Shao-Lin Lee' Strength=1>
<Record Recommended='David Richmond-Peck' Strength=1>
<Record Recommended='Robert Cavanah' Strength=1>
<Record Recommended='Michael Champion' Strength=1>
<Record Recommended='Eamonn Walker' Strength=1>
<Record Recommended='Clotilde Mollet' Strength=1>
<Record Recommended='Shae Marks' Strength=1>
<Record Recommended='Suliamen El Hadi' Strength=1>
<Record Recommended='Clarence Moore' Strength=1>
<Record Recommended='Lysette Anthony' Strength=1>
<Record Recommended='Anne Seymour' Strength=1>
<Record Recommended='Katherine Parkinson' Strength=1>
<Record Recommended='Sonny Landham' Strength=1>
<Record Recommended='Alice Drummond' Strength=1>
<Record Recommended='Aeryk Egan' Strength=1>
<Record Recommended='Pamela Stephenson' Strength=1>
<Record Recommended='Anthony Caruso' Strength=1>
<Record Recommended='Ramsey Campbell' Strength=1>
<Record Recommended='Andrew Schofield' Strength=1>
<Record Recommended='Corinne Reilly' Strength=1>
<Record Recommended='Caroline Sihol' Strength=1>
<Record Recommended='Michael Roberts' Strength=1>
<Record Recommended='Torsten Voges' Strength=1>
<Record Recommended='Ian Blake Nelson' Strength=1>
<Record Recommended='Adam James' Strength=1>
<Record Recommended='Judith Wetzell' Strength=1>
<Record Recommended='Martin Gabel' Strength=1>
<Record Recommended='Ulrike Willenbacher' Strength=1>
<Record Recommended='Rod Taylor' Strength=1>
<Record Recommended='Guy Ritchie' Strength=1>
<Record Recommended='Raymond J. Lee' Strength=1>
<Record Recommended='Jayne Atkinson' Strength=1>
<Record Recommended='Jason Wiles' Strength=1>
<Record Recommended='Mark Kiely' Strength=1>
<Record Recommended='Rico Devereaux' Strength=1>
<Record Recommended='Peter Cornwell' Strength=1>
<Record Recommended='Camille De Pazzis' Strength=1>
<Record Recommended='Sam Thakur' Strength=1>
<Record Recommended='Julian Bucknall' Strength=1>
<Record Recommended='Clinton Leupp' Strength=1>
<Record Recommended='Gertraud Klawitter' Strength=1>
<Record Recommended='Rebecka Hemse' Strength=1>
<Record Recommended='Joely Fisher' Strength=1>
<Record Recommended='Philip Akin' Strength=1>
<Record Recommended='James Douglas Haskins' Strength=1>
<Record Recommended='Philip Stone' Strength=1>
<Record Recommended='Vanessa Bell Calloway' Strength=1>
<Record Recommended='Alex Scarlis' Strength=1>
<Record Recommended='Tess Harper' Strength=1>
<Record Recommended='Kina Cosper' Strength=1>
<Record Recommended='Tony Longo' Strength=1>
<Record Recommended='Mark Johnson' Strength=1>
<Record Recommended='Simon Lloyd-Roberts' Strength=1>
<Record Recommended='Joan Staley' Strength=1>
<Record Recommended='Kipp Hamilton' Strength=1>
<Record Recommended='Debralee Scott' Strength=1>
<Record Recommended='Serge Reggiani' Strength=1>
<Record Recommended='Jaecki Schwarz' Strength=1>
<Record Recommended='Joanna Lumley' Strength=1>
<Record Recommended='Daoud Spencer' Strength=1>
<Record Recommended='Kent Broadhurst' Strength=1>
<Record Recommended='Ntare Mwine' Strength=1>
<Record Recommended='Darrin Reed' Strength=1>
<Record Recommended='Dani' Strength=1>
<Record Recommended='Jeremy Ratchford' Strength=1>
<Record Recommended='Jonathan Firth' Strength=1>
<Record Recommended='Busty Dusty' Strength=1>
<Record Recommended='Christopher Egan' Strength=1>
<Record Recommended='Jacques Spiesser' Strength=1>
<Record Recommended='Daniel Mays' Strength=1>
<Record Recommended='Malick Bowens' Strength=1>
<Record Recommended='Ayanna Berkshire' Strength=1>
<Record Recommended='Claire Maurier' Strength=1>
<Record Recommended='Alan Boyce' Strength=1>
<Record Recommended='Simo Mogwaza' Strength=1>
<Record Recommended='Logan Lerman' Strength=1>
<Record Recommended='Ivana Nolte' Strength=1>
<Record Recommended='Erik Goertz' Strength=1>
<Record Recommended='John Eastham' Strength=1>
<Record Recommended='Kate Jennings Grant' Strength=1>
<Record Recommended='Philippe Babin' Strength=1>
<Record Recommended='Marie-Christine Adam' Strength=1>
<Record Recommended='Hélène Cardona' Strength=1>
<Record Recommended='Jake Abraham' Strength=1>
<Record Recommended='Anny Nelsen' Strength=1>
<Record Recommended='Ramon Bieri' Strength=1>
<Record Recommended='Malcolm David Kelley' Strength=1>
<Record Recommended='Germán Cobos' Strength=1>
<Record Recommended='Scott Capurro' Strength=1>
<Record Recommended='J.D. Walsh' Strength=1>
<Record Recommended='Yorgo Voyagis' Strength=1>
<Record Recommended='Paolo Montalban' Strength=1>
<Record Recommended='Warren Berlinger' Strength=1>
<Record Recommended='Wendell Pierce' Strength=1>
<Record Recommended='John Karlen' Strength=1>
<Record Recommended='Erik Veldre' Strength=1>
<Record Recommended='Garrett Lombard' Strength=1>
<Record Recommended='James M. Hausler' Strength=1>
<Record Recommended='Tanya Roberts' Strength=1>
<Record Recommended='Steve Masters' Strength=1>
<Record Recommended='Adam Herschman' Strength=1>
<Record Recommended='Richard Burgi' Strength=1>
<Record Recommended='Tyler Gatton' Strength=1>
<Record Recommended='Steve Park' Strength=1>
<Record Recommended='Vladimir Cuk' Strength=1>
<Record Recommended='Frank Fontaine' Strength=1>
<Record Recommended='Ed Flanders' Strength=1>
<Record Recommended='James Sikking' Strength=1>
<Record Recommended='Al Matthews' Strength=1>
<Record Recommended='William Ostrander' Strength=1>
<Record Recommended='Muse Watson' Strength=1>
<Record Recommended='Jessica Cauffiel' Strength=1>
<Record Recommended='Robert Newton' Strength=1>
<Record Recommended='Maurice Bénichou' Strength=1>
<Record Recommended='Bridgette Wilson' Strength=1>
<Record Recommended='Catherine McGoohan' Strength=1>
<Record Recommended='Alastair Douglas' Strength=1>
<Record Recommended='Maggie Roswell' Strength=1>
<Record Recommended='Ime Etuk' Strength=1>
<Record Recommended='Jessica Nagle' Strength=1>
<Record Recommended='Muriel Fouilland' Strength=1>
<Record Recommended='John Boncore' Strength=1>
<Record Recommended='David Harewood' Strength=1>
<Record Recommended='Michael Mantenuto' Strength=1>
<Record Recommended='Victoria Thompson' Strength=1>
<Record Recommended='Jonathan Penner' Strength=1>
<Record Recommended='Lynda Boyd' Strength=1>
<Record Recommended='Louis Mustillo' Strength=1>
<Record Recommended='Marc Boyle' Strength=1>
<Record Recommended='Jaime Osorio Gómez' Strength=1>
<Record Recommended='Sean Stone' Strength=1>
<Record Recommended='Elizabeth Newett' Strength=1>
<Record Recommended='Kevin Chevalia' Strength=1>
<Record Recommended='Nadia Farès' Strength=1>
<Record Recommended='Mark Kozelek' Strength=1>
<Record Recommended='Bruce McDonald' Strength=1>
<Record Recommended='Arnaldo Santana' Strength=1>
<Record Recommended='Chief Gordon' Strength=1>
<Record Recommended='Matt Patresi' Strength=1>
<Record Recommended='Christopher Ettridge' Strength=1>
<Record Recommended='Bill Campbell' Strength=1>
<Record Recommended='Nicholas Boulton' Strength=1>
<Record Recommended='Jean-Yves Gautier' Strength=1>
<Record Recommended='Andrew Mackin' Strength=1>
<Record Recommended='Emilio Adrisani' Strength=1>
<Record Recommended='Rod McCary' Strength=1>
<Record Recommended='Mike Pagano' Strength=1>
<Record Recommended='Deanna Dawn' Strength=1>
<Record Recommended='Russell Yuen' Strength=1>
<Record Recommended='GiGi Erneta' Strength=1>
<Record Recommended='Brant von Hoffman' Strength=1>
<Record Recommended='Michelle Horn' Strength=1>
<Record Recommended='Vincent Gardenia' Strength=1>
<Record Recommended='Frank Hennessy' Strength=1>
<Record Recommended='Roger R. Cross' Strength=1>
<Record Recommended='Henry Goodman' Strength=1>
<Record Recommended='Ché J. Avery' Strength=1>
<Record Recommended='Katheryn Winnick' Strength=1>
<Record Recommended='Margit Bara' Strength=1>
<Record Recommended='Kgomotso Seitshohlo' Strength=1>
<Record Recommended='Jill Hennessy' Strength=1>
<Record Recommended='Sabrina Geerinckx' Strength=1>
<Record Recommended='Jose Pomedio Monedero' Strength=1>
<Record Recommended='Henric Nieminen' Strength=1>
<Record Recommended='José María Tasso' Strength=1>
<Record Recommended='Derrick Damon Reeve' Strength=1>
<Record Recommended='Ljubomir Kerekes' Strength=1>
<Record Recommended='Ed Begley' Strength=1>
<Record Recommended='Lewis Arquette' Strength=1>
<Record Recommended='Charlie Phillips' Strength=1>
<Record Recommended='Robby the Robot' Strength=1>
<Record Recommended="Jan D'Arcy" Strength=1>
<Record Recommended='Peter Kuiper' Strength=1>
<Record Recommended='Elle Peterson' Strength=1>
<Record Recommended='Louise Lasser' Strength=1>
<Record Recommended='Elaine Stritch' Strength=1>
<Record Recommended='Otto Sanchez' Strength=1>
<Record Recommended='Dominiquie Vandenberg' Strength=1>
<Record Recommended='Doris Leader Charge' Strength=1>
<Record Recommended='Ewald Larsen' Strength=1>
<Record Recommended='Colin McFarlane' Strength=1>
<Record Recommended='Ben Browder' Strength=1>
<Record Recommended='John Pleshette' Strength=1>
<Record Recommended='David Lodge' Strength=1>
<Record Recommended='James Eckhouse' Strength=1>
<Record Recommended='Javier Coromina' Strength=1>
<Record Recommended='John Hancock' Strength=1>
<Record Recommended='Luke Gallant' Strength=1>
<Record Recommended='Gilles Ségal' Strength=1>
<Record Recommended='Ray Allen' Strength=1>
<Record Recommended='Wesley Jonathan' Strength=1>
<Record Recommended='Hefin Wyn' Strength=1>
<Record Recommended='Timyra-Joi Beatty' Strength=1>
<Record Recommended='Christian Cousins' Strength=1>
<Record Recommended='Francesca Piliero' Strength=1>
<Record Recommended='Michael Beach' Strength=1>
<Record Recommended='Juno Ruddell' Strength=1>
<Record Recommended='Franz Stiefel' Strength=1>
<Record Recommended='Mark Famiglietti' Strength=1>
<Record Recommended='Jutta Hoffmann' Strength=1>
<Record Recommended='Omari Hardwick' Strength=1>
<Record Recommended='Mariah Massa' Strength=1>
<Record Recommended='Richard Gates' Strength=1>
<Record Recommended='Jordan Carlos' Strength=1>
<Record Recommended='Luke Askew' Strength=1>
<Record Recommended='Keith Washington' Strength=1>
<Record Recommended='Horatio Sanz' Strength=1>
<Record Recommended="N'Bushe Wright" Strength=1>
<Record Recommended='James DeBello' Strength=1>
<Record Recommended='Titus Moede' Strength=1>
<Record Recommended='Sophia Lin' Strength=1>
<Record Recommended='Natalie Imbruglia' Strength=1>
<Record Recommended='Burl Ives' Strength=1>
<Record Recommended='Siegfried Hömke' Strength=1>
<Record Recommended='Brandon Molale' Strength=1>
<Record Recommended='Jonathan Kimmel' Strength=1>
<Record Recommended='Scott Weinger' Strength=1>
<Record Recommended='Marvin Hunter' Strength=1>
<Record Recommended='Lorella Cravotta' Strength=1>
<Record Recommended='Jeronn C. Williams' Strength=1>
<Record Recommended='Christopher Collet' Strength=1>
<Record Recommended='Amy Levitt' Strength=1>
<Record Recommended='Günther Grabbert' Strength=1>
<Record Recommended='Lou Cutell' Strength=1>
<Record Recommended='Kenneth Cranham' Strength=1>
<Record Recommended='Marie-Jeanne Montfajon' Strength=1>
<Record Recommended='Jane How' Strength=1>
<Record Recommended='Norman Wooland' Strength=1>
<Record Recommended='Christopher Allen Nelson' Strength=1>
<Record Recommended='Alice Hirson' Strength=1>
<Record Recommended='Cecilia Suárez' Strength=1>
<Record Recommended='Dan Thiel' Strength=1>
<Record Recommended='Vincent Moscato' Strength=1>
<Record Recommended='Virginia Williams' Strength=1>
<Record Recommended='Tania Verafield' Strength=1>
<Record Recommended='Lois Nettleton' Strength=1>
<Record Recommended='David Bradley' Strength=1>
<Record Recommended='Anders Nyborg' Strength=1>
<Record Recommended='Lenny Juliano' Strength=1>
<Record Recommended='Mady Kaplan' Strength=1>
<Record Recommended='Alec Vigil' Strength=1>
<Record Recommended='Richard Rifkin' Strength=1>
<Record Recommended='Lisbet Lundquist' Strength=1>
<Record Recommended='Miles Anderson' Strength=1>
<Record Recommended='Carole Copeland' Strength=1>
<Record Recommended='Ryan Robbins' Strength=1>
<Record Recommended='Patrick Louis' Strength=1>
<Record Recommended='Jeffrey Nordling' Strength=1>
<Record Recommended='Larry David' Strength=1>
<Record Recommended='Francisco Rabal' Strength=1>
<Record Recommended='Lucas Crespi' Strength=1>
<Record Recommended='Sean Fox' Strength=1>
<Record Recommended='David Jensen' Strength=1>
<Record Recommended='Bob Orwig' Strength=1>
<Record Recommended='Krystal Rohrer' Strength=1>
<Record Recommended='Victoire Thivisol' Strength=1>
<Record Recommended='E.J. Rodriguez' Strength=1>
<Record Recommended='Laila Mrabti' Strength=1>
<Record Recommended='Richard Narita' Strength=1>
<Record Recommended='Joseph Rigano' Strength=1>
<Record Recommended='Natalie Wood' Strength=1>
<Record Recommended='John McMartin' Strength=1>
<Record Recommended='David Sotelo' Strength=1>
<Record Recommended='Celino Bleiweiß' Strength=1>
<Record Recommended='Tanushree Dutta' Strength=1>
<Record Recommended='Sharon Lee' Strength=1>
<Record Recommended='Charles Borromel' Strength=1>
<Record Recommended='Luke Massery' Strength=1>
<Record Recommended='Claudio Santamaria' Strength=1>
<Record Recommended='David Blaine' Strength=1>
<Record Recommended='Aria Noelle Curzon' Strength=1>
<Record Recommended='Jennifer Taylor' Strength=1>
<Record Recommended='Darcy DeMoss' Strength=1>
<Record Recommended='Francesca Smith' Strength=1>
<Record Recommended='Morris Birdyellowhead' Strength=1>
<Record Recommended='Milton Berle' Strength=1>
<Record Recommended='Vadim Glowna' Strength=1>
<Record Recommended='Robin Givens' Strength=1>
<Record Recommended='Anne Louise Hassing' Strength=1>
<Record Recommended='Georgann Johnson' Strength=1>
<Record Recommended='Buck Henry' Strength=1>
<Record Recommended='Lucy Cohu' Strength=1>
<Record Recommended='Kevyn Major Howard' Strength=1>
<Record Recommended='Jami Bernard' Strength=1>
<Record Recommended='Eduard von Winterstein' Strength=1>
<Record Recommended='Nat Benchley' Strength=1>
<Record Recommended='Tony London' Strength=1>
<Record Recommended='Peter Köhncke' Strength=1>
<Record Recommended='Jennifer Blaire' Strength=1>
<Record Recommended='Mina E. Mina' Strength=1>
<Record Recommended='Matthew Fenton' Strength=1>
<Record Recommended='Jamel Debbouze' Strength=1>
<Record Recommended='Richard Gabai' Strength=1>
<Record Recommended='Shelley Berman' Strength=1>
<Record Recommended='Tyler Parkinson' Strength=1>
<Record Recommended='Deborah Raffin' Strength=1>
<Record Recommended='Virginia Díez' Strength=1>
<Record Recommended='Steve Gresser' Strength=1>
<Record Recommended='Cheryl Sparks' Strength=1>
<Record Recommended='Jack Benny' Strength=1>
<Record Recommended='Felicity Jones' Strength=1>
<Record Recommended='Anne Openshaw' Strength=1>
<Record Recommended='Albert Michel Jr.' Strength=1>
<Record Recommended='Richard Belzer' Strength=1>
<Record Recommended='Silvana Blasi' Strength=1>
<Record Recommended='Heavy D' Strength=1>
<Record Recommended='Robert James Raymond' Strength=1>
<Record Recommended='David Kriegel' Strength=1>
<Record Recommended='Víctor Coyote' Strength=1>
<Record Recommended='Patricia Place' Strength=1>
<Record Recommended='Mark Cohen' Strength=1>
<Record Recommended='Jeri Ryan' Strength=1>
<Record Recommended='James Eason' Strength=1>
<Record Recommended='Wendy Morgan' Strength=1>
<Record Recommended='Joe Cashman' Strength=1>
<Record Recommended='Tawny Peaks' Strength=1>
<Record Recommended='Augie Blunt' Strength=1>
<Record Recommended='Hans Feldner' Strength=1>
<Record Recommended='Richard Boes' Strength=1>
<Record Recommended='Natalja J. Iljina' Strength=1>
<Record Recommended='Lilia Skala' Strength=1>
<Record Recommended='Zac Efron' Strength=1>
<Record Recommended='Jacno' Strength=1>
<Record Recommended='Willi Schrade' Strength=1>
<Record Recommended='Franck Milhan' Strength=1>
<Record Recommended='Carlos Rodríguez Ramos' Strength=1>
<Record Recommended='Tyree Michael Simpson' Strength=1>
<Record Recommended='Nancy Lollar' Strength=1>
<Record Recommended='Kate Clarke' Strength=1>
<Record Recommended='Emil Marwa' Strength=1>
<Record Recommended='Jason Pennycooke' Strength=1>
<Record Recommended='Eddie Mills' Strength=1>
<Record Recommended='Melvil Poupaud' Strength=1>
<Record Recommended='Debi Derryberry' Strength=1>
<Record Recommended='Theodore Bikel' Strength=1>
<Record Recommended='Robert Strauss' Strength=1>
<Record Recommended='Gene Kelly' Strength=1>
<Record Recommended='John Hyams' Strength=1>
<Record Recommended='Raymond Coulthard' Strength=1>
<Record Recommended='Ruben Santiago-Hudson' Strength=1>
<Record Recommended='Henning Jensen' Strength=1>
<Record Recommended='Sean Sullivan' Strength=1>
<Record Recommended='Wilhelm Koch-Hooge' Strength=1>
<Record Recommended='Lew Hopson' Strength=1>
<Record Recommended='August Zirner' Strength=1>
<Record Recommended='Jordan Prentice' Strength=1>
<Record Recommended='Graham Phillips' Strength=1>
<Record Recommended='Vishal Malhotra' Strength=1>
<Record Recommended="Richard O'Brien" Strength=1>
<Record Recommended='Albert Dupontel' Strength=1>
<Record Recommended='David Holbrook' Strength=1>
<Record Recommended='Feodor Chaliapin Jr.' Strength=1>
<Record Recommended='Vincent Lindon' Strength=1>
<Record Recommended='Brett Cullen' Strength=1>
<Record Recommended='Andrew Farago' Strength=1>
<Record Recommended='Kerry Walker' Strength=1>
<Record Recommended='Lola Cook' Strength=1>
<Record Recommended='Robert Phillips' Strength=1>
<Record Recommended='Jack Weston' Strength=1>
<Record Recommended='Polly Walker' Strength=1>
<Record Recommended='Duncan McLeod' Strength=1>
<Record Recommended='Daniel Hugh Kelly' Strength=1>
<Record Recommended='Stuart Pankin' Strength=1>
<Record Recommended='Michael Ealy' Strength=1>
<Record Recommended='Douglas Kenney' Strength=1>
<Record Recommended='Joe Seneca' Strength=1>
<Record Recommended='Rab Reilly' Strength=1>
<Record Recommended='Matt Barr' Strength=1>
<Record Recommended='Marianne Marks' Strength=1>
<Record Recommended='William Moseley' Strength=1>
<Record Recommended='Lorenzo Monet' Strength=1>
<Record Recommended='Armando Riesco' Strength=1>
<Record Recommended='Pierre Vaneck' Strength=1>
<Record Recommended='Tina Engel' Strength=1>
<Record Recommended='Aviva Briefel' Strength=1>
<Record Recommended='Kyla Pratt' Strength=1>
<Record Recommended='Su Ling' Strength=1>
<Record Recommended="Vito D'Ambrosio" Strength=1>
<Record Recommended='Madeleine Damien' Strength=1>
<Record Recommended='Garry McDonald' Strength=1>
<Record Recommended='Michel Subor' Strength=1>
<Record Recommended='Frank Bolger' Strength=1>
<Record Recommended='Jake Weber' Strength=1>
<Record Recommended='Tori Davis' Strength=1>
<Record Recommended='Hon Lam Bau' Strength=1>
<Record Recommended='Connor Price' Strength=1>
<Record Recommended='Andrea Roth' Strength=1>
<Record Recommended='Carmine Foresta' Strength=1>
<Record Recommended='Valerie Gogan' Strength=1>
<Record Recommended='Mary Ann Thebus' Strength=1>
<Record Recommended="Frank D'Annibale" Strength=1>
<Record Recommended='George Newbern' Strength=1>
<Record Recommended="Emile Abossolo M'bo" Strength=1>
<Record Recommended='Martha Chaves' Strength=1>
<Record Recommended='Bill Goldberg' Strength=1>
<Record Recommended='Mai Lin' Strength=1>
<Record Recommended='Jascha Washington' Strength=1>
<Record Recommended='Milos Forman' Strength=1>
<Record Recommended='Paul Lockwood' Strength=1>
<Record Recommended='Jami Ferrell' Strength=1>
<Record Recommended='Aitana Sánchez-Gijón' Strength=1>
<Record Recommended='Monique Gabriela Curnen' Strength=1>
<Record Recommended='Irving Hellman' Strength=1>
<Record Recommended='Mattia Sbragia' Strength=1>
<Record Recommended='Charles Cyphers' Strength=1>
<Record Recommended='Matt LeBlanc' Strength=1>
<Record Recommended='Nancy Kovack' Strength=1>
<Record Recommended='Anthony Quayle' Strength=1>
<Record Recommended='Joel Edgerton' Strength=1>
<Record Recommended='Walter Schramm' Strength=1>
<Record Recommended='Jean-Marc Montalto' Strength=1>
<Record Recommended='Marco Hofschneider' Strength=1>
<Record Recommended='Jeffery Kissoon' Strength=1>
<Record Recommended='J. Stephen Brady' Strength=1>
<Record Recommended='Richard Pierson' Strength=1>
<Record Recommended='Andréas Voutsinas' Strength=1>
<Record Recommended='Matti Pellonpää' Strength=1>
<Record Recommended='Ali Landry' Strength=1>
<Record Recommended='Sam Lloyd' Strength=1>
<Record Recommended='Ninetto Davoli' Strength=1>
<Record Recommended='Abraham Verduzco' Strength=1>
<Record Recommended='Michael Jordan' Strength=1>
<Record Recommended='Samuel E. Wright' Strength=1>
<Record Recommended='Wilfried Hochholdinger' Strength=1>
<Record Recommended='Brad Leland' Strength=1>
<Record Recommended='Adrienne Barbeau' Strength=1>
<Record Recommended='Jeannine Taylor' Strength=1>
<Record Recommended='Hansjörg Felmy' Strength=1>
<Record Recommended='Brady Corbet' Strength=1>
<Record Recommended='Gal Gadot' Strength=1>
<Record Recommended='Susie Porter' Strength=1>
<Record Recommended='Jennifer Warren' Strength=1>
<Record Recommended='Karl Fischer' Strength=1>
<Record Recommended='Walter Pidgeon' Strength=1>
<Record Recommended='Jack Riley' Strength=1>
<Record Recommended='Regina Bianchi' Strength=1>
<Record Recommended='Betty Loewen' Strength=1>
<Record Recommended='Rocco Sisto' Strength=1>
<Record Recommended='Tuva Novotny' Strength=1>
<Record Recommended='Julia K. Murney' Strength=1>
<Record Recommended='Edward J. Rosen' Strength=1>
<Record Recommended='Thomas Quinn' Strength=1>
<Record Recommended='Bruno Stori' Strength=1>
<Record Recommended='Alain Doutey' Strength=1>
<Record Recommended='Jim Turner' Strength=1>
<Record Recommended='Otto Lange' Strength=1>
<Record Recommended='Janet Blair' Strength=1>
<Record Recommended='Heath Jones' Strength=1>
<Record Recommended='Melissa Moore' Strength=1>
<Record Recommended='Samuel Le Bihan' Strength=1>
<Record Recommended='Deneen Tyler' Strength=1>
<Record Recommended='Jean Villepique' Strength=1>
<Record Recommended='Pratik Dalvi' Strength=1>
<Record Recommended='Bess Armstrong' Strength=1>
<Record Recommended='Clara Bellar' Strength=1>
<Record Recommended='Stephen Hawking' Strength=1>
<Record Recommended='Tim Pearce' Strength=1>
<Record Recommended='Tanya Lawson' Strength=1>
<Record Recommended='Nabil Elouahabi' Strength=1>
<Record Recommended='David Early' Strength=1>
<Record Recommended='Brian Stollery' Strength=1>
<Record Recommended='Cheryl Pollak' Strength=1>
<Record Recommended='Niki Harris' Strength=1>
<Record Recommended='Anna-Mart van der Merwe' Strength=1>
<Record Recommended='Shelley Hack' Strength=1>
<Record Recommended='Nia Ann' Strength=1>
<Record Recommended='Hal Havins' Strength=1>
<Record Recommended='Karin Dor' Strength=1>
<Record Recommended='Kahena Saighi' Strength=1>
<Record Recommended='Martin Benson' Strength=1>
<Record Recommended='Vladimiros Kiriakidis' Strength=1>
<Record Recommended='Riley Smith' Strength=1>
<Record Recommended='Robert Swan' Strength=1>
<Record Recommended='Rex Harrison' Strength=1>
<Record Recommended='Sabine Tingry' Strength=1>
<Record Recommended='Michelle Johnson' Strength=1>
<Record Recommended='Colette Hiller' Strength=1>
<Record Recommended='Cécile Vassort' Strength=1>
<Record Recommended='Olivier Parnière' Strength=1>
<Record Recommended='John Doman' Strength=1>
<Record Recommended='Brooke Langton' Strength=1>
<Record Recommended='Marshall Allman' Strength=1>
<Record Recommended='Brian H. Dierker' Strength=1>
<Record Recommended='Sarah Roemer' Strength=1>
<Record Recommended='Alex Meraz' Strength=1>
<Record Recommended='Trent McMullen' Strength=1>
<Record Recommended='Marcus T. Paulk' Strength=1>
<Record Recommended='Hubert Suschka' Strength=1>
<Record Recommended='Leighton Meester' Strength=1>
<Record Recommended='Connie Britton' Strength=1>
<Record Recommended='Claudia Cron' Strength=1>
<Record Recommended='Joseph Runningfox' Strength=1>
<Record Recommended='Gene Canfield' Strength=1>
<Record Recommended='Alana Curry' Strength=1>
<Record Recommended='Sofie Gråbøl' Strength=1>
<Record Recommended='Mduduzi Mabaso' Strength=1>
<Record Recommended='Daniel Gélin' Strength=1>
<Record Recommended='Mark Lindsay Chapman' Strength=1>
<Record Recommended='Isabel Conner' Strength=1>
<Record Recommended='Hugh Quarshie' Strength=1>
<Record Recommended='Claudia Choi' Strength=1>
<Record Recommended='Christy Carrera' Strength=1>
<Record Recommended='Kyla Dang' Strength=1>
<Record Recommended='Joshua Wolf Coleman' Strength=1>
<Record Recommended='David Ariniello' Strength=1>
<Record Recommended='Stéphane Demers' Strength=1>
<Record Recommended='Adam LeFevre' Strength=1>
<Record Recommended='Imogen Stubbs' Strength=1>
<Record Recommended='John Fleck' Strength=1>
<Record Recommended='Robert Robertson' Strength=1>
<Record Recommended='Sarah Koskoff' Strength=1>
<Record Recommended='Judson Mills' Strength=1>
<Record Recommended='Dennis Fimple' Strength=1>
<Record Recommended='David Niven' Strength=1>
<Record Recommended='Gary Lewis' Strength=1>
<Record Recommended='Haluk Bilginer' Strength=1>
<Record Recommended='Elisabeth Moss' Strength=1>
<Record Recommended='Tony Cox' Strength=1>
<Record Recommended='Jessica Schwarz' Strength=1>
<Record Recommended='José Carlos Ruiz' Strength=1>
<Record Recommended='Hannah Marks' Strength=1>
<Record Recommended='Ana López Mercado' Strength=1>
<Record Recommended='Elijah Kelley' Strength=1>
<Record Recommended='John Lawhorn' Strength=1>
<Record Recommended='Keith A. Glascoe' Strength=1>
<Record Recommended='Christopher Thompson' Strength=1>
<Record Recommended='Lusia Strus' Strength=1>
<Record Recommended='Jacques François' Strength=1>
<Record Recommended='Hringur Ingvarsson' Strength=1>
<Record Recommended='Jarvis Dashkewytch' Strength=1>
<Record Recommended='Leah Remini' Strength=1>
<Record Recommended='Nikki Reed' Strength=1>
<Record Recommended='Jarrett Lennon' Strength=1>
<Record Recommended='Diora Baird' Strength=1>
<Record Recommended='Hans Klering' Strength=1>
<Record Recommended='Barry Kelley' Strength=1>
<Record Recommended='Dody Goodman' Strength=1>
<Record Recommended='Joey Romano' Strength=1>
<Record Recommended='Clémence Poésy' Strength=1>
<Record Recommended='Richard Karn' Strength=1>
<Record Recommended='Keiko Agena' Strength=1>
<Record Recommended='Charles Ludlam' Strength=1>
<Record Recommended='Charlie Creed-Miles' Strength=1>
<Record Recommended='Bob Zany' Strength=1>
<Record Recommended='David Fox' Strength=1>
<Record Recommended='James Phelps' Strength=1>
<Record Recommended='Scott Bairstow' Strength=1>
<Record Recommended='Roger Moore' Strength=1>
<Record Recommended='Bill Stewart' Strength=1>
<Record Recommended='Karen Oldenburg' Strength=1>
<Record Recommended='Michel Scotto di Carlo' Strength=1>
<Record Recommended='Hayley McFarland' Strength=1>
<Record Recommended='Eileen Brennan' Strength=1>
<Record Recommended='Emma Roberts' Strength=1>
<Record Recommended='Omar Ben Hassan' Strength=1>
<Record Recommended='Anezka Novak' Strength=1>
<Record Recommended='Sylvia Kristel' Strength=1>
<Record Recommended='Anthony Addabbo' Strength=1>
<Record Recommended='Günther Simon' Strength=1>
<Record Recommended='Bob Martin' Strength=1>
<Record Recommended='Scott Hazell' Strength=1>
<Record Recommended='Dwight Weist' Strength=1>
<Record Recommended='Damani Roberts' Strength=1>
<Record Recommended='Rossano Brazzi' Strength=1>
<Record Recommended='Martin Casella' Strength=1>
<Record Recommended='Liza Oxnard' Strength=1>
<Record Recommended='Paul Orchard' Strength=1>
<Record Recommended='Adrian Martinez' Strength=1>
<Record Recommended='Israel Aduramo' Strength=1>
<Record Recommended='Donatella Servadio' Strength=1>
<Record Recommended='Ralph Gonzalez' Strength=1>
<Record Recommended='Heinz Hupfer' Strength=1>
<Record Recommended='Claudio Amendola' Strength=1>
<Record Recommended='Antonin Hausknecht' Strength=1>
<Record Recommended='Peter Arne' Strength=1>
<Record Recommended="George 'Red' Schwartz" Strength=1>
<Record Recommended='Nicholas A. Puccio' Strength=1>
<Record Recommended='David Naughton' Strength=1>
<Record Recommended='Melita Morgan' Strength=1>
<Record Recommended='Michele Roberts' Strength=1>
<Record Recommended='Joey Mazzarino' Strength=1>
<Record Recommended='Kate Newby' Strength=1>
<Record Recommended='Wallace Langham' Strength=1>
<Record Recommended='Dan Castellaneta' Strength=1>
<Record Recommended='Christina Myers' Strength=1>
<Record Recommended='Gary Jones' Strength=1>
<Record Recommended='Malcolm Scott' Strength=1>
<Record Recommended='Alexa Havins' Strength=1>
<Record Recommended='Philip Whitchurch' Strength=1>
<Record Recommended='Mimmo Craig' Strength=1>
<Record Recommended='Pancho Córdova' Strength=1>
<Record Recommended='David Huband' Strength=1>
<Record Recommended='Sara Stewart' Strength=1>
<Record Recommended='Mirriam Ngomani' Strength=1>
<Record Recommended='Rika Dialina' Strength=1>
<Record Recommended='Talla S. Nowikowa' Strength=1>
<Record Recommended='Paul Brooke' Strength=1>
<Record Recommended='Joseph D. Reitman' Strength=1>
<Record Recommended='Julia McKenzie' Strength=1>
<Record Recommended='Helmut Ziehlke' Strength=1>
<Record Recommended='Immad Cohen' Strength=1>
<Record Recommended='Cheryl Ladd' Strength=1>
<Record Recommended='Jermaine Williams' Strength=1>
<Record Recommended='Jimmy Raskin' Strength=1>
<Record Recommended='Aksel Erhardtsen' Strength=1>
<Record Recommended='Chantal Neuwirth' Strength=1>
<Record Recommended='Yara Shahidi' Strength=1>
<Record Recommended='Marcia Strassman' Strength=1>
<Record Recommended='Chubby Johnson' Strength=1>
<Record Recommended='Fares Fares' Strength=1>
<Record Recommended='Anatole Taubman' Strength=1>
<Record Recommended='Margarita Franco' Strength=1>
<Record Recommended='Delphine Zentout' Strength=1>
<Record Recommended='Lisa Ray' Strength=1>
<Record Recommended='John Byrne' Strength=1>
<Record Recommended='Mary Louise Wilson' Strength=1>
<Record Recommended='Tim Colmus' Strength=1>
<Record Recommended='Jimmy Shubert' Strength=1>
<Record Recommended='Georgianna Robertson' Strength=1>
<Record Recommended='Aldona Grochal' Strength=1>
<Record Recommended='Dorothy Fielding' Strength=1>
<Record Recommended='Gary Landon Mills' Strength=1>
<Record Recommended='Lotte Munk Fure' Strength=1>
<Record Recommended='Carrie Stevens' Strength=1>
<Record Recommended='Jan Groth' Strength=1>
<Record Recommended='Burn Gorman' Strength=1>
<Record Recommended='Jean-Claude Van Damme' Strength=1>
<Record Recommended='Friedrich von Thun' Strength=1>
<Record Recommended='Rhys Darby' Strength=1>
<Record Recommended='Jean Hagen' Strength=1>
<Record Recommended='Melanee Murray' Strength=1>
<Record Recommended='Nicole Oppermann' Strength=1>
<Record Recommended='Blerim Destani' Strength=1>
<Record Recommended='Joseph Walsh' Strength=1>
<Record Recommended='Himani Shivpuri' Strength=1>
<Record Recommended='Samuel Z. Arkoff' Strength=1>
<Record Recommended='Leslie Feist' Strength=1>
<Record Recommended='Steve Toussaint' Strength=1>
<Record Recommended='Kelly Ivey' Strength=1>
<Record Recommended='Marie Déa' Strength=1>
<Record Recommended='Lissy Tempelhof' Strength=1>
<Record Recommended='Ryoko Hirosue' Strength=1>
<Record Recommended='James Madio' Strength=1>
<Record Recommended='Lisa Marie' Strength=1>
<Record Recommended='Daniel Rovai' Strength=1>
<Record Recommended='A.D. Miles' Strength=1>
<Record Recommended='Natasha Lyonne' Strength=1>
<Record Recommended='Will Sampson' Strength=1>
<Record Recommended='Gyrd Løfquist' Strength=1>
<Record Recommended='Nelly Borgeaud' Strength=1>
<Record Recommended='Dawn Danielle' Strength=1>
<Record Recommended='Courtney Chase' Strength=1>
<Record Recommended='Alan Vint' Strength=1>
<Record Recommended='Lewis Fitz-Gerald' Strength=1>
<Record Recommended='Dylan Brown' Strength=1>
<Record Recommended='Mark Darby Robinson' Strength=1>
<Record Recommended='Okwui Okpokwasili' Strength=1>
<Record Recommended='Al Israel' Strength=1>
<Record Recommended='Nikolai Kinski' Strength=1>
<Record Recommended='Kliph Scurlock' Strength=1>
<Record Recommended='Cedric Pendleton' Strength=1>
<Record Recommended='Mel Ferrer' Strength=1>
<Record Recommended='Robin Shou' Strength=1>
<Record Recommended='Walter Gotell' Strength=1>
<Record Recommended='Lebo Mashile' Strength=1>
<Record Recommended='Steve Schwelling' Strength=1>
<Record Recommended='Gloria Flora' Strength=1>
<Record Recommended='Bill MacDonald' Strength=1>
<Record Recommended='Rance Howard' Strength=1>
<Record Recommended='Brian Martell' Strength=1>
<Record Recommended='Meghan Ashley' Strength=1>
<Record Recommended='Art Chudabala' Strength=1>
<Record Recommended='Jean De Baer' Strength=1>
<Record Recommended='Miguel García' Strength=1>
<Record Recommended='Claire Cox' Strength=1>
<Record Recommended='Saïd Amadis' Strength=1>
<Record Recommended='Barbara Alyn Woods' Strength=1>
<Record Recommended='Cherie Lunghi' Strength=1>
<Record Recommended='Lois Maxwell' Strength=1>
<Record Recommended='Jordan Garrett' Strength=1>
<Record Recommended='Colette Blonigan' Strength=1>
<Record Recommended='Erwin Kohlund' Strength=1>
<Record Recommended='Craig McLachlan' Strength=1>
<Record Recommended='Mark Hammer' Strength=1>
<Record Recommended='Norman Bowler' Strength=1>
<Record Recommended='Elinor Donahue' Strength=1>
<Record Recommended='Rebecca Windheim' Strength=1>
<Record Recommended='Richard Huw' Strength=1>
<Record Recommended='Roef Ragas' Strength=1>
<Record Recommended='Dequina Moore' Strength=1>
<Record Recommended='Gilda Radner' Strength=1>
<Record Recommended='Heather Goldenhersh' Strength=1>
<Record Recommended='Meghan Heffern' Strength=1>
<Record Recommended='Robert Schenkkan' Strength=1>
<Record Recommended='Bill Hunter' Strength=1>
<Record Recommended='Thomas Cannold' Strength=1>
<Record Recommended='Jessie Kamm' Strength=1>
<Record Recommended='Shane Taylor' Strength=1>
<Record Recommended='A Martinez' Strength=1>
<Record Recommended='Alan Oppenheimer' Strength=1>
<Record Recommended='Hans Howes' Strength=1>
<Record Recommended='Rick Roberts' Strength=1>
<Record Recommended='Renato Montalbano' Strength=1>
<Record Recommended='Peggy Knudsen' Strength=1>
<Record Recommended='Christopher Lambert' Strength=1>
<Record Recommended='Ganiat Kasumu' Strength=1>
<Record Recommended='Brendan Donaldson' Strength=1>
<Record Recommended='Will Sanderson' Strength=1>
<Record Recommended='Laura Leighton' Strength=1>
<Record Recommended='Birgit Stein' Strength=1>
<Record Recommended='Lisa Arrindell Anderson' Strength=1>
<Record Recommended='Cordelia Richards' Strength=1>
<Record Recommended='Timothy Avent' Strength=1>
<Record Recommended='Jon Foster' Strength=1>
<Record Recommended='Francis Ford Coppola' Strength=1>
<Record Recommended='Erik Schumann' Strength=1>
<Record Recommended='Vanessa Branch' Strength=1>
<Record Recommended='Michael Cutt' Strength=1>
<Record Recommended='Michael Culkin' Strength=1>
<Record Recommended='Erykah Badu' Strength=1>
<Record Recommended='Nina Foch' Strength=1>
<Record Recommended='Chita Rivera' Strength=1>
<Record Recommended='Jesse Vint' Strength=1>
<Record Recommended='Aaron Au' Strength=1>
<Record Recommended='Corbin Bernsen' Strength=1>
<Record Recommended='Elaine Hendrix' Strength=1>
<Record Recommended='Cinqué Lee' Strength=1>
<Record Recommended='Stacey Travis' Strength=1>
<Record Recommended='Francesco Martoccia' Strength=1>
<Record Recommended='Marc Lynn' Strength=1>
<Record Recommended='Kurt Max Runte' Strength=1>
<Record Recommended='Jim Carrane' Strength=1>
<Record Recommended='George Smith' Strength=1>
<Record Recommended='Jason Priestley' Strength=1>
<Record Recommended='Angelina Estrada' Strength=1>
<Record Recommended='Matthew Davis' Strength=1>
<Record Recommended='David Ferry' Strength=1>
<Record Recommended='Mariana Tolbert' Strength=1>
<Record Recommended='Scott Mechlowicz' Strength=1>
<Record Recommended='Josh Peck' Strength=1>
<Record Recommended='Kenneth David Ebling' Strength=1>
<Record Recommended='Lee Delong' Strength=1>
<Record Recommended='Ron De Roxtra' Strength=1>
<Record Recommended='Joseph Cousins' Strength=1>
<Record Recommended='Barbara Crampton' Strength=1>
<Record Recommended='Suzanne Fields' Strength=1>
<Record Recommended='Andreas Wilson' Strength=1>
<Record Recommended='Harrison Pratt' Strength=1>
<Record Recommended='Beyoncé Knowles' Strength=1>
<Record Recommended='Henrik Prip' Strength=1>
<Record Recommended='Ron Falk' Strength=1>
<Record Recommended='Mark Wilson' Strength=1>
<Record Recommended='Jimmy Herman' Strength=1>
<Record Recommended='Russell Hunter' Strength=1>
<Record Recommended='Hans Putz' Strength=1>
<Record Recommended='Allison Mackie' Strength=1>
<Record Recommended='Karim Belkhadra' Strength=1>
<Record Recommended='Marie Matiko' Strength=1>
<Record Recommended='Michael Williams' Strength=1>
<Record Recommended='Chris Isaak' Strength=1>
<Record Recommended='Edwin Craig' Strength=1>
<Record Recommended='Susan Vidler' Strength=1>
<Record Recommended="Rosine 'Ace' Hatem" Strength=1>
<Record Recommended='Wolfgang Pregler' Strength=1>
<Record Recommended='Max von Thun' Strength=1>
<Record Recommended='Iona Thonger' Strength=1>
<Record Recommended='Charles Pitts' Strength=1>
<Record Recommended='Fay Wray' Strength=1>
<Record Recommended='Erika Wackernagel' Strength=1>
<Record Recommended='Laura Silverman' Strength=1>
<Record Recommended='Brent Carver' Strength=1>
<Record Recommended='Michael Bacall' Strength=1>
<Record Recommended='Donovan Scott' Strength=1>
<Record Recommended='Mary Kate Schellhardt' Strength=1>
<Record Recommended='Garret Dillahunt' Strength=1>
<Record Recommended='René Dif' Strength=1>
<Record Recommended='Vic Morrow' Strength=1>
<Record Recommended='Vincent Mendy' Strength=1>
<Record Recommended='Dawn Dininger' Strength=1>
<Record Recommended='Sylvie Testud' Strength=1>
<Record Recommended='Robert Keith' Strength=1>
<Record Recommended='Monique Mercure' Strength=1>
<Record Recommended='Humbert Balsan' Strength=1>
<Record Recommended='Michael Beasley' Strength=1>
<Record Recommended='Ahmed Ben Massoud' Strength=1>
<Record Recommended='Peter Serafinowicz' Strength=1>
<Record Recommended='Alex Barringer' Strength=1>
<Record Recommended='Jack Carson' Strength=1>
<Record Recommended='Ori Pfeffer' Strength=1>
<Record Recommended='Thomas Weisgerber' Strength=1>
<Record Recommended='Paul Fahrenkopf' Strength=1>
<Record Recommended='Moneca Delain' Strength=1>
<Record Recommended='Eric Edwards' Strength=1>
<Record Recommended='Ty Randolph' Strength=1>
<Record Recommended='Rich Komenich' Strength=1>
<Record Recommended='Carl Heinz Choynski' Strength=1>
<Record Recommended='Kurek Ashley' Strength=1>
<Record Recommended='Caitlin Gold' Strength=1>
<Record Recommended='Alice Marie Crowe' Strength=1>
<Record Recommended='Todd Boyce' Strength=1>
<Record Recommended='Andrew Keegan' Strength=1>
<Record Recommended='Richard Farnsworth' Strength=1>
<Record Recommended='John Rothman' Strength=1>
<Record Recommended='Kellita Smith' Strength=1>
<Record Recommended='Suzanne Flon' Strength=1>
<Record Recommended='Sonny Melendrez' Strength=1>
<Record Recommended='Leo McKern' Strength=1>
<Record Recommended='William T. Orr' Strength=1>
<Record Recommended='Chris Thomas King' Strength=1>
<Record Recommended='Dean Norris' Strength=1>
<Record Recommended='Yaya DaCosta' Strength=1>
<Record Recommended='Christa B. Allen' Strength=1>
<Record Recommended='Alan Randolph Scott' Strength=1>
<Record Recommended='Paul Scheer' Strength=1>
<Record Recommended='Valérie Bonnier' Strength=1>
<Record Recommended='Jeff East' Strength=1>
<Record Recommended='Gary Swanson' Strength=1>
<Record Recommended='Phil Leeds' Strength=1>
<Record Recommended='Jessica Manley' Strength=1>
<Record Recommended='Robert Baker' Strength=1>
<Record Recommended='Victor Sutherland' Strength=1>
<Record Recommended='David Dastmalchian' Strength=1>
<Record Recommended='Louis Corbett' Strength=1>
<Record Recommended='Steve Oliver' Strength=1>
<Record Recommended='Jesse Moss' Strength=1>
<Record Recommended='Ray Reinhardt' Strength=1>
<Record Recommended='Julian Wadham' Strength=1>
<Record Recommended='Olivia de Havilland' Strength=1>
<Record Recommended='John Kani' Strength=1>
<Record Recommended='Juan Lombardero' Strength=1>
<Record Recommended='Lana Schwab' Strength=1>
<Record Recommended='Zakee Howze' Strength=1>
<Record Recommended='Vic Perrin' Strength=1>
<Record Recommended='Buddy Guy' Strength=1>
<Record Recommended='Tangi Miller' Strength=1>
<Record Recommended='Joey Krajcar' Strength=1>
<Record Recommended='Rex Ingram' Strength=1>
<Record Recommended='Cliff Saunders' Strength=1>
<Record Recommended='Ceri Bostock' Strength=1>
<Record Recommended='Francis Huster' Strength=1>
<Record Recommended='Richard Romancito' Strength=1>
<Record Recommended='Julie Dreyfus' Strength=1>
<Record Recommended='Christian Erickson' Strength=1>
<Record Recommended='Eckehard Hoffmann' Strength=1>
<Record Recommended='David Sterne' Strength=1>
<Record Recommended='Patrice Johnson' Strength=1>
<Record Recommended='Yevgeni Lazarev' Strength=1>
<Record Recommended='Frances Sternhagen' Strength=1>
<Record Recommended='Ignazio Oliva' Strength=1>
<Record Recommended='Douglas McFerran' Strength=1>
<Record Recommended='Joe Bucaro III' Strength=1>
<Record Recommended='James Morrison Reese' Strength=1>
<Record Recommended='Nicolas Coster' Strength=1>
<Record Recommended='Chaka Forman' Strength=1>
<Record Recommended='Micky Dolenz' Strength=1>
<Record Recommended='Michel Fortin' Strength=1>
<Record Recommended='Omero Antonutti' Strength=1>
<Record Recommended='Oliver Smith' Strength=1>
<Record Recommended='Norma Donaldson' Strength=1>
<Record Recommended='Michael Barry' Strength=1>
<Record Recommended="Arthur O'Connell" Strength=1>
<Record Recommended='Lester Wiese' Strength=1>
<Record Recommended='David Chokachi' Strength=1>
<Record Recommended='Chantal Deruaz' Strength=1>
<Record Recommended='Cecilia Pérez-Cervera' Strength=1>
<Record Recommended='Daisy Bates' Strength=1>
<Record Recommended='Joan Blondell' Strength=1>
<Record Recommended='Erik Holmey' Strength=1>
<Record Recommended='Ivan Kaye' Strength=1>
<Record Recommended='Alastair Duncan' Strength=1>
<Record Recommended='Naomi Campbell' Strength=1>
<Record Recommended='Susan McConnell' Strength=1>
<Record Recommended='Paula Trueman' Strength=1>
<Record Recommended='Richard Roxburgh' Strength=1>
<Record Recommended='Omar Metwally' Strength=1>
<Record Recommended='Paul Koslo' Strength=1>
<Record Recommended="Patti D'Arbanville" Strength=1>
<Record Recommended="Charles 'Jester' Poston" Strength=1>
<Record Recommended='Lauren Maher' Strength=1>
<Record Recommended='William Redfield' Strength=1>
<Record Recommended='William Scott-Masson' Strength=1>
<Record Recommended='Matt Champagne' Strength=1>
<Record Recommended='Vincent Sardi Jr.' Strength=1>
<Record Recommended='Aimee Brooks' Strength=1>
<Record Recommended='Mary Stein' Strength=1>
<Record Recommended='Henri Garcin' Strength=1>
<Record Recommended='Daniel Southern' Strength=1>
<Record Recommended='Judith Scarpone' Strength=1>
<Record Recommended='Mark Carapezza' Strength=1>
<Record Recommended='Isha Koppikar' Strength=1>
<Record Recommended='Ashley Bryant' Strength=1>
<Record Recommended='Martin Starr' Strength=1>
<Record Recommended='Zakaria Atifi' Strength=1>
<Record Recommended='Hope Elizabeth Reeves' Strength=1>
<Record Recommended='John Badila' Strength=1>
<Record Recommended='María Celedonio' Strength=1>
<Record Recommended='Pam Ferris' Strength=1>
<Record Recommended='Tessa Thompson' Strength=1>
<Record Recommended='Kate Greenhouse' Strength=1>
<Record Recommended='R.D. Reid' Strength=1>
<Record Recommended='Greg Lindsay' Strength=1>
<Record Recommended='Charles Martin Smith' Strength=1>
<Record Recommended='John Legend' Strength=1>
<Record Recommended='Viveca Lindfors' Strength=1>
<Record Recommended='Béatrice Michel' Strength=1>
<Record Recommended='Jessica Amlee' Strength=1>
<Record Recommended='Jennifer Grey' Strength=1>
<Record Recommended='Gary Springer' Strength=1>
<Record Recommended='James Read' Strength=1>
<Record Recommended='H.G. Green' Strength=1>
<Record Recommended='Nigel Havers' Strength=1>
<Record Recommended='Sean Patrick Thomas' Strength=1>
<Record Recommended='Norman Howell' Strength=1>
<Record Recommended='Stefanie Powers' Strength=1>
<Record Recommended='Jack White' Strength=1>
<Record Recommended='Enuka Okuma' Strength=1>
<Record Recommended='Steve John Shepherd' Strength=1>
<Record Recommended='Annika Foo' Strength=1>
<Record Recommended='Jim Breuer' Strength=1>
<Record Recommended='Katherine Denning' Strength=1>
<Record Recommended='Jean Rougerie' Strength=1>
<Record Recommended='Doris Wishman' Strength=1>
<Record Recommended='Roger Cobra' Strength=1>
<Record Recommended='Jerry Houser' Strength=1>
<Record Recommended='Ken Parker' Strength=1>
<Record Recommended='Sean Marquette' Strength=1>
<Record Recommended='Cliff Potts' Strength=1>
<Record Recommended='Ray Burdis' Strength=1>
<Record Recommended='Manny Jacobs' Strength=1>
<Record Recommended='Mayf Nutter' Strength=1>
<Record Recommended='Bonita Friedericy' Strength=1>
<Record Recommended='Mona Lee Fultz' Strength=1>
<Record Recommended='Omry Reznik' Strength=1>
<Record Recommended='Joseph Hudgins' Strength=1>
<Record Recommended='F. Gary Gray' Strength=1>
<Record Recommended='Florin Piersic Jr.' Strength=1>
<Record Recommended='Mark Waschke' Strength=1>
<Record Recommended='Eric Pohlmann' Strength=1>
<Record Recommended='Christina Kirk' Strength=1>
<Record Recommended='Jérôme Kircher' Strength=1>
<Record Recommended='Katt Shea' Strength=1>
<Record Recommended='Mark A. Cummins' Strength=1>
<Record Recommended='Yangzom Brauen' Strength=1>
<Record Recommended='Peter Jurasik' Strength=1>
<Record Recommended='Patricia Heaton' Strength=1>
<Record Recommended='Nehemiah Persoff' Strength=1>
<Record Recommended='Lila Kedrova' Strength=1>
<Record Recommended='Larry Carter' Strength=1>
<Record Recommended='John Holmes' Strength=1>
<Record Recommended='Regina Rice' Strength=1>
<Record Recommended='Zoe Weizenbaum' Strength=1>
<Record Recommended='Pepe Callahan' Strength=1>
<Record Recommended='Don Stanton' Strength=1>
<Record Recommended="Matt O'Leary" Strength=1>
<Record Recommended='Karin Gregorek' Strength=1>
<Record Recommended='Miles Herter' Strength=1>
<Record Recommended='Renaud Verley' Strength=1>
<Record Recommended='Robert Aiken' Strength=1>
<Record Recommended='Edwina Moore' Strength=1>
<Record Recommended='Jennifer Sears' Strength=1>
<Record Recommended='Amy Wright' Strength=1>
<Record Recommended='Georgina Chapman' Strength=1>
<Record Recommended='Alexondra Lee' Strength=1>
<Record Recommended='William Armstrong' Strength=1>
<Record Recommended='Kati Bus' Strength=1>
<Record Recommended='Bess Motta' Strength=1>
<Record Recommended='Sung Hi Lee' Strength=1>
<Record Recommended='Ali A. Wahhab' Strength=1>
<Record Recommended='Kenn Michael' Strength=1>
<Record Recommended='Frank Orth' Strength=1>
<Record Recommended='Murli Sharma' Strength=1>
<Record Recommended='Roy Werner' Strength=1>
<Record Recommended='Robert Adler' Strength=1>
<Record Recommended='Lisa Baur' Strength=1>
<Record Recommended='Gisela Strauss' Strength=1>
<Record Recommended='Dania Ramirez' Strength=1>
<Record Recommended='Ronnie Lorenzen' Strength=1>
<Record Recommended='Peter Rühring' Strength=1>
<Record Recommended='Tod Fennell' Strength=1>
<Record Recommended='Craig Wasson' Strength=1>
<Record Recommended='David Bateson' Strength=1>
<Record Recommended='Trevor Wright' Strength=1>
<Record Recommended='Norman Alden' Strength=1>
<Record Recommended='Christina Cox' Strength=1>
<Record Recommended='Josh Hutcherson' Strength=1>
<Record Recommended='Marge Morgan' Strength=1>
<Record Recommended='Tiffany Samuels' Strength=1>
<Record Recommended='David Brisbin' Strength=1>
<Record Recommended='Albert Moses' Strength=1>
<Record Recommended='Silvana Mangano' Strength=1>
<Record Recommended='Roger Van Hool' Strength=1>
<Record Recommended='Brian Scolaro' Strength=1>
<Record Recommended='Christian J. Meoli' Strength=1>
<Record Recommended='Steve Nicolson' Strength=1>
<Record Recommended='Ágnes Bánfalvy' Strength=1>
<Record Recommended='Matt Winston' Strength=1>
<Record Recommended='Michael Wright' Strength=1>
<Record Recommended='Catherine Tate' Strength=1>
<Record Recommended='Wilford Brimley' Strength=1>
<Record Recommended='Matthew McGrory' Strength=1>
<Record Recommended='Erno Müller' Strength=1>
<Record Recommended='Conrad Pla' Strength=1>
<Record Recommended='Togo Igawa' Strength=1>
<Record Recommended='Hubertus Bengsch' Strength=1>
<Record Recommended='Eva Siva' Strength=1>
<Record Recommended='Jenna Milton' Strength=1>
<Record Recommended='Samuel Gould' Strength=1>
<Record Recommended='Pierre Semmler' Strength=1>
<Record Recommended='Cork Hubbert' Strength=1>
<Record Recommended='Jaclyn Tze Wey' Strength=1>
<Record Recommended='Teddy Newton' Strength=1>
<Record Recommended='Anna Katarina' Strength=1>
<Record Recommended='Tyron Leitso' Strength=1>
<Record Recommended='Michael McMillen' Strength=1>
<Record Recommended='Natasha Williams' Strength=1>
<Record Recommended='Costas Dino Chimona' Strength=1>
<Record Recommended='Allen Boudreaux' Strength=1>
<Record Recommended='John Cassavetes' Strength=1>
<Record Recommended='Chad Harber' Strength=1>
<Record Recommended='Richard Brake' Strength=1>
<Record Recommended='Catherine Lloyd Burns' Strength=1>
<Record Recommended='Laura Morante' Strength=1>
<Record Recommended='Arnold Johnson' Strength=1>
<Record Recommended='Patrick Henry' Strength=1>
<Record Recommended='Jacques Dutronc' Strength=1>
<Record Recommended='Patrick Chesnais' Strength=1>
<Record Recommended='Ivan Kane' Strength=1>
<Record Recommended='Vahina Giocante' Strength=1>
<Record Recommended='Gene Okerlund' Strength=1>
<Record Recommended='Ryan Milkovich' Strength=1>
<Record Recommended='Chantal Perron' Strength=1>
<Record Recommended='Gianfranco Varetto' Strength=1>
<Record Recommended='Henry Simmons' Strength=1>
<Record Recommended='Marianna Palka' Strength=1>
<Record Recommended='Claudia Schiffer' Strength=1>
<Record Recommended='Vivienne Sendaydiego' Strength=1>
<Record Recommended='Nellie Bellflower' Strength=1>
<Record Recommended='Fredric March' Strength=1>
<Record Recommended='Ilan Mitchell-Smith' Strength=1>
<Record Recommended='Adriana Millan' Strength=1>
<Record Recommended='Ken Webster' Strength=1>
<Record Recommended='Kristen Wilson' Strength=1>
<Record Recommended='Jerry Levine' Strength=1>
<Record Recommended='Danny Cooksey' Strength=1>
<Record Recommended='Matthew Stefiuk' Strength=1>
<Record Recommended='Bibiana Fernández' Strength=1>
<Record Recommended='Simon Abkarian' Strength=1>
<Record Recommended='Nina Zoe Bakshi' Strength=1>
<Record Recommended='Scott Jacoby' Strength=1>
<Record Recommended='Hans van Tongeren' Strength=1>
<Record Recommended='Eleanor David' Strength=1>
<Record Recommended='Sheila Tousey' Strength=1>
<Record Recommended='Luke Perry' Strength=1>
<Record Recommended='Simon Merrells' Strength=1>
<Record Recommended='Diane Ladd' Strength=1>
<Record Recommended='Patrick Maléon' Strength=1>
<Record Recommended='Noxolo Maqashalala' Strength=1>
<Record Recommended='Kelly Junkerman' Strength=1>
<Record Recommended='Annette Charles' Strength=1>
<Record Recommended='Peter J. Lucas' Strength=1>
<Record Recommended='Alex Colon' Strength=1>
<Record Recommended='Gordon Westcott' Strength=1>
<Record Recommended='James Smith' Strength=1>
<Record Recommended='Nancy Beatty' Strength=1>
<Record Recommended='Rowland Davies' Strength=1>
<Record Recommended='Alexandra Bastedo' Strength=1>
<Record Recommended='Eddie Gossling' Strength=1>
<Record Recommended='Charlie Rose' Strength=1>
<Record Recommended='Vivian Smallwood' Strength=1>
<Record Recommended='Glenn R. Wilder' Strength=1>
<Record Recommended='Evan C. Kim' Strength=1>
<Record Recommended='Dustin Bollinger' Strength=1>
<Record Recommended='Zahf Paroo' Strength=1>
<Record Recommended='Zahn McClarnon' Strength=1>
<Record Recommended='Maurice Barrier' Strength=1>
<Record Recommended='Horatius Häberle' Strength=1>
<Record Recommended='Jenny Wright' Strength=1>
<Record Recommended='Hal Hopper' Strength=1>
<Record Recommended='Peter Schneider' Strength=1>
<Record Recommended='Dorian Kingi' Strength=1>
<Record Recommended='Brigitte Ariel' Strength=1>
<Record Recommended='Mike Marshall' Strength=1>
<Record Recommended='Carole Cook' Strength=1>
<Record Recommended='Eric Schweig' Strength=1>
<Record Recommended='Michael McMurtry' Strength=1>
<Record Recommended='Kelly Wolf' Strength=1>
<Record Recommended='James Fleet' Strength=1>
<Record Recommended='Merritt Wever' Strength=1>
<Record Recommended='John Hannah' Strength=1>
<Record Recommended='Steven Brand' Strength=1>
<Record Recommended='Finesse Mitchell' Strength=1>
<Record Recommended='Sophie Wyburd' Strength=1>
<Record Recommended='Shane MacGowan' Strength=1>
<Record Recommended='Zouzou' Strength=1>
<Record Recommended='Ryan Radis' Strength=1>
<Record Recommended='Kerry Condon' Strength=1>
<Record Recommended='Arshalouis Aivazian' Strength=1>
<Record Recommended='Jimmy Thompson' Strength=1>
<Record Recommended='George McNeilage' Strength=1>
<Record Recommended='Leanne Cochran' Strength=1>
<Record Recommended='Robert Gerringer' Strength=1>
<Record Recommended='Amber Morgan' Strength=1>
<Record Recommended='Richard Widmark' Strength=1>
<Record Recommended='Eduardo Yáñez' Strength=1>
<Record Recommended='Duane Howard' Strength=1>
<Record Recommended='Ricky Jay' Strength=1>
<Record Recommended='Noel Kaufmann' Strength=1>
<Record Recommended='Doug Rand' Strength=1>
<Record Recommended='Luis Van Rooten' Strength=1>
<Record Recommended='Mathilda May' Strength=1>
<Record Recommended='Peter Edmund' Strength=1>
<Record Recommended='Lou Ferrigno' Strength=1>
<Record Recommended='Adriano Magistretti' Strength=1>
<Record Recommended='Sarah Burns' Strength=1>
<Record Recommended='Rene Pereia' Strength=1>
<Record Recommended='Dusty Clare' Strength=1>
<Record Recommended='Estelle Winwood' Strength=1>
<Record Recommended='Anthony Warren' Strength=1>
<Record Recommended='Oliver Nägele' Strength=1>
<Record Recommended='Cassandra Peterson' Strength=1>
<Record Recommended='Peter Williams' Strength=1>
<Record Recommended='Julia Hsu' Strength=1>
<Record Recommended='Jon Korkes' Strength=1>
<Record Recommended='C.O.C.O. Brown' Strength=1>
<Record Recommended='Susan Misner' Strength=1>
<Record Recommended='Pierre Segui' Strength=1>
<Record Recommended='Michael Jenn' Strength=1>
<Record Recommended='Allan Havey' Strength=1>
<Record Recommended='Barbara Radecki' Strength=1>
<Record Recommended='David Del Valle' Strength=1>
<Record Recommended='Alvin Van Der Kuech' Strength=1>
<Record Recommended='Wayne Newton' Strength=1>
<Record Recommended='Gisela Fischer' Strength=1>
<Record Recommended='Robert Maillet' Strength=1>
<Record Recommended='Larry Block' Strength=1>
<Record Recommended='Monte Markham' Strength=1>
<Record Recommended='June Allyson' Strength=1>
<Record Recommended='Bruce Kluger' Strength=1>
<Record Recommended='Annie Morgan' Strength=1>
<Record Recommended='Mustafa Ali' Strength=1>
<Record Recommended='Owen Lay' Strength=1>
<Record Recommended='Rashida Jones' Strength=1>
<Record Recommended='Iggy Pop' Strength=1>
<Record Recommended='Jamie Anderson' Strength=1>
<Record Recommended='Erica Yohn' Strength=1>
<Record Recommended='Maria Besendahl' Strength=1>
<Record Recommended='Valérie Lagrange' Strength=1>
<Record Recommended='Jim Norton' Strength=1>
<Record Recommended='Alain Goulem' Strength=1>
<Record Recommended='Cameron Mitchell' Strength=1>
<Record Recommended='Sophie Edmond' Strength=1>
<Record Recommended='Taurean Blacque' Strength=1>
<Record Recommended='Jean-Paul Belmondo' Strength=1>
<Record Recommended='Jürgen Nau' Strength=1>
<Record Recommended='Bonnie Piesse' Strength=1>
<Record Recommended='Fenella Woolgar' Strength=1>
<Record Recommended='Kristin Rudrüd' Strength=1>
<Record Recommended='Willi Schwabe' Strength=1>
<Record Recommended='Don Cherry' Strength=1>
<Record Recommended='Tyler Labine' Strength=1>
<Record Recommended='Liam Daniels' Strength=1>
<Record Recommended='Eric Christmas' Strength=1>
<Record Recommended="Anthony O'Donnell" Strength=1>
<Record Recommended='Alicia Borrachero' Strength=1>
<Record Recommended='Jonathan Togo' Strength=1>
<Record Recommended='O-Lan Jones' Strength=1>
<Record Recommended='Sig Ruman' Strength=1>
<Record Recommended='Tanja Reichert' Strength=1>
<Record Recommended='Steven Goldstein' Strength=1>
<Record Recommended='Darren Victoria' Strength=1>
<Record Recommended='Zachary Ferren' Strength=1>
<Record Recommended='Jean-Pierre Marielle' Strength=1>
<Record Recommended='Zénaïde Rossi' Strength=1>
<Record Recommended='Paul Butler' Strength=1>
<Record Recommended='William Knowles' Strength=1>
<Record Recommended='John Waugh' Strength=1>
<Record Recommended='Patricia Hitchcock' Strength=1>
<Record Recommended='Paul Dillon' Strength=1>
<Record Recommended='Hans Finohr' Strength=1>
<Record Recommended='Robert Alan Beuth' Strength=1>
<Record Recommended='Kai Wiesinger' Strength=1>
<Record Recommended='Pete Karas' Strength=1>
<Record Recommended='Gail Downey' Strength=1>
<Record Recommended='Kevin Hart' Strength=1>
<Record Recommended='Kristyn Butcher' Strength=1>
<Record Recommended='Susan Fitzer' Strength=1>
<Record Recommended='Dean Rader-Duval' Strength=1>
<Record Recommended='Mordecai Lawner' Strength=1>
<Record Recommended='Paul Sanchez' Strength=1>
<Record Recommended='Kirsty Stuart' Strength=1>
<Record Recommended='Mathilde Danegger' Strength=1>
<Record Recommended='Lerato Mokgotho' Strength=1>
<Record Recommended='Sharon Farrell' Strength=1>
<Record Recommended='Tyrone Huggins' Strength=1>
<Record Recommended='Jessica Stroup' Strength=1>
<Record Recommended='George Loftus' Strength=1>
<Record Recommended='Richard LeParmentier' Strength=1>
<Record Recommended='Emer Gillespie' Strength=1>
<Record Recommended='Sarah-Jeanne Labrosse' Strength=1>
<Record Recommended='John Marshall' Strength=1>
<Record Recommended="Q'orianka Kilcher" Strength=1>
<Record Recommended='Jack Scalia' Strength=1>
<Record Recommended='Jayne Eastwood' Strength=1>
<Record Recommended='Vittorio Gassman' Strength=1>
<Record Recommended='Nancy Walker' Strength=1>
<Record Recommended='Troy Garity' Strength=1>
<Record Recommended='Eric Balliet' Strength=1>
<Record Recommended='Dominic Colenso' Strength=1>
<Record Recommended='Stacy Sanches' Strength=1>
<Record Recommended='Boleslaw Plotnicki' Strength=1>
<Record Recommended='Joshua Bogues' Strength=1>
<Record Recommended='Laura Soltis' Strength=1>
<Record Recommended='Béatrice Dalle' Strength=1>
<Record Recommended='Hans Robert Wille' Strength=1>
<Record Recommended='Florence Moody' Strength=1>
<Record Recommended='Ginnifer Goodwin' Strength=1>
<Record Recommended='Mike Kirton' Strength=1>
<Record Recommended='Evan Gilchrist' Strength=1>
<Record Recommended='Trudi Jackson' Strength=1>
<Record Recommended='Steven Gary Banks' Strength=1>
<Record Recommended='Roger Frost' Strength=1>
<Record Recommended='Jesse Scott Nelson' Strength=1>
<Record Recommended='Lauren Ambrose' Strength=1>
<Record Recommended='Laurent Gamelon' Strength=1>
<Record Recommended='Ellie Cornell' Strength=1>
<Record Recommended='Douglas Hodge' Strength=1>
<Record Recommended='Dan Lauria' Strength=1>
<Record Recommended="Jenny O'Hara" Strength=1>
<Record Recommended='Charlotte J. Helmkamp' Strength=1>
<Record Recommended='Claude Besson' Strength=1>
<Record Recommended='Jennifer Lawrence' Strength=1>
<Record Recommended='Kenny Doughty' Strength=1>
<Record Recommended='Laura Cerón' Strength=1>
<Record Recommended='Edison Chen' Strength=1>
<Record Recommended='George DiCenzo' Strength=1>
<Record Recommended='Joshua Shalikar' Strength=1>
<Record Recommended='Michael Dwyer' Strength=1>
<Record Recommended='Melanie Manos' Strength=1>
<Record Recommended='Christian Mueller-Stahl' Strength=1>
<Record Recommended='Kristen Hager' Strength=1>
<Record Recommended='Paul Satterfield' Strength=1>
<Record Recommended='Brandy Norwood' Strength=1>
<Record Recommended='Alvin Myerovich' Strength=1>
<Record Recommended='Christiane Millet' Strength=1>
<Record Recommended='Tamaki' Strength=1>
<Record Recommended='Jean-Claude Dreyfus' Strength=1>
<Record Recommended='Damián Alcázar' Strength=1>
<Record Recommended='Earl Maddox' Strength=1>
<Record Recommended='John Fedevich' Strength=1>
<Record Recommended='Pedro Gonzalez Gonzalez' Strength=1>
<Record Recommended='Jennifer Jones' Strength=1>
<Record Recommended='Fanny Ardant' Strength=1>
<Record Recommended='Eve Arden' Strength=1>
<Record Recommended='Flea' Strength=1>
<Record Recommended='Kathryn Walker' Strength=1>
<Record Recommended='Zelda Tinska' Strength=1>
<Record Recommended='Lehlohonolo Makoko' Strength=1>
<Record Recommended='Jochen Horst' Strength=1>
<Record Recommended='John Hoyt' Strength=1>
<Record Recommended='Randy Pearlstein' Strength=1>
<Record Recommended='Edward I. Koch' Strength=1>
<Record Recommended='Antoinette Cristiani' Strength=1>
<Record Recommended='Madison Lanc' Strength=1>
<Record Recommended='Vincent Pagano' Strength=1>
<Record Recommended='Oliver Phelps' Strength=1>
<Record Recommended='Sofia Milos' Strength=1>
<Record Recommended='Bienvenue Kindoki' Strength=1>
<Record Recommended='Jana Mitsoula' Strength=1>
<Record Recommended='Stephen Campbell Moore' Strength=1>
<Record Recommended='Gloria Miralles Ruiz' Strength=1>
<Record Recommended='Bernard Dhéran' Strength=1>
<Record Recommended='Albert Misak' Strength=1>
<Record Recommended='Gene Dinovi' Strength=1>
<Record Recommended='Morris Chestnut' Strength=1>
<Record Recommended='Lorna Maitland' Strength=1>
<Record Recommended='Karen Getz' Strength=1>
<Record Recommended="O'Neal Compton" Strength=1>
<Record Recommended='John Tordoff' Strength=1>
<Record Recommended='Philippe Vendan-Borin' Strength=1>
<Record Recommended='Doug Murray' Strength=1>
<Record Recommended='Willeke van Ammelrooy' Strength=1>
<Record Recommended='Victoria Hamilton' Strength=1>
<Record Recommended='Kati Székely' Strength=1>
<Record Recommended='Mizuo Peck' Strength=1>
<Record Recommended='Jack Weber' Strength=1>
<Record Recommended='Moses Gunn' Strength=1>
<Record Recommended='Keisha Castle-Hughes' Strength=1>
<Record Recommended='Samaire Armstrong' Strength=1>
<Record Recommended='Ron Jeremy' Strength=1>
<Record Recommended='Payal Rohatgi' Strength=1>
<Record Recommended='Donald James Malmberg' Strength=1>
<Record Recommended='Andrea Di Stefano' Strength=1>
<Record Recommended='Liz Stauber' Strength=1>
<Record Recommended='Matt Mulhern' Strength=1>
<Record Recommended='Richard James' Strength=1>
<Record Recommended='Jesper Asholt' Strength=1>
<Record Recommended='Thomas Lockyer' Strength=1>
<Record Recommended='Gwen McGee' Strength=1>
<Record Recommended='Tim Booth' Strength=1>
<Record Recommended='Dick Rude' Strength=1>
<Record Recommended='Nathalie Shats' Strength=1>
<Record Recommended='Josette Maccario' Strength=1>
<Record Recommended='Michael Feast' Strength=1>
<Record Recommended='Linda Sue Ragsdale' Strength=1>
<Record Recommended='John Lehne' Strength=1>
<Record Recommended='Torkel Petersson' Strength=1>
<Record Recommended="Darren O'Donnell" Strength=1>
<Record Recommended='Faith Daniels' Strength=1>
<Record Recommended='Sean Nelson' Strength=1>
<Record Recommended='Saverio Guerra' Strength=1>
<Record Recommended='Malinda Williams' Strength=1>
<Record Recommended='Alan Ford' Strength=1>
<Record Recommended='Florian Panzner' Strength=1>
<Record Recommended='Kennedy Montano' Strength=1>
<Record Recommended='Meredith MacNeill' Strength=1>
<Record Recommended='John Anton' Strength=1>
<Record Recommended='Lou Reed' Strength=1>
<Record Recommended='Bryetta Calloway' Strength=1>
<Record Recommended='Kari Väänänen' Strength=1>
<Record Recommended='Owain Yeoman' Strength=1>
<Record Recommended='Ricco Ross' Strength=1>
<Record Recommended='David Hemmings' Strength=1>
<Record Recommended='Lia Williams' Strength=1>
<Record Recommended='Olivia Darnley' Strength=1>
<Record Recommended='Cristiano Bonora' Strength=1>
<Record Recommended='John Aquino' Strength=1>
<Record Recommended='William R. Moses' Strength=1>
<Record Recommended='Louisa Jones' Strength=1>
<Record Recommended="Jamie Linck O'Brien" Strength=1>
<Record Recommended='Carol Burnett' Strength=1>
<Record Recommended='Dean Andrews' Strength=1>
<Record Recommended='Martin May' Strength=1>
<Record Recommended='Anna Pirri' Strength=1>
<Record Recommended='Bill Moseley' Strength=1>
<Record Recommended='Jukka Hiltunen' Strength=1>
<Record Recommended='Cesare Danova' Strength=1>
<Record Recommended='Adam Brooks' Strength=1>
<Record Recommended='Kevin James' Strength=1>
<Record Recommended='Jim Meskimen' Strength=1>
<Record Recommended='Lance Larsen' Strength=1>
<Record Recommended='Wallace Earl' Strength=1>
<Record Recommended='Najib Oudghiri' Strength=1>
<Record Recommended='Chris Mitchell' Strength=1>
<Record Recommended='Isiah Whitlock Jr.' Strength=1>
<Record Recommended='Richard Dean Anderson' Strength=1>
<Record Recommended='Gloria Votsis' Strength=1>
<Record Recommended='Laurent Stocker' Strength=1>
<Record Recommended='Alisa Grace Greaves' Strength=1>
<Record Recommended='Dom de Beern' Strength=1>
<Record Recommended='William Houston' Strength=1>
<Record Recommended='Cathryn Damon' Strength=1>
<Record Recommended='Ray McAnally' Strength=1>
<Record Recommended='Paget Brewster' Strength=1>
<Record Recommended='Matyelok Gibbs' Strength=1>
<Record Recommended='Andrej Jautze' Strength=1>
<Record Recommended='Ade' Strength=1>
<Record Recommended='Sergi López' Strength=1>
<Record Recommended='Curtis McClarin' Strength=1>
<Record Recommended='Sean MacMahon' Strength=1>
<Record Recommended='Hans Henrik Clemensen' Strength=1>
<Record Recommended='Ted McGinley' Strength=1>
<Record Recommended='Andy Lucas' Strength=1>
<Record Recommended='Ozzy Osbourne' Strength=1>
<Record Recommended='Bo Brundin' Strength=1>
<Record Recommended='Clare Carey' Strength=1>
<Record Recommended='Darren Dowler' Strength=1>
<Record Recommended='Dominique McElligott' Strength=1>
<Record Recommended='Robert Pattinson' Strength=1>
<Record Recommended='Barbara Kelsch' Strength=1>
<Record Recommended='Richard DeDomenico' Strength=1>
<Record Recommended='David Mendenhall' Strength=1>
<Record Recommended='Art De La Torre' Strength=1>
<Record Recommended='Meghan Black' Strength=1>
<Record Recommended='Angelica Domröse' Strength=1>
<Record Recommended='George Macready' Strength=1>
<Record Recommended='Paul Lynde' Strength=1>
<Record Recommended='Lisa Owen' Strength=1>
<Record Recommended='Nigel Planer' Strength=1>
<Record Recommended='Ralph Boettner' Strength=1>
<Record Recommended='Charles Malik Whitfield' Strength=1>
<Record Recommended='Buddy Bolton' Strength=1>
<Record Recommended='Joachim Bober' Strength=1>
<Record Recommended='Jane Hoffman' Strength=1>
<Record Recommended='Lorie Griffin' Strength=1>
<Record Recommended='Paul Kelly' Strength=1>
<Record Recommended='Rebecca Rigg' Strength=1>
<Record Recommended='John Marriott' Strength=1>
<Record Recommended='Pino Colizzi' Strength=1>
<Record Recommended='John Moraitis' Strength=1>
<Record Recommended='Collin Thornton' Strength=1>
<Record Recommended='Maurice Jacquemont' Strength=1>
<Record Recommended='Eric Edelstein' Strength=1>
<Record Recommended='Cayden Boyd' Strength=1>
<Record Recommended='Thomas Chabrol' Strength=1>
<Record Recommended='Zak Santiago' Strength=1>
<Record Recommended='Amy Green' Strength=1>
<Record Recommended='Barbara Peckinpaugh' Strength=1>
<Record Recommended='Karanvir Bohra' Strength=1>
<Record Recommended='Melissa Errico' Strength=1>
<Record Recommended='Victoria Shaw' Strength=1>
<Record Recommended='Travis Wester' Strength=1>
<Record Recommended='Mario David' Strength=1>
<Record Recommended='Majel Barrett' Strength=1>
<Record Recommended='Larissa Laskin' Strength=1>
<Record Recommended='Miranda Garrison' Strength=1>
<Record Recommended='Georg Stanford Brown' Strength=1>
<Record Recommended='Joseph Morgan' Strength=1>
<Record Recommended='Genevieve Sabourin' Strength=1>
<Record Recommended='RuPaul' Strength=1>
<Record Recommended='Dana Ashbrook' Strength=1>
<Record Recommended='Mark Arnold' Strength=1>
<Record Recommended='Elijah St. Germain' Strength=1>
<Record Recommended='Jill Gatsby' Strength=1>
<Record Recommended='Stacy Ferguson' Strength=1>
<Record Recommended='Kenneth White' Strength=1>
<Record Recommended='Wayne Charles Baker' Strength=1>
<Record Recommended='Lily Mariye' Strength=1>
<Record Recommended='Karl Yune' Strength=1>
<Record Recommended='Hillary Tuck' Strength=1>
<Record Recommended='Jason Schwartzman' Strength=1>
<Record Recommended='Tim Berrington' Strength=1>
<Record Recommended='Nicholas Colasanto' Strength=1>
<Record Recommended='Craig Stevenson' Strength=1>
<Record Recommended='Eliza Bennett' Strength=1>
<Record Recommended='Steve McQueen' Strength=1>
<Record Recommended='Dorothy Lyman' Strength=1>
<Record Recommended='Riki Lindhome' Strength=1>
<Record Recommended='Kristanna Loken' Strength=1>
<Record Recommended='Adrienne Shaw' Strength=1>
<Record Recommended='Estelle Getty' Strength=1>
<Record Recommended='Michael Showalter' Strength=1>
<Record Recommended='Tom Atkins' Strength=1>
<Record Recommended='Ken Berry' Strength=1>
<Record Recommended='Richard McCabe' Strength=1>
<Record Recommended='Dylan Smith' Strength=1>
<Record Recommended='Trevor Matthews' Strength=1>
<Record Recommended='Joe Dorsey' Strength=1>
<Record Recommended='Elizabeth Croft' Strength=1>
<Record Recommended='Ringo Starr' Strength=1>
<Record Recommended='Lillias White' Strength=1>
<Record Recommended='Heather Davis' Strength=1>
<Record Recommended='Michael Vartan' Strength=1>
<Record Recommended='Michael Stefani' Strength=1>
<Record Recommended='Michele Placido' Strength=1>
<Record Recommended='Phil Davies' Strength=1>
<Record Recommended='Shane Haboucha' Strength=1>
<Record Recommended='Julie Carmen' Strength=1>
<Record Recommended='Jess Hahn' Strength=1>
<Record Recommended='Amy Stryker' Strength=1>
<Record Recommended='Knud Romer Jørgensen' Strength=1>
<Record Recommended='Philip Moon' Strength=1>
<Record Recommended='Laura Drasbæk' Strength=1>
<Record Recommended='Julian Clary' Strength=1>
<Record Recommended='Peter Mygind' Strength=1>
<Record Recommended='Clive Barker' Strength=1>
<Record Recommended='Tim Kazurinsky' Strength=1>
<Record Recommended='Guy Torry' Strength=1>
<Record Recommended='François-Eric Gendron' Strength=1>
<Record Recommended='Daniel Pilon' Strength=1>
<Record Recommended='Del Pentecost' Strength=1>
<Record Recommended='Arthur Malet' Strength=1>
<Record Recommended='Guillermo Montesinos' Strength=1>
<Record Recommended='Dennis Stewart' Strength=1>
<Record Recommended='Mary Ann Haenel' Strength=1>
<Record Recommended='Larry Romano' Strength=1>
<Record Recommended='Matt Doran' Strength=1>
<Record Recommended='Juliette Cummins' Strength=1>
<Record Recommended='Michael Chow' Strength=1>
<Record Recommended='Carolyn Seymour' Strength=1>
<Record Recommended='Pernille Vallentin' Strength=1>
<Record Recommended='Antonio Gil' Strength=1>
<Record Recommended='Jack Knight' Strength=1>
<Record Recommended='Mary Woronov' Strength=1>
<Record Recommended='Robert Middleton' Strength=1>
<Record Recommended='Hill Harper' Strength=1>
<Record Recommended='Daniel Tay' Strength=1>
<Record Recommended="Damian O'Hare" Strength=1>
<Record Recommended='Polly Holliday' Strength=1>
<Record Recommended='Amid Farid' Strength=1>
<Record Recommended='Paul Barrett' Strength=1>
<Record Recommended='Hector Vega Mauricio' Strength=1>
<Record Recommended='Søren Sætter-Lassen' Strength=1>
<Record Recommended='Johnathon Schaech' Strength=1>
<Record Recommended='Robert Young' Strength=1>
<Record Recommended='Zita Görög' Strength=1>
<Record Recommended='Quinn Gasaway' Strength=1>
<Record Recommended='Laura Allen' Strength=1>
<Record Recommended='Wolf Gaudlitz' Strength=1>
<Record Recommended='Annabel Linder' Strength=1>
<Record Recommended='Mindy Cohn' Strength=1>
<Record Recommended='Chloe Moretz' Strength=1>
<Record Recommended='Ian Hart' Strength=1>
<Record Recommended='Carlos Ponce' Strength=1>
<Record Recommended='Stéphane Bonnet' Strength=1>
<Record Recommended='Alanis Morissette' Strength=1>
<Record Recommended='Giancarlo Prete' Strength=1>
<Record Recommended='Roland Bertin' Strength=1>
<Record Recommended='Mari Töröcsik' Strength=1>
<Record Recommended='Philippe Brenninkmeyer' Strength=1>
<Record Recommended='Jason Earles' Strength=1>
<Record Recommended='Clement Fowler' Strength=1>
<Record Recommended='Lurene Tuttle' Strength=1>
<Record Recommended='Silvio Muccino' Strength=1>
<Record Recommended='Robert Walden' Strength=1>
<Record Recommended='Bryan Cranston' Strength=1>
<Record Recommended='Chloe Webb' Strength=1>
<Record Recommended='Rena Horten' Strength=1>
<Record Recommended='Joe Renteria' Strength=1>
<Record Recommended='Jeanne Moreau' Strength=1>
<Record Recommended='Neil Thompson' Strength=1>
<Record Recommended='Clarence Williams III' Strength=1>
<Record Recommended='Tom Fisher' Strength=1>
<Record Recommended='Elisabeth Commelin' Strength=1>
<Record Recommended='Imanol Arias' Strength=1>
<Record Recommended="Paige O'Hara" Strength=1>
<Record Recommended='Roy Chiao' Strength=1>
<Record Recommended='Gérard Oury' Strength=1>
<Record Recommended='Richard Reed' Strength=1>
<Record Recommended='Brian Bosworth' Strength=1>
<Record Recommended='Holly Bird' Strength=1>
<Record Recommended='Constance Forslund' Strength=1>
<Record Recommended='Anthony Kiedis' Strength=1>
<Record Recommended='Didier Bénureau' Strength=1>
<Record Recommended='Katharina Lind' Strength=1>
<Record Recommended='Roberto Blanco' Strength=1>
<Record Recommended='Sean S. Cunningham' Strength=1>
<Record Recommended='Christian Serratos' Strength=1>
<Record Recommended='Jerry Di Giacomo' Strength=1>
<Record Recommended='Scott McLean' Strength=1>
<Record Recommended='Anna Maria Mühe' Strength=1>
<Record Recommended='Usher Raymond' Strength=1>
<Record Recommended='Bridget White' Strength=1>
<Record Recommended='Ava Gardner' Strength=1>
<Record Recommended='Gabrielle Scharnitzky' Strength=1>
<Record Recommended='Bruce Way' Strength=1>
<Record Recommended='Shannon Whirry' Strength=1>
<Record Recommended='Martin Donovan' Strength=1>
<Record Recommended='Gedde Watanabe' Strength=1>
<Record Recommended='Erin Foley' Strength=1>
<Record Recommended='Aida Turturro' Strength=1>
<Record Recommended='Logan Polish' Strength=1>
<Record Recommended='Galina Polskikh' Strength=1>
<Record Recommended='Margie Impert' Strength=1>
<Record Recommended='Kathy Kriegel' Strength=1>
<Record Recommended='Madeleine Sherwood' Strength=1>
<Record Recommended='Carole Ann Wilson' Strength=1>
<Record Recommended='Afi McClendon' Strength=1>
<Record Recommended='Camilla Begnoni' Strength=1>
<Record Recommended='Christine Lahti' Strength=1>
<Record Recommended='Will Knickerbocker' Strength=1>
<Record Recommended='Ernie Grunwald' Strength=1>
<Record Recommended='David Dorfman' Strength=1>
<Record Recommended='Charles Aidman' Strength=1>
<Record Recommended='Mikael Persbrandt' Strength=1>
<Record Recommended='John Maclaren' Strength=1>
<Record Recommended='Tamara Sovchi' Strength=1>
<Record Recommended='Gregory Smith' Strength=1>
<Record Recommended='Gina Athans' Strength=1>
<Record Recommended='John Byner' Strength=1>
<Record Recommended='Aldred Montoya' Strength=1>
<Record Recommended='Donna Hanover' Strength=1>
<Record Recommended='Vickie Roberts' Strength=1>
<Record Recommended='Christopher Masterson' Strength=1>
<Record Recommended='Enrico Lo Verso' Strength=1>
<Record Recommended='Robert Vaughn' Strength=1>
<Record Recommended='M.R. Fletcher' Strength=1>
<Record Recommended='Chris Miller' Strength=1>
<Record Recommended='Nicole Patrick' Strength=1>
<Record Recommended='Helga Göring' Strength=1>
<Record Recommended='Steve Bacic' Strength=1>
<Record Recommended='Alex Barrett' Strength=1>
<Record Recommended='Ruth Nelson' Strength=1>
<Record Recommended='Wayne Duvall' Strength=1>
<Record Recommended='Nicoletta Braschi' Strength=1>
<Record Recommended='Katie Griffin' Strength=1>
<Record Recommended='Carrie Westcott' Strength=1>
<Record Recommended='Geneviève Mnich' Strength=1>
<Record Recommended='Maitland Ward' Strength=1>
<Record Recommended='Susan Willis' Strength=1>
<Record Recommended='Stewart Arnott' Strength=1>
<Record Recommended='Harry Nehring' Strength=1>
<Record Recommended='James Avery' Strength=1>
<Record Recommended='András Márton' Strength=1>
<Record Recommended='Patrick Carroll' Strength=1>
<Record Recommended='Laurent Grévill' Strength=1>
<Record Recommended='Marc Klee' Strength=1>
<Record Recommended='James A. Woods' Strength=1>
<Record Recommended='Colin McCredie' Strength=1>
<Record Recommended='Jacek Wójcicki' Strength=1>
<Record Recommended='Wallace Wood' Strength=1>
<Record Recommended='Ann Jillian' Strength=1>
<Record Recommended='Kayren Butler' Strength=1>
<Record Recommended='Rhoda Griffis' Strength=1>
<Record Recommended='Lalla Ward' Strength=1>
<Record Recommended='Heidi Marnhout' Strength=1>
<Record Recommended='Anna Massey' Strength=1>
<Record Recommended='Kent Williams' Strength=1>
<Record Recommended='Jonathan Bailey' Strength=1>
<Record Recommended='Doris Thalmer' Strength=1>
<Record Recommended='Penny Singleton' Strength=1>
<Record Recommended='Tom Baker' Strength=1>
<Record Recommended='Sorin Misiriantu' Strength=1>
<Record Recommended='Dany Canino' Strength=1>
<Record Recommended='Michel Aumont' Strength=1>
<Record Recommended='Bruce Bonnheim' Strength=1>
<Record Recommended='Rolf Schneider' Strength=1>
<Record Recommended='Jörg Vincent Malotki' Strength=1>
<Record Recommended='Stephen Macht' Strength=1>
<Record Recommended='Tony Beckley' Strength=1>
<Record Recommended='Vincent Palmieri' Strength=1>
<Record Recommended='Francesco De Vito' Strength=1>
<Record Recommended='Suzy Delair' Strength=1>
<Record Recommended='Sergio Fantoni' Strength=1>
<Record Recommended='Joe Basile' Strength=1>
<Record Recommended='Adan Jodorowsky' Strength=1>
<Record Recommended='Miguel Fernandes' Strength=1>
<Record Recommended='Craig Gardner' Strength=1>
<Record Recommended='Iván Esquivel' Strength=1>
<Record Recommended="Christina Jo'Leigh" Strength=1>
<Record Recommended='Souleymane Dicko' Strength=1>
<Record Recommended='Adrian Pintea' Strength=1>
<Record Recommended='James Hampton' Strength=1>
<Record Recommended='Daniel York' Strength=1>
<Record Recommended='Mohammad Shamsi' Strength=1>
<Record Recommended='Chris Ackerman' Strength=1>
<Record Recommended='Susan Strasberg' Strength=1>
<Record Recommended='Bill Teas' Strength=1>
<Record Recommended='Sully Boyar' Strength=1>
<Record Recommended='Chin Han' Strength=1>
<Record Recommended='Howard Silverman' Strength=1>
<Record Recommended='Anita Pallenberg' Strength=1>
<Record Recommended='Herbert Rawlins' Strength=1>
<Record Recommended='Lymari Nadal' Strength=1>
<Record Recommended='Ken Kerr' Strength=1>
<Record Recommended='Duncan Fraser' Strength=1>
<Record Recommended='Papillon Soo' Strength=1>
<Record Recommended='Laura Benson' Strength=1>
<Record Recommended='Loreto Barcelo' Strength=1>
<Record Recommended='Amanda Babin' Strength=1>
<Record Recommended='Alexandre Nahon' Strength=1>
<Record Recommended='Melinda Gilhen' Strength=1>
<Record Recommended='Don Fellows' Strength=1>
<Record Recommended='Jerome Butler' Strength=1>
<Record Recommended='Birthe Neumann' Strength=1>
<Record Recommended='Renato Terra' Strength=1>
<Record Recommended='Jason Douglas' Strength=1>
<Record Recommended='Jonathan Freeman' Strength=1>
<Record Recommended='Megan Mullally' Strength=1>
<Record Recommended='Jayne Mansfield' Strength=1>
<Record Recommended='Bernadette Heerwagen' Strength=1>
<Record Recommended='Norman Bartold' Strength=1>
<Record Recommended='Amanda Root' Strength=1>
<Record Recommended='Roberto Purvis' Strength=1>
<Record Recommended='Frank Girardeau' Strength=1>
<Record Recommended='Monika Lennartz' Strength=1>
<Record Recommended='Carson Aune' Strength=1>
<Record Recommended='Norman Mikeal Berketa' Strength=1>
<Record Recommended='Mika Boorem' Strength=1>
<Record Recommended='Julian Spencer' Strength=1>
<Record Recommended='Michael Haughey' Strength=1>
<Record Recommended='Eli Fucile' Strength=1>
<Record Recommended='John Benfield' Strength=1>
<Record Recommended='Mary-Jessica Pitts' Strength=1>
<Record Recommended='Kwan Hi Lim' Strength=1>
<Record Recommended='Christine Chow' Strength=1>
<Record Recommended='Randy Travis' Strength=1>
<Record Recommended='Army Archerd' Strength=1>
<Record Recommended='Rio Scafone' Strength=1>
<Record Recommended='Robyn Arthur' Strength=1>
<Record Recommended='Jeff Chamberlain' Strength=1>
<Record Recommended='Christopher Ryan' Strength=1>
<Record Recommended='Marita Geraghty' Strength=1>
<Record Recommended='Sergei Bodrov Jr.' Strength=1>
<Record Recommended='Olivia Wilde' Strength=1>
<Record Recommended='Linda Emond' Strength=1>
<Record Recommended='Tracey Lee Smythe' Strength=1>
<Record Recommended='Corey Parker' Strength=1>
<Record Recommended='Christopher Sayegh' Strength=1>
<Record Recommended='Hannes Fischer' Strength=1>
<Record Recommended='Rachel Montez Collins' Strength=1>
<Record Recommended='Justina Machado' Strength=1>
<Record Recommended='Lucia Zotti' Strength=1>
<Record Recommended='Kyle Herbert' Strength=1>
<Record Recommended='Bille Brown' Strength=1>
<Record Recommended='Lucie Arnaz' Strength=1>
<Record Recommended='Bret Harrison' Strength=1>
<Record Recommended='Nora Ferrari' Strength=1>
<Record Recommended='Zane Cassidy' Strength=1>
<Record Recommended='M. Night Shyamalan' Strength=1>
<Record Recommended='Kais Nashif' Strength=1>
<Record Recommended='Abdul Salis' Strength=1>
<Record Recommended='Annick Alane' Strength=1>
<Record Recommended='Katherine Waterston' Strength=1>
<Record Recommended='Kristin Holby' Strength=1>
<Record Recommended='Werner Schwuchow' Strength=1>
<Record Recommended='Penelope Allen' Strength=1>
<Record Recommended='Juliana Donald' Strength=1>
<Record Recommended='Laura Benanti' Strength=1>
<Record Recommended='John Doty' Strength=1>
<Record Recommended='Mohamed Malek Bchatnia' Strength=1>
<Record Recommended='Coronji Calhoun' Strength=1>
<Record Recommended='Irma P. Hall' Strength=1>
<Record Recommended='Kelci Stephenson' Strength=1>
<Record Recommended='Serge Merlin' Strength=1>
<Record Recommended='Pedro Losada' Strength=1>
<Record Recommended='Neran Persaud' Strength=1>
<Record Recommended='Marianne Sägebrecht' Strength=1>
<Record Recommended='Christian Rabe' Strength=1>
<Record Recommended='Jack Valan' Strength=1>
<Record Recommended='Javier Grajeda' Strength=1>
<Record Recommended='Amit Varma' Strength=1>
<Record Recommended="Dick O'Neill" Strength=1>
<Record Recommended='Ofelia Angélica' Strength=1>
<Record Recommended='Dave Buzzotta' Strength=1>
<Record Recommended='Alicia Keys' Strength=1>
<Record Recommended='Brennan Delaney' Strength=1>
<Record Recommended='Anthony Bean' Strength=1>
<Record Recommended='Nicole Dubos' Strength=1>
<Record Recommended='Helga Jordan' Strength=1>
<Record Recommended='Pavan Malhotra' Strength=1>
<Record Recommended='Jean-Pierre Darroussin' Strength=1>
<Record Recommended='Hulk Hogan' Strength=1>
<Record Recommended='Kathleen Landis' Strength=1>
<Record Recommended='Raynold Gideon' Strength=1>
<Record Recommended='Klaus Wennemann' Strength=1>
<Record Recommended='Kagiso Kuypers' Strength=1>
<Record Recommended='George Lopez' Strength=1>
<Record Recommended='Brent Roam' Strength=1>
<Record Recommended='Henry Czerny' Strength=1>
<Record Recommended='Joel McNichol' Strength=1>
<Record Recommended='Eberhard Cohrs' Strength=1>
<Record Recommended='Stevan Rimkus' Strength=1>
<Record Recommended='Rex Ngui' Strength=1>
<Record Recommended='Hank Garrett' Strength=1>
<Record Recommended='Robert Longstreet' Strength=1>
<Record Recommended='Fritz Ernst Fechner' Strength=1>
<Record Recommended='Benjamin Hendrickson' Strength=1>
<Record Recommended='Zhang Ziyi' Strength=1>
<Record Recommended='James Carraway' Strength=1>
<Record Recommended='Geoff Pierson' Strength=1>
<Record Recommended='Austin Douglas Smith' Strength=1>
<Record Recommended='Peter Lewis' Strength=1>
<Record Recommended='Hans-Peter Minetti' Strength=1>
<Record Recommended='Tantoo Cardinal' Strength=1>
<Record Recommended='Ángel Salazar' Strength=1>
<Record Recommended='Philippe Léotard' Strength=1>
<Record Recommended='Ken Leung' Strength=1>
<Record Recommended='Gerhard Bienert' Strength=1>
<Record Recommended='Ute Garnitz' Strength=1>
<Record Recommended='Domiziana Giordano' Strength=1>
<Record Recommended='Kirk Taylor' Strength=1>
<Record Recommended='Loryn Locklin' Strength=1>
<Record Recommended='Bill Smitrovich' Strength=1>
<Record Recommended='Yvan Ponton' Strength=1>
<Record Recommended='Chad Power' Strength=1>
<Record Recommended='Don Alder' Strength=1>
<Record Recommended='Karen Beyer' Strength=1>
<Record Recommended='Michael Mehlmann' Strength=1>
<Record Recommended='Paul Curran' Strength=1>
<Record Recommended='Rex Allen' Strength=1>
<Record Recommended='Aralelly Davidson' Strength=1>
<Record Recommended='Chaske Spencer' Strength=1>
<Record Recommended='Juliet Stevenson' Strength=1>
<Record Recommended='Don McCorkindale' Strength=1>
<Record Recommended='Nial Iskhakov' Strength=1>
<Record Recommended='Jack Conley' Strength=1>
<Record Recommended='Marcello Mastroianni' Strength=1>
<Record Recommended='Jim Chimento' Strength=1>
<Record Recommended='Marty Belafsky' Strength=1>
<Record Recommended='Mary B. McCann' Strength=1>
<Record Recommended='Susanne Wright' Strength=1>
<Record Recommended='Valéry Koko Kingue' Strength=1>
<Record Recommended='Laura Harris' Strength=1>
<Record Recommended='Steve Lemme' Strength=1>
<Record Recommended='Michael Ormsby' Strength=1>
<Record Recommended='Aurora Depestre' Strength=1>
<Record Recommended='William Bronder' Strength=1>
<Record Recommended='J.R. Horne' Strength=1>
<Record Recommended='Melissa Brasselle' Strength=1>
<Record Recommended='Bernard-Pierre Donnadieu' Strength=1>
<Record Recommended='Amy Stiller' Strength=1>
<Record Recommended='Olivier Baroux' Strength=1>
<Record Recommended='Cindy Cheung' Strength=1>
<Record Recommended='Kellan Lutz' Strength=1>
<Record Recommended='Patrick Dewaere' Strength=1>
<Record Recommended='Liz Vassey' Strength=1>
<Record Recommended='Beatrice Straight' Strength=1>
<Record Recommended='Edd Byrnes' Strength=1>
<Record Recommended='Lara Dutta' Strength=1>
<Record Recommended='Terrylene' Strength=1>
<Record Recommended='Salman Rushdie' Strength=1>
<Record Recommended='Samantha Fox' Strength=1>
<Record Recommended='Anne-Grethe Bjarup Riis' Strength=1>
<Record Recommended='Gideon Emery' Strength=1>
<Record Recommended='Alyson Michalk' Strength=1>
<Record Recommended='Tricia Helfer' Strength=1>
<Record Recommended='Doris Schade' Strength=1>
<Record Recommended='Rajesh Khattar' Strength=1>
<Record Recommended='Cory Hardrict' Strength=1>
<Record Recommended='Gerry Black' Strength=1>
<Record Recommended='Maria Mason' Strength=1>
<Record Recommended='Xavier Saint-Macary' Strength=1>
<Record Recommended='Shelley Fabares' Strength=1>
<Record Recommended='Michel Robin' Strength=1>
<Record Recommended='Matt Adler' Strength=1>
<Record Recommended='Barbara Dittus' Strength=1>
<Record Recommended='Tajsha Thomas' Strength=1>
<Record Recommended='Michael Sorich' Strength=1>
<Record Recommended='Jack Mulcahy' Strength=1>
<Record Recommended='Joanna Scanlan' Strength=1>
<Record Recommended='Al White' Strength=1>
<Record Recommended='Karen Ford' Strength=1>
<Record Recommended='Gregory Nicotero' Strength=1>
<Record Recommended='Bill Brochtrup' Strength=1>
<Record Recommended='Stéphane Boucher' Strength=1>
<Record Recommended='Elisabeth Trissenaar' Strength=1>
<Record Recommended='Harry Van Gorkum' Strength=1>
<Record Recommended='Gertraud Kreissig' Strength=1>
<Record Recommended='Clemens Deindl' Strength=1>
<Record Recommended='Henry Calvert' Strength=1>
<Record Recommended='Dennis Lipscomb' Strength=1>
<Record Recommended='Katharine Hepburn' Strength=1>
<Record Recommended='Courtney Gains' Strength=1>
<Record Recommended='Alfie Bass' Strength=1>
<Record Recommended='Xzibit' Strength=1>
<Record Recommended='Ed Wheeler' Strength=1>
<Record Recommended='Scott Thompson' Strength=1>
<Record Recommended='Dominique Lavanant' Strength=1>
<Record Recommended='Thomas L. Corneliussen' Strength=1>
<Record Recommended='Ruth Roman' Strength=1>
<Record Recommended='Damian Jewan Lee' Strength=1>
<Record Recommended='Viktoria Dihen' Strength=1>
<Record Recommended='Alexander Fehling' Strength=1>
<Record Recommended='Landall Goolsby' Strength=1>
<Record Recommended='Steven Culp' Strength=1>
<Record Recommended='Judy Toll' Strength=1>
<Record Recommended='Dave Hill' Strength=1>
<Record Recommended='Mélanie Thierry' Strength=1>
<Record Recommended="'Cousin Brucie' Morrow" Strength=1>
<Record Recommended='Andy Smart' Strength=1>
<Record Recommended='Ken Jones' Strength=1>
<Record Recommended='Carlton Headley' Strength=1>
<Record Recommended='Maxence Mailfort' Strength=1>
<Record Recommended='Marie Versini' Strength=1>
<Record Recommended='Celia Imrie' Strength=1>
<Record Recommended='Charlotte Vermeil' Strength=1>
<Record Recommended='Joey Dedio' Strength=1>
<Record Recommended='Steven Waddington' Strength=1>
<Record Recommended='Kasha Kropinski' Strength=1>
<Record Recommended='Michael Gordon' Strength=1>
<Record Recommended='Fritz Muliar' Strength=1>
<Record Recommended='Kaya Scodelario' Strength=1>
<Record Recommended='Holly Valance' Strength=1>
<Record Recommended='Dwight Schultz' Strength=1>
<Record Recommended='David Brian' Strength=1>
<Record Recommended='Kelly Jo Minter' Strength=1>
<Record Recommended='Alejandro Rey' Strength=1>
<Record Recommended='Robert Machray' Strength=1>
<Record Recommended='Bill M. Ryusaki' Strength=1>
<Record Recommended='Marshall McLuhan' Strength=1>
<Record Recommended='Marlene Lawston' Strength=1>
<Record Recommended='Manny Brown' Strength=1>
<Record Recommended='Valerie Azlynn' Strength=1>
<Record Recommended='Trine Dyrholm' Strength=1>
<Record Recommended='Robbie Rist' Strength=1>
<Record Recommended='Tilli Breidenbach' Strength=1>
<Record Recommended='Philippe Caroit' Strength=1>
<Record Recommended='Andrew Lincoln' Strength=1>
<Record Recommended='Margot Werner' Strength=1>
<Record Recommended='Kate Mulgrew' Strength=1>
<Record Recommended='Thom Sharp' Strength=1>
<Record Recommended='Danny Schiller' Strength=1>
<Record Recommended='Manuela Simon' Strength=1>
<Record Recommended='Ingvar Eggert Sigurðsson' Strength=1>
<Record Recommended='Jason Kelly' Strength=1>
<Record Recommended='Greg Burson' Strength=1>
<Record Recommended='Rene Elizondo' Strength=1>
<Record Recommended='Geordie Johnson' Strength=1>
<Record Recommended='Pierre Michaël' Strength=1>
<Record Recommended='Debra Feuer' Strength=1>
<Record Recommended='Jonathan Walker' Strength=1>
<Record Recommended='Tomas Milian' Strength=1>
<Record Recommended='Rachel Skarsten' Strength=1>
<Record Recommended='Laila Morse' Strength=1>
<Record Recommended='Akhil Jackson' Strength=1>
<Record Recommended='Andrew Charles Koch' Strength=1>
<Record Recommended='Noam Jenkins' Strength=1>
<Record Recommended='Lila Munro' Strength=1>
<Record Recommended='Kara Beth Taylor' Strength=1>
<Record Recommended='Tom Felton' Strength=1>
<Record Recommended='Brennan Brown' Strength=1>
<Record Recommended='Jonathon Trent' Strength=1>
<Record Recommended='Anna Becker' Strength=1>
<Record Recommended='Nana Gbewonyo' Strength=1>
<Record Recommended='Ruth Sheen' Strength=1>
<Record Recommended='Massimo Girotti' Strength=1>
<Record Recommended='Priscilla Lauris' Strength=1>
<Record Recommended='Ginger Lynn Allen' Strength=1>
<Record Recommended='Sheryl Crow' Strength=1>
<Record Recommended='Elaine Riley' Strength=1>
<Record Recommended='Fiona Fullerton' Strength=1>
<Record Recommended='James Defelice' Strength=1>
<Record Recommended='Mark Devine' Strength=1>
<Record Recommended="John O'Hurley" Strength=1>
<Record Recommended='George Murcell' Strength=1>
<Record Recommended='Eddie Rouse' Strength=1>
<Record Recommended='Philippe Laudenbach' Strength=1>
<Record Recommended='Ludwig Donath' Strength=1>
<Record Recommended='Harald Jopt' Strength=1>
<Record Recommended='Doug Lennox' Strength=1>
<Record Recommended='Chandler Hill' Strength=1>
<Record Recommended='Mario Loya' Strength=1>
<Record Recommended='Elizabeth Rice' Strength=1>
<Record Recommended='Sven-Bertil Taube' Strength=1>
<Record Recommended='Richard M. McNally' Strength=1>
<Record Recommended='Victor Gojcaj' Strength=1>
<Record Recommended='Dennis Sakamoto' Strength=1>
<Record Recommended='Ryan Kennedy' Strength=1>
<Record Recommended='Terry Alderton' Strength=1>
<Record Recommended='Patricia Neal' Strength=1>
<Record Recommended='Jeremy Callaghan' Strength=1>
<Record Recommended='Don Bloomfield' Strength=1>
<Record Recommended='Olga Kurylenko' Strength=1>
<Record Recommended='David Palffy' Strength=1>
<Record Recommended='Debbie Reynolds' Strength=1>
<Record Recommended='Sanjit De Silva' Strength=1>
<Record Recommended='Raban Bieling' Strength=1>
<Record Recommended='Peter Hübner' Strength=1>
<Record Recommended='Michael Treanor' Strength=1>
<Record Recommended='Morten Faldaas' Strength=1>
<Record Recommended='Yvette Heyden' Strength=1>
<Record Recommended='Marcus Lyle Brown' Strength=1>
<Record Recommended='Kai-Maria Steinkühler' Strength=1>
<Record Recommended='Brett DelBuono' Strength=1>
<Record Recommended='Dennis Burkley' Strength=1>
<Record Recommended='Roxanne Hart' Strength=1>
<Record Recommended='Jason Gedrick' Strength=1>
<Record Recommended='Robert Elliott' Strength=1>
<Record Recommended='Alex Hyde-White' Strength=1>
<Record Recommended='Michelle Bonilla' Strength=1>
<Record Recommended='Jan Triska' Strength=1>
<Record Recommended='Patti Yasutake' Strength=1>
<Record Recommended='Renato Scarpa' Strength=1>
<Record Recommended='Kristina Krepela' Strength=1>
<Record Recommended='Christian Camargo' Strength=1>
<Record Recommended='Fausto Callegarini' Strength=1>
<Record Recommended='Frank Latimore' Strength=1>
<Record Recommended='Fritz Diez' Strength=1>
<Record Recommended='Nthati Moshesh' Strength=1>
<Record Recommended='Hrothgar Mathews' Strength=1>
<Record Recommended='Wesley Addy' Strength=1>
<Record Recommended='Romy Schneider' Strength=1>
<Record Recommended='Melissa Rae Mahon' Strength=1>
<Record Recommended='Annette Linder' Strength=1>
<Record Recommended='Sami Bouajila' Strength=1>
<Record Recommended='Chiara Di Pede' Strength=1>
<Record Recommended='Jack May' Strength=1>
<Record Recommended='Nadine Van der Velde' Strength=1>
<Record Recommended='Kim Greist' Strength=1>
<Record Recommended='Benjamin Whitrow' Strength=1>
<Record Recommended='Mark Moses' Strength=1>
<Record Recommended='Carlos Leon' Strength=1>
<Record Recommended='Vince Corazza' Strength=1>
<Record Recommended='Mark Consuelos' Strength=1>
<Record Recommended='Daisy' Strength=1>
<Record Recommended='Jörg Gillner' Strength=1>
<Record Recommended='Frank Wood' Strength=1>
<Record Recommended='Earl Holliman' Strength=1>
<Record Recommended='Biff Elliot' Strength=1>
<Record Recommended='Tom Irwin' Strength=1>
<Record Recommended='Maurice Denham' Strength=1>
<Record Recommended='Umberto Orsini' Strength=1>
<Record Recommended='Christopher Dempsey' Strength=1>
<Record Recommended='Peter Guinness' Strength=1>
<Record Recommended='Bruce Locke' Strength=1>
<Record Recommended='Janet Carroll' Strength=1>
<Record Recommended='Charles Cioffi' Strength=1>
<Record Recommended='Chris Pedersen' Strength=1>
<Record Recommended='Robert Lesser' Strength=1>
<Record Recommended='Glenn Plummer' Strength=1>
<Record Recommended='Ernest Abuba' Strength=1>
<Record Recommended='John Francis Daley' Strength=1>
<Record Recommended='K.D. Lang' Strength=1>
<Record Recommended='Carrie Snodgress' Strength=1>
<Record Recommended='Tom Parker' Strength=1>
<Record Recommended='Anthony Lemke' Strength=1>
<Record Recommended='Charles Fleischer' Strength=1>
<Record Recommended='Stana Katic' Strength=1>
<Record Recommended='Dennis Holahan' Strength=1>
<Record Recommended='Jonathan Orcutt' Strength=1>
<Record Recommended='Marta Fernández Muro' Strength=1>
<Record Recommended='Kane Kosugi' Strength=1>
<Record Recommended='Jana Pallaske' Strength=1>
<Record Recommended='Kimberly Brooks' Strength=1>
<Record Recommended='Christopher Stone' Strength=1>
<Record Recommended='Nikita Lespinasse' Strength=1>
<Record Recommended='Khandi Alexander' Strength=1>
<Record Recommended='Renato Salvatori' Strength=1>
<Record Recommended='Peyton Hayslip' Strength=1>
<Record Recommended='Michael P. Moran' Strength=1>
<Record Recommended='Ian Abercrombie' Strength=1>
<Record Recommended='Sean Smith' Strength=1>
<Record Recommended='Wendy Gazelle' Strength=1>
<Record Recommended='Cindy Crawford' Strength=1>
<Record Recommended='Alan Fletcher' Strength=1>
<Record Recommended='Ned Brower' Strength=1>
<Record Recommended='Lina Sastri' Strength=1>
<Record Recommended='Sylva Kelegian' Strength=1>
<Record Recommended='Jeff Corey' Strength=1>
<Record Recommended='Oded Fehr' Strength=1>
<Record Recommended='Richard Biggs' Strength=1>
<Record Recommended='Jared Dorrance' Strength=1>
<Record Recommended='Arthur Young' Strength=1>
<Record Recommended='S. Epatha Merkerson' Strength=1>
<Record Recommended='Nina Dobrev' Strength=1>
<Record Recommended='Carole Lombard' Strength=1>
<Record Recommended='Kyalo Mativo' Strength=1>
<Record Recommended='Clara Hopkins Daniels' Strength=1>
<Record Recommended='Luis Mesonero' Strength=1>
<Record Recommended='Matthew Macfadyen' Strength=1>
<Record Recommended='Helga Feddersen' Strength=1>
<Record Recommended='Rutanya Alda' Strength=1>
<Record Recommended='Brendan Fehr' Strength=1>
<Record Recommended='Lauren C. Mayhew' Strength=1>
<Record Recommended='Clint James' Strength=1>
<Record Recommended='Alessandro Piscitelli' Strength=1>
<Record Recommended='Michael Nicolosi' Strength=1>
<Record Recommended='John Carter' Strength=1>
<Record Recommended='Merwin Mondesir' Strength=1>
<Record Recommended='Clément Sibony' Strength=1>
<Record Recommended='Gaye Brown' Strength=1>
<Record Recommended='J. Richey Nash' Strength=1>
<Record Recommended='Maximilian Schell' Strength=1>
<Record Recommended='Enzo Squillino Jr.' Strength=1>
<Record Recommended='Marvin Benoit' Strength=1>
<Record Recommended='Frankie Perrone' Strength=1>
<Record Recommended='Alain Uy' Strength=1>
<Record Recommended='Lee Sheward' Strength=1>
<Record Recommended='Chris Ambrose' Strength=1>
<Record Recommended='Solomon Burke' Strength=1>
<Record Recommended='Fabio Zenoni' Strength=1>
<Record Recommended='Philip Bolden' Strength=1>
<Record Recommended='Egon Krenz' Strength=1>
<Record Recommended='Matt Devere' Strength=1>
<Record Recommended='Denys Hawthorne' Strength=1>
<Record Recommended='Torben Liebrecht' Strength=1>
<Record Recommended='Ryan Scott' Strength=1>
<Record Recommended='Karl Johnson' Strength=1>
<Record Recommended='Gene Pyrz' Strength=1>
<Record Recommended='Phillip Jarrett' Strength=1>
<Record Recommended='Jack Gill' Strength=1>
<Record Recommended='Marcia Jean Kurtz' Strength=1>
<Record Recommended='Millford Fortenberry' Strength=1>
<Record Recommended='Terri J. Vaughn' Strength=1>
<Record Recommended='Juan Riedinger' Strength=1>
<Record Recommended='Anne Randall' Strength=1>
<Record Recommended='Konstantin Khabenskiy' Strength=1>
<Record Recommended='Noot Seear' Strength=1>
<Record Recommended='Virginia Christine' Strength=1>
<Record Recommended='Dante Spinotti' Strength=1>
<Record Recommended='Pietro Ragusa' Strength=1>
<Record Recommended='Eric Porter' Strength=1>
<Record Recommended='Richard Kuss' Strength=1>
<Record Recommended='Michael Mandell' Strength=1>
<Record Recommended='Peter Mensah' Strength=1>
<Record Recommended='Renee Props' Strength=1>
<Record Recommended='Jenny Mollen' Strength=1>
<Record Recommended='Guy Tréjan' Strength=1>
<Record Recommended='Juhi Chawla' Strength=1>
<Record Recommended='Ian Buchanan' Strength=1>
<Record Recommended='Chunky Pandey' Strength=1>
<Record Recommended='Liam James' Strength=1>
<Record Recommended='Candace Scholz' Strength=1>
<Record Recommended='Raegan Lamb' Strength=1>
<Record Recommended='Joie Lee' Strength=1>
<Record Recommended='Jakub Zdenek' Strength=1>
<Record Recommended='Stefanie Drummond' Strength=1>
<Record Recommended='Simone Signoret' Strength=1>
<Record Recommended='Oswaldo Delgado' Strength=1>
<Record Recommended='Hugh Gillin' Strength=1>
<Record Recommended='Louise B. Clausen' Strength=1>
<Record Recommended='Dana Eskelson' Strength=1>
<Record Recommended='Emilia Fortunato' Strength=1>
<Record Recommended='Mitch Kreindel' Strength=1>
<Record Recommended='Nicola Facondo' Strength=1>
<Record Recommended='Emma Chambers' Strength=1>
<Record Recommended='Claire Lautier' Strength=1>
<Record Recommended='Armin Rohde' Strength=1>
<Record Recommended='Maurice Compte' Strength=1>
<Record Recommended='John Alderton' Strength=1>
<Record Recommended='Stéphane Moquet' Strength=1>
<Record Recommended='Lee Weaver' Strength=1>
<Record Recommended='Amberlee Colson' Strength=1>
<Record Recommended='Judy Cornwell' Strength=1>
<Record Recommended='Sarah Jean Kubik' Strength=1>
<Record Recommended='David Forman' Strength=1>
<Record Recommended='Renee French' Strength=1>
<Record Recommended='Ambrosia Kelley' Strength=1>
<Record Recommended='Rick Mali' Strength=1>
<Record Recommended='Margo Harshman' Strength=1>
<Record Recommended='Jeremy McCurdie' Strength=1>
<Record Recommended='Joan Pringle' Strength=1>
<Record Recommended='Pál Makrai' Strength=1>
<Record Recommended='Johannes Zadrozny' Strength=1>
<Record Recommended='Robert Hansen' Strength=1>
<Record Recommended='Charley Ramm' Strength=1>
<Record Recommended='Saul Williams' Strength=1>
<Record Recommended='Bruce Purchase' Strength=1>
<Record Recommended='Rachel Lederman' Strength=1>
<Record Recommended='Stanley Ridges' Strength=1>
<Record Recommended='Teri Hatcher' Strength=1>
<Record Recommended='Alexandre Brik' Strength=1>
<Record Recommended='Levon Helm' Strength=1>
<Record Recommended='Richard Chamberlain' Strength=1>
<Record Recommended='Emiliano Redondo' Strength=1>
<Record Recommended='Alexandra Tydings' Strength=1>
<Record Recommended='Kelly Joe Dugan' Strength=1>
<Record Recommended='Skye McCole Bartusiak' Strength=1>
<Record Recommended='Simon Burke' Strength=1>
<Record Recommended='Matt De Matt' Strength=1>
<Record Recommended='Steven M. Gagnon' Strength=1>
<Record Recommended='Kai Rautenberg' Strength=1>
<Record Recommended='Michael Nyqvist' Strength=1>
<Record Recommended='Karen Hines' Strength=1>
<Record Recommended='Rebecca Wisocky' Strength=1>
<Record Recommended='Denise Daniels' Strength=1>
<Record Recommended='Laura Ward' Strength=1>
<Record Recommended='Sue Clark' Strength=1>
<Record Recommended='Calvin Lockhart' Strength=1>
<Record Recommended='Warren Stevens' Strength=1>
<Record Recommended='Barney Cohen' Strength=1>
<Record Recommended='Elina Larrauga' Strength=1>
<Record Recommended='Rand Kingsley' Strength=1>
<Record Recommended='Elio Germano' Strength=1>
<Record Recommended='Bo Svenson' Strength=1>
<Record Recommended='Emily Brownell' Strength=1>
<Record Recommended='Tamara Doege' Strength=1>
<Record Recommended='John Hall' Strength=1>
<Record Recommended='Sid Owen' Strength=1>
<Record Recommended='Christopher Chen' Strength=1>
<Record Recommended='Nancy McKeon' Strength=1>
<Record Recommended='Kadeem Hardison' Strength=1>
<Record Recommended='Hans Lucke' Strength=1>
<Record Recommended='Timothy Bottoms' Strength=1>
<Record Recommended='Roman Polanski' Strength=1>
<Record Recommended='Carole Davis' Strength=1>
<Record Recommended='Olivier Martinez' Strength=1>
<Record Recommended='Gregg Daniel' Strength=1>
<Record Recommended='Christina Vidal' Strength=1>
<Record Recommended="Federico D'Anna" Strength=1>
<Record Recommended='Urbain Cancelier' Strength=1>
<Record Recommended='Henry Judd Baker' Strength=1>
<Record Recommended='Jay C. Flippen' Strength=1>
<Record Recommended='Lori Birdsong' Strength=1>
<Record Recommended='Mathew Bose' Strength=1>
<Record Recommended='Maeve Andrews' Strength=1>
<Record Recommended='Matthew Romero Moore' Strength=1>
<Record Recommended='Ron Kolman' Strength=1>
<Record Recommended='Herbert Fux' Strength=1>
<Record Recommended='Don Strouse' Strength=1>
<Record Recommended='John Harms' Strength=1>
<Record Recommended='Jason James Richter' Strength=1>
<Record Recommended='David Haig' Strength=1>
<Record Recommended='Mark Nelmes' Strength=1>
<Record Recommended='Hattie Winston' Strength=1>
<Record Recommended='Suzanne Krull' Strength=1>
<Record Recommended='Jodhi May' Strength=1>
<Record Recommended='Francine Segal' Strength=1>
<Record Recommended='Audrie Neenan' Strength=1>
<Record Recommended='Stuart Lancaster' Strength=1>
<Record Recommended='Katya Virshilas' Strength=1>
<Record Recommended='James Van Der Beek' Strength=1>
<Record Recommended='Michelle Forbes' Strength=1>
<Record Recommended='Willoughby Gray' Strength=1>
<Record Recommended='Paul Antrim' Strength=1>
<Record Recommended='Delta Burke' Strength=1>
<Record Recommended='Elisabeth Fricker' Strength=1>
<Record Recommended='Adrien Dorval' Strength=1>
<Record Recommended='Christoph Luser' Strength=1>
<Record Recommended='Mark Persons' Strength=1>
<Record Recommended='Neal Jones' Strength=1>
<Record Recommended='Tracey Cherelle Jones' Strength=1>
<Record Recommended='Anatoli Davydov' Strength=1>
<Record Recommended='Emmanuel Xuereb' Strength=1>
<Record Recommended='Fred Owens' Strength=1>
<Record Recommended='Blanche Kommerell' Strength=1>
<Record Recommended='Doua Moua' Strength=1>
<Record Recommended='Elisabeth Waterston' Strength=1>
<Record Recommended='Nina Young' Strength=1>
<Record Recommended='Jessica Paré' Strength=1>
<Record Recommended='Pierre Jolivet' Strength=1>
<Record Recommended='David Markham' Strength=1>
<Record Recommended="Eddy 'Big Eddy' Bekombo" Strength=1>
<Record Recommended='Jim Bouton' Strength=1>
<Record Recommended='Friedo Solter' Strength=1>
<Record Recommended='Carl Forgione' Strength=1>
<Record Recommended='Montse G. Romeu' Strength=1>
<Record Recommended='Michael Petroni' Strength=1>
<Record Recommended='Chloe Bailey' Strength=1>
<Record Recommended='Alessandro Giuggioli' Strength=1>
<Record Recommended='Hilarie Burton' Strength=1>
<Record Recommended='Eva Longoria Parker' Strength=1>
<Record Recommended='Pat Musick' Strength=1>
<Record Recommended='Alexandra Nowak' Strength=1>
<Record Recommended='Melissa Saltzman' Strength=1>
<Record Recommended='Anthony Piccininni' Strength=1>
<Record Recommended='Josie Ho' Strength=1>
<Record Recommended='Louise Latham' Strength=1>
<Record Recommended='Malgoscha Gebel' Strength=1>
<Record Recommended="Eric 'Mick' Nathanson" Strength=1>
<Record Recommended='James Victor' Strength=1>
<Record Recommended='Ángel Alcázar' Strength=1>
<Record Recommended='David Denman' Strength=1>
<Record Recommended='Nancy Everhard' Strength=1>
<Record Recommended='Michelle Griffin' Strength=1>
<Record Recommended='Karmin Murcelo' Strength=1>
<Record Recommended='Raymone Robinson' Strength=1>
<Record Recommended='Laura Fraser' Strength=1>
<Record Recommended='Anne Swift' Strength=1>
<Record Recommended='Johnny Lewis' Strength=1>
<Record Recommended='Mackenzie Astin' Strength=1>
<Record Recommended='David Keeley' Strength=1>
<Record Recommended='John Finnegan' Strength=1>
<Record Recommended='Jeremy Glazer' Strength=1>
<Record Recommended='Ion Caramitru' Strength=1>
<Record Recommended='Hallee Hirsh' Strength=1>
<Record Recommended='Ronald Pickup' Strength=1>
<Record Recommended='Angie Mattson' Strength=1>
<Record Recommended='Robert J. Steinmiller Jr.' Strength=1>
<Record Recommended='Cara Buono' Strength=1>
<Record Recommended='Erwin Parker' Strength=1>
<Record Recommended='Ernst Hannawald' Strength=1>
<Record Recommended='Jason R. Lone Hill' Strength=1>
<Record Recommended='Hans Christian Blech' Strength=1>
<Record Recommended='Jason Blicker' Strength=1>
<Record Recommended='Rebecca Stanley' Strength=1>
<Record Recommended='Dan Monahan' Strength=1>
<Record Recommended='Katherine Heigl' Strength=1>
<Record Recommended='Alex Meneses' Strength=1>
<Record Recommended='Brad Whitford' Strength=1>
<Record Recommended='Chris McCarty' Strength=1>
<Record Recommended='Steve Benedict' Strength=1>
<Record Recommended='Cristina Brondo' Strength=1>
<Record Recommended='Ann Mahoney' Strength=1>
<Record Recommended='Dave Ruby' Strength=1>
<Record Recommended='Carole Bouquet' Strength=1>
<Record Recommended='Christine Harnos' Strength=1>
<Record Recommended='Felicity Dean' Strength=1>
<Record Recommended='Jean-Claude Binoc' Strength=1>
<Record Recommended='Lee Mong Vang' Strength=1>
<Record Recommended='Monty Bane' Strength=1>
<Record Recommended='Arjun Rampal' Strength=1>
<Record Recommended='Bobby Bell' Strength=1>
<Record Recommended='Robin Mullins' Strength=1>
<Record Recommended='Shmuel Levy' Strength=1>
<Record Recommended='Sara Sugarman' Strength=1>
<Record Recommended='Carlos López Moctezuma' Strength=1>
<Record Recommended='Kirk Penberthy' Strength=1>
<Record Recommended='Ron Fassler' Strength=1>
<Record Recommended='Brian Rhodes' Strength=1>
<Record Recommended='Valérie Quennessen' Strength=1>
<Record Recommended='Paola Sotgiu' Strength=1>
<Record Recommended='David Darlow' Strength=1>
<Record Recommended='David Calder' Strength=1>
<Record Recommended='Ursula Andress' Strength=1>
<Record Recommended='Valerie Wildman' Strength=1>
<Record Recommended='Matthew Borlenghi' Strength=1>
<Record Recommended='Pamela Collins' Strength=1>
<Record Recommended='Charles Boyer' Strength=1>
<Record Recommended='James Allodi' Strength=1>
<Record Recommended='Jean-Michel Lahmi' Strength=1>
<Record Recommended='Bertina Acevedo' Strength=1>
<Record Recommended='Tom McCamus' Strength=1>
<Record Recommended='Audie England' Strength=1>
<Record Recommended='András Bálint' Strength=1>
<Record Recommended='Akaji Maro' Strength=1>
<Record Recommended="Joe D'Angerio" Strength=1>
<Record Recommended='Chiara Pirri' Strength=1>
<Record Recommended='Maria Kalinina' Strength=1>
<Record Recommended='Marcelle Larice' Strength=1>
<Record Recommended='Chuck Shamata' Strength=1>
<Record Recommended='Owen Smith' Strength=1>
<Record Recommended='Scott Beach' Strength=1>
<Record Recommended='Nancy Sinatra' Strength=1>
<Record Recommended='Sigfrit Steiner' Strength=1>
<Record Recommended='Iain Glen' Strength=1>
<Record Recommended='Werner Ehrlicher' Strength=1>
<Record Recommended='John Halsey' Strength=1>
<Record Recommended='Zineb Oukach' Strength=1>
<Record Recommended='Danny Mummert' Strength=1>
<Record Recommended='Annabel Armour' Strength=1>
<Record Recommended='Christiane Paul' Strength=1>
<Record Recommended='Tip Tipping' Strength=1>
<Record Recommended='Raymond Gérôme' Strength=1>
<Record Recommended='Eric Cantona' Strength=1>
<Record Recommended='Chris April' Strength=1>
<Record Recommended='Jim Hope' Strength=1>
<Record Recommended='Kenya Jo Kennedy' Strength=1>
<Record Recommended='Mark Eden' Strength=1>
<Record Recommended='Penny Balfour' Strength=1>
<Record Recommended='Clive Merrison' Strength=1>
<Record Recommended='Tony Pierce' Strength=1>
<Record Recommended='Joe Spano' Strength=1>
<Record Recommended='Cliff Osmond' Strength=1>
<Record Recommended='Autumn Reeser' Strength=1>
<Record Recommended='Michael Ziegfeld' Strength=1>
<Record Recommended='Peter MacNeill' Strength=1>
<Record Recommended='Vincent Regan' Strength=1>
<Record Recommended='Francesco De Rosa' Strength=1>
<Record Recommended='Chua Kah Joo' Strength=1>
<Record Recommended='Natalie Jackson Mendoza' Strength=1>
<Record Recommended='Anaïs Demoustier' Strength=1>
<Record Recommended='Aleksander Mikic' Strength=1>
<Record Recommended='Brooke Burns' Strength=1>
<Record Recommended='Martin Joswick' Strength=1>
<Record Recommended='Sarita Choudhury' Strength=1>
<Record Recommended='Ona Grauer' Strength=1>
<Record Recommended='Traute Höss' Strength=1>
<Record Recommended='Dan Stanton' Strength=1>
<Record Recommended='Valérie Lemercier' Strength=1>
<Record Recommended='Olivia Hussey' Strength=1>
<Record Recommended='Nathan Osgood' Strength=1>
<Record Recommended='Christopher Fairbank' Strength=1>
<Record Recommended='Johannes Silberschneider' Strength=1>
<Record Recommended='Will Barnett' Strength=1>
<Record Recommended='Kim Stanley' Strength=1>
<Record Recommended='Alice Lo' Strength=1>
<Record Recommended='Klaus Manchen' Strength=1>
<Record Recommended='Michelle Martin-Coyne' Strength=1>
<Record Recommended='Marlene Artov' Strength=1>
<Record Recommended='Rachel Wilson' Strength=1>
<Record Recommended='Bill Maher' Strength=1>
<Record Recommended='Shuhe' Strength=1>
<Record Recommended='Marc de Jonge' Strength=1>
<Record Recommended='Sid Mitchell' Strength=1>
<Record Recommended='Duane Martin' Strength=1>
<Record Recommended='Veronica Mosgrove' Strength=1>
<Record Recommended='Benu Mabhena' Strength=1>
<Record Recommended='George Maharis' Strength=1>
<Record Recommended='Brigitte Nielsen' Strength=1>
<Record Recommended='Kerr Smith' Strength=1>
<Record Recommended='Georgie Cranford' Strength=1>
<Record Recommended='Léopoldine Serre' Strength=1>
<Record Recommended='Debra Berger' Strength=1>
<Record Recommended='John Phillips' Strength=1>
<Record Recommended='Jonathan Muller' Strength=1>
<Record Recommended='Don Keith Opper' Strength=1>
<Record Recommended='Joshua Cox' Strength=1>
<Record Recommended='Ann Peters' Strength=1>
<Record Recommended='Ashlyn Gere' Strength=1>
<Record Recommended='Virginia Kiser' Strength=1>
<Record Recommended='Barrie Ingham' Strength=1>
<Record Recommended='Erica Gavin' Strength=1>
<Record Recommended='Manuela Velasco' Strength=1>
<Record Recommended='Rob Zombie' Strength=1>
<Record Recommended='Benjamin Sadler' Strength=1>
<Record Recommended='Cordell Clyde' Strength=1>
<Record Recommended='Steve White' Strength=1>
<Record Recommended='Zitto Kazann' Strength=1>
<Record Recommended='Tasha Smith' Strength=1>
<Record Recommended='Leopoldo Trieste' Strength=1>
<Record Recommended='Lily Weiding' Strength=1>
<Record Recommended='Nectar Rose' Strength=1>
<Record Recommended='Jorge Luke' Strength=1>
<Record Recommended='Cory Lane' Strength=1>
<Record Recommended='David Cowgill' Strength=1>
<Record Recommended='Corey Glover' Strength=1>
<Record Recommended='Rudolf Wessely' Strength=1>
<Record Recommended='Margaret Sullavan' Strength=1>
<Record Recommended='Peter Fitz' Strength=1>
<Record Recommended='William Traylor' Strength=1>
<Record Recommended='Paul Ritter' Strength=1>
<Record Recommended='Daniel Caltagirone' Strength=1>
<Record Recommended='Juli Ashton' Strength=1>
<Record Recommended='Mort Shuman' Strength=1>
<Record Recommended='Adam Nelson' Strength=1>
<Record Recommended='Anian Zollner' Strength=1>
<Record Recommended='Geoffrey Wigdor' Strength=1>
<Record Recommended='Chuck Aber' Strength=1>
<Record Recommended='Angela Iurilli' Strength=1>
<Record Recommended='Patience Cleveland' Strength=1>
<Record Recommended='Eric Cornet' Strength=1>
<Record Recommended='Ian Shaw' Strength=1>
<Record Recommended='Doug Liechty Caskey' Strength=1>
<Record Recommended='Mark Derwin' Strength=1>
<Record Recommended='Jan Fedder' Strength=1>
<Record Recommended='Tony Steedman' Strength=1>
<Record Recommended='Marnette Patterson' Strength=1>
<Record Recommended='Michelan Sisti' Strength=1>
<Record Recommended='Robert A. Burns' Strength=1>
<Record Recommended='Traci Lords' Strength=1>
<Record Recommended='Anthony Mangano' Strength=1>
<Record Recommended='Robert Beatty' Strength=1>
<Record Recommended='Ann Selepegno' Strength=1>
<Record Recommended='Dominic Anciano' Strength=1>
<Record Recommended='Terrence Parks' Strength=1>
<Record Recommended='David Mattey' Strength=1>
<Record Recommended='Nikki Schieler Ziering' Strength=1>
<Record Recommended='Victoria Fodor' Strength=1>
<Record Recommended='Marius Weyers' Strength=1>
<Record Recommended='Mary Faktor' Strength=1>
<Record Recommended='Rick Gomez' Strength=1>
<Record Recommended='Ian Aspinall' Strength=1>
<Record Recommended='Frances de la Tour' Strength=1>
<Record Recommended='Carla Gallo' Strength=1>
<Record Recommended='Diana Maria Riva' Strength=1>
<Record Recommended='Rosemary Garris' Strength=1>
<Record Recommended='Sabine Azéma' Strength=1>
<Record Recommended='Sophie Monk' Strength=1>
<Record Recommended='Noel Marshall' Strength=1>
<Record Recommended='Damir Todorovic' Strength=1>
<Record Recommended='Madeleine Robinson' Strength=1>
<Record Recommended='Danielle Louise Harley' Strength=1>
<Record Recommended='Robert Blanche' Strength=1>
<Record Recommended='Christina Cabot' Strength=1>
<Record Recommended='Mildred Natwick' Strength=1>
<Record Recommended='Dylan Roberts' Strength=1>
<Record Recommended='Katrin Cartlidge' Strength=1>
<Record Recommended='Caroline Junko King' Strength=1>
<Record Recommended='Heather Lea Gerdes' Strength=1>
<Record Recommended='Cecilia Roth' Strength=1>
<Record Recommended='Chelan Simmons' Strength=1>
<Record Recommended='Mary Jo Catlett' Strength=1>
<Record Recommended='Keith Szarabajka' Strength=1>
<Record Recommended='Bert Freed' Strength=1>
<Record Recommended='Hardee T. Lineham' Strength=1>
<Record Recommended='Gary McCormack' Strength=1>
<Record Recommended='Carly Schroeder' Strength=1>
<Record Recommended='Veanne Cox' Strength=1>
<Record Recommended='Michael Chinyamurindi' Strength=1>
<Record Recommended='Colleen Crabtree' Strength=1>
<Record Recommended='George Shane' Strength=1>
<Record Recommended='Steve Austin' Strength=1>
<Record Recommended='Giovanna Mezzogiorno' Strength=1>
<Record Recommended='Deborah Foreman' Strength=1>
<Record Recommended='Jean Rochefort' Strength=1>
<Record Recommended='Maximo Morrone' Strength=1>
<Record Recommended='Finlay Welsh' Strength=1>
<Record Recommended='Willi Narloch' Strength=1>
<Record Recommended='Stewart Scudamore' Strength=1>
<Record Recommended='Beulah Garrick' Strength=1>
<Record Recommended='Chris Walker' Strength=1>
<Record Recommended='Michael Berry Jr.' Strength=1>
<Record Recommended='Dietrich Siegl' Strength=1>
<Record Recommended='Keith Skinner' Strength=1>
<Record Recommended='Franz Buchrieser' Strength=1>
<Record Recommended='Lulu Molina' Strength=1>
<Record Recommended='Sophie Rousseau' Strength=1>
<Record Recommended='Kim Sanches' Strength=1>
<Record Recommended='Leib Lensky' Strength=1>
<Record Recommended='Dave Madden' Strength=1>
<Record Recommended='Clarence Felder' Strength=1>
<Record Recommended='Judie Aronson' Strength=1>
<Record Recommended='Jerry Doyle' Strength=1>
<Record Recommended='Alex Norton' Strength=1>
<Record Recommended='Jessica Ashworth' Strength=1>
<Record Recommended='Miguel Molina' Strength=1>
<Record Recommended='Henri Serre' Strength=1>
<Record Recommended='Lala Sloatman' Strength=1>
<Record Recommended='Kyle Hansen' Strength=1>
<Record Recommended='Nathaniel Arcand' Strength=1>
<Record Recommended='Lawrence P. Casey' Strength=1>
<Record Recommended='Monika Woytowicz' Strength=1>
<Record Recommended='Jacob Pitts' Strength=1>
<Record Recommended='Sai-Kit Yung' Strength=1>
<Record Recommended='Adele Mara' Strength=1>
<Record Recommended='Charles Laughton' Strength=1>
<Record Recommended='David Swift' Strength=1>
<Record Recommended='Larry Flash Jenkins' Strength=1>
<Record Recommended='Mycle Brandy' Strength=1>
<Record Recommended='Denise Balthrop Cassidy' Strength=1>
<Record Recommended='Suzanne Snyder' Strength=1>
<Record Recommended='Brian Libby' Strength=1>
<Record Recommended='Linda Lavin' Strength=1>
<Record Recommended='Amber Rules' Strength=1>
<Record Recommended='Nicholas Elia' Strength=1>
<Record Recommended='Matt Ingersoll' Strength=1>
<Record Recommended='Mikeysha Calimoke' Strength=1>
<Record Recommended='Spike Jonze' Strength=1>
<Record Recommended='Jean Bejote Njamba' Strength=1>
<Record Recommended='Scatman Crothers' Strength=1>
<Record Recommended='Sarah Lassez' Strength=1>
<Record Recommended='Darrell Foster' Strength=1>
<Record Recommended='Vanya Rose' Strength=1>
<Record Recommended='Robert Buckley' Strength=1>
<Record Recommended='Marla Sokoloff' Strength=1>
<Record Recommended='Leonard Earl Howze' Strength=1>
<Record Recommended='Mike Lambert' Strength=1>
<Record Recommended='Shannon Woodward' Strength=1>
<Record Recommended='Cathleen Crier' Strength=1>
<Record Recommended='Enrique Lucero' Strength=1>
<Record Recommended='Shari Eubank' Strength=1>
<Record Recommended='Annette Badland' Strength=1>
<Record Recommended='George Furth' Strength=1>
<Record Recommended='Marissa Jaret Winokur' Strength=1>
<Record Recommended='Jo Ann Brody' Strength=1>
<Record Recommended='John Forsythe' Strength=1>
<Record Recommended='Billy Louviere' Strength=1>
<Record Recommended='Jean-Pierre Malo' Strength=1>
<Record Recommended='Wes Chatham' Strength=1>
<Record Recommended='Stine Stengade' Strength=1>
<Record Recommended='Matt McKenna' Strength=1>
<Record Recommended='J.D. Cannon' Strength=1>
<Record Recommended='Lilyan Chauvin' Strength=1>
<Record Recommended='Georges Poujouly' Strength=1>
<Record Recommended='Krzysztof Luft' Strength=1>
<Record Recommended='Will Roberts' Strength=1>
<Record Recommended='Bradley Cole' Strength=1>
<Record Recommended='Doug Bradley' Strength=1>
<Record Recommended='Elisabeth Brooks' Strength=1>
<Record Recommended='Mary Lou Vukov' Strength=1>
<Record Recommended='Elide Melli' Strength=1>
<Record Recommended='Mary González' Strength=1>
<Record Recommended='Geoffrey Keen' Strength=1>
<Record Recommended='Klaus Heydemann' Strength=1>
<Record Recommended='Finlay Currie' Strength=1>
<Record Recommended='Jay Johnston' Strength=1>
<Record Recommended='Jemma Blackwell' Strength=1>
<Record Recommended='Damon Gupton' Strength=1>
<Record Recommended="Chris O'Neil" Strength=1>
<Record Recommended='Corinne Calvet' Strength=1>
<Record Recommended='Karin Baal' Strength=1>
<Record Recommended='Heinz Peter Scholz' Strength=1>
<Record Recommended='Ho Hon Chou' Strength=1>
<Record Recommended='Morgan Brittany' Strength=1>
<Record Recommended='Reb Brown' Strength=1>
<Record Recommended='Mikkel Gaup' Strength=1>
<Record Recommended='Gwendoline Yeo' Strength=1>
<Record Recommended='Dustin Nguyen' Strength=1>
<Record Recommended='Agathe Natanson' Strength=1>
<Record Recommended='Michael Dolan' Strength=1>
<Record Recommended='Adrienne King' Strength=1>
<Record Recommended='Li Gong' Strength=1>
<Record Recommended='Crystle Lightning' Strength=1>
<Record Recommended='Keith Coogan' Strength=1>
<Record Recommended='Kyle T. Heffner' Strength=1>
<Record Recommended='Amber Benson' Strength=1>
<Record Recommended='Tracy Reed' Strength=1>
<Record Recommended='Robert Mammone' Strength=1>
<Record Recommended='Cornell John' Strength=1>
<Record Recommended='Travis Fine' Strength=1>
<Record Recommended='Lee Wallace' Strength=1>
<Record Recommended='Antonie Knoppers' Strength=1>
<Record Recommended='Jack McElhone' Strength=1>
<Record Recommended='Sandrine Bonnaire' Strength=1>
<Record Recommended='Robby Benson' Strength=1>
<Record Recommended='John Aylward' Strength=1>
<Record Recommended='Jay Bilas' Strength=1>
<Record Recommended='Jeanne Herviale' Strength=1>
<Record Recommended='Ricky Fataar' Strength=1>
<Record Recommended='Cassi Davis' Strength=1>
<Record Recommended='Anna Galiena' Strength=1>
<Record Recommended='Brett Rice' Strength=1>
<Record Recommended='Gianni Schettino' Strength=1>
<Record Recommended='Holly Cruikshank' Strength=1>
<Record Recommended='Minglie Chen' Strength=1>
<Record Recommended='Frédéric Bocquet' Strength=1>
<Record Recommended='Christian Kane' Strength=1>
<Record Recommended='Nicholas Sidi' Strength=1>
<Record Recommended='Anna Kendrick' Strength=1>
<Record Recommended='Julia Hornisch' Strength=1>
<Record Recommended='Irene Rich' Strength=1>
<Record Recommended='Sharman Joshi' Strength=1>
<Record Recommended='Jane March' Strength=1>
<Record Recommended='Ray Porter' Strength=1>
<Record Recommended='Mitali Mayekar' Strength=1>
<Record Recommended='Meshach Taylor' Strength=1>
<Record Recommended='Scott Cumberbatch' Strength=1>
<Record Recommended='Malcolm Stumpf' Strength=1>
<Record Recommended='Martina Gedeck' Strength=1>
<Record Recommended='Bill Cobbs' Strength=1>
<Record Recommended='Marina Berti' Strength=1>
<Record Recommended='Bailee Madison' Strength=1>
<Record Recommended='Eli Roth' Strength=1>
<Record Recommended='Bob Schott' Strength=1>
<Record Recommended='Pierre Zucca' Strength=1>
<Record Recommended='Gábor Hortobágyi' Strength=1>
<Record Recommended='Dennis Christopher' Strength=1>
<Record Recommended='Brandon Hammond' Strength=1>
<Record Recommended='Bruce Mahler' Strength=1>
<Record Recommended='Alan Scarfe' Strength=1>
<Record Recommended='Christopher Atkins' Strength=1>
<Record Recommended='Jerry Grayson' Strength=1>
<Record Recommended='Donna Harrison' Strength=1>
<Record Recommended='Robert Ridgely' Strength=1>
<Record Recommended='Ralph Brown' Strength=1>
<Record Recommended='Simon Shackleton' Strength=1>
<Record Recommended='Lorenzo Renzi' Strength=1>
<Record Recommended='Annette Paulmann' Strength=1>
<Record Recommended='Lee J. Cobb' Strength=1>
<Record Recommended='Sunil Shetty' Strength=1>
<Record Recommended='David Cowley' Strength=1>
<Record Recommended='Frank Baker' Strength=1>
<Record Recommended='Steve Williams' Strength=1>
<Record Recommended='Catherine Bell' Strength=1>
<Record Recommended='Arthur Lake' Strength=1>
<Record Recommended='Kay E. Kuter' Strength=1>
<Record Recommended='Kabir Bedi' Strength=1>
<Record Recommended='Wolf Kahler' Strength=1>
<Record Recommended='Isabelle Sadoyan' Strength=1>
<Record Recommended='Kim Raver' Strength=1>
<Record Recommended='Mosa Kaiser' Strength=1>
<Record Recommended='Manfred Maretzki' Strength=1>
<Record Recommended='Rodney Kageyama' Strength=1>
<Record Recommended='Horst Drinda' Strength=1>
<Record Recommended='Jerzy Skolimowski' Strength=1>
<Record Recommended='Fernando Vivanco' Strength=1>
<Record Recommended='Wills Robbins' Strength=1>
<Record Recommended='Carroll Baker' Strength=1>
<Record Recommended='Zachary David Cope' Strength=1>
<Record Recommended='Frank Albertson' Strength=1>
<Record Recommended='Radost Bokel' Strength=1>
<Record Recommended='Tiberio Greco' Strength=1>
<Record Recommended='Peter Halliday' Strength=1>
<Record Recommended='Jeff Kosloski' Strength=1>
<Record Recommended='Jeffrey Garcia' Strength=1>
<Record Recommended='Claus Strandberg' Strength=1>
<Record Recommended='Günter Strack' Strength=1>
<Record Recommended='Ed Speleers' Strength=1>
<Record Recommended='Jacques Perrin' Strength=1>
<Record Recommended='Tim Colceri' Strength=1>
<Record Recommended='Paw Henriksen' Strength=1>
<Record Recommended='Bodo Schmidt' Strength=1>
<Record Recommended='Carsten Naumann' Strength=1>
<Record Recommended='Franco Barbero' Strength=1>
<Record Recommended='Rachael Taylor' Strength=1>
<Record Recommended='Lothar Schellhorn' Strength=1>
<Record Recommended='Ahmed Best' Strength=1>
<Record Recommended='Farshad Kholghi' Strength=1>
<Record Recommended='Chandra Muszka' Strength=1>
<Record Recommended='Rick Davis' Strength=1>
<Record Recommended='Brenda Vaccaro' Strength=1>
<Record Recommended='Taye Diggs' Strength=1>
<Record Recommended='Rusty Schwimmer' Strength=1>
<Record Recommended='Lauren Hutton' Strength=1>
<Record Recommended='Colin Lawrence' Strength=1>
<Record Recommended='Paul Sloan' Strength=1>
<Record Recommended='Harriet Lenabe' Strength=1>
<Record Recommended='Belinda Balaski' Strength=1>
<Record Recommended='Adam Bramble' Strength=1>
<Record Recommended='Sabina Ruiz' Strength=1>
<Record Recommended='Piotr Polk' Strength=1>
<Record Recommended='Judd Omen' Strength=1>
<Record Recommended='Ernie Sabella' Strength=1>
<Record Recommended='Jim Ryan' Strength=1>
<Record Recommended='Emmanuelle Devos' Strength=1>
<Record Recommended='Jerry Paris' Strength=1>
<Record Recommended='Scott Grimes' Strength=1>
<Record Recommended='Kenny Ausubel' Strength=1>
<Record Recommended='Otto Preminger' Strength=1>
<Record Recommended='Robert Drivas' Strength=1>
<Record Recommended='Anna Popplewell' Strength=1>
<Record Recommended='Maria Carta' Strength=1>
<Record Recommended='Kaitlin Doubleday' Strength=1>
<Record Recommended='Charles Rahi Chun' Strength=1>
<Record Recommended='Katia Romanoff' Strength=1>
<Record Recommended='Olek Krupa' Strength=1>
<Record Recommended='Cortez Nance Jr.' Strength=1>
<Record Recommended='Roy Holder' Strength=1>
<Record Recommended='Jeremy Roberts' Strength=1>
<Record Recommended='Sophia Bush' Strength=1>
<Record Recommended='Joe Bostick' Strength=1>
<Record Recommended='Bobby Fite' Strength=1>
<Record Recommended='Laura Christensen' Strength=1>
<Record Recommended='Barbora Lukesová' Strength=1>
<Record Recommended='Jason Oliver' Strength=1>
<Record Recommended='Hugh Sachs' Strength=1>
<Record Recommended='Anointing Lukola' Strength=1>
<Record Recommended='Louis Emerick' Strength=1>
<Record Recommended='Thomas Scott' Strength=1>
<Record Recommended='Karen Glave' Strength=1>
<Record Recommended='June Whitfield' Strength=1>
<Record Recommended='Cindy Pickett' Strength=1>
<Record Recommended='Andy Griffith' Strength=1>
<Record Recommended='Steve Hytner' Strength=1>
<Record Recommended='Charlie Yanko' Strength=1>
<Record Recommended='Wiebke Reed' Strength=1>
<Record Recommended='Nikki Blonsky' Strength=1>
<Record Recommended='Jerry Hall' Strength=1>
<Record Recommended='Miles Christopher Bakshi' Strength=1>
<Record Recommended='Stephanie March' Strength=1>
<Record Recommended='Ed Ramey' Strength=1>
<Record Recommended='Boris Leskin' Strength=1>
<Record Recommended='Rose Keegan' Strength=1>
<Record Recommended='Alexa Gerasimovich' Strength=1>
<Record Recommended='James Ritz' Strength=1>
<Record Recommended='Annemarie Düringer' Strength=1>
<Record Recommended='Georgie Henley' Strength=1>
<Record Recommended='David Gallacher' Strength=1>
<Record Recommended='Rosario Zúñiga' Strength=1>
<Record Recommended='Colby Chester' Strength=1>
<Record Recommended='Clint Walker' Strength=1>
<Record Recommended='Francesco Quinn' Strength=1>
<Record Recommended='Robin Walsh' Strength=1>
<Record Recommended='Jun Kunimura' Strength=1>
<Record Recommended='Marie Gillain' Strength=1>
<Record Recommended='Angela Rawna' Strength=1>
<Record Recommended='Cara Lott' Strength=1>
<Record Recommended='Antal Farkas' Strength=1>
<Record Recommended='Erik Wedersøe' Strength=1>
<Record Recommended='Bronwen Coleman' Strength=1>
<Record Recommended='Antony Coleman' Strength=1>
<Record Recommended='Jerry Marshall' Strength=1>
<Record Recommended='Olivia Birkelund' Strength=1>
<Record Recommended='Peter Michael Goetz' Strength=1>
<Record Recommended='Kal Penn' Strength=1>
<Record Recommended='Catherine Disher' Strength=1>
<Record Recommended='Sarah Trigger' Strength=1>
<Record Recommended='Maud Buquet' Strength=1>
<Record Recommended='Annie Lennox' Strength=1>
<Record Recommended='Cathleen Nesbitt' Strength=1>
<Record Recommended='Jason Cerbone' Strength=1>
<Record Recommended='April Wood' Strength=1>
<Record Recommended='Ángel de Andrés López' Strength=1>
<Record Recommended='Alberto Fernández de Rosa' Strength=1>
<Record Recommended='Ryo Ishibashi' Strength=1>
<Record Recommended='Hugh Bonneville' Strength=1>
<Record Recommended='Bernadette Lafont' Strength=1>
<Record Recommended='Shari Albert' Strength=1>
<Record Recommended='Claude-Oliver Rudolph' Strength=1>
<Record Recommended='Michel Dubois' Strength=1>
<Record Recommended='Carlton Wilborn' Strength=1>
<Record Recommended='Laurie Bartram' Strength=1>
<Record Recommended='Bernard Johnson' Strength=1>
<Record Recommended='Dina D.' Strength=1>
<Record Recommended='Dana LaRue' Strength=1>
<Record Recommended='Sophiya Haque' Strength=1>
<Record Recommended='Christian Grenier' Strength=1>
<Record Recommended='Robbie Gee' Strength=1>
<Record Recommended='Alexis Rhee' Strength=1>
<Record Recommended='Michael Moritzen' Strength=1>
<Record Recommended='Hunter Stiebel' Strength=1>
<Record Recommended='Janet MacLachlan' Strength=1>
<Record Recommended='Vijessna Ferkic' Strength=1>
<Record Recommended='Nicholas Alexander' Strength=1>
<Record Recommended='Lucia Poli' Strength=1>
<Record Recommended='Steffen Wink' Strength=1>
<Record Recommended='Ryan McDonald' Strength=1>
<Record Recommended='Debora Weston' Strength=1>
<Record Recommended='Michael J. Burg' Strength=1>
<Record Recommended='Tan Hung Francione' Strength=1>
<Record Recommended='Zoë Wanamaker' Strength=1>
<Record Recommended='Larry Bird' Strength=1>
<Record Recommended='Leilani Sarelle' Strength=1>
<Record Recommended='Joseph C. Hopkins' Strength=1>
<Record Recommended='Nina Axelrod' Strength=1>
<Record Recommended='Paco Morayta' Strength=1>
<Record Recommended='Michael Dougherty' Strength=1>
<Record Recommended='Lindsay Crouse' Strength=1>
<Record Recommended='Jonathan Kaplan' Strength=1>
<Record Recommended='Simon MacCorkindale' Strength=1>
<Record Recommended='Klaus Maria Brandauer' Strength=1>
<Record Recommended='Elaine Kao' Strength=1>
<Record Recommended='Angel Aviles' Strength=1>
<Record Recommended='Roger Planchon' Strength=1>
<Record Recommended='Rodolfo Montero' Strength=1>
<Record Recommended='Star Birdyellowhead' Strength=1>
<Record Recommended='Marco Assante' Strength=1>
<Record Recommended='Charles Zucker' Strength=1>
<Record Recommended='Valeria Cavalli' Strength=1>
<Record Recommended='Joachim Hansen' Strength=1>
<Record Recommended='Susan Norman' Strength=1>
<Record Recommended='Kathleen Quinlan' Strength=1>
<Record Recommended='Johnny Walker' Strength=1>
<Record Recommended='Donna Douglas' Strength=1>
<Record Recommended='Joseph Badalucco Jr.' Strength=1>
<Record Recommended='Kevin Clash' Strength=1>
<Record Recommended='Steven Tash' Strength=1>
<Record Recommended='Harold Pinter' Strength=1>
<Record Recommended='Mille Lehfeldt' Strength=1>
<Record Recommended='Predrag Bjelac' Strength=1>
<Record Recommended='Cristina Contes' Strength=1>
<Record Recommended='Elizabeth Gorcey' Strength=1>
<Record Recommended='Cynthia Dale Scott' Strength=1>
<Record Recommended='Wyatt Knight' Strength=1>
<Record Recommended='Izabella Miko' Strength=1>
<Record Recommended='Jaason Simmons' Strength=1>
<Record Recommended='Ric Young' Strength=1>
<Record Recommended='Salvatore Paul Piro' Strength=1>
<Record Recommended='Barocca' Strength=1>
<Record Recommended='Armelia McQueen' Strength=1>
<Record Recommended='Robert Dix' Strength=1>
<Record Recommended='Georgina Grenville' Strength=1>
<Record Recommended='Walter Cronkite' Strength=1>
<Record Recommended='Taylor Lautner' Strength=1>
<Record Recommended='Colleen Foy' Strength=1>
<Record Recommended='T.P. McKenna' Strength=1>
<Record Recommended='Lyndsey Marshal' Strength=1>
<Record Recommended='Larry Simms' Strength=1>
<Record Recommended='Dalip Singh' Strength=1>
<Record Recommended='David Thornton' Strength=1>
<Record Recommended='Yorgo Constantine' Strength=1>
<Record Recommended='Gary Grubbs' Strength=1>
<Record Recommended='Mac McDonald' Strength=1>
<Record Recommended='Carlos García Cambero' Strength=1>
<Record Recommended='Sarah Livingston' Strength=1>
<Record Recommended='Sophie Loewe' Strength=1>
<Record Recommended='Eleanor Parker' Strength=1>
<Record Recommended='Luca Venantini' Strength=1>
<Record Recommended='Anthony Higgins' Strength=1>
<Record Recommended='Christine Belford' Strength=1>
<Record Recommended='Ulrich Tukur' Strength=1>
<Record Recommended='Irving Metzman' Strength=1>
<Record Recommended='Dennis Miller' Strength=1>
<Record Recommended='Gabriel Mann' Strength=1>
<Record Recommended='Wally George' Strength=1>
<Record Recommended='Juliette Arnaud' Strength=1>
<Record Recommended='Anouk Aimée' Strength=1>
<Record Recommended='Bill Henderson' Strength=1>
<Record Recommended='Henry Rowland' Strength=1>
<Record Recommended='Melody Kay' Strength=1>
<Record Recommended='Arlene Golonka' Strength=1>
<Record Recommended='Herschell Gordon Lewis' Strength=1>
<Record Recommended='Beau Starr' Strength=1>
<Record Recommended='George Lucas' Strength=1>
<Record Recommended='G. Ferrus' Strength=1>
<Record Recommended='Lorissa McComas' Strength=1>
<Record Recommended='Cameron Bowen' Strength=1>
<Record Recommended='Jesse Ventura' Strength=1>
<Record Recommended='Nikolai J. Lukinow' Strength=1>
<Record Recommended='Ekaterina Chtchelkanova' Strength=1>
<Record Recommended='Jeff Cohen' Strength=1>
<Record Recommended='Jean de Coninck' Strength=1>
<Record Recommended='Taylor LaGrange' Strength=1>
<Record Recommended='Karina Logue' Strength=1>
<Record Recommended='Richard Moir' Strength=1>
<Record Recommended='Janet Leigh' Strength=1>
<Record Recommended='Austin Macdonald' Strength=1>
<Record Recommended="Michael Donovan O'Donnell" Strength=1>
<Record Recommended='Jimmy Kimmel' Strength=1>
<Record Recommended='Gabrielle Union' Strength=1>
<Record Recommended='Mike Reid' Strength=1>
<Record Recommended='Siegfried Rauch' Strength=1>
<Record Recommended='Catherine Lachens' Strength=1>
<Record Recommended='Patrick St. Esprit' Strength=1>
<Record Recommended='Lisa Eilbacher' Strength=1>
<Record Recommended='Stacy Grooman' Strength=1>
<Record Recommended='Septula Sebogodi' Strength=1>
<Record Recommended='Uwe Mansshardt' Strength=1>
<Record Recommended='Rochelle Aytes' Strength=1>
<Record Recommended='Al Leong' Strength=1>
<Record Recommended='Louis de Funès' Strength=1>
<Record Recommended="Gina 'Ginger' Bernal" Strength=1>
<Record Recommended='Anne-Marie Blanc' Strength=1>
<Record Recommended='Douglas M. Griffin' Strength=1>
<Record Recommended='Elaine Jones' Strength=1>
<Record Recommended='Kel Mitchell' Strength=1>
<Record Recommended='Jessica Lee' Strength=1>
<Record Recommended='Véronique Balme' Strength=1>
<Record Recommended='Yvon Barrette' Strength=1>
<Record Recommended='Robert Jimenez' Strength=1>
<Record Recommended='Kimberley Davies' Strength=1>
<Record Recommended='James Patrick Stuart' Strength=1>
<Record Recommended='Monica Monica' Strength=1>
<Record Recommended='Cerrlera' Strength=1>
<Record Recommended='Tzi Ma' Strength=1>
<Record Recommended='Megan Fox' Strength=1>
<Record Recommended='Pat Kilbane' Strength=1>
<Record Recommended='André Hennicke' Strength=1>
<Record Recommended='Daniel Rey' Strength=1>
<Record Recommended='Klaus Pohl' Strength=1>
<Record Recommended='Heidi Hayes' Strength=1>
<Record Recommended='Edson T. Ribeiro' Strength=1>
<Record Recommended='Judith Anderson' Strength=1>
<Record Recommended='Tinsel Korey' Strength=1>
<Record Recommended='David Birney' Strength=1>
<Record Recommended='Heather Kole' Strength=1>
<Record Recommended='Tina Caspary' Strength=1>
<Record Recommended='Eddie Spears' Strength=1>
<Record Recommended='Günter Drescher' Strength=1>
<Record Recommended='Lombardo Boyar' Strength=1>
<Record Recommended='Siân Phillips' Strength=1>
<Record Recommended='Julian Richings' Strength=1>
<Record Recommended='John Billingsley' Strength=1>
<Record Recommended='Reginald C. Hayes' Strength=1>
<Record Recommended='Friederike Aust' Strength=1>
<Record Recommended='Dock P. Ellis Jr.' Strength=1>
<Record Recommended='Luciana Paolicelli' Strength=1>
<Record Recommended='Rolf Ludwig' Strength=1>
<Record Recommended='Johnny Legend' Strength=1>
<Record Recommended='George Costello' Strength=1>
<Record Recommended='Sumela Kay' Strength=1>
<Record Recommended='Malcolm Shields' Strength=1>
<Record Recommended='Barry Pearl' Strength=1>
<Record Recommended='Patricia Allison' Strength=1>
<Record Recommended='Vlastimil Brodský' Strength=1>
<Record Recommended='Garry Goodrow' Strength=1>
<Record Recommended='Andrea Fazekas' Strength=1>
<Record Recommended='Dana Wheeler-Nicholson' Strength=1>
<Record Recommended='Christian Coulson' Strength=1>
<Record Recommended='Véronique Jannot' Strength=1>
<Record Recommended='Cylk Cozart' Strength=1>
<Record Recommended='Ezra Dagan' Strength=1>
<Record Recommended='Lavelle Roby' Strength=1>
<Record Recommended='Christopher Buchholz' Strength=1>
<Record Recommended='Ken Lerner' Strength=1>
<Record Recommended='Diane Bellego' Strength=1>
<Record Recommended='Didi Conn' Strength=1>
<Record Recommended='Irene Karas' Strength=1>
<Record Recommended='Rudolph Anders' Strength=1>
<Record Recommended='Dominique Page' Strength=1>
<Record Recommended='Justin Urich' Strength=1>
<Record Recommended='Kai Lennox' Strength=1>
<Record Recommended='Inger Stevens' Strength=1>
<Record Recommended='Anne Marie Timoney' Strength=1>
<Record Recommended='Betty Laird' Strength=1>
<Record Recommended='Serge Marquand' Strength=1>
<Record Recommended='Lloyd Corrigan' Strength=1>
<Record Recommended='Rick Eby' Strength=1>
<Record Recommended='Herbert Grönemeyer' Strength=1>
<Record Recommended='Marilyn Wesley' Strength=1>
<Record Recommended='Lawrence Pressman' Strength=1>
<Record Recommended='Michael-Joel David Stuart' Strength=1>
<Record Recommended='Rami Malek' Strength=1>
<Record Recommended='Dan Sonney' Strength=1>
<Record Recommended='Jimmie Dale Gilmore' Strength=1>
<Record Recommended='Mel Gorham' Strength=1>
<Record Recommended='Gary Whelan' Strength=1>
<Record Recommended='Garry Tubbs' Strength=1>
<Record Recommended='Chris Benson' Strength=1>
<Record Recommended='Edward Schaaf' Strength=1>
<Record Recommended='Flemming Enevold' Strength=1>
<Record Recommended='Amidou' Strength=1>
<Record Recommended='Camille Natta' Strength=1>
<Record Recommended='Steve Whitmire' Strength=1>
<Record Recommended='Deborah Drakeford' Strength=1>
<Record Recommended='Oscar A. Colon' Strength=1>
<Record Recommended='Cyril Ritchard' Strength=1>
<Record Recommended='Monica Contini' Strength=1>
<Record Recommended='Tom Burlinson' Strength=1>
<Record Recommended='Wolf Kaiser' Strength=1>
<Record Recommended='Jake Milkovich' Strength=1>
<Record Recommended='Frances Lee McCain' Strength=1>
<Record Recommended='Amanda Schull' Strength=1>
<Record Recommended='Evanna Lynch' Strength=1>
<Record Recommended='Busy Philipps' Strength=1>
<Record Recommended='Edward G. Robinson' Strength=1>
<Record Recommended='Rupert Grint' Strength=1>
<Record Recommended='Kiti Manver' Strength=1>
<Record Recommended='Jamil Walker Smith' Strength=1>
<Record Recommended='Regina Taylor' Strength=1>
<Record Recommended='Karyn Parsons' Strength=1>
<Record Recommended='Glenn Taranto' Strength=1>
<Record Recommended='Ben Torgersen' Strength=1>
<Record Recommended='Om Puri' Strength=1>
<Record Recommended='Christopher Carley' Strength=1>
<Record Recommended='Frances Bergen' Strength=1>
<Record Recommended='Sally Wingert' Strength=1>
<Record Recommended='Susan Floyd' Strength=1>
<Record Recommended='Bruce Lidington' Strength=1>
<Record Recommended='Angelina Llongueras' Strength=1>
<Record Recommended='Bruce Guerre-Berthelot' Strength=1>
<Record Recommended='Owen Kavanagh' Strength=1>
<Record Recommended='Patrick Güldenberg' Strength=1>
<Record Recommended='Gerd Michael Henneberg' Strength=1>
<Record Recommended='Nia Peeples' Strength=1>
<Record Recommended='Bruce Bennett' Strength=1>
<Record Recommended='J.A. Preston' Strength=1>
<Record Recommended='Curtis Harrington' Strength=1>
<Record Recommended='Finn Carter' Strength=1>
<Record Recommended='Maria Andre' Strength=1>
<Record Recommended='Liisa Repo-Martell' Strength=1>
<Record Recommended='Hayley Marie Norman' Strength=1>
<Record Recommended='Aron Warner' Strength=1>
<Record Recommended='Claudia Ferri' Strength=1>
<Record Recommended='Jae Head' Strength=1>
<Record Recommended='Judith Ivey' Strength=1>
<Record Recommended='Barbara Rush' Strength=1>
<Record Recommended='Robert Deveau' Strength=1>
<Record Recommended='Sharon Ullrick' Strength=1>
<Record Recommended='Tom Tammi' Strength=1>
<Record Recommended='Alexa Davalos' Strength=1>
<Record Recommended='Gloria Stroock' Strength=1>
<Record Recommended='Wilfried Ortmann' Strength=1>
<Record Recommended='Jerry Swindall' Strength=1>
<Record Recommended='Morgan Fairchild' Strength=1>
<Record Recommended='Sidse Babett Knudsen' Strength=1>
<Record Recommended='Ben Lipitz' Strength=1>
<Record Recommended='Debbie Rochon' Strength=1>
<Record Recommended='Johanna Ray' Strength=1>
<Record Recommended='Dean Abston' Strength=1>
<Record Recommended='Tim Abell' Strength=1>
<Record Recommended='Kirk Baltz' Strength=1>
<Record Recommended='Richard Epcar' Strength=1>
<Record Recommended='Elsie Hilario' Strength=1>
<Record Recommended='William S. Taylor' Strength=1>
<Record Recommended='Ben Hamby' Strength=1>
<Record Recommended='Tamás Deák' Strength=1>
<Record Recommended='Matthew Berry' Strength=1>
<Record Recommended='Phil Harris' Strength=1>
<Record Recommended='Daniel Iron' Strength=1>
<Record Recommended='Jim Boeven' Strength=1>
<Record Recommended='Helen Ludlam' Strength=1>
<Record Recommended='David Haskell' Strength=1>
<Record Recommended='Jean Del Val' Strength=1>
<Record Recommended='James Holmes' Strength=1>
<Record Recommended='Tom Tate' Strength=1>
<Record Recommended='Jesse Cadotte' Strength=1>
<Record Recommended='Cyril Shaps' Strength=1>
<Record Recommended='Keith McErlean' Strength=1>
<Record Recommended='Natalia Avelon' Strength=1>
<Record Recommended='Giles New' Strength=1>
<Record Recommended='Cheryl Francis Harrington' Strength=1>
<Record Recommended='Amanda Barnett' Strength=1>
<Record Recommended='Isaiah Robinson' Strength=1>
<Record Recommended='Fawn Reed' Strength=1>
<Record Recommended='Shaun Sipos' Strength=1>
<Record Recommended='Estelle Omens' Strength=1>
<Record Recommended='Greta Lind' Strength=1>
<Record Recommended='Carl Weathers' Strength=1>
<Record Recommended='Hélène Surgère' Strength=1>
<Record Recommended='Zachary Quinto' Strength=1>
<Record Recommended='Alex Descas' Strength=1>
<Record Recommended='Remy K. Selma' Strength=1>
<Record Recommended='Sab Shimono' Strength=1>
<Record Recommended='Robert Ginty' Strength=1>
<Record Recommended='Holt McCallany' Strength=1>
<Record Recommended='Selma Stern' Strength=1>
<Record Recommended='Juan Uribe' Strength=1>
<Record Recommended='Dub Taylor' Strength=1>
<Record Recommended='Kelly LeBrock' Strength=1>
<Record Recommended='William Rice' Strength=1>
<Record Recommended='Valerie Casault' Strength=1>
<Record Recommended='Riccardo Francia' Strength=1>
<Record Recommended='Philip Davis' Strength=1>
<Record Recommended='Kali Hawk' Strength=1>
<Record Recommended='Natalie May' Strength=1>
<Record Recommended='Angela Winkler' Strength=1>
<Record Recommended='Torrey DeVitto' Strength=1>
<Record Recommended='Raul Julia Jr.' Strength=1>
<Record Recommended='William Lustig' Strength=1>
<Record Recommended='Gina Philips' Strength=1>
<Record Recommended='Leslie Hope' Strength=1>
<Record Recommended='Miguel Benavides' Strength=1>
<Record Recommended='Devin Oatway' Strength=1>
<Record Recommended='Anthony Thomas' Strength=1>
<Record Recommended='Michael Mark Edmondson' Strength=1>
<Record Recommended='Jenya Dodina' Strength=1>
<Record Recommended='Christopher Lawford' Strength=1>
<Record Recommended='Alexander Ziegler' Strength=1>
<Record Recommended='Jessy Schram' Strength=1>
<Record Recommended='Barbara Petritsch' Strength=1>
<Record Recommended='James McDaniel' Strength=1>
<Record Recommended='Christopher M. Clark' Strength=1>
<Record Recommended='Gilbert Gottfried' Strength=1>
<Record Recommended='Murray Salem' Strength=1>
<Record Recommended='George Wallace' Strength=1>
<Record Recommended='Xantha Radley' Strength=1>
<Record Recommended='Leo G. Carroll' Strength=1>
<Record Recommended='Matthew Currie Holmes' Strength=1>
<Record Recommended='Nicolas Beauvy' Strength=1>
<Record Recommended='Beata Paluch' Strength=1>
<Record Recommended='Saul Jephcott' Strength=1>
<Record Recommended='Ritchie Coster' Strength=1>
<Record Recommended='Howard Stern' Strength=1>
<Record Recommended='Geoff Stults' Strength=1>
<Record Recommended='Danny Blanco Hall' Strength=1>
<Record Recommended='Alex Pettyfer' Strength=1>
<Record Recommended='Assumpta Serna' Strength=1>
<Record Recommended='Johanna Clas' Strength=1>
<Record Recommended='Jean-Michel Noirey' Strength=1>
<Record Recommended='Sean Kelly' Strength=1>
<Record Recommended='Aaron Hendry' Strength=1>
<Record Recommended='Hans Irle' Strength=1>
<Record Recommended='Bernard Behrens' Strength=1>
<Record Recommended='Ilza Prestinari' Strength=1>
<Record Recommended='Rob Kerkovich' Strength=1>
<Record Recommended='Richard Linklater' Strength=1>
<Record Recommended='Zalman King' Strength=1>
<Record Recommended='Walo Lüönd' Strength=1>
<Record Recommended='Jason Rodriguez' Strength=1>
<Record Recommended='Berta Domínguez D.' Strength=1>
<Record Recommended='Sting' Strength=1>
<Record Recommended='Janice Karman' Strength=1>
<Record Recommended='The GZA' Strength=1>
<Record Recommended='Robin Harris' Strength=1>
<Record Recommended='Candus Churchill' Strength=1>
<Record Recommended='Alan Fudge' Strength=1>
<Record Recommended='Devon Alan' Strength=1>
<Record Recommended='Nelly' Strength=1>
<Record Recommended='Gaelan Connell' Strength=1>
<Record Recommended='Gina Ravera' Strength=1>
<Record Recommended='Julianne Phillips' Strength=1>
<Record Recommended='Donald Gibb' Strength=1>
<Record Recommended='Tito Larriva' Strength=1>
<Record Recommended='Brandon Ford Green' Strength=1>
<Record Recommended='Tony Kgoroge' Strength=1>
<Record Recommended='Binkie Stewart' Strength=1>
<Record Recommended="Larry 'Tank' Jones" Strength=1>
<Record Recommended='Peter Richardson' Strength=1>
<Record Recommended='Carola Braunbock' Strength=1>
<Record Recommended='Basil Wallace' Strength=1>
<Record Recommended='Jan Hooks' Strength=1>
<Record Recommended='Sylvia Syms' Strength=1>
<Record Recommended='Rachel Korine' Strength=1>
<Record Recommended='Aba Koïta' Strength=1>
<Record Recommended='Katey Sagal' Strength=1>
<Record Recommended='Enrique Almeida' Strength=1>
<Record Recommended='Tracy Scoggins' Strength=1>
<Record Recommended='Sam Ayers' Strength=1>
<Record Recommended='Kwesi Ameyaw' Strength=1>
<Record Recommended='Marc Poppel' Strength=1>
<Record Recommended='T. Bruce Page' Strength=1>
<Record Recommended='Krista Swan' Strength=1>
<Record Recommended='Natalie Press' Strength=1>
<Record Recommended='Thérèse Liotard' Strength=1>
<Record Recommended='Stuart Charno' Strength=1>
<Record Recommended='Laura Bro' Strength=1>
<Record Recommended='Julie Brown' Strength=1>
<Record Recommended='Kyle Cassie' Strength=1>
<Record Recommended='David Aaron Baker' Strength=1>
<Record Recommended='Phillip Rhys' Strength=1>
<Record Recommended='Josh Holt' Strength=1>
<Record Recommended='Cliff Gorman' Strength=1>
<Record Recommended='Gunnar Eyjólfsson' Strength=1>
<Record Recommended='David Graf' Strength=1>
<Record Recommended='Molly Bryant' Strength=1>
<Record Recommended='Jaakko Talaskivi' Strength=1>
<Record Recommended='Emmanuelle Béart' Strength=1>
<Record Recommended='Christopher Reid' Strength=1>
<Record Recommended='Austin Wolff' Strength=1>
<Record Recommended='Philip Tan' Strength=1>
<Record Recommended='Karel Roden' Strength=1>
<Record Recommended='Natasha Wightman' Strength=1>
<Record Recommended='Jean-Louis Trintignant' Strength=1>
<Record Recommended='Hichem Rostom' Strength=1>
<Record Recommended='Quinn Culkin' Strength=1>
<Record Recommended='Judith Roberts' Strength=1>
<Record Recommended='Moa Khouas' Strength=1>
<Record Recommended='Christina Sauvé' Strength=1>
<Record Recommended='Gaby Martone' Strength=1>
<Record Recommended='Jens Winter' Strength=1>
<Record Recommended='Pab Schwendimann' Strength=1>
<Record Recommended='Mickey Cottrell' Strength=1>
<Record Recommended='Joanna Pavlis' Strength=1>
<Record Recommended='Christine Laurent' Strength=1>
<Record Recommended='Werner Stocker' Strength=1>
<Record Recommended='Rosana Pastor' Strength=1>
<Record Recommended='Stephen Amell' Strength=1>
<Record Recommended='Andy Comeau' Strength=1>
<Record Recommended='Malena Gracia' Strength=1>
<Record Recommended='Ben Lin' Strength=1>
<Record Recommended='Mara Wilson' Strength=1>
<Record Recommended='Claude Gensac' Strength=1>
<Record Recommended='Sydney McCallister' Strength=1>
<Record Recommended='Don Galloway' Strength=1>
<Record Recommended='James Broderick' Strength=1>
<Record Recommended='Leonor Watling' Strength=1>
<Record Recommended='David Blazina' Strength=1>
<Record Recommended='Amira Casar' Strength=1>
<Record Recommended='Camilla Bendix' Strength=1>
<Record Recommended='Gerry Bednob' Strength=1>
<Record Recommended='Felix Klare' Strength=1>
<Record Recommended='Marcel Berbert' Strength=1>
<Record Recommended='Maureen Lipman' Strength=1>
<Record Recommended='Michel Gelobter' Strength=1>
<Record Recommended='George Chakiris' Strength=1>
<Record Recommended='Melissa Joan Hart' Strength=1>
<Record Recommended='Morgan Flynn' Strength=1>
<Record Recommended='David Anthony Marshall' Strength=1>
<Record Recommended='Tom Hulce' Strength=1>
<Record Recommended='Courtney-Jane White' Strength=1>
<Record Recommended='Amy Irving' Strength=1>
<Record Recommended='Camillia Sanes' Strength=1>
<Record Recommended='Billy Slaughter' Strength=1>
<Record Recommended='John Kapelos' Strength=1>
<Record Recommended='Dante Basco' Strength=1>
<Record Recommended='Juana Cordero' Strength=1>
<Record Recommended='Lars Mikkelsen' Strength=1>
<Record Recommended='Cathy Moriarty' Strength=1>
<Record Recommended='Vidya Balan' Strength=1>
<Record Recommended='Caitlin Clarke' Strength=1>
<Record Recommended='Antonio David Lyons' Strength=1>
<Record Recommended='Stephen Elliott' Strength=1>
<Record Recommended='Andrew Halbreich' Strength=1>
<Record Recommended='Carolyn Conwell' Strength=1>
<Record Recommended='Loni Anderson' Strength=1>
<Record Recommended='Meg White' Strength=1>
<Record Recommended='Anne Francis' Strength=1>
<Record Recommended='Andrew Stanton' Strength=1>
<Record Recommended='Brian Benben' Strength=1>
<Record Recommended='Teresa DePriest' Strength=1>
<Record Recommended='Jimmy Pike' Strength=1>
<Record Recommended='Diego J. Torres' Strength=1>
<Record Recommended='Debbie James' Strength=1>
<Record Recommended='Gitta Schweighöfer' Strength=1>
<Record Recommended='Judi Barton' Strength=1>
<Record Recommended='Deobia Oparei' Strength=1>
<Record Recommended='Brooke Bloom' Strength=1>
<Record Recommended='John Newton' Strength=1>
<Record Recommended='Juliane Köhler' Strength=1>
<Record Recommended='Pierre Elrick' Strength=1>
<Record Recommended='Mary Jo Smith' Strength=1>
<Record Recommended='Tomer Sisley' Strength=1>
<Record Recommended='Hunt Block' Strength=1>
<Record Recommended='Sandy Fox' Strength=1>
<Record Recommended='Bernhard Wicki' Strength=1>
<Record Recommended='Goran Kostic' Strength=1>
<Record Recommended='Terry Wilson' Strength=1>
<Record Recommended='Deborah Wittenberg' Strength=1>
<Record Recommended='Marco Bonini' Strength=1>
<Record Recommended='Francisca Caballero' Strength=1>
<Record Recommended='Allie Mickelson' Strength=1>
<Record Recommended='Anyury Trotman' Strength=1>
<Record Recommended='Mark Davenport' Strength=1>
<Record Recommended='Jesús Ochoa' Strength=1>
<Record Recommended='Marion Eaton' Strength=1>
<Record Recommended='Paul Simon' Strength=1>
<Record Recommended='Mark Pellington' Strength=1>
<Record Recommended='Stine Fischer Christensen' Strength=1>
<Record Recommended='Joel Kirby' Strength=1>
<Record Recommended='Scout Taylor-Compton' Strength=1>
<Record Recommended='Arne MacPherson' Strength=1>
<Record Recommended='Edward D. Wood Jr.' Strength=1>
<Record Recommended='Silvia Neef' Strength=1>
<Record Recommended='Dezsö Garas' Strength=1>
<Record Recommended='Meg Charette' Strength=1>
<Record Recommended='Peter Jeffrey' Strength=1>
<Record Recommended='Ellen Travolta' Strength=1>
<Record Recommended='Marianne Wünscher' Strength=1>
<Record Recommended='Antonello Campodifiori' Strength=1>
<Record Recommended='John Short' Strength=1>
<Record Recommended='Jonathan Hackett' Strength=1>
<Record Recommended='Joseph Maher' Strength=1>
<Record Recommended='Charlotte Chatton' Strength=1>
<Record Recommended='Derek Godfrey' Strength=1>
<Record Recommended='Isaac Sharry' Strength=1>
<Record Recommended='Trine Michelsen' Strength=1>
<Record Recommended='Paul Rae' Strength=1>
<Record Recommended='Frank Finlay' Strength=1>
<Record Recommended='Tatjana Patitz' Strength=1>
<Record Recommended='Bubba Smith' Strength=1>
<Record Recommended='Sal Lopez' Strength=1>
<Record Recommended='Phillip Glasser' Strength=1>
<Record Recommended='Lauren German' Strength=1>
<Record Recommended='Jim Cummings' Strength=1>
<Record Recommended='Sandra Kazan' Strength=1>
<Record Recommended='Morocco Omari' Strength=1>
<Record Recommended='James A. Watson Jr.' Strength=1>
<Record Recommended='Lloyd Avery II' Strength=1>
<Record Recommended="Chris O'Dowd" Strength=1>
<Record Recommended='Robert Donner' Strength=1>
<Record Recommended='Don Brady' Strength=1>
<Record Recommended='Christian Pagh' Strength=1>
<Record Recommended='Céline Dion' Strength=1>
<Record Recommended='Claire Trevor' Strength=1>
<Record Recommended='Ashley Artus' Strength=1>
<Record Recommended='Tino Insana' Strength=1>
<Record Recommended='Erik S. Klein' Strength=1>
<Record Recommended='Tom Hamilton' Strength=1>
<Record Recommended='Terence Hill' Strength=1>
<Record Recommended='Jennifer Balgobin' Strength=1>
<Record Recommended='Joseph Bologna' Strength=1>
<Record Recommended='Kimber West' Strength=1>
<Record Recommended='Sonny Chiba' Strength=1>
<Record Recommended='Rob Riggle' Strength=1>
<Record Recommended='Kirsten Prout' Strength=1>
<Record Recommended='Keith Stuart Thayer' Strength=1>
<Record Recommended='Adrienne Corri' Strength=1>
<Record Recommended='Derek Waters' Strength=1>
<Record Recommended='Malcolm Goodwin' Strength=1>
<Record Recommended='Liza Lapira' Strength=1>
<Record Recommended='Jesus Fuentes' Strength=1>
<Record Recommended='Richard Zeman' Strength=1>
<Record Recommended='Jeff Carlson' Strength=1>
<Record Recommended='Coati Mundi' Strength=1>
<Record Recommended='Peter Finch' Strength=1>
<Record Recommended='Anna Maxwell Martin' Strength=1>
<Record Recommended='Megan Dodds' Strength=1>
<Record Recommended='John Hines' Strength=1>
<Record Recommended='Véronique Genest' Strength=1>
<Record Recommended='Tamela J. Mann' Strength=1>
<Record Recommended='Frank Novak' Strength=1>
<Record Recommended='Mothusi Magano' Strength=1>
<Record Recommended='Eduardo Noriega' Strength=1>
<Record Recommended='Olivia Rosewood' Strength=1>
<Record Recommended='José Antonio Navarro' Strength=1>
<Record Recommended='Kieron Jecchinis' Strength=1>
<Record Recommended='Gail Boggs' Strength=1>
<Record Recommended='Candice Azzara' Strength=1>
<Record Recommended='Luis Camacho' Strength=1>
<Record Recommended='Mathar Licka Gueye' Strength=1>
<Record Recommended='Beverly Sheehan' Strength=1>
<Record Recommended='Ernestine Mercer' Strength=1>
<Record Recommended='Rebecca Hall' Strength=1>
<Record Recommended='Michael Durrell' Strength=1>
<Record Recommended='Carrie Henn' Strength=1>
<Record Recommended='Michael York' Strength=1>
<Record Recommended='Robert R. Shafer' Strength=1>
<Record Recommended='Lee Montgomery' Strength=1>
<Record Recommended='Mary Ellen Trainor' Strength=1>
<Record Recommended='Raven De La Croix' Strength=1>
<Record Recommended='Kaley Cuoco' Strength=1>
<Record Recommended='Danny Burstein' Strength=1>
<Record Recommended='Vivian Bonnell' Strength=1>
<Record Recommended='Ted Rusoff' Strength=1>
<Record Recommended='Robert Musgrave' Strength=1>
<Record Recommended='Jürgen Zartmann' Strength=1>
<Record Recommended='Marita Böhme' Strength=1>
<Record Recommended='Barbara Howard' Strength=1>
<Record Recommended='Surama De Castro' Strength=1>
<Record Recommended='Johannes Maus' Strength=1>
<Record Recommended='Brad Gibb' Strength=1>
<Record Recommended='Regine Lutz' Strength=1>
<Record Recommended='Bronson Pelletier' Strength=1>
<Record Recommended='Larry Aubrey' Strength=1>
<Record Recommended='Danny McCarthy' Strength=1>
<Record Recommended='Farida Ouchani' Strength=1>
<Record Recommended='Donna Townsend' Strength=1>
<Record Recommended='Marcella Lowery' Strength=1>
<Record Recommended='Tracy Wright' Strength=1>
<Record Recommended='Bradley Gregg' Strength=1>
<Record Recommended='Madeline Carroll' Strength=1>
<Record Recommended='Daniell Edwards' Strength=1>
<Record Recommended="'Big Jack' Provan" Strength=1>
<Record Recommended='Hiro Kanagawa' Strength=1>
<Record Recommended='Walter Breaux' Strength=1>
<Record Recommended='Jim Metzler' Strength=1>
<Record Recommended='Natalia Tena' Strength=1>
<Record Recommended='Tundi' Strength=1>
<Record Recommended='Michael DeLorenzo' Strength=1>
<Record Recommended='William Conrad' Strength=1>
<Record Recommended='Don Omar' Strength=1>
<Record Recommended='Beate Bille' Strength=1>
<Record Recommended='Scott Hamilton' Strength=1>
<Record Recommended='Bill Erwin' Strength=1>
<Record Recommended='Martin Benrath' Strength=1>
<Record Recommended='Barnaby Metschurat' Strength=1>
<Record Recommended='Henry Kingi' Strength=1>
<Record Recommended='Adriana DeMeo' Strength=1>
<Record Recommended='Nicolas Chagrin' Strength=1>
<Record Recommended='Cameron Daddo' Strength=1>
<Record Recommended='Esme Creed-Miles' Strength=1>
<Record Recommended='Jonathan Munk' Strength=1>
<Record Recommended='Deborah Duke' Strength=1>
<Record Recommended='Anthony Portillo' Strength=1>
<Record Recommended='Collins Pennie' Strength=1>
<Record Recommended='Dominic Purcell' Strength=1>
<Record Recommended='Karen Alexander' Strength=1>
<Record Recommended='Gérard Ismaël' Strength=1>
<Record Recommended='Barbara Steele' Strength=1>
<Record Recommended='Ian Tyler' Strength=1>
<Record Recommended='Robert Wilson' Strength=1>
<Record Recommended='Charlie Stratton' Strength=1>
<Record Recommended='Jens Jørn Spottag' Strength=1>
<Record Recommended='Sara Stockbridge' Strength=1>
<Record Recommended='Frederick Koehler' Strength=1>
<Record Recommended='Stefano Accorsi' Strength=1>
<Record Recommended='Rowena King' Strength=1>
<Record Recommended='Tori Spelling' Strength=1>
<Record Recommended='Daphne Rubin-Vega' Strength=1>
<Record Recommended='Leni Harper' Strength=1>
<Record Recommended='Ariane' Strength=1>
<Record Recommended='Jack LaLanne' Strength=1>
<Record Recommended='Charles Gunning' Strength=1>
<Record Recommended="Hugh O'Conor" Strength=1>
<Record Recommended='John Stephenson' Strength=1>
<Record Recommended='Jack De Sena' Strength=1>
<Record Recommended='Susan Buckner' Strength=1>
<Record Recommended='Frank O. Hill' Strength=1>
<Record Recommended='Vince Vieluf' Strength=1>
<Record Recommended='Ashley C. Coombs' Strength=1>
<Record Recommended='Simon Day' Strength=1>
<Record Recommended='Helga Sasse' Strength=1>
<Record Recommended='Ian Hanmore' Strength=1>
<Record Recommended='Alex Jennings' Strength=1>
<Record Recommended='Julieanne Steger' Strength=1>
<Record Recommended='Jeanette Miller' Strength=1>
<Record Recommended='Joy Boushel' Strength=1>
<Record Recommended='Danielle Kind' Strength=1>
<Record Recommended='Daran Norris' Strength=1>
<Record Recommended='Rachel Strouse' Strength=1>
<Record Recommended='Bernard Woringer' Strength=1>
<Record Recommended='Donna Anderson' Strength=1>
<Record Recommended='Rick Glassey' Strength=1>
<Record Recommended='Shaun Johnston' Strength=1>
<Record Recommended='O.J. Simpson' Strength=1>
<Record Recommended='Dan Joffre' Strength=1>
<Record Recommended='Michel Peyrelon' Strength=1>
<Record Recommended='Kim Chan' Strength=1>
<Record Recommended='Serge Dupire' Strength=1>
<Record Recommended='Bruno Barnabe' Strength=1>
<Record Recommended='Anne Christianson' Strength=1>
<Record Recommended='Howard Fong' Strength=1>
<Record Recommended='Guillaume Verdier' Strength=1>
<Record Recommended='Valérie Chassigneux' Strength=1>
<Record Recommended='Bill Wise' Strength=1>
<Record Recommended='Martin Scorsese' Strength=1>
<Record Recommended='Lennox Mathabathe' Strength=1>
<Record Recommended='Ponch Fenwick' Strength=1>
<Record Recommended='Daniel Radcliffe' Strength=1>
<Record Recommended='Fernando Vargas' Strength=1>
<Record Recommended='Francisca Pajuelo' Strength=1>
<Record Recommended='Lester Speight' Strength=1>
<Record Recommended='Laraine Day' Strength=1>
<Record Recommended='Daniel Roebuck' Strength=1>
<Record Recommended='Daiquan Smith' Strength=1>
<Record Recommended='Gary Bayer' Strength=1>
<Record Recommended='Wayne Alexander' Strength=1>
<Record Recommended='Jean-Claude Deret' Strength=1>
<Record Recommended='Theo Shall' Strength=1>
<Record Recommended='David Castro' Strength=1>
<Record Recommended='Don Messick' Strength=1>
<Record Recommended='Cleavon Little' Strength=1>
<Record Recommended='Alfonso Freeman' Strength=1>
<Record Recommended='Dale Godboldo' Strength=1>
<Record Recommended='Jodelle Ferland' Strength=1>
<Record Recommended='Michel Auclair' Strength=1>
<Record Recommended='Robert Davey' Strength=1>
<Record Recommended='Justin Walker' Strength=1>
<Record Recommended='Bimbo Hart' Strength=1>
<Record Recommended='Pauline Lynch' Strength=1>
<Record Recommended='Idil Üner' Strength=1>
<Record Recommended='Michelle Meyrink' Strength=1>
<Record Recommended='Martha Tenorio' Strength=1>
<Record Recommended='Tammi Cubilette' Strength=1>
<Record Recommended='Desmond Reilly' Strength=1>
<Record Recommended='Mike Horner' Strength=1>
<Record Recommended='William Prince' Strength=1>
<Record Recommended='Kenan Thompson' Strength=1>
<Record Recommended='Hans-Dieter Delkus' Strength=1>
<Record Recommended='Derek Thompson' Strength=1>
<Record Recommended='Desiree Zurowski' Strength=1>
<Record Recommended='Robert Kenneth Cooper' Strength=1>
<Record Recommended='K. Dock Yip' Strength=1>
<Record Recommended='Grayson McCouch' Strength=1>
<Record Recommended='John Lurie' Strength=1>
<Record Recommended='Melanie Harris' Strength=1>
<Record Recommended='David Dukes' Strength=1>
<Record Recommended='French Tickner' Strength=1>
<Record Recommended='Joe Marinelli' Strength=1>
<Record Recommended='Jesse Eisenberg' Strength=1>
<Record Recommended='Mark Feuerstein' Strength=1>
<Record Recommended='Margret Stange' Strength=1>
<Record Recommended='Kevin Whately' Strength=1>
<Record Recommended='Tara Leon' Strength=1>
<Record Recommended='Antonio Ragusa' Strength=1>
<Record Recommended='Murray Moston' Strength=1>
<Record Recommended='Francis Magee' Strength=1>
<Record Recommended='Yvonne Sciò' Strength=1>
<Record Recommended='Anndi McAfee' Strength=1>
<Record Recommended='Michael Tucci' Strength=1>
<Record Recommended='Sy Richardson' Strength=1>
<Record Recommended='Susan Lynch' Strength=1>
<Record Recommended='Robert Rudelson' Strength=1>
<Record Recommended='Romy Windsor' Strength=1>
<Record Recommended='Robert Costanzo' Strength=1>
<Record Recommended='Dick York' Strength=1>
<Record Recommended='Gabriel Hogan' Strength=1>
<Record Recommended='Shakti Kapoor' Strength=1>
<Record Recommended='Larry Joshua' Strength=1>
<Record Recommended='Eli Muñoz' Strength=1>
<Record Recommended='Heinz Hoenig' Strength=1>
<Record Recommended='Christine Barger' Strength=1>
<Record Recommended='David Alvarado' Strength=1>
<Record Recommended='Nils Düwell' Strength=1>
<Record Recommended='Franz Kollasch' Strength=1>
<Record Recommended='Lenore Thomas' Strength=1>
<Record Recommended='Adam Van Conant' Strength=1>
<Record Recommended='Dennis Storhøi' Strength=1>
<Record Recommended='Caveh Zahedi' Strength=1>
<Record Recommended='Jennifer Walcott' Strength=1>
<Record Recommended='Steven Hartley' Strength=1>
<Record Recommended='Ben Becker' Strength=1>
<Record Recommended="William 'Wee Willie' Davis" Strength=1>
<Record Recommended='Alex McSweeney' Strength=1>
<Record Recommended='Alan Cooke' Strength=1>
<Record Recommended='Aseneth Jurgenson' Strength=1>
<Record Recommended='Edith Volkmann' Strength=1>
<Record Recommended='Nathan Bexton' Strength=1>
<Record Recommended='James Pax' Strength=1>
<Record Recommended='Lee Ballard' Strength=1>
<Record Recommended='Eyal Podell' Strength=1>
<Record Recommended='Freda Foh Shen' Strength=1>
<Record Recommended='Humphrey Bogart' Strength=1>
<Record Recommended='Mark Rubin' Strength=1>
<Record Recommended='Rosalind Ayres' Strength=1>
<Record Recommended='Ed Bernard' Strength=1>
<Record Recommended='Harold Bennett' Strength=1>
<Record Recommended='Way Dong Woo' Strength=1>
<Record Recommended='Gerard McSorley' Strength=1>
<Record Recommended='Robert J. Ewald' Strength=1>
<Record Recommended='Millie Tirelli' Strength=1>
<Record Recommended='Jebidiah R. Dumas' Strength=1>
<Record Recommended='Spider Stacy' Strength=1>
<Record Recommended='Teri Austin' Strength=1>
<Record Recommended='Donald Moffat' Strength=1>
<Record Recommended='Russell G. Jones' Strength=1>
<Record Recommended='Doghmi Larbi' Strength=1>
<Record Recommended='Craig Zobel' Strength=1>
<Record Recommended='Hugo Steele' Strength=1>
<Record Recommended='Romane Bohringer' Strength=1>
<Record Recommended='Nicola Harrington' Strength=1>
<Record Recommended='David Gore' Strength=1>
<Record Recommended='Helena Carroll' Strength=1>
<Record Recommended='Norbert Leo Butz' Strength=1>
<Record Recommended='Will Estes' Strength=1>
<Record Recommended='Dorian Missick' Strength=1>
<Record Recommended='Sonya Ryzy-Ryski' Strength=1>
<Record Recommended='Roger Dunn' Strength=1>
<Record Recommended='Sean McCartin' Strength=1>
<Record Recommended="Cam'ron" Strength=1>
<Record Recommended='Kristin Adams' Strength=1>
<Record Recommended='Joe Torry' Strength=1>
<Record Recommended='Harve Presnell' Strength=1>
<Record Recommended='Valentina Yakunina' Strength=1>
<Record Recommended='Jennifer Stahl' Strength=1>
<Record Recommended='Elena Sahagun' Strength=1>
<Record Recommended='Slavko Labovic' Strength=1>
<Record Recommended='Tomi Salmela' Strength=1>
<Record Recommended='Luis Lantigua' Strength=1>
<Record Recommended='Bruce Kirby' Strength=1>
<Record Recommended='Jack Kehoe' Strength=1>
<Record Recommended='Chris Matthews' Strength=1>
<Record Recommended='Christiane Krüger' Strength=1>
<Record Recommended='Jenny Strubin' Strength=1>
<Record Recommended='Irvine Welsh' Strength=1>
<Record Recommended='LaToya Chisholm' Strength=1>
<Record Recommended='Coleman Francis' Strength=1>
<Record Recommended='John Scurti' Strength=1>
<Record Recommended='Lone Lindorff' Strength=1>
<Record Recommended='William Fowle' Strength=1>
<Record Recommended='Gary Allen' Strength=1>
<Record Recommended='Elke Sommer' Strength=1>
<Record Recommended='Sabrina' Strength=1>
<Record Recommended='Luke Goss' Strength=1>
<Record Recommended='Peter Andersson' Strength=1>
<Record Recommended='Jody St. Michael' Strength=1>
<Record Recommended='Bruce Elliott' Strength=1>
<Record Recommended='Wendy Morrow Donaldson' Strength=1>
<Record Recommended='Monica White' Strength=1>
<Record Recommended='Paul Freeman' Strength=1>
<Record Recommended='Abdelhafid Metalsi' Strength=1>
<Record Recommended='Peter Boyles' Strength=1>
<Record Recommended='Volker Prechtel' Strength=1>
<Record Recommended='Jonathan Cherry' Strength=1>
<Record Recommended='Linda Gaye Scott' Strength=1>
<Record Recommended='Reynaldo Rey' Strength=1>
<Record Recommended='Walter Flanagan' Strength=1>
<Record Recommended='Steven Drozd' Strength=1>
<Record Recommended='Walter Bal' Strength=1>
<Record Recommended='John Boyd' Strength=1>
<Record Recommended='Corey Rand' Strength=1>
<Record Recommended='Roy McCrerey' Strength=1>
<Record Recommended='Morton Downey Jr.' Strength=1>
<Record Recommended='Paul Anthony' Strength=1>
<Record Recommended='Ahney Her' Strength=1>
<Record Recommended='Larry Dean' Strength=1>
<Record Recommended='Sydney Tamiia Poitier' Strength=1>
<Record Recommended='Mohmed Hedi Bahri' Strength=1>
<Record Recommended='Martin Spang Olsen' Strength=1>
<Record Recommended='Peter Onorati' Strength=1>
<Record Recommended='Renée Taylor' Strength=1>
<Record Recommended='Hope Clarke' Strength=1>
<Record Recommended='Waltraud Kogel' Strength=1>
<Record Recommended='Charles Aznavour' Strength=1>
<Record Recommended='Markus Lyle Brown' Strength=1>
<Record Recommended='Francisco Bosch' Strength=1>
<Record Recommended='Elizabeth Lawrence' Strength=1>
<Record Recommended='Marius Frey' Strength=1>
<Record Recommended='Daniel Margotta' Strength=1>
<Record Recommended='Paul Préboist' Strength=1>
<Record Recommended='Ty Simpkins' Strength=1>
<Record Recommended='Bow Wow' Strength=1>
<Record Recommended='Niccolò Senni' Strength=1>
<Record Recommended='Ann Miller' Strength=1>
<Record Recommended='Angelika Gersdorf' Strength=1>
<Record Recommended='Marie Windsor' Strength=1>
<Record Recommended='Geraldine Hughes' Strength=1>
<Record Recommended='Jemima Rooper' Strength=1>
<Record Recommended='Christian Payne' Strength=1>
<Record Recommended='Vanessa Anne Hudgens' Strength=1>
<Record Recommended='Alain Delon' Strength=1>
<Record Recommended='Lana Young' Strength=1>
<Record Recommended='Roger E. Mosley' Strength=1>
<Record Recommended='Richard Cox' Strength=1>
<Record Recommended='Stephen E. Miller' Strength=1>
<Record Recommended='Charlotte Maier' Strength=1>
<Record Recommended='Stephen Nichols' Strength=1>
<Record Recommended='Antoinette Engel' Strength=1>
<Record Recommended='José María Yazpik' Strength=1>
<Record Recommended='Bee Vang' Strength=1>
<Record Recommended='John Franklyn-Robbins' Strength=1>
<Record Recommended='Frank Morgan' Strength=1>
<Record Recommended='Franck Xie Cheng' Strength=1>
<Record Recommended='Nicholas Rich' Strength=1>
<Record Recommended='Essie Davis' Strength=1>
<Record Recommended='Cornelia Froboess' Strength=1>
<Record Recommended='Tyra Ferrell' Strength=1>
<Record Recommended='Jon Evans' Strength=1>
<Record Recommended='Ursula Am-Ende' Strength=1>
<Record Recommended='Fernando Rey' Strength=1>
<Record Recommended='Nell Carter' Strength=1>
<Record Recommended='Tom Aldredge' Strength=1>
<Record Recommended='Shaker Paleja' Strength=1>
<Record Recommended='Caitlin McLean' Strength=1>
<Record Recommended='Willi One Blood' Strength=1>
<Record Recommended='Tony Bentley' Strength=1>
<Record Recommended='Naseeruddin Shah' Strength=1>
<Record Recommended='Hans-Joachim Blochwitz' Strength=1>
<Record Recommended='Anne Marie Dove' Strength=1>
<Record Recommended='Byrne Piven' Strength=1>
<Record Recommended='Meghanne Kessels' Strength=1>
<Record Recommended='John Wengraf' Strength=1>
<Record Recommended='Liz Wicker' Strength=1>
<Record Recommended='Elle Mckenzie' Strength=1>
<Record Recommended='Joseph Cellini' Strength=1>
<Record Recommended='Max Kasch' Strength=1>
<Record Recommended='Alain Lathière' Strength=1>
<Record Recommended='Trey Burvant' Strength=1>
<Record Recommended='Will Yun Lee' Strength=1>
<Record Recommended='David F. Friedman' Strength=1>
<Record Recommended='George A. Romero' Strength=1>
<Record Recommended='Karine Vanasse' Strength=1>
<Record Recommended='Jackie Illman' Strength=1>
<Record Recommended='Dennis Dun' Strength=1>
<Record Recommended='Del Reeves' Strength=1>
<Record Recommended='Rachel McDowall' Strength=1>
<Record Recommended='Sharif Rashed' Strength=1>
<Record Recommended="Sam O'Brien" Strength=1>
<Record Recommended='Richard Gilliland' Strength=1>
<Record Recommended='Lex Shrapnel' Strength=1>
<Record Recommended='Harsh Nayyar' Strength=1>
<Record Recommended='Samuel West' Strength=1>
<Record Recommended='Simón Andreu' Strength=1>
<Record Recommended='Chuck Loring' Strength=1>
<Record Recommended='Claudine Wilde' Strength=1>
<Record Recommended='Regan Moore' Strength=1>
<Record Recommended='John Ross' Strength=1>
<Record Recommended='Michael Enright' Strength=1>
<Record Recommended='Kevin Peter Hall' Strength=1>
<Record Recommended='James Otis' Strength=1>
<Record Recommended='Giampiero Judica' Strength=1>
<Record Recommended='Yves Montand' Strength=1>
<Record Recommended='Howard Vernon' Strength=1>
<Record Recommended='Shirley Stoler' Strength=1>
<Record Recommended='Aida Linares' Strength=1>
<Record Recommended='Stewart Howson' Strength=1>
<Record Recommended='Fred Tatasciore' Strength=1>
<Record Recommended='James Eric' Strength=1>
<Record Recommended='Cyril Raffaelli' Strength=1>
<Record Recommended='Bryan Renfro' Strength=1>
<Record Recommended='Dante James Hauser' Strength=1>
<Record Recommended='Nadine Velazquez' Strength=1>
<Record Recommended='Donna DeLory' Strength=1>
<Record Recommended='Taylor Mead' Strength=1>
<Record Recommended='Marc Cavell' Strength=1>
<Record Recommended='Jennifer Billingsley' Strength=1>
<Record Recommended='Charles Cowan Jr.' Strength=1>
<Record Recommended='Ali Kazim' Strength=1>
<Record Recommended='Jochen Thomas' Strength=1>
<Record Recommended='Nicholas George Stark' Strength=1>
<Record Recommended='Maria Machado' Strength=1>
<Record Recommended='Zabou Breitman' Strength=1>
<Record Recommended="Sean 'P. Diddy' Combs" Strength=1>
<Record Recommended='Andrew Manson' Strength=1>
<Record Recommended='Dane Rhodes' Strength=1>
<Record Recommended='John Calvin' Strength=1>
<Record Recommended='Stefan Lisewski' Strength=1>
<Record Recommended='Anders W. Berthelsen' Strength=1>
<Record Recommended='Harish Patel' Strength=1>
<Record Recommended='Rick Green' Strength=1>
<Record Recommended='Dave Spector' Strength=1>
<Record Recommended='Andrew Keir' Strength=1>
<Record Recommended='Ola Ray' Strength=1>
<Record Recommended="Floyd 'Red Crow' Westerman" Strength=1>
<Record Recommended='Bernard Le Coq' Strength=1>
<Record Recommended='Peter Donat' Strength=1>
<Record Recommended='Faith Ford' Strength=1>
<Record Recommended='Martha Gehman' Strength=1>
<Record Recommended='Andrew Sachs' Strength=1>
<Record Recommended='Ivo Garrani' Strength=1>
<Record Recommended='Anne Lambton' Strength=1>
<Record Recommended='Mike Vogel' Strength=1>
<Record Recommended='Jack Kelly' Strength=1>
<Record Recommended='Lou Perryman' Strength=1>
<Record Recommended='Julie Ordon' Strength=1>
<Record Recommended='Austyn Myers' Strength=1>
<Record Recommended='John Lavelle' Strength=1>
<Record Recommended='James Westerfield' Strength=1>
<Record Recommended='Joey DuPrez' Strength=1>
<Record Recommended='Brent Smiga' Strength=1>
<Record Recommended='David Baxt' Strength=1>
<Record Recommended='Ken Hutchison' Strength=1>
<Record Recommended='Gary Stretch' Strength=1>
<Record Recommended='Christopher Mintz-Plasse' Strength=1>
<Record Recommended='Elizabeth J. Carlisle' Strength=1>
<Record Recommended='Veronica Cartwright' Strength=1>
<Record Recommended='Tom Towles' Strength=1>
<Record Recommended='Barbara Sukowa' Strength=1>
<Record Recommended='Forbes Collins' Strength=1>
<Record Recommended='David Willis' Strength=1>
<Record Recommended='Andrew Blanchard' Strength=1>
<Record Recommended='Lola Cardona' Strength=1>
<Record Recommended='Chris McElprang' Strength=1>
<Record Recommended='Blaine Horton' Strength=1>
<Record Recommended='Frank Stoegerer' Strength=1>
<Record Recommended='Zinedine Soualem' Strength=1>
<Record Recommended='Carlene Moore' Strength=1>
<Record Recommended='Claude Berri' Strength=1>
<Record Recommended='Laurence Fox' Strength=1>
<Record Recommended='Joe Hursley' Strength=1>
<Record Recommended='Peggy Wood' Strength=1>
<Record Recommended='Tyler Foden' Strength=1>
<Record Recommended='Jonathan Ibbotson' Strength=1>
<Record Recommended='Gerald Lepkowski' Strength=1>
<Record Recommended='Linda Dano' Strength=1>
<Record Recommended='Annelise Hesme' Strength=1>
<Record Recommended='Algerita Wynn Lewis' Strength=1>
<Record Recommended='Linda Cardellini' Strength=1>
<Record Recommended='Tammy Trull' Strength=1>
<Record Recommended='Josh Hamilton' Strength=1>
<Record Recommended='Anton Pardoe' Strength=1>
<Record Recommended='Cassie Friel' Strength=1>
<Record Recommended='Aryeh Cooperstock' Strength=1>
<Record Recommended='Vincent Gallo' Strength=1>
<Record Recommended='Alex Boling' Strength=1>
<Record Recommended='Rio Hackford' Strength=1>
<Record Recommended='Ella Joyce' Strength=1>
<Record Recommended='Christopher Pettiet' Strength=1>
<Record Recommended='Brian Costantini' Strength=1>
<Record Recommended='Urs Althaus' Strength=1>
<Record Recommended='Christopher Erwin' Strength=1>
<Record Recommended='Raymond Cruz' Strength=1>
<Record Recommended='Linda Mpondo' Strength=1>
<Record Recommended='Georg Corten' Strength=1>
<Record Recommended='Colin Ferguson' Strength=1>
<Record Recommended='Edgar Givry' Strength=1>
<Record Recommended='Mathieu Carrière' Strength=1>
<Record Recommended='Michael Buie' Strength=1>
<Record Recommended='Maya Rudolph' Strength=1>
<Record Recommended='Donald Symington' Strength=1>
<Record Recommended='Reynaldo Gallegos' Strength=1>
<Record Recommended='Justin Louis' Strength=1>
<Record Recommended='Mary Louise Weller' Strength=1>
<Record Recommended='Mary-Margaret Humes' Strength=1>
<Record Recommended='Radek Bruna' Strength=1>
<Record Recommended='Lisanne Falk' Strength=1>
<Record Recommended='Ernst-Georg Schwill' Strength=1>
<Record Recommended='Sonja Richter' Strength=1>
<Record Recommended='Ruth White' Strength=1>
<Record Recommended='Georges Corraface' Strength=1>
<Record Recommended='Myleene Klass' Strength=1>
<Record Recommended='Paul Heidemann' Strength=1>
<Record Recommended='Bill Treacher' Strength=1>
<Record Recommended='Alexis Cassar' Strength=1>
<Record Recommended='Patsy Kensit' Strength=1>
<Record Recommended='Lars Rudolph' Strength=1>
<Record Recommended='Laura Ortiz' Strength=1>
<Record Recommended='Robin Sagstetter' Strength=1>
<Record Recommended='John Carpenter' Strength=1>
<Record Recommended='Bridget Moloney' Strength=1>
<Record Recommended='Carlos DeLoach' Strength=1>
<Record Recommended='Mike Pyeatt' Strength=1>
<Record Recommended='Bob Peck' Strength=1>
<Record Recommended='Kate Sargeant' Strength=1>
<Record Recommended='Vinny Vella Jr.' Strength=1>
<Record Recommended='Cornel Wilde' Strength=1>
<Record Recommended='Michael Sutton' Strength=1>
<Record Recommended='Eleanor Coppola' Strength=1>
<Record Recommended='Deidre Goodwin' Strength=1>
<Record Recommended="Ettore D'Alessandro" Strength=1>
<Record Recommended='Ramon Rodriguez' Strength=1>
<Record Recommended='Edward Hardwicke' Strength=1>
<Record Recommended='Jamie Donnelly' Strength=1>
<Record Recommended='Glenn Danzig' Strength=1>
<Record Recommended='Yomi Perry' Strength=1>
<Record Recommended='Jay Goede' Strength=1>
<Record Recommended='Joseph Siravo' Strength=1>
<Record Recommended='Anthony Johnson' Strength=1>
<Record Recommended='Lionel Atwill' Strength=1>
<Record Recommended='Arthur Sellers' Strength=1>
<Record Recommended='Cheryl Chase' Strength=1>
<Record Recommended='Aurélien Recoing' Strength=1>
<Record Recommended='Preben Harris' Strength=1>
<Record Recommended='Lars Bodin-Jorgensen' Strength=1>
<Record Recommended='Charlotte Ayanna' Strength=1>
<Record Recommended='Jake McLaughlin' Strength=1>
<Record Recommended='Mehcad Brooks' Strength=1>
<Record Recommended='Mike Henry' Strength=1>
<Record Recommended='Tom Leopold' Strength=1>
<Record Recommended='Angela Lanza' Strength=1>
<Record Recommended='Rock Hudson' Strength=1>
<Record Recommended='Rey Arteaga' Strength=1>
<Record Recommended='Claudia Stedelin' Strength=1>
<Record Recommended='Yoshi Oida' Strength=1>
<Record Recommended='Sammi Hanratty' Strength=1>
<Record Recommended='Ryan Wilson' Strength=1>
<Record Recommended='Lauren Ash' Strength=1>
<Record Recommended='Damon Younger' Strength=1>
<Record Recommended='Mia Tate' Strength=1>
<Record Recommended='Angelo Spizzirri' Strength=1>
<Record Recommended='Andrew Cassese' Strength=1>
<Record Recommended='Mari Morrow' Strength=1>
<Record Recommended='Reed Alexander' Strength=1>
<Record Recommended='Eve Korine' Strength=1>
<Record Recommended='Tony Nappo' Strength=1>
<Record Recommended='Tammy Blanchard' Strength=1>
<Record Recommended='Sydney Zarp' Strength=1>
<Record Recommended='Gail Strickland' Strength=1>
<Record Recommended='Dudley Moore' Strength=1>
<Record Recommended='Richard Webb' Strength=1>
<Record Recommended='Harvey Silver' Strength=1>
<Record Recommended='Larry Parks' Strength=1>
<Record Recommended='Maxine Bahns' Strength=1>
<Record Recommended='John V. Lindsay' Strength=1>
<Record Recommended='Jacek Koman' Strength=1>
<Record Recommended='Aaron Yoo' Strength=1>
<Record Recommended='Ken Foree' Strength=1>
<Record Recommended='Hans Conried' Strength=1>
<Record Recommended='Deepika Padukone' Strength=1>
<Record Recommended='Marguerite Moreau' Strength=1>
<Record Recommended='Hans-Joachim Teuscher' Strength=1>
<Record Recommended='Puthirith Chou' Strength=1>
<Record Recommended='Penelope Wilton' Strength=1>
<Record Recommended='Tonio Descanvelle' Strength=1>
<Record Recommended='Jean-Pierre Bacri' Strength=1>
<Record Recommended='Dale Neal' Strength=1>
<Record Recommended='Jennifer Saunders' Strength=1>
<Record Recommended='Rita Johnson' Strength=1>
<Record Recommended='Claire Ross-Brown' Strength=1>
<Record Recommended='Jake Lloyd' Strength=1>
<Record Recommended='Heike Makatsch' Strength=1>
<Record Recommended="Clay O'Brien" Strength=1>
<Record Recommended='Jesse Garcia' Strength=1>
<Record Recommended='Goran Visnjic' Strength=1>
<Record Recommended='Davenia McFadden' Strength=1>
<Record Recommended='Janet Julian' Strength=1>
<Record Recommended='Richy Müller' Strength=1>
<Record Recommended='Christine Lakin' Strength=1>
<Record Recommended='Andrew Ginsburg' Strength=1>
<Record Recommended='Christopher Reich' Strength=1>
<Record Recommended='Gordon B. Clarke' Strength=1>
<Record Recommended='Timothy Carhart' Strength=1>
<Record Recommended='Ramon Camacho' Strength=1>
<Record Recommended='Henry Victor' Strength=1>
<Record Recommended='Thomas Haerin' Strength=1>
<Record Recommended='Rachel Blanchard' Strength=1>
<Record Recommended='Erica Durance' Strength=1>
<Record Recommended='Charles Denner' Strength=1>
<Record Recommended='Gilbert R. Hill' Strength=1>
<Record Recommended='Harry Eden' Strength=1>
<Record Recommended='Jerry Ziesmer' Strength=1>
<Record Recommended='Cyril Cusack' Strength=1>
<Record Recommended='Kevin Nash' Strength=1>
<Record Recommended='Sylvia Saurel' Strength=1>
<Record Recommended='Sonny Castillo' Strength=1>
<Record Recommended='Karolina Muller' Strength=1>
<Record Recommended='Idris Elba' Strength=1>
<Record Recommended='Jacques Villeret' Strength=1>
<Record Recommended='Nate Parker' Strength=1>
<Record Recommended='Peter Lerchbaumer' Strength=1>
<Record Recommended='Betty Lou Holland' Strength=1>
<Record Recommended='Noureen DeWulf' Strength=1>
<Record Recommended='Johnathan Hallgrey' Strength=1>
<Record Recommended='Hassani Shapi' Strength=1>
<Record Recommended='Julie Ølgaard' Strength=1>
<Record Recommended='Valentine Pelka' Strength=1>
<Record Recommended='Marc Rioufol' Strength=1>
<Record Recommended='Budge Prewitt' Strength=1>
<Record Recommended='Richard Haydn' Strength=1>
<Record Recommended='Leon Lamar' Strength=1>
<Record Recommended='Keith Allan' Strength=1>
<Record Recommended='Nicholas Campbell' Strength=1>
<Record Recommended='Juanin Clay' Strength=1>
<Record Recommended='Greg Levine' Strength=1>
<Record Recommended='Hannah Pilkes' Strength=1>
<Record Recommended='Brad Dexter' Strength=1>
<Record Recommended='Lorelei King' Strength=1>
<Record Recommended='Oxmo Puccino' Strength=1>
<Record Recommended='Adrian Zmed' Strength=1>
<Record Recommended='Dagmara Dominczyk' Strength=1>
<Record Recommended='François Girard' Strength=1>
<Record Recommended='Harmony Blossom' Strength=1>
<Record Recommended='Hal Williams' Strength=1>
<Record Recommended='Michael Kopsa' Strength=1>
<Record Recommended='Dan Conroy' Strength=1>
<Record Recommended='Wolfgang Bodison' Strength=1>
<Record Recommended='Germaine de France' Strength=1>
<Record Recommended='Michel Fugain' Strength=1>
<Record Recommended='John Wells' Strength=1>
<Record Recommended='Trey Parker' Strength=1>
<Record Recommended='Heinz Bennent' Strength=1>
<Record Recommended='Marilyn Monroe' Strength=1>
<Record Recommended='David Dayan Fisher' Strength=1>
<Record Recommended='Chris Albrecht' Strength=1>
<Record Recommended='Pat Buttram' Strength=1>
<Record Recommended='Maurice Lamy' Strength=1>
<Record Recommended='Cullen Douglas' Strength=1>
<Record Recommended='Matt Bettinelli-Olpin' Strength=1>
<Record Recommended='Dick Cavett' Strength=1>
<Record Recommended='John Zurlo' Strength=1>
<Record Recommended='Dumisani Mbebe' Strength=1>
<Record Recommended='Maribel Verdú' Strength=1>
<Record Recommended='Ian Bannen' Strength=1>
<Record Recommended='Fiona Victory' Strength=1>
<Record Recommended='Sheri Moon Zombie' Strength=1>
<Record Recommended='Peggy Morgan' Strength=1>
<Record Recommended='Grace Lynn Kung' Strength=1>
<Record Recommended='Brian Reddy' Strength=1>
<Record Recommended='Roddy McDowall' Strength=1>
<Record Recommended='Brenda Canela' Strength=1>
<Record Recommended='Kristian Kiehling' Strength=1>
<Record Recommended='Pat Crawford Brown' Strength=1>
<Record Recommended='Brian Kerwin' Strength=1>
<Record Recommended='Tracy Middendorf' Strength=1>
<Record Recommended='George Rocky Sullivan' Strength=1>
<Record Recommended='Mike White' Strength=1>
<Record Recommended='Miri Fabian' Strength=1>
<Record Recommended='Daniel Polo' Strength=1>
<Record Recommended='Katharina Böhm' Strength=1>
<Record Recommended='Sean Gullette' Strength=1>
<Record Recommended='Janine LaManna' Strength=1>
<Record Recommended='Richard Berry' Strength=1>
<Record Recommended='Shane Rangi' Strength=1>
<Record Recommended='Gail Ann Lewis' Strength=1>
<Record Recommended='Adi Nitzan' Strength=1>
<Record Recommended='Ryan Kelley' Strength=1>
<Record Recommended='Tom Platz' Strength=1>
<Record Recommended='David Wilson Barnes' Strength=1>
<Record Recommended='Alma Martinez' Strength=1>
<Record Recommended='Melissa Holliday' Strength=1>
<Record Recommended='Samia Shoaib' Strength=1>
<Record Recommended='Peter Khubeke' Strength=1>
<Record Recommended='Nicola Walker' Strength=1>
<Record Recommended='Gottfried John' Strength=1>
<Record Recommended='Chevez Ezaneh' Strength=1>
<Record Recommended='Hammou Graïa' Strength=1>
<Record Recommended='Suzanne Pleshette' Strength=1>
<Record Recommended='Ele Keats' Strength=1>
<Record Recommended="Edmond O'Brien" Strength=1>
<Record Recommended='Alexis Thorpe' Strength=1>
<Record Recommended='Lane Garrison' Strength=1>
<Record Recommended='Moon Bloodgood' Strength=1>
<Record Recommended='Scott Booker' Strength=1>
<Record Recommended='Victor Rivers' Strength=1>
<Record Recommended='Rémy Girard' Strength=1>
<Record Recommended='Ben Barnes' Strength=1>
<Record Recommended='Jocelin Donahue' Strength=1>
<Record Recommended='Tony Ray Rossi' Strength=1>
<Record Recommended='Ludivine Sagnier' Strength=1>
<Record Recommended='Reg E. Cathey' Strength=1>
<Record Recommended='Tony Vogel' Strength=1>
<Record Recommended='Jim Dale' Strength=1>
<Record Recommended='Annabel Kershaw' Strength=1>
<Record Recommended='Max Deacon' Strength=1>
<Record Recommended='Steven Brown' Strength=1>
<Record Recommended='Michael Schneider' Strength=1>
<Record Recommended='Ben Brasier' Strength=1>
<Record Recommended='Quentin Grosset' Strength=1>
<Record Recommended='Steve Gardner' Strength=1>
<Record Recommended='Mark Cheng' Strength=1>
<Record Recommended='Herb Edelman' Strength=1>
<Record Recommended='Sam Scarber' Strength=1>
<Record Recommended='William D. Turner' Strength=1>
<Record Recommended='Dorian Sanchez' Strength=1>
<Record Recommended='Katja Paryla' Strength=1>
<Record Recommended='Alison Elliott' Strength=1>
<Record Recommended='Stefano Petronelli' Strength=1>
<Record Recommended='Chow Yun-Fat' Strength=1>
<Record Recommended='Eric Weinstein' Strength=1>
<Record Recommended='Ryan Ransdell' Strength=1>
<Record Recommended='Emily VanCamp' Strength=1>
<Record Recommended='Greg Wise' Strength=1>
<Record Recommended='Bernard Bourdeau' Strength=1>
<Record Recommended='Krystyn Wójcik' Strength=1>
<Record Recommended='Michael Cronin' Strength=1>
<Record Recommended='Steve DeCastro' Strength=1>
<Record Recommended='Sam Horrigan' Strength=1>
<Record Recommended='Will Ryan' Strength=1>
<Record Recommended='Brent Huff' Strength=1>
<Record Recommended='Debi Parker' Strength=1>
<Record Recommended='Jason Williams' Strength=1>
<Record Recommended='Paul Williams' Strength=1>
<Record Recommended='Renee Blaine' Strength=1>
<Record Recommended='Elizabeth McKay' Strength=1>
<Record Recommended='Brad Surosky' Strength=1>
<Record Recommended='Edward Mulhare' Strength=1>
<Record Recommended='Taylor Simpson' Strength=1>
<Record Recommended='Howie Mandel' Strength=1>
<Record Recommended='David Tennant' Strength=1>
<Record Recommended='Vinessa Shaw' Strength=1>
<Record Recommended='Alexander Skarsgård' Strength=1>
<Record Recommended='Emma Watson' Strength=1>
<Record Recommended='John Maxwell' Strength=1>
<Record Recommended='Amelia Warner' Strength=1>
<Record Recommended='Kristina Klebe' Strength=1>
<Record Recommended='Mark Williams' Strength=1>
<Record Recommended='Johnny Messner' Strength=1>
<Record Recommended='Roger Miremont' Strength=1>
<Record Recommended='Linda Shaw' Strength=1>
<Record Recommended='Erinn Allison' Strength=1>
<Record Recommended='Víctor González' Strength=1>
<Record Recommended='Spencer Klein' Strength=1>
<Record Recommended='Susie Essman' Strength=1>
<Record Recommended='Justin Chon' Strength=1>
<Record Recommended='Reimar J. Baur' Strength=1>
<Record Recommended='Wendie Malick' Strength=1>
<Record Recommended='Jake Cherry' Strength=1>
<Record Recommended='Dorothy Tree' Strength=1>
<Record Recommended='Nino Castelnuovo' Strength=1>
<Record Recommended='Cristos' Strength=1>
<Record Recommended='Achim Strietzel' Strength=1>
<Record Recommended='Guy Di Rigo' Strength=1>
<Record Recommended='Amita Nangia' Strength=1>
<Record Recommended='Don Dubbins' Strength=1>
<Record Recommended='Harry Melling' Strength=1>
<Record Recommended='Jürgen Tarrach' Strength=1>
<Record Recommended='Alice Lau' Strength=1>
<Record Recommended="Carmel O'Sullivan" Strength=1>
<Record Recommended='Hayley Atwell' Strength=1>
<Record Recommended='Peggy Miley' Strength=1>
<Record Recommended='AnnaSophia Robb' Strength=1>
<Record Recommended='Holly Sampson' Strength=1>
<Record Recommended='Benjamin Bryan' Strength=1>
<Record Recommended='Gina McKee' Strength=1>
<Record Recommended='Cathy Rankin' Strength=1>
<Record Recommended='Pasha D. Lychnikoff' Strength=1>
<Record Recommended='Eve Matheson' Strength=1>
<Record Recommended="Tom O'Brien" Strength=1>
<Record Recommended='Julie Strain' Strength=1>
<Record Recommended='Richard Tyson' Strength=1>
<Record Recommended='Petr Jákl' Strength=1>
<Record Recommended='Mike Hagerty' Strength=1>
<Record Recommended='Dustin Friel' Strength=1>
<Record Recommended='Vladimir Kulich' Strength=1>
<Record Recommended='Monika Gabriel' Strength=1>
<Record Recommended='Bob Wiltfong' Strength=1>
<Record Recommended='Michael Spears' Strength=1>
<Record Recommended='Mitch Pileggi' Strength=1>
<Record Recommended='Patrick Fontana' Strength=1>
<Record Recommended='Andrew Parks' Strength=1>
<Record Recommended='Robert Darnell' Strength=1>
<Record Recommended='Jonathan Hale' Strength=1>
<Record Recommended='Michael Welch' Strength=1>
<Record Recommended='Britta Gartner' Strength=1>
<Record Recommended='Alfred M. Jackson' Strength=1>
<Record Recommended='Jenny Gröllmann' Strength=1>
<Record Recommended='Gustaf Skarsgård' Strength=1>
<Record Recommended='Stine Bjerregaard' Strength=1>
<Record Recommended='Maisie Camilleri Preziosi' Strength=1>
<Record Recommended='Angus MacInnes' Strength=1>
<Record Recommended='Carrie Sturdevant Fisher' Strength=1>
<Record Recommended='William Bogert' Strength=1>
<Record Recommended='Loic Brabant' Strength=1>
<Record Recommended='Françoise Bertin' Strength=1>
<Record Recommended='Richard Ridings' Strength=1>
<Record Recommended='Karen Shenaz David' Strength=1>
<Record Recommended='Corinne Dacla' Strength=1>
<Record Recommended='Lorraine D. Glick' Strength=1>
<Record Recommended='Leasha' Strength=1>
<Record Recommended='Felice Orlandi' Strength=1>
<Record Recommended='Dave King' Strength=1>
<Record Recommended='Aimee Allen' Strength=1>
<Record Recommended='Matthew Barry' Strength=1>
<Record Recommended='Volkmar Kleinert' Strength=1>
<Record Recommended='Lionel Guyett' Strength=1>
<Record Recommended='Jun Hee Lee' Strength=1>
<Record Recommended='Deborah Grover' Strength=1>
<Record Recommended='Amanda Brooks' Strength=1>
<Record Recommended='Diwakar Pundir' Strength=1>
<Record Recommended='Sean Galdo' Strength=1>
<Record Recommended='Wes Bentley' Strength=1>
<Record Recommended='Olivia Munn' Strength=1>
<Record Recommended='Espher Lao Nieves' Strength=1>
<Record Recommended='Derek de Lint' Strength=1>
<Record Recommended='Jim Storm' Strength=1>
<Record Recommended='Helen Hayes' Strength=1>
<Record Recommended='Lou Adler' Strength=1>
<Record Recommended='Telma Hopkins' Strength=1>
<Record Recommended='Karl Bury' Strength=1>
<Record Recommended='Tracey Vilar' Strength=1>
<Record Recommended='Walt Dohrn' Strength=1>
<Record Recommended='Charlotte Fich' Strength=1>
<Record Recommended='Daniel Shalikar' Strength=1>
<Record Recommended='Wolfgang Kieling' Strength=1>
<Record Recommended='Concha Rabal' Strength=1>
<Record Recommended='Helle Dolleris' Strength=1>
<Record Recommended='Robert Alan Browne' Strength=1>
<Record Recommended='Sebastian Koch' Strength=1>
<Record Recommended='Alain Mottet' Strength=1>
<Record Recommended='Ralph Tabakin' Strength=1>
<Record Recommended='Christian Bujeau' Strength=1>
<Record Recommended='Donnelly Rhodes' Strength=1>
<Record Recommended='Michael Lombard' Strength=1>
<Record Recommended='Billy Frick' Strength=1>
<Record Recommended='Katharine Towne' Strength=1>
<Record Recommended='Maria Schell' Strength=1>
<Record Recommended='Gerhard Olschewski' Strength=1>
<Record Recommended='George Harrison' Strength=1>
<Record Recommended='Terry McIlvain' Strength=1>
<Record Recommended='Cesar Garcia' Strength=1>
<Record Recommended='Adrienne Bonnet' Strength=1>
<Record Recommended='Lisa Malkiewicz' Strength=1>
<Record Recommended='Edgar Kühlow' Strength=1>
<Record Recommended='Dreama Walker' Strength=1>
<Record Recommended='Adrian Rawlins' Strength=1>
<Record Recommended='Meg Foster' Strength=1>
<Record Recommended='David Mann' Strength=1>
<Record Recommended='Mark-Paul Gosselaar' Strength=1>
<Record Recommended='Jo Zimmerman' Strength=1>
<Record Recommended='John Cothran Jr.' Strength=1>
<Record Recommended='Bob Lujan' Strength=1>
<Record Recommended='Miles Marsico' Strength=1>
<Record Recommended='Felix Bressart' Strength=1>
<Record Recommended='Matthew Goode' Strength=1>
<Record Recommended='Tom Sturridge' Strength=1>
<Record Recommended='Nancy Nevinson' Strength=1>
<Record Recommended='Judyann Elder' Strength=1>
<Record Recommended='Gojko Mitic' Strength=1>
<Record Recommended='Remy Sweeney' Strength=1>
<Record Recommended='Dan Byrd' Strength=1>
<Record Recommended='Niels Anders Thorn' Strength=1>
<Record Recommended='Laurie Holden' Strength=1>
<Record Recommended='Erica Jones' Strength=1>
<Record Recommended='Sarah Lancaster' Strength=1>
<Record Recommended='Frank Roman' Strength=1>
<Record Recommended='Neil Innes' Strength=1>
<Record Recommended='John Beckett' Strength=1>
<Record Recommended='Lenny Venito' Strength=1>
<Record Recommended='Josh Charles' Strength=1>
<Record Recommended='Tess McCarthy' Strength=1>
<Record Recommended='Joan Neuman' Strength=1>
<Record Recommended='Gift Leotlela' Strength=1>
<Record Recommended='Mal Whiteley' Strength=1>
<Record Recommended='Philippine Leroy-Beaulieu' Strength=1>
<Record Recommended='Didier Brice' Strength=1>
<Record Recommended='Karen Akers' Strength=1>
<Record Recommended='Valerie Murphy' Strength=1>
<Record Recommended='Jennifer Ehle' Strength=1>
<Record Recommended='Mark Lutz' Strength=1>
<Record Recommended='Bhasker Patel' Strength=1>
<Record Recommended='Christopher Judge' Strength=1>
<Record Recommended='Vic Tablian' Strength=1>
<Record Recommended='Bonnie Gallup' Strength=1>
<Record Recommended='Skye Arens' Strength=1>
<Record Recommended='Camille Martinez' Strength=1>
<Record Recommended='Karroom Ben Bouih' Strength=1>
<Record Recommended="Patrick O'Brien Demsey" Strength=1>
<Record Recommended='Kevin Durand' Strength=1>
<Record Recommended='James Widdoes' Strength=1>
<Record Recommended='Jamil Shaw' Strength=1>
<Record Recommended='Scott Bellefeville' Strength=1>
<Record Recommended='Miriam Colon' Strength=1>
<Record Recommended='Ayllene Gibbons' Strength=1>
<Record Recommended='Amanda Tapping' Strength=1>
<Record Recommended='Biff Manard' Strength=1>
<Record Recommended='Max Alexander' Strength=1>
<Record Recommended='Tait Ruppert' Strength=1>
<Record Recommended='Justin Sherburn' Strength=1>
<Record Recommended='Susan Aceron' Strength=1>
<Record Recommended='Robert Webber' Strength=1>
<Record Recommended='Soren Fulton' Strength=1>
<Record Recommended='Christy Taylor' Strength=1>
<Record Recommended='Sarah Neubauer' Strength=1>
<Record Recommended='Michael Sarne' Strength=1>
<Record Recommended='Ron Yuan' Strength=1>
<Record Recommended='Jessica James' Strength=1>
<Record Recommended='Piotr Lysak' Strength=1>
<Record Recommended='Leigh Hill' Strength=1>
<Record Recommended='Lilly McDowell' Strength=1>
<Record Recommended='Sarah Vowell' Strength=1>
<Record Recommended='Louis Calhern' Strength=1>
<Record Recommended='Kathryn Dowling' Strength=1>
<Record Recommended='Stephen Tompkinson' Strength=1>
<Record Recommended='Thierry Mugler' Strength=1>
<Record Recommended='Catherine Schell' Strength=1>
<Record Recommended='Jo Van Fleet' Strength=1>
<Record Recommended='June Wilkinson' Strength=1>
<Record Recommended='Artus de Penguern' Strength=1>
<Record Recommended='Fannie Flagg' Strength=1>
<Record Recommended='Elliott Street' Strength=1>
<Record Recommended='Brian Backer' Strength=1>
<Record Recommended='George De La Pena' Strength=1>
<Record Recommended='Peter Harlowe' Strength=1>
<Record Recommended='Cathy Meils' Strength=1>
<Record Recommended='Fana Mokoena' Strength=1>
<Record Recommended='Pauline Turner' Strength=1>
<Record Recommended='Lyle Kanouse' Strength=1>
<Record Recommended='Liz Gordon' Strength=1>
<Record Recommended='Dan Duryea' Strength=1>
<Record Recommended='Lela Rochon' Strength=1>
<Record Recommended='Fiona Loewi' Strength=1>
<Record Recommended='Garcelle Beauvais' Strength=1>
<Record Recommended='Sandra Voe' Strength=1>
<Record Recommended='Sakari Kuosmanen' Strength=1>
<Record Recommended='Helmut Qualtinger' Strength=1>
<Record Recommended='Thekla Carola Wied' Strength=1>
<Record Recommended='Harvey Pekar' Strength=1>
<Record Recommended='Philip Jackson' Strength=1>
<Record Recommended='Natasha Dorfhuber' Strength=1>
<Record Recommended='Dominique Louis' Strength=1>
<Record Recommended='Martha Smith' Strength=1>
<Record Recommended='Tracy Dali' Strength=1>
<Record Recommended='Damon Charles' Strength=1>
<Record Recommended='Mathew St. Patrick' Strength=1>
<Record Recommended='Mark Houghton' Strength=1>
<Record Recommended='Rob Huebel' Strength=1>
<Record Recommended='Tony Roberts' Strength=1>
<Record Recommended='Kym Whitley' Strength=1>
<Record Recommended='Thyme Lewis' Strength=1>
<Record Recommended='L.Q. Jones' Strength=1>
<Record Recommended='Sofie Lassen-Kahlke' Strength=1>
<Record Recommended='Christian Sinniger' Strength=1>
<Record Recommended='Charlotte Gainsbourg' Strength=1>
<Record Recommended='Vic Manni' Strength=1>
<Record Recommended='Erwin Leder' Strength=1>
<Record Recommended='Charles Rocket' Strength=1>
<Record Recommended='Stefanie von Pfetten' Strength=1>
<Record Recommended='Simon Russell Beale' Strength=1>
<Record Recommended='Mimi Kuzyk' Strength=1>
<Record Recommended='Judah Friedlander' Strength=1>
<Record Recommended='James Deeth' Strength=1>
<Record Recommended='Christian Kohlund' Strength=1>
<Record Recommended='Grégoire Aslan' Strength=1>
<Record Recommended='Gerald Emerick' Strength=1>
<Record Recommended='Slade Pearce' Strength=1>
<Record Recommended='Ted Bafaloukos' Strength=1>
<Record Recommended='Jacinto Taras Riddick' Strength=1>
<Record Recommended='Nik Hagler' Strength=1>
<Record Recommended='Alix Elias' Strength=1>
<Record Recommended='Nic Nac' Strength=1>
<Record Recommended='Kim Rossi Stuart' Strength=1>
<Record Recommended='Paul-Antoine Taillefer' Strength=1>
<Record Recommended='Howard K. Smith' Strength=1>
<Record Recommended='Liz Smith' Strength=1>
<Record Recommended='Richard Johnson' Strength=1>
<Record Recommended='Billy Kearns' Strength=1>
<Record Recommended='Concha Grégori' Strength=1>
<Record Recommended='Werner Eichhorn' Strength=1>
<Record Recommended='Rhiannon Leigh Wryn' Strength=1>
<Record Recommended='Eva Cobo' Strength=1>
<Record Recommended='Paul Provenza' Strength=1>
<Record Recommended='Chris Williams' Strength=1>
<Record Recommended='Marc Coppola' Strength=1>
<Record Recommended='Samantha Esteban' Strength=1>
<Record Recommended='Deborah DeMille' Strength=1>
<Record Recommended='Michael McManus' Strength=1>
<Record Recommended='Oliver Stone' Strength=1>
<Record Recommended='Kevin Duda' Strength=1>
<Record Recommended='Omar Doom' Strength=1>
<Record Recommended='Alexandra Day' Strength=1>
<Record Recommended='Lauren Shiohama' Strength=1>
<Record Recommended='Jérôme Le Banner' Strength=1>
<Record Recommended='James Stephens' Strength=1>
<Record Recommended='Petr Skarke' Strength=1>
<Record Recommended='Anna Mouglalis' Strength=1>
<Record Recommended='John Freeman' Strength=1>
<Record Recommended='David Fabrizio' Strength=1>
<Record Recommended='Curtis Armstrong' Strength=1>
<Record Recommended='Anne Canovas' Strength=1>
<Record Recommended='Michael T. Mikler' Strength=1>
<Record Recommended='Kate Vernon' Strength=1>
<Record Recommended='Sunshine Parker' Strength=1>
<Record Recommended='Bill Weston' Strength=1>
<Record Recommended='Hanna Schygulla' Strength=1>
<Record Recommended='Victor Browne' Strength=1>
<Record Recommended='Sean Boyd' Strength=1>
<Record Recommended='Terry Moore' Strength=1>
<Record Recommended='Léa Bosco' Strength=1>
<Record Recommended='Keith Richards' Strength=1>
<Record Recommended='David Fincher' Strength=1>
<Record Recommended='Bernard Bloch' Strength=1>
<Record Recommended='Drucie McDaniel' Strength=1>
<Record Recommended='Colleen Brennan' Strength=1>
<Record Recommended='Hector Babenco' Strength=1>
<Record Recommended='Maria Antonietta DiMonte' Strength=1>
<Record Recommended='Günter Reisch' Strength=1>
<Record Recommended='Lauren Lee Smith' Strength=1>
<Record Recommended='Carolyn McCormick' Strength=1>
<Record Recommended='Richard Bremmer' Strength=1>
<Record Recommended='John Travers' Strength=1>
<Record Recommended='Todd Stashwick' Strength=1>
<Record Recommended='Darren Bransford' Strength=1>
<Record Recommended='Warren Clarke' Strength=1>
<Record Recommended='Rio Ahn' Strength=1>
<Record Recommended='Rachel Appleton' Strength=1>
<Record Recommended='Dan Tobin' Strength=1>
<Record Recommended='Regitze Estrup' Strength=1>
<Record Recommended='David Hedison' Strength=1>
<Record Recommended='Matthew Porretta' Strength=1>
<Record Recommended='David McCallum' Strength=1>
<Record Recommended='Claudine Auger' Strength=1>
<Record Recommended='Zelda Cleaver' Strength=1>
<Record Recommended='Steven Soderbergh' Strength=1>
<Record Recommended='Pam Angell' Strength=1>
<Record Recommended='Stephen Liska' Strength=1>
<Record Recommended='Wren T. Brown' Strength=1>
<Record Recommended='Rick Greenough' Strength=1>
<Record Recommended='Deborah Yates' Strength=1>
<Record Recommended='Tom Vaughan-Lawlor' Strength=1>
<Record Recommended='Taryn Manning' Strength=1>
<Record Recommended='Brian McCardie' Strength=1>
<Record Recommended='Peter McRobbie' Strength=1>
<Record Recommended='Sarah Gudgeon' Strength=1>
<Record Recommended='Frank Beyer' Strength=1>
<Record Recommended='Billy Crawford' Strength=1>
<Record Recommended='Mihaela Tudorof' Strength=1>
<Record Recommended='Natalie Becker' Strength=1>
<Record Recommended='Mirja Turestedt' Strength=1>
<Record Recommended='Emilio Rivera' Strength=1>
<Record Recommended='John Furey' Strength=1>
<Record Recommended='Chuck Aspegren' Strength=1>
<Record Recommended='John Bluthal' Strength=1>
<Record Recommended='Lauren Zaganas' Strength=1>
<Record Recommended='Al Freeman Jr.' Strength=1>
<Record Recommended='Phil LaMarr' Strength=1>
<Record Recommended='David Nichols' Strength=1>
<Record Recommended='Starletta DuPois' Strength=1>
<Record Recommended='Gerald Hiken' Strength=1>
<Record Recommended='Shannon Eubanks' Strength=1>
<Record Recommended='Pál Mácsai' Strength=1>
<Record Recommended='Harold Vermilyea' Strength=1>
<Record Recommended='Colin Hay' Strength=1>
<Record Recommended='Steven Barr' Strength=1>
<Record Recommended='Brooklynn Proulx' Strength=1>
<Record Recommended='Samantha Cannon' Strength=1>
<Record Recommended='Hana Laszlo' Strength=1>
<Record Recommended='Rohan Nichol' Strength=1>
<Record Recommended='Angelina Peláez' Strength=1>
<Record Recommended='Stubby Kaye' Strength=1>
<Record Recommended='David Brenner' Strength=1>
<Record Recommended='Meredith Vieira' Strength=1>
<Record Recommended='Monica Bleibtreu' Strength=1>
<Record Recommended='Carol Bivins' Strength=1>
<Record Recommended='Hiam Abbass' Strength=1>
<Record Recommended='Steph Song' Strength=1>
<Record Recommended='Evan Ross' Strength=1>
<Record Recommended='Matt Walsh' Strength=1>
<Record Recommended='Alastair MacIntosh' Strength=1>
<Record Recommended='Robert Mandan' Strength=1>
<Record Recommended='George Camiller' Strength=1>
<Record Recommended="Julian O'Donnell" Strength=1>
<Record Recommended='Margaret Whitton' Strength=1>
<Record Recommended='Harald Kuhlmann' Strength=1>
<Record Recommended='F.E. Falconer' Strength=1>
<Record Recommended='Marie-France Mignal' Strength=1>
<Record Recommended='Paula Newsome' Strength=1>
<Record Recommended='Maria Ouspenskaya' Strength=1>
<Record Recommended='Paulette Firestone' Strength=1>
<Record Recommended='Cameron Carter' Strength=1>
<Record Recommended='Terry Funk' Strength=1>
<Record Recommended='Ewan Chung' Strength=1>
<Record Recommended='Dominique Dunne' Strength=1>
<Record Recommended='David Gee' Strength=1>
<Record Recommended='Harry Baer' Strength=1>
<Record Recommended='Trude Bechmann' Strength=1>
<Record Recommended='Dennis Dugan' Strength=1>
<Record Recommended='Deborah McGuire' Strength=1>
<Record Recommended='Warren Kole' Strength=1>
<Record Recommended='Susan Fleetwood' Strength=1>
<Record Recommended='James Denton' Strength=1>
<Record Recommended='Gil Birmingham' Strength=1>
<Record Recommended='Kristen Schaal' Strength=1>
<Record Recommended='Raquel Castro' Strength=1>
<Record Recommended='Marnix Van Den Broeke' Strength=1>
<Record Recommended='Sara Gilbert' Strength=1>
<Record Recommended='Antony Cotton' Strength=1>
<Record Recommended='Eddie Cahill' Strength=1>
<Record Recommended='Victor Wolf' Strength=1>
<Record Recommended='Traci Topps' Strength=1>
<Record Recommended='Kira Clavell' Strength=1>
<Record Recommended='Harald Hauser' Strength=1>
<Record Recommended='Lasse Lunderskov' Strength=1>
<Record Recommended='Tamara Toumanova' Strength=1>
<Record Recommended='Werner Ilsemann' Strength=1>
<Record Recommended='Steven Gilborn' Strength=1>
<Record Recommended='Arthur Burghardt' Strength=1>
<Record Recommended='Deborah Shelton' Strength=1>
<Record Recommended='China Anderson' Strength=1>
<Record Recommended='Lucien Bodard' Strength=1>
<Record Recommended='Kent Davis' Strength=1>
<Record Recommended='Sarah Strouse' Strength=1>
<Record Recommended='Rob Morrow' Strength=1>
<Record Recommended='Neil Finnighan' Strength=1>
<Record Recommended='Mary Kay Bergman' Strength=1>
<Record Recommended='Alan Tilvern' Strength=1>
<Record Recommended='Piet Fuchs' Strength=1>
<Record Recommended='Bonnie Wright' Strength=1>
<Record Recommended='Taliesin Jaffe' Strength=1>
<Record Recommended='Catherine Grgicakuk' Strength=1>
<Record Recommended='Leo Bill' Strength=1>
<Record Recommended='Mylène Jampanoï' Strength=1>
<Record Recommended='Demetri Goritsas' Strength=1>
<Record Recommended='Annette Crosbie' Strength=1>
<Record Recommended='Aman Johal' Strength=1>
<Record Recommended='Dinah Manoff' Strength=1>
<Record Recommended='Robert William Bradford' Strength=1>
<Record Recommended='Janet Wright' Strength=1>
<Record Recommended='Nicky Guadagni' Strength=1>
<Record Recommended='Lee Montague' Strength=1>
<Record Recommended='Tom Cavanagh' Strength=1>
<Record Recommended='Anneke Weidemann' Strength=1>
<Record Recommended='Ann Wedgeworth' Strength=1>
<Record Recommended='Agnete Oernsholt' Strength=1>
<Record Recommended='Raymond Burr' Strength=1>
<Record Recommended='Lars Bjarke' Strength=1>
<Record Recommended='Sam Jaffe' Strength=1>
<Record Recommended='Rainer Werner Fassbinder' Strength=1>
<Record Recommended='Denice D. Lewis' Strength=1>
<Record Recommended='Patrick McCullough' Strength=1>
<Record Recommended='Charmion King' Strength=1>
<Record Recommended='Norman Sotolongo' Strength=1>
<Record Recommended='David Neidorf' Strength=1>
<Record Recommended='Dale C. Bronner' Strength=1>
<Record Recommended='Zygmunt Malanowicz' Strength=1>
<Record Recommended='Miles Heizer' Strength=1>
<Record Recommended='Maximilian Simonischek' Strength=1>
<Record Recommended='Nevan Finegan' Strength=1>
<Record Recommended='Susan Clark' Strength=1>
<Record Recommended="Charles 'Honi' Coles" Strength=1>
<Record Recommended='Lorna Scott' Strength=1>
<Record Recommended='Zoe Perry' Strength=1>
<Record Recommended='Stephen Gevedon' Strength=1>
<Record Recommended='Terrence Hardy Jr.' Strength=1>
<Record Recommended='Holle K. Winters' Strength=1>
<Record Recommended='Nigel Cooper' Strength=1>
<Record Recommended='Belinda Becker' Strength=1>
<Record Recommended='Jermaine Scooter Smith' Strength=1>
<Record Recommended='Steve Carlson' Strength=1>
<Record Recommended='Arbaaz Khan' Strength=1>
<Record Recommended='Béatrice Macola' Strength=1>
<Record Recommended='Mr. T' Strength=1>
<Record Recommended='Gregory Alan Williams' Strength=1>
<Record Recommended='Karl-Fred Müller' Strength=1>
<Record Recommended='Ryan Northcott' Strength=1>
<Record Recommended='Cheryl Lynn Bruce' Strength=1>
<Record Recommended='Philipp Hochmair' Strength=1>
<Record Recommended='Gary Olsen' Strength=1>
<Record Recommended='Catlin Foster' Strength=1>
<Record Recommended='Andre Royo' Strength=1>
<Record Recommended='Josef Bierbichler' Strength=1>
<Record Recommended='Bob Docherty' Strength=1>
<Record Recommended='Máté Haumann' Strength=1>
<Record Recommended='Jennifer Morrison' Strength=1>
<Record Recommended='Bernie Casey' Strength=1>
<Record Recommended='Athena Currey' Strength=1>
<Record Recommended='Carrie Genzel' Strength=1>
<Record Recommended='Micki Moore' Strength=1>
<Record Recommended='Teresa Wright' Strength=1>
<Record Recommended='Serge Riaboukine' Strength=1>
<Record Recommended='Helen Vick' Strength=1>
<Record Recommended='Shea Curry' Strength=1>
<Record Recommended='Wass Stevens' Strength=1>
<Record Recommended='Thomas Crowther' Strength=1>
<Record Recommended='Emmanuelle Vaugier' Strength=1>
<Record Recommended='Pat Jenkinson' Strength=1>
<Record Recommended='Joyce Jameson' Strength=1>
<Record Recommended='Anilú Pardo' Strength=1>
<Record Recommended='Luis Tosar' Strength=1>
<Record Recommended='Myron McCormick' Strength=1>
<Record Recommended='Rolf Ripperger' Strength=1>
<Record Recommended='Magnus Lindgren' Strength=1>
<Record Recommended='Joanne Rubino' Strength=1>
<Record Recommended='Ted Ross' Strength=1>
<Record Recommended='Ginnie Randall' Strength=1>
<Record Recommended='Brian Glover' Strength=1>
<Record Recommended='Adam Del Rio' Strength=1>
<Record Recommended='David Schramm' Strength=1>
<Record Recommended='David Johnston' Strength=1>
<Record Recommended='Alfie Allen' Strength=1>
<Record Recommended='Rick Duplissie' Strength=1>
<Record Recommended='Bryan Keith Ponton' Strength=1>
<Record Recommended='Anne Chapman' Strength=1>
<Record Recommended='Vusi Kunene' Strength=1>
<Record Recommended='Gerhard Rachold' Strength=1>
<Record Recommended="Anthony 'Citric' Campos" Strength=1>
<Record Recommended='Karin van der Laag' Strength=1>
<Record Recommended='Veronica Segura' Strength=1>
<Record Recommended='Debby Bishop' Strength=1>
<Record Recommended='Frank Ferrara' Strength=1>
<Record Recommended='Billy A. Newhouse' Strength=1>
<Record Recommended='Jacqueline Samuda' Strength=1>
<Record Recommended='Do Thi Hai Yen' Strength=1>
<Record Recommended='Jessica Steen' Strength=1>
<Record Recommended='Maggie Kirkpatrick' Strength=1>
<Record Recommended='Jerry Potter' Strength=1>
<Record Recommended='Robert Benirschke' Strength=1>
<Record Recommended='Tara Fitzgerald' Strength=1>
<Record Recommended='Willie' Strength=1>
<Record Recommended='Erica Cerra' Strength=1>
<Record Recommended='Carol Sutton' Strength=1>
<Record Recommended='Mike Colter' Strength=1>
<Record Recommended='Alito Rodgers' Strength=1>
<Record Recommended='Spencer Tracy' Strength=1>
<Record Recommended='Katharina Eckerfeld' Strength=1>
<Record Recommended='Nate Dogg' Strength=1>
<Record Recommended='Ryan Gentles' Strength=1>
<Record Recommended='Giuliana Calandra' Strength=1>
<Record Recommended='Hakeem Kae-Kazim' Strength=1>
<Record Recommended='Shawn Weatherly' Strength=1>
<Record Recommended='Michael-Ann Connor' Strength=1>
<Record Recommended='Sam Redford' Strength=1>
<Record Recommended='Yvonne Cortell' Strength=1>
<Record Recommended='Andrea Fears' Strength=1>
<Record Recommended='Ralph Waite' Strength=1>
<Record Recommended='Robert Wuhl' Strength=1>
<Record Recommended='Sean Curley' Strength=1>
<Record Recommended='Françoise Brion' Strength=1>
<Record Recommended='Carrie Nygren' Strength=1>
<Record Recommended='Michael Monks' Strength=1>
<Record Recommended='Nina Fog' Strength=1>
<Record Recommended='Kathleen Miller' Strength=1>
<Record Recommended='John Walcutt' Strength=1>
<Record Recommended='Cameron Scher' Strength=1>
<Record Recommended='Al Santos' Strength=1>
<Record Recommended='Greg Evigan' Strength=1>
<Record Recommended='J. Miles Dale' Strength=1>
<Record Recommended='Mark King' Strength=1>
<Record Recommended='Lee Marvin' Strength=1>
<Record Recommended='John P. Whitecloud' Strength=1>
<Record Recommended='Andrew Butcher' Strength=1>
<Record Recommended='Sherry Stringfield' Strength=1>
<Record Recommended='Beau Garrett' Strength=1>
<Record Recommended='Scottie Thompson' Strength=1>
<Record Recommended='Elaine Collins' Strength=1>
<Record Recommended='Marcel Guy' Strength=1>
<Record Recommended='Michael Palin' Strength=1>
<Record Recommended='Laurie Walters' Strength=1>
<Record Recommended='Escher Holloway' Strength=1>
<Record Recommended='Victor Garrivier' Strength=1>
<Record Recommended='Juliet Anderson' Strength=1>
<Record Recommended='Chris Aberdein' Strength=1>
<Record Recommended='James Murtaugh' Strength=1>
<Record Recommended='Phyllis Thaxter' Strength=1>
<Record Recommended='Kitten Natividad' Strength=1>
<Record Recommended='Robyn Lively' Strength=1>
<Record Recommended='Alan McRae' Strength=1>
<Record Recommended='Michael Ivins' Strength=1>
<Record Recommended='Gabrielle Witcher' Strength=1>
<Record Recommended='Andreas Filippides' Strength=1>
<Record Recommended='Josef Altin' Strength=1>
<Record Recommended='Chris Moss' Strength=1>
<Record Recommended='David Bowers' Strength=1>
<Record Recommended='Laurent Claret' Strength=1>
<Record Recommended='Tony Abatemarco' Strength=1>
<Record Recommended='Jackson Rathbone' Strength=1>
<Record Recommended='Mark Metcalf' Strength=1>
<Record Recommended='Jimmy Sun' Strength=1>
<Record Recommended='Bo Hopkins' Strength=1>
<Record Recommended='Mick Øgendahl' Strength=1>
<Record Recommended='Bobby Harwell' Strength=1>
<Record Recommended='Francesco Benigno' Strength=1>
<Record Recommended='Jacqueline McKenzie' Strength=1>
<Record Recommended='Rod Loomis' Strength=1>
<Record Recommended='Daniel Auteuil' Strength=1>
<Record Recommended='Scooter' Strength=1>
<Record Recommended='Patricia Wettig' Strength=1>
<Record Recommended='Oscar Isaac' Strength=1>
<Record Recommended='Emily Nelson' Strength=1>
<Record Recommended='David Ackroyd' Strength=1>
<Record Recommended='Damon Dash' Strength=1>
<Record Recommended='Emily Longstreth' Strength=1>
<Record Recommended='Erin Boyes' Strength=1>
<Record Recommended='Leslie Stefanson' Strength=1>
<Record Recommended='Géraldine Pailhas' Strength=1>
<Record Recommended='David Birkin' Strength=1>
<Record Recommended='Lisa Blount' Strength=1>
<Record Recommended='George Gaynes' Strength=1>
<Record Recommended='Sue Lloyd' Strength=1>
<Record Recommended='José Luis de Villalonga' Strength=1>
<Record Recommended='Freddie Joe Farnsworth' Strength=1>
<Record Recommended='Ivana Trump' Strength=1>
<Record Recommended='Martina Nation' Strength=1>
<Record Recommended='Neil McCarthy' Strength=1>
<Record Recommended='Glover Johns Gill' Strength=1>
<Record Recommended='Stuart Graham' Strength=1>
<Record Recommended='Gary Littlejohn' Strength=1>
<Record Recommended='Stephen R. Hudis' Strength=1>
<Record Recommended='Simon Rainville' Strength=1>
<Record Recommended='Jace Alexander' Strength=1>
<Record Recommended='Christian Argueta' Strength=1>
<Record Recommended='Jürgen Hentsch' Strength=1>
<Record Recommended='Glori Renee Euwer' Strength=1>
<Record Recommended='Jeremy Bobb' Strength=1>
<Record Recommended='Sami Samir' Strength=1>
<Record Recommended='Michael Gulick' Strength=1>
<Record Recommended='Siegfried Kilian' Strength=1>
<Record Recommended='Ofentse Modiselle' Strength=1>
<Record Recommended='Erich Anderson' Strength=1>
<Record Recommended='Sofia Helin' Strength=1>
<Record Recommended='Ian Dury' Strength=1>
<Record Recommended='Isabelle Nanty' Strength=1>
<Record Recommended='Kiely Williams' Strength=1>
<Record Recommended='Sara Crowe' Strength=1>
<Record Recommended='Nana Visitor' Strength=1>
<Record Recommended='Wayne Coyne' Strength=1>
<Record Recommended='Ted Cassidy' Strength=1>
<Record Recommended='Rossif Sutherland' Strength=1>
<Record Recommended='Angie Ruiz' Strength=1>
<Record Recommended='Herb Andress' Strength=1>
<Record Recommended='Lance Gross' Strength=1>
<Record Recommended='Charlotte Crossley' Strength=1>
<Record Recommended='Dominique Blanchar' Strength=1>
<Record Recommended='Lydia Lenossi' Strength=1>
<Record Recommended='Cliff Simon' Strength=1>
<Record Recommended='Richard McGonagle' Strength=1>
<Record Recommended='Bob Einstein' Strength=1>
"""
	
	
#Q9) Find someone to introduce Tom Hanks to Tom Cruise.


result = transaction.run("""
MATCH (tom:Actor {name:'Tom Hanks'})-[:ACTS_IN]->(m)<-[:ACTS_IN]-(coActors),
(coActors)-[:ACTS_IN]->(m2)<-[:ACTS_IN]-(cruise:Actor {name:'Tom Cruise'})
RETURN tom, m, coActors, m2, cruise
;""")
for record in result:
    print (record)
	
"""	
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=38829 labels={'Movie'} properties={'studio': 'Pixar Animation Studios', 'releaseDate': '1276812000000', 'imdbId': 'tt0435761', 'runtime': 103, 'description': "Woody, Buzz, and the rest of Andy's toys haven't been played with in years. With Andy about to go to college, the gang find themselves accidentally left at a nefarious day care center. The toys must band together to escape and return home to Andy.", 'language': 'en', 'title': 'Toy Story 3', 'version': 971, 'trailer': 'http://www.youtube.com/watch?v=TNMpa5yBf5o', 'imageUrl': 'http://cf1.imgobject.com/posters/011/4cdb8b335e73d605e6000011/toy-story-3-mid.jpg', 'genre': 'Animation', 'tagline': 'No toy gets left behind.', 'lastModified': '1301900808000', 'id': '10193', 'homepage': 'http://disney.go.com/toystory/'}> coActors=<Node id=783 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-261190800000', 'birthplace': 'Chicago, Illinois, USA', 'name': 'Bonnie Hunt', 'lastModified': '1299840028000', 'id': '5149', 'biography': '', 'version': 143, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/072/4c4e74387b9aa1326d000072/bonnie-hunt-profile.jpg'}> m2=<Node id=4182 labels={'Movie'} properties={'studio': 'United Artists', 'releaseDate': '598230000000', 'imdbId': 'tt0095953', 'runtime': 133, 'description': 'The sensible drama about the reunification of two very different brothers and their struggle to stay together. Dustin Hoffman won an Oscar for best actor for his memorable performance as the autistic Raymond.', 'language': 'en', 'title': 'Rain Man', 'version': 185, 'trailer': 'http://www.youtube.com/watch?v=KKC3W0awjm0', 'imageUrl': 'http://cf1.imgobject.com/posters/4d5/4bc90717017a3c57fe0024d5/rain-man-mid.jpg', 'genre': 'Drama', 'tagline': '', 'lastModified': '1299999907000', 'id': '380', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=35088 labels={'Movie'} properties={'releaseDate': '661734000000', 'imdbId': 'tt0099165', 'runtime': 125, 'description': 'Take one Wall Street tycoon, his Fifth Avenue mistress, a reporter hungry for fame, and make the wrong turn in The Bronx...then sit back and watch the sparks fly.', 'language': 'en', 'title': 'The Bonfire of the Vanities', 'version': 188, 'imageUrl': 'http://cf1.imgobject.com/posters/201/4c6088755e73d63462000201/the-bonfire-of-the-vanities-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1301903336000', 'id': '9586', 'homepage': ''}> coActors=<Node id=1072 labels={'Actor', 'Person'} properties={'birthday': '-1028336400000', 'birthplace': 'Memphis, Tennessee, USA', 'name': 'Morgan Freeman', 'lastModified': '1300002025000', 'id': '192', 'biography': 'Morgan Porterfield Freeman, Jr. is an American actor, film director, and narrator. He is noted for his reserved demeanor and authoritative speaking voice.\nFreeman has received Academy Award nominations for his performances in Street Smart, Driving Miss Daisy, The Shawshank Redemption and Invictus and won in 2005 for Million Dollar Baby. He has also won a Golden Globe Award and a Screen Actors Guild Award.\n\nMorgan Freeman was born in Memphis, Tennessee, the son of Mayme Edna (née Revere) and Morg', 'version': 308, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/019/4bc9f4ac017a3c0e8b000019/morgan-freeman-profile.jpg'}> m2=<Node id=1270 labels={'Movie'} properties={'studio': 'Paramount Pictures', 'releaseDate': '1119996000000', 'imdbId': 'tt0407304', 'runtime': 117, 'description': 'The extraordinary battle for the future of humankind through the eyes of one American family fighting to survive it. Ray Ferrier is a divorced dockworker and less-than-perfect father. Soon after his ex-wife and her new husband drop of his teenage son Robbie and young daughter Rachel for a rare weekend visit, a strange and powerful lightning storm touches down.', 'language': 'en', 'title': 'War of the Worlds', 'version': 200, 'trailer': 'http://www.youtube.com/watch?v=hrCnXLlhuls&hd=1', 'imageUrl': 'http://cf1.imgobject.com/posters/296/4d509afb7b9aa13aba00e296/war-of-the-worlds-mid.jpg', 'genre': 'Science Fiction', 'tagline': "They're already here.", 'lastModified': '1299939670000', 'id': '74', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=34820 labels={'Movie'} properties={'releaseDate': '913935600000', 'imdbId': 'tt0128853', 'runtime': 119, 'description': "In this valentine to modern romance, book superstore magnate Joe Fox and independent book shop owner Kathleen Kelly fall in love in the anonymity of the Internet -- both blissfully unaware that he's trying to put her out of business.", 'language': 'en', 'title': "You've Got Mail", 'version': 284, 'trailer': 'http://www.youtube.com/watch?v=jCetfaS7GAo', 'imageUrl': 'http://cf1.imgobject.com/posters/a07/4d55b2da5e73d617c7006a07/you-ve-got-mail-mid.jpg', 'genre': 'Comedy', 'tagline': 'Someone you pass on the street may already be the love of your life.', 'lastModified': '1301970051000', 'id': '9489', 'homepage': ''}> coActors=<Node id=4290 labels={'Actor', 'Person'} properties={'birthday': '-256179600000', 'birthplace': 'Fairfield, Connecticut, USA', 'name': 'Meg Ryan', 'lastModified': '1299779156000', 'id': '5344', 'biography': 'Margaret Mary Emily Anne Hyra (born November 19, 1961) professionally known as Meg Ryan. She had lead roles in six films, When Harry Met Sally..., Sleepless in Seattle, French Kiss, City of Angels, Addicted to Love and You\'ve Got Mail whose total gross was over $870 million worldwide. In 1995, critic Richard Corliss called her "the current soul of romantic comedy." She had leads in several romantic comedies, including When Harry Met Sally... (1989), Sleepless in Seattle (1993) and You\'ve Got Mai', 'version': 110, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/e34/4bfedd7f017a3c7031000e34/meg-ryan-profile.jpg'}> m2=<Node id=7049 labels={'Movie'} properties={'studio': 'Paramount Pictures', 'releaseDate': '516578400000', 'imdbId': 'tt0092099', 'runtime': 110, 'description': 'For Lieutenant Pete Mitchell and his friend and Co-Pilot Nick Bradshaw being accepted into an elite training school for fighter pilots is a dream come true. In the training Pete falls madly in love with one of his instructors named Charlie. Yet life isn’t all roses, Pete’s friend Nick has a fatal plane crash that tests Pete’s will to continue his training.', 'language': 'en', 'title': 'Top Gun', 'version': 178, 'trailer': 'http://www.youtube.com/watch?v=VN8ze3S0Uj8', 'imageUrl': 'http://cf1.imgobject.com/posters/1cd/4bc90bb9017a3c57fe0041cd/top-gun-mid.jpg', 'genre': 'Action', 'tagline': 'Up there with the best of the best.', 'lastModified': '1299912032000', 'id': '744', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=30040 labels={'Movie'} properties={'studio': 'Touchstone Pictures', 'releaseDate': '599612400000', 'imdbId': 'tt0098536', 'runtime': 97, 'description': 'Scott Turner has 3 days left in the local police department before he moves to a bigger city to get some "real" cases, not just misdemeanors. Then Amos Reed is murdered, and Scott Turner sets himself on the case. The closest thing to a witness in the case is Amos Reed\'s dog, Hooch, which Scott Turner has to take care of if it\'s going to avoid being "put to sleep".', 'language': 'en', 'title': 'Turner & Hooch', 'version': 378, 'trailer': 'http://www.youtube.com/watch?v=gHc_eaKhKlo', 'imageUrl': 'http://cf1.imgobject.com/posters/eb9/4bc91e52017a3c57fe00beb9/turner-hooch-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301904352000', 'id': '6951', 'homepage': ''}> coActors=<Node id=510 labels={'Actor', 'Person'} properties={'name': 'Craig T. Nelson', 'lastModified': '1300090395000', 'id': '8977', 'biography': '', 'version': 72, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/0e0/4cdc6b6e7b9aa137ff0000e0/craig-t-nelson-profile.jpg'}> m2=<Node id=67809 labels={'Movie'} properties={'releaseDate': '435538800000', 'imdbId': 'tt0085154', 'runtime': 91, 'description': "Sensitive study of a headstrong high school football star who dreams of getting out of his small Western Pennsylvania steel town with a football scholarship. His equally ambitious coach aims at a college position, resulting in a clash which could crush the player's dreams", 'language': 'en', 'title': 'All the Right Moves', 'version': 135, 'trailer': 'http://www.youtube.com/watch?v=JPhbQLhy4fQ', 'imageUrl': 'http://cf1.imgobject.com/posters/414/4cb655df7b9aa138d8000414/all-the-right-moves-mid.jpg', 'genre': 'Drama', 'tagline': '', 'lastModified': '1301904774000', 'id': '18172', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=29354 labels={'Movie'} properties={'studio': 'Universal Pictures', 'releaseDate': '1198191600000', 'imdbId': 'tt0472062', 'runtime': 97, 'description': "A drama based on a Texas congressman Charlie Wilson's covert dealings in Afghanistan, where his efforts to assist rebels in their war with the Soviets have some unforeseen and long-reaching effects.", 'language': 'en', 'title': "Charlie Wilson's War", 'version': 320, 'trailer': 'http://www.youtube.com/watch?v=410', 'imageUrl': 'http://cf1.imgobject.com/posters/375/4d5a2b785e73d65e85000375/charlie-wilson-s-war-mid.jpg', 'genre': 'Comedy', 'tagline': 'Based on a true story. You think we could make all this up?', 'lastModified': '1301901834000', 'id': '6538', 'homepage': 'http://www.charliewilsonswar.net/'}> coActors=<Node id=1755 labels={'Actor', 'Person'} properties={'name': 'Philip Seymour Hoffman', 'lastModified': '1299958130000', 'id': '1233', 'biography': '', 'version': 151, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/0a2/4bf07986017a3c53100000a2/philip-seymour-hoffman-profile.jpg'}> m2=<Node id=8981 labels={'Movie'} properties={'studio': 'Paramount Pictures', 'releaseDate': '1145829600000', 'imdbId': 'tt0317919', 'runtime': 126, 'description': "Super-spy Ethan Hunt has retired from active duty to train new IMF agents. But he is called back into action to confront the toughest villain he's ever faced - Owen Davian, an international weapons and information provider with no remorse and no conscience. Hunt assembles his team, his old friend Luther Strickell, transportation expert Declan, background operative Zhen, and fresh recruit Lindsey..", 'language': 'en', 'title': 'Mission: Impossible III', 'version': 240, 'imageUrl': 'http://cf1.imgobject.com/posters/4a6/4bc90ecd017a3c57fe0054a6/mission-impossible-iii-mid.jpg', 'genre': 'Action', 'tagline': '', 'lastModified': '1301901168000', 'id': '956', 'homepage': 'http://www.missionimpossible.com/'}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=29354 labels={'Movie'} properties={'studio': 'Universal Pictures', 'releaseDate': '1198191600000', 'imdbId': 'tt0472062', 'runtime': 97, 'description': "A drama based on a Texas congressman Charlie Wilson's covert dealings in Afghanistan, where his efforts to assist rebels in their war with the Soviets have some unforeseen and long-reaching effects.", 'language': 'en', 'title': "Charlie Wilson's War", 'version': 320, 'trailer': 'http://www.youtube.com/watch?v=410', 'imageUrl': 'http://cf1.imgobject.com/posters/375/4d5a2b785e73d65e85000375/charlie-wilson-s-war-mid.jpg', 'genre': 'Comedy', 'tagline': 'Based on a true story. You think we could make all this up?', 'lastModified': '1301901834000', 'id': '6538', 'homepage': 'http://www.charliewilsonswar.net/'}> coActors=<Node id=1755 labels={'Actor', 'Person'} properties={'name': 'Philip Seymour Hoffman', 'lastModified': '1299958130000', 'id': '1233', 'biography': '', 'version': 151, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/0a2/4bf07986017a3c53100000a2/philip-seymour-hoffman-profile.jpg'}> m2=<Node id=3908 labels={'Movie'} properties={'studio': 'New Line Cinema', 'releaseDate': '944607600000', 'imdbId': 'tt0175880', 'runtime': 188, 'description': 'A film about lonely and unhappy people in California played out in emotion-filled episodes of star-packed drama. In the search of love, the main character reencounters the traumas of her past.', 'language': 'en', 'title': 'Magnolia', 'version': 216, 'trailer': 'http://www.youtube.com/watch?v=QYTqhmzROko', 'imageUrl': 'http://cf1.imgobject.com/posters/f7b/4d6284595e73d60c62003f7b/magnolia-mid.jpg', 'genre': 'Drama', 'tagline': 'Things fall down. People look up. And when it rains, it pours.', 'lastModified': '1300003070000', 'id': '334', 'homepage': 'http://www.magnoliamovie.com/'}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=21072 labels={'Movie'} properties={'studio': 'The Zanuck Company', 'releaseDate': '1026424800000', 'imdbId': 'tt0257044', 'runtime': 119, 'description': "Hit man Michael Sullivan, known in his 1930s Chicago world as The Angel of Death, is on the run after his wife and son are murdered. With his surviving son in tow, Michael sets out to exact brutal vengeance. Complicating matters are a reporter, Al Capone's enforcer and other shady characters.", 'language': 'en', 'title': 'Road to Perdition', 'version': 362, 'imageUrl': 'http://cf1.imgobject.com/posters/023/4c11d16f7b9aa17ec5000023/road-to-perdition-mid.jpg', 'genre': 'Action', 'tagline': 'Every son holds the future for his father.', 'lastModified': '1301901482000', 'id': '4147', 'homepage': ''}> coActors=<Node id=3227 labels={'Actor', 'Person'} properties={'name': 'Paul Newman', 'lastModified': '1299909440000', 'id': '3636', 'biography': '', 'version': 132, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/170/4c178ef87b9aa108d4000170/paul-newman-profile.jpg'}> m2=<Node id=43737 labels={'Movie'} properties={'releaseDate': '529110000000', 'imdbId': 'tt0090863', 'runtime': 119, 'description': 'Fast Eddie Felson teaches a cocky but immensely talented protégé the ropes of pool hustling, which in turn inspires him to make an unlikely comeback.', 'language': 'en', 'title': 'The Color of Money', 'version': 267, 'trailer': 'http://www.youtube.com/watch?v=k7gmrKAFshE', 'imageUrl': 'http://cf1.imgobject.com/posters/a90/4bc936b4017a3c57fe016a90/the-color-of-money-mid.jpg', 'genre': 'Drama', 'tagline': '', 'lastModified': '1301902227000', 'id': '11873', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=16044 labels={'Movie'} properties={'studio': 'Amblin Entertainment', 'releaseDate': '636937200000', 'imdbId': 'tt0099892', 'runtime': 102, 'description': 'Hypochondriac Joe Banks finds out he has six months to live, quits his dead end job, musters the courage to ask his female co-workder out on a date, and is then hired to jump into a volcano by a mysterious visitor.', 'language': 'en', 'title': 'Joe Versus the Volcano', 'version': 89, 'imageUrl': 'http://cf1.imgobject.com/posters/b1c/4bc916f0017a3c57fe008b1c/joe-versus-the-volcano-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1301904643000', 'id': '2565', 'homepage': ''}> coActors=<Node id=4290 labels={'Actor', 'Person'} properties={'birthday': '-256179600000', 'birthplace': 'Fairfield, Connecticut, USA', 'name': 'Meg Ryan', 'lastModified': '1299779156000', 'id': '5344', 'biography': 'Margaret Mary Emily Anne Hyra (born November 19, 1961) professionally known as Meg Ryan. She had lead roles in six films, When Harry Met Sally..., Sleepless in Seattle, French Kiss, City of Angels, Addicted to Love and You\'ve Got Mail whose total gross was over $870 million worldwide. In 1995, critic Richard Corliss called her "the current soul of romantic comedy." She had leads in several romantic comedies, including When Harry Met Sally... (1989), Sleepless in Seattle (1993) and You\'ve Got Mai', 'version': 110, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/e34/4bfedd7f017a3c7031000e34/meg-ryan-profile.jpg'}> m2=<Node id=7049 labels={'Movie'} properties={'studio': 'Paramount Pictures', 'releaseDate': '516578400000', 'imdbId': 'tt0092099', 'runtime': 110, 'description': 'For Lieutenant Pete Mitchell and his friend and Co-Pilot Nick Bradshaw being accepted into an elite training school for fighter pilots is a dream come true. In the training Pete falls madly in love with one of his instructors named Charlie. Yet life isn’t all roses, Pete’s friend Nick has a fatal plane crash that tests Pete’s will to continue his training.', 'language': 'en', 'title': 'Top Gun', 'version': 178, 'trailer': 'http://www.youtube.com/watch?v=VN8ze3S0Uj8', 'imageUrl': 'http://cf1.imgobject.com/posters/1cd/4bc90bb9017a3c57fe0041cd/top-gun-mid.jpg', 'genre': 'Action', 'tagline': 'Up there with the best of the best.', 'lastModified': '1299912032000', 'id': '744', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=8139 labels={'Movie'} properties={'studio': 'Tristar Pictures', 'releaseDate': '740959200000', 'imdbId': 'tt0108160', 'runtime': 105, 'description': 'A young boy who tries to set his dad up on a date after the death of his mother. He calls into a radio station to talk about his dad’s loneliness which soon leads the dad into meeting a Journalist Annie who flies to Seattle to write a story about the boy and his dad.  Yet Annie ends up with more than just a story in this popular romantic comedy.', 'language': 'en', 'title': 'Sleepless in Seattle', 'version': 158, 'trailer': 'http://www.youtube.com/watch?v=1341', 'imageUrl': 'http://cf1.imgobject.com/posters/2c0/4c879fee5e73d66b5e0002c0/sleepless-in-seattle-mid.jpg', 'genre': 'Comedy', 'tagline': '', 'lastModified': '1300261966000', 'id': '858', 'homepage': ''}> coActors=<Node id=4290 labels={'Actor', 'Person'} properties={'birthday': '-256179600000', 'birthplace': 'Fairfield, Connecticut, USA', 'name': 'Meg Ryan', 'lastModified': '1299779156000', 'id': '5344', 'biography': 'Margaret Mary Emily Anne Hyra (born November 19, 1961) professionally known as Meg Ryan. She had lead roles in six films, When Harry Met Sally..., Sleepless in Seattle, French Kiss, City of Angels, Addicted to Love and You\'ve Got Mail whose total gross was over $870 million worldwide. In 1995, critic Richard Corliss called her "the current soul of romantic comedy." She had leads in several romantic comedies, including When Harry Met Sally... (1989), Sleepless in Seattle (1993) and You\'ve Got Mai', 'version': 110, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/e34/4bfedd7f017a3c7031000e34/meg-ryan-profile.jpg'}> m2=<Node id=7049 labels={'Movie'} properties={'studio': 'Paramount Pictures', 'releaseDate': '516578400000', 'imdbId': 'tt0092099', 'runtime': 110, 'description': 'For Lieutenant Pete Mitchell and his friend and Co-Pilot Nick Bradshaw being accepted into an elite training school for fighter pilots is a dream come true. In the training Pete falls madly in love with one of his instructors named Charlie. Yet life isn’t all roses, Pete’s friend Nick has a fatal plane crash that tests Pete’s will to continue his training.', 'language': 'en', 'title': 'Top Gun', 'version': 178, 'trailer': 'http://www.youtube.com/watch?v=VN8ze3S0Uj8', 'imageUrl': 'http://cf1.imgobject.com/posters/1cd/4bc90bb9017a3c57fe0041cd/top-gun-mid.jpg', 'genre': 'Action', 'tagline': 'Up there with the best of the best.', 'lastModified': '1299912032000', 'id': '744', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=5934 labels={'Movie'} properties={'studio': ' Columbia Pictures', 'releaseDate': '1147989600000', 'imdbId': 'tt0382625', 'runtime': 149, 'description': 'A murder inside the Louvre and clues in Da Vinci paintings lead to the discovery of a religious mystery protected by a secret society for two thousand years, which could shake the foundations of Christianity.', 'language': 'en', 'title': 'The Da Vinci Code', 'version': 304, 'trailer': 'http://www.youtube.com/watch?v=pE7apZzCIAA', 'imageUrl': 'http://cf1.imgobject.com/posters/011/4c493bf27b9aa115fc000011/the-da-vinci-code-mid.jpg', 'genre': 'Drama', 'tagline': 'So Dark The Con Of Man', 'lastModified': '1299971059000', 'id': '591', 'homepage': 'http://www.sonypictures.com/homevideo/thedavincicode/index.html'}> coActors=<Node id=731 labels={'Actor', 'Person'} properties={'birthday': '-524106000000', 'birthplace': 'London, England, UK', 'name': 'Alfred Molina', 'lastModified': '1299992131000', 'id': '658', 'biography': '', 'version': 179, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/01d/4c30f80f5e73d640bc00001d/alfred-molina-profile.jpg'}> m2=<Node id=3908 labels={'Movie'} properties={'studio': 'New Line Cinema', 'releaseDate': '944607600000', 'imdbId': 'tt0175880', 'runtime': 188, 'description': 'A film about lonely and unhappy people in California played out in emotion-filled episodes of star-packed drama. In the search of love, the main character reencounters the traumas of her past.', 'language': 'en', 'title': 'Magnolia', 'version': 216, 'trailer': 'http://www.youtube.com/watch?v=QYTqhmzROko', 'imageUrl': 'http://cf1.imgobject.com/posters/f7b/4d6284595e73d60c62003f7b/magnolia-mid.jpg', 'genre': 'Drama', 'tagline': 'Things fall down. People look up. And when it rains, it pours.', 'lastModified': '1300003070000', 'id': '334', 'homepage': 'http://www.magnoliamovie.com/'}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=5934 labels={'Movie'} properties={'studio': ' Columbia Pictures', 'releaseDate': '1147989600000', 'imdbId': 'tt0382625', 'runtime': 149, 'description': 'A murder inside the Louvre and clues in Da Vinci paintings lead to the discovery of a religious mystery protected by a secret society for two thousand years, which could shake the foundations of Christianity.', 'language': 'en', 'title': 'The Da Vinci Code', 'version': 304, 'trailer': 'http://www.youtube.com/watch?v=pE7apZzCIAA', 'imageUrl': 'http://cf1.imgobject.com/posters/011/4c493bf27b9aa115fc000011/the-da-vinci-code-mid.jpg', 'genre': 'Drama', 'tagline': 'So Dark The Con Of Man', 'lastModified': '1299971059000', 'id': '591', 'homepage': 'http://www.sonypictures.com/homevideo/thedavincicode/index.html'}> coActors=<Node id=794 labels={'Actor', 'Person'} properties={'birthday': '-676087200000', 'birthplace': 'Casablanca, Morocco', 'name': 'Jean Reno', 'lastModified': '1299873489000', 'id': '1003', 'biography': '', 'version': 189, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/f61/4be964ff017a3c35b5000f61/jean-reno-profile.jpg'}> m2=<Node id=8963 labels={'Movie'} properties={'studio': 'Cruise/Wagner Productions', 'releaseDate': '832716000000', 'imdbId': 'tt0117060', 'runtime': 110, 'description': "When Ethan Hunt, the leader of a crack espionage team whose perilous operation has gone awry with no explanation, discovers that a mole has penetrated the CIA, he's surprised to learn that he's the No. 1 suspect. To clear his name, Hunt now must ferret out the real double agent and, in the process, even the score.", 'language': 'en', 'title': 'Mission: Impossible', 'version': 193, 'imageUrl': 'http://cf1.imgobject.com/posters/315/4d2fb7d55e73d667ea000315/mission-impossible-mid.jpg', 'genre': 'Action', 'tagline': 'Expect the Impossible.', 'lastModified': '1301901083000', 'id': '954', 'homepage': 'http://www.missionimpossible.com/'}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=780 labels={'Movie'} properties={'studio': 'Warner Bros. Pictures', 'releaseDate': '944780400000', 'imdbId': 'tt0120689', 'runtime': 188, 'description': "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cellblock's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.", 'language': 'en', 'title': 'The Green Mile', 'version': 200, 'trailer': 'http://www.youtube.com/watch?v=ctRK-4Vt7dA', 'imageUrl': 'http://cf1.imgobject.com/posters/c01/4bc90828017a3c57fe002c01/the-green-mile-mid.jpg', 'genre': 'Crime', 'tagline': 'Miracles do happen.', 'lastModified': '1299985732000', 'id': '497', 'homepage': 'http://thegreenmile.warnerbros.com/'}> coActors=<Node id=783 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-261190800000', 'birthplace': 'Chicago, Illinois, USA', 'name': 'Bonnie Hunt', 'lastModified': '1299840028000', 'id': '5149', 'biography': '', 'version': 143, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/072/4c4e74387b9aa1326d000072/bonnie-hunt-profile.jpg'}> m2=<Node id=4182 labels={'Movie'} properties={'studio': 'United Artists', 'releaseDate': '598230000000', 'imdbId': 'tt0095953', 'runtime': 133, 'description': 'The sensible drama about the reunification of two very different brothers and their struggle to stay together. Dustin Hoffman won an Oscar for best actor for his memorable performance as the autistic Raymond.', 'language': 'en', 'title': 'Rain Man', 'version': 185, 'trailer': 'http://www.youtube.com/watch?v=KKC3W0awjm0', 'imageUrl': 'http://cf1.imgobject.com/posters/4d5/4bc90717017a3c57fe0024d5/rain-man-mid.jpg', 'genre': 'Drama', 'tagline': '', 'lastModified': '1299999907000', 'id': '380', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=774 labels={'Movie'} properties={'releaseDate': '756601200000', 'imdbId': 'tt0107818', 'runtime': 125, 'description': 'No one would take his case until one man was willing to take on the system. Two competing lawyers join forces to sue a prestigious law firm for aids discrimination. As their unlikely friendship develops their courage overcomes the prejudice and corruption of their powerful adversaries.', 'language': 'en', 'title': 'Philadelphia', 'version': 148, 'imageUrl': 'http://cf1.imgobject.com/posters/ac4/4bc92922017a3c57fe010ac4/philadelphia-mid.jpg', 'genre': 'Drama', 'tagline': '', 'lastModified': '1300170007000', 'id': '9800', 'homepage': ''}> coActors=<Node id=777 labels={'Actor', 'Person'} properties={'birthday': '-296442000000', 'birthplace': 'Málaga, Andalucía, Spain ', 'name': 'Antonio Banderas', 'lastModified': '1300015795000', 'id': '3131', 'biography': "<p>Antonio Banderas, one of Spain's most famous faces who was a soccer \nplayer until he broke his foot at age 14, is now an international film \nstar best known as Zorro in the eponymous film franchise.\n\nHe was \nborn José Antonio Domínguez Banderas on August 10, 1960, in Málaga, \nAndalusia, Spain. His father, Jose Dominguez, was a policeman in the \nSpanish civil guards. His mother, Doña Ana Banderas, was a school \nteacher. Young Banderas was brought up a Roman Catholic, but eventually \nhad libera", 'version': 196, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/0d9/4bf8843c017a3c490c0000d9/antonio-banderas-profile.jpg'}> m2=<Node id=6216 labels={'Movie'} properties={'studio': 'Warner Bros. Pictures', 'releaseDate': '784508400000', 'imdbId': 'tt0110148', 'runtime': 123, 'description': "It hadn't even been a year since a plantation owner named Louis had lost his wife in childbirth. Both his wife and the infant died, and now he has lost his will to live. A vampire named Lestat takes a liking to Louis and offers him the chance to become a creature of the night: a vampire. Louis accepts, and Lestat drains Louis' mortal blood and then replaces it with his own, turning Louis into a vampire. Louis must learn from Lestat the ways of the vampire.", 'language': 'en', 'title': 'Interview with the Vampire', 'version': 178, 'trailer': 'http://www.youtube.com/watch?v=672', 'imageUrl': 'http://cf1.imgobject.com/posters/05f/4d101a517b9aa1147a00005f/interview-with-the-vampire-the-vampire-chronicles-mid.jpg', 'genre': 'Drama', 'tagline': 'Drink From Me And Live Forever.', 'lastModified': '1299963949000', 'id': '628', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=756 labels={'Movie'} properties={'studio': 'Universal Pictures', 'releaseDate': '803772000000', 'imdbId': 'tt0112384', 'runtime': 140, 'description': "Technical troubles scuttle the Apollo 13 lunar mission in 1971, risking the lives of astronaut Jim Lovell  and his crew in director Ron Howard's chronicle of this true-life story, which turns a failed journey into a thrilling saga of heroism. Drifting more than 200,000 miles from Earth, the astronauts work furiously with the ground crew to avert tragedy.", 'language': 'en', 'title': 'Apollo 13', 'version': 236, 'trailer': 'http://www.youtube.com/watch?v=nEl0NsYn1fU', 'imageUrl': 'http://cf1.imgobject.com/posters/177/4d68030e7b9aa13636000177/apollo-13-mid.jpg', 'genre': 'Action', 'tagline': 'Houston, we have a problem.', 'lastModified': '1299974865000', 'id': '568', 'homepage': ''}> coActors=<Node id=772 labels={'Actor', 'Person'} properties={'name': 'Xander Berkeley', 'lastModified': '1299944929000', 'id': '3982', 'biography': '', 'version': 121}> m2=<Node id=8340 labels={'Movie'} properties={'studio': 'Castle Rock Entertainment', 'releaseDate': '724028400000', 'imdbId': 'tt0104257', 'runtime': 138, 'description': 'When cocky military lawyer Lt. Daniel Kaffee  and his co-counsel, Lt. Cmdr. JoAnne Galloway, are assigned to a murder case, they uncover a hazing ritual that could implicate high-ranking officials such as shady Col. Nathan Jessep.', 'language': 'en', 'title': 'A Few Good Men', 'version': 541, 'trailer': 'http://www.youtube.com/watch?v=2270', 'imageUrl': 'http://cf1.imgobject.com/posters/121/4d67fff57b9aa13636000121/a-few-good-men-mid.jpg', 'genre': 'Crime', 'tagline': "In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth.", 'lastModified': '1300257700000', 'id': '881', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
<Record tom=<Node id=524 labels={'Director', 'Actor', 'Person'} properties={'birthday': '-425437200000', 'birthplace': 'Concord, California, USA', 'name': 'Tom Hanks', 'lastModified': '1299958130000', 'id': '31', 'biography': '<FONT size=3><FONT face=Calibri><B style="mso-bidi-font-weight: normal"><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN>Thomas Jeffrey "Tom" Hanks</SPAN></B><SPAN style="mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: Calibri; mso-ansi-language: EN" lang=EN> (born July 9, 1956) is an American actor, producer, writer and director. Hanks worked in television and family-f', 'version': 359, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/191/4bd0874d017a3c63f3000191/tom-hanks-profile.jpg'}> m=<Node id=756 labels={'Movie'} properties={'studio': 'Universal Pictures', 'releaseDate': '803772000000', 'imdbId': 'tt0112384', 'runtime': 140, 'description': "Technical troubles scuttle the Apollo 13 lunar mission in 1971, risking the lives of astronaut Jim Lovell  and his crew in director Ron Howard's chronicle of this true-life story, which turns a failed journey into a thrilling saga of heroism. Drifting more than 200,000 miles from Earth, the astronauts work furiously with the ground crew to avert tragedy.", 'language': 'en', 'title': 'Apollo 13', 'version': 236, 'trailer': 'http://www.youtube.com/watch?v=nEl0NsYn1fU', 'imageUrl': 'http://cf1.imgobject.com/posters/177/4d68030e7b9aa13636000177/apollo-13-mid.jpg', 'genre': 'Action', 'tagline': 'Houston, we have a problem.', 'lastModified': '1299974865000', 'id': '568', 'homepage': ''}> coActors=<Node id=759 labels={'Actor', 'Person'} properties={'birthday': '-362451600000', 'birthplace': 'Philadelphia', 'name': 'Kevin Bacon', 'lastModified': '1299491319000', 'id': '4724', 'biography': '', 'version': 146, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/3e0/4bed49cf017a3c37a30003e0/kevin-bacon-profile.jpg'}> m2=<Node id=8340 labels={'Movie'} properties={'studio': 'Castle Rock Entertainment', 'releaseDate': '724028400000', 'imdbId': 'tt0104257', 'runtime': 138, 'description': 'When cocky military lawyer Lt. Daniel Kaffee  and his co-counsel, Lt. Cmdr. JoAnne Galloway, are assigned to a murder case, they uncover a hazing ritual that could implicate high-ranking officials such as shady Col. Nathan Jessep.', 'language': 'en', 'title': 'A Few Good Men', 'version': 541, 'trailer': 'http://www.youtube.com/watch?v=2270', 'imageUrl': 'http://cf1.imgobject.com/posters/121/4d67fff57b9aa13636000121/a-few-good-men-mid.jpg', 'genre': 'Crime', 'tagline': "In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth.", 'lastModified': '1300257700000', 'id': '881', 'homepage': ''}> cruise=<Node id=1271 labels={'Actor', 'Person'} properties={'birthday': '-236653200000', 'birthplace': 'Syracuse, New York, U.S', 'name': 'Tom Cruise', 'lastModified': '1299997322000', 'id': '500', 'biography': '<P style="MARGIN: 0in 0in 10pt" class=MsoNormal><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY: \'Times New Roman\',\'serif\'; FONT-SIZE: 12pt">Thomas Cruise Mapother IV, born on July 3, 1962, better known by his screen name of Tom Cruise, is an American film actor and producer. He has been nominated for three Academy Awards and won three Golden Globe Awards. His first leading role was the 1983 film Risky Business, which has been described as "A Generation X classic, and a career-maker" for the actor. ', 'version': 231, 'profileImageUrl': 'http://cf1.imgobject.com/profiles/422/4be03d42017a3c35b9000422/tom-cruise-profile.jpg'}>>
"""
#Let's close the session and the transaction.


transaction.close()
session.close()