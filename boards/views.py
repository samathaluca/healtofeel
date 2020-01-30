from django.shortcuts import render, HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

def pitch_desk(request):
    return render(request, "pitch_desk.html")
