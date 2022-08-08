from django.shortcuts import render
 
# Create your views here.
 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import workouts
from .serializers import workoutsSerializer
 
 
class workoutslist(APIView):
 
    def get(self,request):
        book1 = workouts.objects.all()
        serializer = workoutsSerializer(book1, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass