from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('<h1 style="color:red;">This is the Index Page</h1>')
    return render(request, 'dashboard/index.html')

def staff(request):
    #return HttpResponse('This is the Staff Page')
    return render(request, 'dashboard/staff.html')