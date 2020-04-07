from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from account.models import Profile
# Create your models here.

# Post:
# title
# content
# status : Draft/Published 

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    statuses = [
        ("D","Draft"),
        ("P","Published"),
    ] 
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank = True)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    image = models.ImageField(upload_to="blog/post",blank = True)
    author = models.ForeignKey(Profile,on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'slug':self.slug})

# Model : Post  1 validation check max length of title 
# Form  : PostForm  : 1 validation check max length of title + 1 validation for image size 
# View :  PostFormCreateView
#     1 if model validations are enough then Model and View 
#             model 
#             fields
#             success_url 
#             template_name 
#     2. if you need additional validation : Model => Form => View
#             form_class
#             success_url
#             template_name

# M

# V : Based on Request 
#     Fetch the data from db : queries 
#     render template

# T   data to be shown 


# AWS :

# EC2 instances : servers => os ram storage 
# S3 : storage bucket 

# RDS 
# posts.objects.filter(category__name ="AI")

# c.post_set.all()