from django.contrib import admin
from .models import Genre, Director, Movie

# Register your models here.

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)

