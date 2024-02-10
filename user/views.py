from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from .forms import CustemRegistrationForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
