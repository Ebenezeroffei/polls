from django.shortcuts import render
from .forms import NewUserForm
from django.views import View,generic
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class NewUserView(View):
    template_name = 'user/user_signup.html'
    form_class = NewUserForm
    
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        context = {'form':form}
        return render(request,self.template_name,context)
    
    def post(self,request,*args,**kwargs):
        form = self.form_class()
        if form.is_valid():
            return HttpResonseRedirect(reverse('polls:home'))
        context = {'form',form}
        return render(request,self.template_name,context)