from django.shortcuts import render
from django.http import HttpResponse as HtResp #TODO remove

# Create your views here.
def index(request):
    return HtResp("<h2>This is supposed to be a header number 2 </h2>")
