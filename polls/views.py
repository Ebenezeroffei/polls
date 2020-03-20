from django.shortcuts import render,get_object_or_404
from django.views import generic,View
from django.http import JsonResponse
from .models import Question,Choice

# Create your views here.

class HomeView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'questions'
    
class PollsDetailView(generic.DetailView):
    model = Question
    
class RegisterVoteView(View):
    def get(self,request,*args,**kwargs):
        # Get the choice id
        choice_id = int(request.GET.get('choice_id',None));
        # Increase the vote for that choice
        choice = get_object_or_404(Choice,id = choice_id )
        choice.votes += 1
        current_vote = choice.votes
        choice.save()
        data = {
            'current_vote': current_vote,
        }
        return JsonResponse(data)
