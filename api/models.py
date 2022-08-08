from django.db import models
 
class workouts(models.Model):
    workout_name = models.CharField(max_length=10)
    set_weight = models.CharField(max_length=10)
    number_of_reps = models.IntegerField()
 
# Create a string representation
    def __str__(self):
        return self.workout_name
 