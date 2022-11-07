from django.db import models
from myuser.models import MyUser
# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=100)

    def __str__(self):
        return self.courseName

class Student(models.Model):
    address = models.CharField(max_length=20,null=True,blank=True)
    batch = models.CharField(max_length=30)
    contactNo = models.CharField(max_length=20)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.fullname