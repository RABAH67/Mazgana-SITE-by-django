from django.shortcuts import render
from .models import Univarsty
# Create your views here.





def home(request):
    
    return render(request,'index.html')



def etude(request):
    univarsity = Univarsty.objects.all()

    return render(request,'etudepage.html',{'univarsity':univarsity})




def tourism(request):
    
    return render(request,'tourismpage.html')




def bisnase(request):
    
    return render(request,'bisnasepage.html')
    
    
    
    

