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
        "help": """Please use your e-mail from your university or
            organization.  Please avoid using gmail, hotmail or
                    other non organizational e-mails, as they may lead to
                    a delay or in some cases to a rejection of the account
                    request. All e-mails from the system will be sent to
                    this address. The e-mail address is not made public
                    and will only be used if you wish to receive a new
                    password or wish to receive certain news or
                    notifications by e-mail."""
        },
     "password"    : {    
        "label"="Password",
        "required" = True
        },
      # Does not have a stringfield for confirm password yet
     "Confirm_password" : {
        "label" = "Confirm password",
        "required" = True,
        "help" : """Provide a password for the new account in both fields.
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
        "help" : """Enter your desired title, such as Mr., Dr., Prof.,
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
        "help" : """Please use your e-mail from your university or
            organization. Please avoid using gmail, hotmail or
                     other non organizational e-mails, as they may lead to
                     a delay or in some cases to a rejection of the account
                     request. The content of this field is kept private and
                     will not be shown publicly."""
        },

    "Phone" : {
        "label" = "Phone Number",
        "required" = True,
        "help" : """The content of this field is kept private and will not
            be shown publicly.""" 
        },

    "Department" : {
        "label" = "Department / Organizational Unit / Division / Lab",
        "required" = True,
        "help" : """This is your institution name, department, or similar
            ... Examples are Computer Science Department,
                     Mathematics and Computer Science Division."""
        },
        
    "Institution" : {
        "label" = "University / Government Organization / Company ",
        "required" = True,
        "help" : """The name of your University, Government Organization,
            or Company.  Examples are Indiana University, Argonne
                     National Laboratory, Google, Open Science Grid. Please
                     do not use abbreviations."""
        },
#"Does not have a assigned string for this yet"    

    "Institutional_Role" : {
        "label" = "Institutional Role",
        "required" = True,
        "help" : """Select the institutional role that best identifies you
            in your organization. The content of this field is
                     kept private and will not be shown publicly."""
        },

    "Adviser_Contact" : {    
        "label" = "Adviser's Contact Information",
        "required" = False,
        "help" : """For students, please put your adviser's contact
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
        "help" : """If applicable, please include the URL of your personal
            profile page in your organization's website."""
        },

    "citizenship" : {
        "label" = "Citizenship",
        "required" = True,
        "help" : """The content of this field is kept private and will not
            be shown publicly."""
        },

    "Bio" : {
        "label" = "Bio",
        "required" = False,
        "help" : "A short bio about yourself"
    },
    
    "SignUp_Code" : {
        "label" = "Sign up code",
        "required" = False,
        "help" : """If you have been given a signup code, enter it
            here. If you do not have a sign up code, enter nothing
                     in this box."""
        }
        
}
                 
}
    "Will update this to look like the above!"

Home

    Welcome, rowland17!
    Logout

    Blogger
    Facebook
    Google
    Twitter
    RSS

