from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from .forms import CustemRegistrationForm 
from django.contrib.auth.decorators import login_required
from sitelogic.models import Univarsty


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
    
    
    
    
def profile(request):
    
    
    return render(request,'profile.html')
    
    
    
def getoffre(request,univarsty_id):
    
    detail = get_object_or_404(Univarsty,pk=univarsty_id)
    
    return render(request,'getoffre.html',{'detail':detail})
    
    
