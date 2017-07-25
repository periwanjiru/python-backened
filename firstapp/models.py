# from django.db import models
# import datetime


# # Create your views here.

# class Student(models.Model):
#     names = models.TextField(max_length = 12) 
#     course = models.CharField(max_length = 100)
#     year = models.IntegerField
#     description = models.TextField(default='Good student')
#     registration_date = models.DateTimeField(default = datetime.date(2017,6,20))
#     graduation_date = models.DateTimeField(default = datetime.date(2017,12,1))
# from django.db import models
from __future__ import unicode_literals
from django.db import models

#create your views here.

class student(models.Model):

 name = models.CharField(max_length = 12)
 course = models.CharField(max_length = 100)
 def __str__(self):
     pass



    
   

    

    
    
    


