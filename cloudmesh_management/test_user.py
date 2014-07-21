from user import User, Users

def main():

    users = Users()
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

    from pprint import pprint 
    import sys
    pprint (User.__dict__)
    print gregor.fields()
    print gregor.fields("optinal")
    print gregor.fields("required")
    print "\n".join(gregor._fields)
    print "ORDER", gregor.order
    print gregor.json()
    print gregor.yaml()
    sys.exit()
    
    users.add(gregor)
    print "Gregor username: ", gregor.username
    print gregor.date_created
    print gregor.date_deactivate

    print


    #print users.find("laszewski@gmail.com")
    
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
                
        
        # add the other fields
    )
    users.add(ifeanyi)
    print    
    print "ifeanyi username: ", ifeanyi.username
    print

    #print users.find("rowlandifeanyi17@gmail.com")
    
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
        
        # add the other fields
    )
    users.add(fugang)
    print    
    print "Fugang username: "#, fugang.username
    print
    print users.find_user("gregvon12")
    
    #users.find()


if __name__ == "__main__":
    main()
