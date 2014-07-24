Improvements
======================================================================

Achievements:

* django can be used
* we used bottstrap
* we can add users via GUI (new)
* we can add projects via GUI (new)
* we can edit user (with limitations) (new)
* we can edit projects (with limitations) (new)
* we figured out how to pass parameters to a get method (not yet utilized) (new)

Future activities (easy)

* redisign project gui with checkboxes etc
* implement management of members
* implement committee object definitions and workflows
* implement grant object definitions and workflows
* making the GUI fully working with all fields

FutureActivities (moderate)

* using django rest
* GUI interface to slurm

Future Activities (Difficult)

* vm management form flask to django
* proper security model
* making sure the functionality we have in flask is mostly done also
  in django

GET routes
======================================================================

http://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get

If your url is something like domain/search/?q=haha, Then you would
use request.GET.get('q', '').

q is the parameter you want, And '' is the default value if q isn't
found.

If you are instead just configuring your URLconf, Then your captures
from the regex are passed to the function as arguments (or named
arguments).

Such as:

(r'^user/(?P<username>\w{0,50})/$', views.profile_page,),
Then in your views.py you would have

def profile_page(request, username):
    # Rest of the method
