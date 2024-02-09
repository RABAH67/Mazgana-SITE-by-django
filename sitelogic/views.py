from django.shortcuts import render

# Create your views here.





def home(request):
    
    return render(request,'index.html')



def etude(request):
    
    return render(request,'etudepage.html')




def tourism(request):
    
    return render(request,'tourismpage.html')




def bisnase(request):
    
    return render(request,'bisnasepage.html')
    
