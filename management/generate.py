from mongoengine import *
#from other.user_dict import *
from user import User, Users
from project import Project, Projects

connect ('user', port=27777)

#----------------------------------------------------------
#	The generate class generates 10 random users
#----------------------------------------------------------

users = Users()
projects = Projects()

def add_users():
    """This function adds 10 users"""
    users.clear()
    
    gregor = User(
        title = "",
        firstname = "Gregor",
        lastname = "von Laszewski",
        email = "laszewski@gmail.com",
        username = "gregvon",
        active = True,
        password = "none",
        phone = "6625768900",
        department = "School of Informatics and Computing",
        institution = "Indiana University",
        address = "Bloomington",
        country = "USA",
        citizenship = "Germany",
        bio = "I work at Indiana University Bloomington",
    )
    users.add(gregor)
        
        
    ifeanyi = User(
        title = "",
        firstname = "Ifeanyi",
        lastname = "Onyenweaku",
        email = "rowlandifeanyi17@gmail.com",
        username = "gregvon",
        active = True,
        password = "none",
        phone = "6625768900",
        department = "School of Informatics and Computing",
        institution = "Indiana University",
        address = "Bloomington",
        country = "USA",
        citizenship = "Nigeria",
        bio = "I research at Indiana University Bloomington"  
    )
    users.add(ifeanyi)
        
    fugang = User(
        title = "",
        firstname = "Fungang",
        lastname = "Nelson",
        email = "nelsonfug@gmail.com",
        username = "fugang",
        active = True,
        password = "none",
        phone = "6627865400",
        department = "School of Informatics and Computing",
        institution = "Indiana University",
        address = "Bloomington",
        country = "USA",
        citizenship = "China",
        bio = "I work at Indiana University Bloomington"  
    )
    users.add(fugang)
      
    users.find()

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
