from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    # work with database
    # data transformation
    # data pass
    # http response
    # json responses

    return HttpResponse('well come task management system')

def show_task(request):
    return HttpResponse('show all task')