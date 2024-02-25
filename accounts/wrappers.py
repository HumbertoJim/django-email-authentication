from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

def authentication_required(function, as_method=True):
    if as_method:
        def wrapper(self, request:HttpRequest, *args, **kwargs) -> HttpResponse:
            if request.user.is_authenticated:
                return function(self, request, *args, **kwargs)
            else:
                return redirect('/accounts/signin')
    else:
        def wrapper(request:HttpRequest, *args, **kwargs) -> HttpResponse:
            if request.user.is_authenticated:
                return function(request, *args, **kwargs)
            else:
                return redirect('/accounts/signin')
    return wrapper