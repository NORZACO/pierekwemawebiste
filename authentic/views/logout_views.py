from django.shortcuts import redirect #HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout





def logoutHandler(request):
    logout(request)
    messages.success(request, "Logout Successfully 😃 ")
    return redirect("Home")