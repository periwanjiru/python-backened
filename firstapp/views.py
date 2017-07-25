# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Students

# # Create your views here.

# def welcome(request):
#     return render(request,'welcome_student.html')
# def students_view(request):

#     return HttpResponse("<p> All students are here </p>")
from django.shortcuts import render
from django.http import HttpResponse
from .models import student

#create your views here.

def welcome(request):
    return render(request,'welcome_student.html')
def Students(request):
    students = student.objects.all()
    # return HttpResponse(students)
    # return HttpResponse(student[0])
    return HttpResponse(student[0].names)
    # return HttpResponse(student[0].description)
    



    
