from django.shortcuts import render
from django.template import context


def index(request):
    context={
        'title':'Home'
    }
    return render(request, 'api/index.html',context)