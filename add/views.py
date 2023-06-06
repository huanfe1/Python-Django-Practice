from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'add.html')


def get_add(request):
    result = int(request.GET.get('num1')) + int(request.GET.get('num2'))
    return HttpResponse(result)
