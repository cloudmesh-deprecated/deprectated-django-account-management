from management import User
from management import Account
from management import Contact
from mongoengine import *

# https://code.google.com/p/prettytable/
#  https://code.google.com/p/prettytable/source/browse/trunk/README
# 
#

connect ('user', port=27777)

ifeanyi = User(title="Mr.", firstname="Ifeanyi",
               lastname="Onyenweaku",
               email="rowlandifeanyi17@gmail.com")
ifeanyi.save()

account = Account(username="rowlandifeanyi",
                    email="rowlandifeanyi17@gmail.com",
                    password="17ROW1992")
account.owner = ifeanyi
account.save()

jeff = User(title="Mr.", firstname="Jeffery",
            lastname="Ridgeway",
            email="jeff01@gmail.com")
jeff.save()

account = Account(username="jeff01",
                    email="jeff01@gmail.com",
                    password="17JEFF1992")
account.owner = jeff
account.save()

print
print "LIST OBJECTS"
print 70 * "-"
print

accounts = Account.objects()

for account in accounts:
    print account.owner.firstname, ":", account

print
print 70 * "-"

names=["Juan", "Benjamin", "Santiago", "Thiago", "Lucas", "Joaquin", "Santino", "Lautaro",
        "Ian", "Mateo", "Daniel", "Dylan/Dyllan", "Kevin/Keven", "Miguel", "Davi", "Arthur",
        "Gabriel", "Pedro", "Lucas", "Matheus", "Bernardo", "Rafael", "Guilherme", "William",
        "Jacob", "Liam", "Nathan", "Noah", "Ethan", "Lucas", "Lukas", "Benjamin", "Samuel",
        "Logan", "Liam", "Ethan", "Jacob", "Logan", "Mason", "Benjamin", "Lucas", "Alexander",
        "Carter", "Noah", "Ethan", "Liam", "Lucas", "Mason", "Logan", "Noah", "Alexander",
        "Benjamin", "Jacob", "Jack", "Liam", "Mason", "Carter", "Noah", "Logan", "Lucas",
        "William", "Benjamin", "Jacob", "Hunter", "Jacob", "Ethan", "Benjamin", "Lucas", "Owen",
        "Noah", "Liam", "Mason", "Carter", "Hunter", "Liam", "Ethan", "Jacob", "Lucas",
        "Benjamin", "Liam", "Hunter", "Connor", "Jack", "Cohen", "Jaxon", "John", "Landon",
        "Owen", "William", "Benjamin", "Caleb", "Henry", "Lucas", "Mason", "Noah", "Alex",
        "Alexander", "Carter", "Charlie", "David", "Jackson", "James", "Jase", "Joseph",
        "Wyatt", "Austin", "Camden", "Cameron", "Emmett", "Griffin", "Harrison", "Hudson",
        "Jace", "Jonah", "Kingston", "Lincoln", "Marcus", "Nash", "Nathan", "Oliver", "Parker",
        "Ryan", "Ryder", "Seth", "Xavier", "Charles", "Clark", "Cooper", "Daniel", "Drake",
        "Dylan", "Edward", "Eli", "Elijah", "Emerson", "Evan", "Felix", "Gabriel", "Gavin",
        "Gus", "Isaac", "Isaiah", "Jacob", "Jax", "Kai", "Kaiden", "Malcolm", "Michael",
        "Nathaniel", "Riley", "Sawyer", "Thomas", "Tristan", "Antonio", "Beau", "Beckett",
        "Brayden", "Bryce", "Caden", "Casey", "Cash", "Chase", "Clarke", "Dawson", "Declan",
        "Dominic", "Drew", "Elliot", "Elliott", "Ethan", "Ezra", "Gage", "Grayson", "Hayden",
        "Jaxson", "Jayden", "Kole", "Levi", "Logan", "Luke", "Matthew", "Morgan", "Nate",
        "Nolan", "Peter", "Ryker", "Sebastian", "Simon", "Tanner", "Taylor", "Theo", "Turner",
        "Ty", "Tye", "William", "Nathan", "Samuel"]

for name in names:
    print name

print len(names)



def print_contacts(columns):
    pass

print_contacts(["username", "phone", "email"])

print_summary()

"""how many users from bloomington
   how many from chicago
   mhao many for that isntitue"""

   
   
