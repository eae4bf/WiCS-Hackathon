from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Assignment, Student

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'skillMatch/base.html'
    model = Student
    context_object_name = 'students'

class todoView(ListView):
    model = Assignment
    assignmentList = Assignment.objects.all()
    template_name = '/todo.html'

