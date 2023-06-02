from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hulk(request):
    return HttpResponse(" <h1> hey guys ,thanks for all the love and trust signing off ur hulk.</h1>")
