from django import forms
from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from .forms import CustemRegistrationForm, NewComment 
from django.contrib.auth.decorators import login_required
from sitelogic.models import Univarsty 
from .models import Command
from django.contrib.auth.decorators import login_required


# Create your views here.



class CustemRegistrationView(View):
    
    def get(self,request):

        form = CustemRegistrationForm()
        
        return render(request,"login.html",locals())
    def post(self,request):
        
        form = CustemRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations, your account has been created")
            
        else:
            messages.warning(request,"Personal information is incorrect, please correct it")
        return render(request,"login.html",locals())
    
    
    
@login_required()
def profile(request):
    
    comond = Command.objects.filter(user = request.user)
    comondes = Command.objects.get(user = request.user)

    
    return render(request,'profile.html',{'comond':comond,'comondes':comondes})
    
    
@login_required()
def getoffre(request,univarsty_id):
    
    detail = get_object_or_404(Univarsty,pk=univarsty_id)
    
    univarsty = detail.univarsty.filter()
    comment_form = NewComment()

    if request.method == 'POST':
        comment_form = NewComment(request.POST , request.FILES) 
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = detail
            new_comment.user = request.user
            new_comment.save()

            return redirect('profile')
    else:
        comment_form = NewComment()
    return render(request,'getoffre.html',{'detail':detail,'comment_form':comment_form,'univarsty':univarsty})
    
    
