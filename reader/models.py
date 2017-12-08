from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    document = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['epub'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()
