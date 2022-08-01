from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'fitness/index.html')

def signin(request):
    return render(request, 'fitness/signin.html')

def signup(request):
    return render(request, 'fitness/signup.html')

def viewworkouts(request):
    return render(request, 'fitness/viewworkouts.html')
    

def selectworkouts(request, selectedworkout):
    try:
        result = request[selectedworkout]
        return HttpResponse(result)
    except KeyError:
        return HttpResponseNotFound("Workout not found!!!")
    