from django.urls import path

from . import views
from .views import SignupView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
]
