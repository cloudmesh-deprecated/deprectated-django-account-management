from mongoengine import *
#from other.user_dict import *
from user import User, Users
from project import Project, Projects
import sys
from faker import Factory

connect ('user', port=27777)

#----------------------------------------------------------
#	The generate class generates 10 random users
#----------------------------------------------------------

users = Users()
projects = Projects()


# http://www.joke2k.net/faker/

fake = Factory.create()

def random_user():
    firstname = fake.first_name()    
    data = User(
        title = fake.prefix(),
        firstname = firstname,
        lastname = fake.last_name(),
        email = fake.safe_email(),
        username = firstname.lower(),
        active = True,
        password = fake.word(),
        phone = fake.phone_number(),
        department = "IT",
        institution = fake.company(),
        address = fake.address(),
        country = "USA",
        citizenship = "US",
        bio = fake.paragraph(),
    )
    return data


print 70 * "="
users.clear()
for i in range(0,10):
    data = random_user()
    print data
    users.add(data)    

print 70 * "="
print users.find()

sys.exit()

      


def add_projects():
    """This function adds projects"""
    projects.clear()
    django = Project(
    	    title = "Django",
    	    abstract = "This is my abstract",
            intellectual_merit = "All about the merit thingy",    
            broader_impact = "Everything is broad according ...",
            use_of_fg = "Fg is about to use it",
            scale_of_use = "Would be used to implement djandgo",
            categories = ['FutureGrid'],
            keywords = ['sqllite'],
            primary_discipline = "other",  
            orientation = "Lot's of all make",
            contact = "Bloomington",
            url = 'https://www.facebook.com/',
            active = True,
            status = "pending",
            username = "gregvon",
            resources_services = ['hadoop','openstack'],
            resources_software = ['other'],
            resources_clusters = ['india'],
            resources_provision = ['paas']
          )
    print django.abstract
    projects.add_project(django)
    
    projects.add_member("gregvon1", django)
    
    projects.find()


def main():

    add_users()
    add_projects()

    

if __name__ == "__main__":
    main()
