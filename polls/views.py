from django.shortcuts import render
from django.views import generic,View
from .models import Question

# Create your views here.

class HomeView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'questions'
    
