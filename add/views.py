from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'add.html')


def get_add(request):
    result = int(request.GET.get('num1')) + int(request.GET.get('num2'))
    return HttpResponse(result)