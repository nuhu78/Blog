from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Tag (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
class Post(models.Model):
    title=models.CharField(max_length=100)  
    content=RichTextField(blank=True, null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 
    Catagory=models.ForeignKey(Catagory, on_delete=models.SET_NULL , null=True)
    tags=models.ManyToManyField(Tag)
    view_count=models.PositiveBigIntegerField(default=0)
    liked_users=models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
