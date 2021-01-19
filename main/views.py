from django.shortcuts import render,HttpResponse

def homepage(request):
    return HttpResponse("Hello world")


def test(request):
    return render(request,"test.html")

def go(request):
    return HttpResponse("This is my first page")

def index(request):
    return render(request,"index.html")