Create FG Projects
Title: *
Vocabularies
Project Categories:
Project Keywords: *
Provide some useful keywords related to the project, separated by comma (", ").
Project Contact
If the info in this section need to be updated, you're recommended to do that in your profile page.
Project Lead: *
The person that initiates the project and is responsible for its execution as well as the completion of reporting results to FG.
Project Manager: *
A person that works with the project lead to interact with FG. If specified, we assume we will contact this person in addition to the project lead when asking for results.
Project Contact:
Please include here your primary contact address for the project. This could be different from the Project Lead and Manager. Please use this field only if the Project contact is different than the project lead.
Project Members:
 
    
 
    
Please add the members of your project here that have accounts on the FG portal. All project members that need to have access to FG resources must have a portal account. If a member has applied for an account, but you do not yet see him or her in the list, the portal account is in the process of being approved. Come back at another time to add that member.
Project Alumni:
 
    
These are users that were part of the project but have since left.
Project Information
Project Orientation: *
Research
Education
Industry
Government
Primary Discipline: *
Please identify your primary subdiscipline as defined by the NSF.
Abstract: *
Please provide a short abstract of your proposed research or educational activity using FutureGrid.
Input format
Intellectual Merit: *
In reference to NSF merit review criteria, please briefly describe the intellectual merit of your proposed research or educational activity.
Input format
Broader Impact: *
In reference to NSF merit review criteria, please briefly describe the broader impact of your proposed research or educational activity.
Input format
Software Contributions: *
Yes, this project will generate software that can be used by other FutureGrid users.
No, this project will not generate software that can be used by other FutureGrid users.
Will your project generate any software that can be used by other Futuregrid Users?
Documentation Contribution: *
Yes, I will be able to generate documentation for the project and software we create.
No, I will not be able to generate documentation for the project and software we create.
Will your project generate any documentation that can be used by other Futuregrid Users?
Will you be able to provide support for the software you develop?: *
Yes
No
Related NSF Grant
NSF Grant Number:
NSF Grant Number associated with your experiment, if any.
NSF Grant URL:
URL to the NSF Grant Abstract on the NSF web site associated with your experiment, if any.
Resource Requirements
Hardware Resources: *
alamo (Dell optiplex at TACC)
foxtrot (IBM iDataPlex at UF)
hotel (IBM iDataPlex at U Chicago)
india (IBM iDataPlex at IU)
sierra (IBM iDataPlex at SDSC)
xray (Cray XM5 at IU)
bravo (large memory machine at IU)
delta (GPU Cloud)
Network Impairment Device
Not sure
I don't care (what I really need is a software environment and I don't care where it runs)
Which currently available FutureGrid hardware systems do you wish to use in your research (check all that apply).
Provisioning Type: *
The ability to provision VMs across FutureGrid, log in to provisioned VMs as a privileged or unprivileged user.
The ability to log into provisioned VMs (by providing credentials, e.g. ssh key) as a privileged or unprivileged user.
The ability to log into provisioned bare metal nodes as an unprivileged user.
The ability to provision and log into VMs, but only on a restricted FutureGrid outreach sandbox. (Select this if you are attending a class or outreach event)
This question is irrelevant for me or I do not yet know the answer.
Base Environments: *
High Performance Computing Environment
Eucalyptus
Nimbus
OpenStack
OpenNebula
Other
Which currently available software environment do you need to use (check all that apply)
Services:
Genesis II
gLite
Hadoop
MapReduce
Twister
Unicore 6
OpenNebula
OpenStack
XSEDE Software Stack
Globus
Pegasus
Vampir
PAPI
ScaleMP
CUDA(GPU Software))
SAGA
MPI
Which not yet available software environment do you wish to use when it becomes available (check all that apply).
Comment:
Other software environment not specified above.
Use of FutureGrid: *
How do you intend to use FutureGrid in your proposed research or educational activity?
Input format
Scale of use: *
Briefly describe the scale of resources you expect to need (e.g. "every system you have for a week for a class"; "a few VMs for an experiment"; "I want to run a set of comparisons on entire systems and for each I'll need about ____ days to do that").
Input format
Project Results
Results:
Please document in this section the results of your project and include pointers as urls. Please also add all references that use FG resources.
Input format
NSF Agreement
In order for you to use FutureGrid, you must agree to the following:

I will provide FutureGrid with citations to:

    peer reviewed published papers that were developed at least in part based on use of FutureGrid or which make reference to FutureGrid
    technical reports and other non-peer reviewed published papers that were developed at least in part based on use of FutureGrid or which make reference to FutureGrid
    web pages that include information technical reports and other non-peer reviewed published papers that were developed base on use of FutureGrid or which make reference to FutureGrid 

Additionally, I agree to

    provide a brief result of key performance results at the end of your work with FutureGrid (or once per year summarizing the year's work for multi-year projects)
    I agree to acknowledge FutureGrid properly in. The text to be included is:

    This material is based upon work supported in part by the National Science Foundation under Grant No. 0910812 to Indiana University for "FutureGrid: An Experimental, High-Performance Grid Test-bed." Partners in the FutureGrid project include U. Chicago, U. Florida, San Diego Supercomputer Center - UC San Diego, U. Southern California, U. Texas at Austin, U. Tennessee at Knoxville, U. of Virginia, Purdue I., and T-U. Dresden.

    -Or the shorter-

    This material is based upon work supported in part by the National Science Foundation under Grant No. 0910812. 

Do you agree: *
no, I do not agree (your project can not be approved)
yes, I do agree
Slide Collection Agreement
I will provide FutureGrid with Electronic copies of slides from talks that reference your work done with FutureGrid or which mention FutureGrid (.pdfs or other 'not easily reusable' format o.k.; we will ask you for your permission to post slides publicly and will *not* post them publicly without your permission)
Do you agree?: *
no, I do not agree
yes, I do agree
Other
Other comments:
If you have additional comments that did not fit in any of the above fields, please add them here.
Project Membership Management
Allow project join button: *
This is a public project. Allow users to request to join this project through the portal.
Do not allow users to request to join this project. I will manage project membership myself.
Public projects will have a "Join" link on the project page. Users will be able to request to be added to the project through this link.
Join notification: *
Send an email notification when a user joins
Do not send join notifications
Indicate whether you would like to be notified via email when a user requests to join the project.
Location
Flags
Bookmark this




