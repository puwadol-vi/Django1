from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Student(models.Model):
    #id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    student_id=models.CharField(max_length=20,null=True,blank=True)
    school_id=models.ForeignKey('School',null=True,on_delete=SET_NULL)
    
class School(models.Model):
    school_name=models.CharField(max_length=20,null=True,blank=True)
    max_student=models.IntegerField()
    

