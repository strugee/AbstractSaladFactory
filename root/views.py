from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
    return render(request, "index.html")
