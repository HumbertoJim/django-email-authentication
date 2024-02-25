from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'home.html')
