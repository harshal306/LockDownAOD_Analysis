from django.shortcuts import render
from django.http import HttpResponse


file_data = open('E:/Important_files/CollegeWorld/IIRS_Dehradun/Semester 1/Module 3/PilotProject3-2a/pilotProject/mainsite/templates/mainsite/index.html')

# Create your views here.
def index(request):
    return HttpResponse(file_data.read())