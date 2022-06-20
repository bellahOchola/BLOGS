from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(blank=True)    
    blog_pic = ImageField(blank=True, manual_crop="")
    blog_info= models.CharField(max_length=200, blank=True,)
    class Meta:
        db_table = "Blog"


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    class Meta:
        db_table = "Author"


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = "Category"


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to = "images/")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table = "Article"

