account_information = {

{"username" : {
    "label"="Username",
    "required" = True,
    "help": """Usernames must be between 3 and 10 characters in
		     length and may contain only lowercase letters (a-z),
		     numbers (0-9), and hyphens (-), and should begin with
		     a letter."""
             },
 "email" : {
    "label"="E-mail",
    "required" = True,
    "help":	"""Please use your e-mail from your university or
		    organization.  Please avoid using gmail, hotmail or
		    other non organizational e-mails, as they may lead to
		    a delay or in some cases to a rejection of the account
		    request. All e-mails from the system will be sent to
		    this address. The e-mail address is not made public
		    and will only be used if you wish to receive a new
		    password or wish to receive certain news or
		    notifications by e-mail."""
            },
 "password"	: {	
    "label"="Password",
    "required" = True
    },
#"Does not have a stringfield for confirm password yet"
 "Confirm_password" : {
    "label" = "Confirm password",
    "required" = True,
    "help" = """Provide a password for the new account in both fields.
		Force password change on first-time login If this box
		is checked, the user will be forced to change their
		password on their first login."""
        }

        }

        }

contact_info =  {

{"title" : {
    "label" = "Title",
    "required" = False,
    "help" = """Enter your desired title, such as Mr., Dr., Prof.,
		etc. (Optional)"""
        },
"firstname" : {
    "label" = "Firstname",
    "required" = True},

"lastname" : {
    "label" = "Lastname",
    "required" = True},

"email" : {
    "label" = "E-mail",
    "required" = True,
    "help" = """Please use your e-mail from your university or
		organization. Please avoid using gmail, hotmail or
		other non organizational e-mails, as they may lead to
		a delay or in some cases to a rejection of the account
		request. The content of this field is kept private and
		will not be shown publicly."""
        },

"Phone" : {
    "label" = "Phone Number",
    "required" = True,
    "help" = """The content of this field is kept private and will not
		be shown publicly."""
        },

"Department" : {
    "label" = "Department / Organizational Unit / Division / Lab",
    "required" = True,
    "help" = """This is your institution name, department, or similar
		... Examples are Computer Science Department,
		Mathematics and Computer Science Division."""
        },
        
"Institution" : {
    "label" = "University / Government Organization / Company ",
    "required" = True,
    "help" = """The name of your University, Government Organization,
		or Company.  Examples are Indiana University, Argonne
		National Laboratory, Google, Open Science Grid. Please
		do not use abbreviations."""
        },
#"Does not have a assigned string for this yet"	

"Institutional_Role" : {
    "label" = "Institutional Role",
    "required" = True,
    "help" = """Select the institutional role that best identifies you
		in your organization. The content of this field is
		kept private and will not be shown publicly."""
        },

"Adviser_Contact" : {	
    "label" = "Adviser's Contact Information",
    "required" = False,
    "help" = """For students, please put your adviser's contact
		information, which includes full name, department,
		phone number, email, URL, address, etc., otherwise
		your application may get delayed or even declined.
		The content of this field is kept private and will not
		be shown publicly."""
        },
        
"Institute_Address" : {
    "label" = "Institution Address",
    "required" = True},
    
"Institute_Country" : {
    "label" = "Institution Country",
    "required" = True},
    
"url" : {
    "label" = "URL",
    "required" = False
    "help" = """If applicable, please include the URL of your personal
		profile page in your organization's website."""
        },

"citizenship" : {
    "label" = "Citizenship",
    "required" = True,
    "help" = """The content of this field is kept private and will not
		be shown publicly."""
        },

"Bio" : {
    "label" = "Bio",
    "required" = False,
    "help" = "A short bio about yourself"
    },
    
"SignUp_Code" : {
    "label" = "Sign up code",
    "required" = False,
    "help" = """If you have been given a signup code, enter it
		here. If you do not have a sign up code, enter nothing
		in this box."""
        }
        
        }
                 
        }


