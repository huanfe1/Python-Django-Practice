from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    userlist = [
        {'name': 'zhangsan', 'age': 18, 'sex': '男'},
        {"name": 'lili', 'age': 17, 'sex': "女"},
        {"name": "wangzheng", 'age': 18, "sex": "女"},
        {"name": "chaochuan", 'age': 18, "sex": "男"},
    ]
    return render(request, 'index.html', {"ulist": userlist})


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
