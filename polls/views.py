from django.shortcuts import render
from django.views import generic,View

# Create your views here.

class HomeView(View):
    def dispatch(self,request,*args,**kwargs):
        return render(self.request,'polls/index.html')
