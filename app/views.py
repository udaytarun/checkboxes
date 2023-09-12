from django.shortcuts import render
from app.forms import*
from django.http import HttpResponse

# Create your views here.

def registration(request):
    SREO=Registrationform()
    d={'SREO':SREO}
    if request.method=='POST':
        SRDO=Registrationform(request.POST)
        
        if SRDO.is_valid():
            return HttpResponse(str(SRDO.cleaned_data))

    
    




    return render(request,'registration.html',d)
