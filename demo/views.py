from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def greet(request):
    return render(request, 'demo/hello.html',{"name":" uye"})


def greet_me(request, name):
    return HttpResponse(f"hello {name}")
