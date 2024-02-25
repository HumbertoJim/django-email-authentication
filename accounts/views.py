from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import auth, messages
from django.views import View

from accounts.forms import SignInForm, SignUpForm
from accounts.models import User

from accounts.wrappers import authentication_required
from accounts.tools import generate_username

# Create your views here.
class SignInView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('/')
        context = {'form': SignInForm()}
        return render(request, 'signin.html', context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('/')
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid user or password')
        return render(request, 'signin.html', {'form':form})


class SignUpView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('/')
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('/')
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = User(
                username = generate_username(),
                email = form.cleaned_data.get('email'),
                first_name = form.cleaned_data.get('first_name', ''),
                last_name = form.cleaned_data.get('last_name', '')
            )
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User registered')
            return redirect('/accounts/signin')
        context = {'form': form}
        return render(request, 'signup.html', context)


def sign_out(request : HttpRequest):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')


class ProfileView(View):
    @authentication_required
    def get(self, request):
        return render(request, 'profile.html')
        