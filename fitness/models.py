from django.db import models
from django.db.models import Q # for queries
# Create your models here.

class Exercises(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    musclegroup = models.PositiveSmallIntegerField(
        choices=(
            (1,"Hamstrings"),
            (2,"Calves"),
            (3,"Chest"),
            (4,"Back"), 
            (5,"Shoulders"),
            (6,"Triceps"),
            (7,"Biceps"),
            (8,"Forearms"),
            (9,"Traps"),
            (10,"Abs")
        ))
    text = models.TextField()
    def __str__(self):
        return self.name


class User(models.Model):
    UserID =
    Username = 
    Password = 

class Userinfo

class Workout

class Workoutdetail
