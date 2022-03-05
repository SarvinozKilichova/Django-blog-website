from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from httpx import delete

# Create your models here.z

STATUS = ((0, "Draft"), (1, "Published"))

class user_profile(models.Model):
  slug =   models.SlugField(max_length=200, unique=True, default=0)
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  bio = models.TextField()
  picture = models.ImageField(upload_to='images/users', null=True, verbose_name="")
  status = models.IntegerField(default=0)  

  def __str__(self):
    return str(self.user)

class Post(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  slug =   models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(user_profile, null=True,  on_delete=models.CASCADE, related_name='post')
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  image= models.ImageField(upload_to='images/', null=True, verbose_name="")
  count = models.IntegerField(default=0)
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-count']
    ordering = ['-created_on']

  def __str__(self):
    return self.title

  def add_visit(self):
        if self.count is not None:
            self.count += 1
        else:
            self.count = 0  
            
  def get_absolute_url(self):
        return reverse('App')
          



