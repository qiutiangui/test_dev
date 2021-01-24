from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def hello(request):
    if request.method == "GET":
        print("get 请求")
        name = request.GET.get("name", "")
        print("--->", name)
        return render(request, "hello.html", {"n": name})


def index(request):
    """
    实现登录
    :param request:
    :return:
    """
    # 返回登录页面
    if request.method == "GET":
        return render(request, "index.html")
    # 处理登录的数据
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print("------->", username, password)

        if username == "" or password == "":
            print("用户名密码不能为空！")
            return render(request, "index.html", {"error": "The user name or password is empty"})

        user = auth.authenticate(username=username, password=password)
        print("====>", user)
        if user is not None:
            # 实现登录
            auth.login(request, user)  # 到数据库写session
            return HttpResponseRedirect("/manage/")
        else:
            return render(request, "index.html", {"error": "Wrong user name or password!"})


@login_required()  # 控制用户在未登录的情况下不能登录
def manage(request):
    """
    管理页面
    :param request:
    :return:
    """
    return render(request, "manage.html")


def logout(request):
    auth.logout(request)  # 删除session
    return HttpResponseRedirect("/index/")
