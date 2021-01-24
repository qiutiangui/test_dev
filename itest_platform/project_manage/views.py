from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    if request.method == "GET":
        print("get 请求")
        name = request.GET.get("name", "")
        print("--->", name)
        return render(request, "hello.html", {"n": name})


def login(request):
    return render(request, "index.html")
