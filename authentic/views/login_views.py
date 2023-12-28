# import
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login #, logout


# login
def loginHandler(request):
    if request.method == "POST":
        user_username = request.POST["email"]
        user_password = request.POST["password"]
        # user = authenticate(request, username=email, password=password)
        user = authenticate(username=user_username, password=user_password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully 😃 ")
            return redirect("Home")
            # return render(request, "authentic/registration/login.html")
        else:
            messages.warning(request, "Invalid Credentials 😡 ")
            # return HttpResponse("Invalid Credentials")
            return render(request, "authentic/registration/login.html")
    return render(request, "authentic/registration/login.html")