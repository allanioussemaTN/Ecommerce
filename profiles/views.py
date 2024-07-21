from django.shortcuts import render

# Create your views here.
def home(request):
    context= locals() #The locals() function returns a dictionary containing all the local variables in the current scope. 
    template= 'home.html'
    return render(request,template,context)