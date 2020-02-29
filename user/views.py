from django.shortcuts import render
from .forms import NewUserForm
from django.views import View,generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

class NewUserView(View):
    template_name = 'user/user_signup.html'
    form_class = NewUserForm
    
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        context = {'form':form}
        return render(request,self.template_name,context)
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        # If the form is valid then save it
        if form.is_valid():
            form.save()
            messages.success(request,f'Welcome {request.user.username}')
            return HttpResponseRedirect(reverse('polls:home'))
        context = {'form':form}
        return render(request,self.template_name,context)