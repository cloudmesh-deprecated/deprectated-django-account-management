from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
	first_name = models.CharField(max_length=120, 
				      null =True, 
                                      blank=True)
	last_name = models.CharField(max_length=120, 
                                     null =True, 
                                     blank=True)
	email = models.EmailField()
	#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	#def __unicode__(self):
		#return smart_unicode(self.email)


'''class Person(models.Model):
	name = models.CharField(max_length =120, 
                                null =True,
                                blank = True,
                                verbose_name="full name")'''


	


