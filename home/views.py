from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home/main.html')