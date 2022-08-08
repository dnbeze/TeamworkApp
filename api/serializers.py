from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import workouts

class workoutsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = workouts
        fields = '__all__'