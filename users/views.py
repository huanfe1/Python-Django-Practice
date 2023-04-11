from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        pwd = request.GET.get('pwd')
        context = {name: name, pwd: pwd}
        print(str(context))
        return HttpResponse("拒绝访问")
    else:
        name = request.GET.get('name')
        pwd = request.GET.get('pwd')
        context = {name: name, pwd: pwd}
        print(str(context))
        return redirect('https://baidu.com')
