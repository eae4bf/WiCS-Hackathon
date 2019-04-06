from django.shortcuts import render
from django.views import generic

from assignments.models import Student


class IndexView(generic.ListView):
    template_name = 'assignments/index.html'
    model = Student
    context_object_name = 'students'
    paginate_by = 5


# Create your views here.
