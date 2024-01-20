from django.db import models
from django.utils.timezone import now
from sqlite3 import Timestamp

class DoctorProfile(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100) 
    address = models.CharField(max_length=100 , default="") 
    def __str__(self):
        return self.username

class PatientProfile(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100) 
    address = models.CharField(max_length=100 , default="") 
    def __str__(self):
        return self.username
    
    
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='Myapp/static')
    category =models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=60)
    slug = models.CharField(max_length=130)
    timestamp= models.DateTimeField(default=now)


    def __str__(self):
        return self.title + ' by '+ self.author
# class BlogPost(models.Model):
#     heading = models.CharField(max_length=255)
#     author_name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='blog_images/')
#     description = models.TextField()

#     def __str__(self):
#         return self.heading
# Create your models here.
