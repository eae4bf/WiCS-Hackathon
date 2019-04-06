from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from .models import Assignment, Student
from django.utils import timezone

from assignments.models import Student


class IndexView(generic.ListView):
    template_name = 'assignments/index.html'
    model = Assignment
    context_object_name = 'assignment_list'
    paginate_by = 10


# Create your views here.

class todoView(ListView):
    model = Assignment
    assignment_list = Assignment.objects.all()
    template_name = 'assignments/todo.html'


class AssignmentCreateView(generic.CreateView):
    model = Assignment
    fields = ('title', 'description', 'due_date')
    success_url = reverse_lazy('assignments:index')

def delete_assignment(request,assignment_id):
    Assignment.objects.filter(id=assignment_id).delete()
    allAssignments = Assignment.objects.all()
    context = {
        'assignment_list': allAssignments
    }
    return render(request, 'assignments/index.html',context)
