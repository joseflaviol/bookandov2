from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout

# Create your views here.
class SignupView(View):

    def get(self, request):
        return render(request, "registration/signup.html")

    def post(self, request):
        User = get_user_model()

        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            return render(request, "registration/signup.html", {"error_msg": "Email already being used."})

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        user.first_name = name
        user.save()

        login(request, user)

        return redirect("home")

class LoginView(View):

    def get(self, request):
        return render(request, "registration/login.html")

    def post(self, request):

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
        else:
            return render(request, "registration/login.html", {"error_msg": "Email or password are incorrect."})

        return redirect("home")

def logout_view(request):
    logout(request)
    return redirect("home")
