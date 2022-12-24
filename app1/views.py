from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.
def chandu(request):
    return HttpResponse('<i>chandana reddy good girl</i>')

def prakash(request):
    return HttpResponse('<h1><marquee>my lovely brother</marquee></h1>')