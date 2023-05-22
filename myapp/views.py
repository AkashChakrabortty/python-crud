from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def home(request):
    student = Student.objects.all()
    dict = {
        'students': student
    }
    return render(request,'home.html',dict)

def create(request):
  
   name = request.GET['name']
   student_id = request.GET['student_id']
   phone_number = request.GET['phone_number']
  
   data = Student(name=name,student_id=student_id,phone_number=phone_number)
   data.save()
   return redirect('/')

def delete(request, id):
    data = Student.objects.get(pk=id)
    data.delete()
    return redirect('/')