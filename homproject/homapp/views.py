from django.shortcuts import render,HttpResponse

from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hello world</h2>")

def home(request):
    temp=loader.get_template("index.html")
    return HttpResponse(temp.render())

def payment(request):
    temp=loader.get_template("payment.html")
    return HttpResponse(temp.render())