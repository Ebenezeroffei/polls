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
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        question = self.get_object()
        if self.request.user.is_authenticated:
            for vote in question.centralvotes_set.all():
                if vote.user == self.request.user.username:
                    context['vote'] = True
        return context
    
class RegisterVoteView(View):
    def get(self,request,*args,**kwargs):
        # Get the choice and question id
        choice_id = int(request.GET.get('choice_id',None))
        question_id = int(request.GET.get('question_id',None))
        # Increase the vote for that choice
        choice = get_object_or_404(Choice,id = choice_id )
        choice.votes += 1
        current_vote = choice.votes
        choice.save()
        # Get the question and register a vote for the question
        question = get_object_or_404(Question,id = question_id)
        print(question)
        question.centralvotes_set.create(user = request.user.username).save()
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
        
        date = com.pub_date.date()
        time = com.pub_date.time()
        date = date.strftime("%a %b %d, %Y")
        time = time.strftime("%r")
        com.save()
        data = {
            'total_comments':question.comment_set.count(),
            'author':com.author,
            'comment_text':com.comment_text,
            'pub_date': f"{date} {time}",
        }
        return JsonResponse(data)
