from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

#abstract user model
#id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, groups, user_permissions

class FitUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name


class Workout(models.Model):
    owner = models.ForeignKey(FitUser, on_delete=models.CASCADE)
    workoutid = models.AutoField(primary_key=True)
    weight = models.IntegerField(blank=true)
    reps = models.IntegerField(blank=true)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.workout


class WorkoutDetail(models.Model):
    workout = models.models.OneToOneField(Workout, on_delete=models.CASCADE)
    workoutdetailid = models.AutoField(primary_key=True)
    exercise = models.CharField(max_length=30)
    weight = models.IntegerField(blank=true)
    reps = models.IntegerField(blank=true)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.exercise