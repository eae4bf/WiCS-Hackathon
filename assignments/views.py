from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Assignment, Student

from assignments.models import Student


class IndexView(generic.ListView):
    template_name = 'assignments/index.html'
    model = Student
    context_object_name = 'students'
    paginate_by = 5


# Create your views here.

class todoView(ListView):
    model = Assignment
    assignmentList = Assignment.objects.all()
    template_name = '/todo.html'

