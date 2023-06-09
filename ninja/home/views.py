from django.shortcuts import render

from django.http import HttpResponse
from .models import Student

def home(request):
    return HttpResponse('<h1>Hallo Welt</h1>')

def student(request):
   context = {
       'first_name':'TOST',
       'my_list': [2020, 2021, 2022],
       'book_name':'lord of the rings'
   }
   return render(request, 'home/home.html' , context)

def student_detail(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request,'home/student_detail.html', context)

from .forms import StudentForm
from django.shortcuts import redirect
def student_add(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = { 
        'form':form
    }
    return render(request, 'home/student_add.html', context)