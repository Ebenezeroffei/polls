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
    
class SaveCommentView(View):
    
    def get(self,request,*args,**kwargs):
        # First get the comment and the question id
        comment = request.GET.get('comment',None)
        question_id = int(request.GET.get('question_id',None))
        # Get the question object
        question = get_object_or_404(Question,id = question_id )
        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = 'AnonymousUser'
#         Create and save the comment to the question
        com = question.comment_set.create(
            comment_text = comment,
            author = user,
        )
        com.save()
        data = {
            'total_comments':question.comment_set.count(),
            'author':com.author,
            'comment_text':com.comment_text,
            'pub_date':com.pub_date,
        }
        return JsonResponse(data)
