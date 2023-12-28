
from django.shortcuts import render, redirect #HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import View  # noqa: F401
from ..verification_utility import token_generator  # noqa: F401




class ActivateAcountView(View):  # noqa: F811
    def get(self, request, uidb64, token):
        try:
            # decode the uid
            uid = force_str(urlsafe_base64_decode(uidb64))
            # get the user
            user = User.objects.get(pk=uid)
        # if user does not exist
        except Exception as identifier:  # noqa: F841
            # user = None
            user = None
        # if user exist and token is valid
        if user is not None and token_generator.check_token(user, token):
            # activate the user
            user.is_active = True
            # set user to active
            user.save()
            # return success page
            messages.success(request, "Account activated successfully 😃 ")
            return redirect("Login")
        return render(request, "authentic/registration/activate_failed.html")
