from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    country_of_origin = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    date_of_release = models.DateField(null=True, blank=True)
    budget = models.CharField(max_length=20, null=True, blank=True)
    duration = models.CharField(max_length=15)
    starring = models.CharField(max_length=500)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    summary = models.TextField(max_length=500)
    poster_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title