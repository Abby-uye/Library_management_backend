import uuid

from django.db import models
from django.conf import settings


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}  {self.genre}"

    def list_genres(self):
        return ', '.join(genre.name for genre in self.genre.all()[:2])


class Author(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.FirstName}"


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class BookInstance(models.Model):
    AVAILABLE = "A"
    UNAVAILABLE = "U"
    Available_choices = [
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable")
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=Available_choices, default="Available")
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.status}"
