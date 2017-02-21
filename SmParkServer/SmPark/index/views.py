from django.shortcuts import render
from django.http import HttpResponse as HttpRe #TODO remove

# Create your views here.
def index(request):
    return render(request, 'index')
