
from django.shortcuts import render




# Create your views here.
def signupHandler(request):
    return render(request, "authentic/registration/signup.html")
