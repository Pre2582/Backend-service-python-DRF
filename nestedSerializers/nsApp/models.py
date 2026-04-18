from django.db import models

# Create your models here.

class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    ratings = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title    