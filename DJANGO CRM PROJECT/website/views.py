from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username, password)

        if user is not None:
            messages.success("Logged in")
            return redirect('home')

        print(username, " ", password)

    else:
        messages.error("Failed")
    return render(request, 'home.html', {})

def logout_user(request):
    pass