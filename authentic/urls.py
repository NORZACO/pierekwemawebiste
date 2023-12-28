from django.urls import path

# from store import views
from .views import (
    logout_views,
    signup_views,
    login_views,
    verification_utility_views,
)

urlpatterns = [
    path("signup", signup_views.signupHandler, name="Signup"),
    path("login", login_views.loginHandler, name="Login"),
    path("logout", logout_views.logoutHandler, name="Logout"),
    path(
        "activate/<uidb64>/<token>",
        verification_utility_views.ActivateAcountView.as_view(),
        name="activate",
    ),
]