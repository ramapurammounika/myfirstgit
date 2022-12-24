from django.shortcuts import render
from django. http import HttpResponse 
# Create your views here.
def rajareddy(request):
    return HttpResponse('<h1><b> he is farmer</b></h1>')

def rameswari(request):
    return HttpResponse('<h2><marquee>she is best mom in the world</marquee></h2>')