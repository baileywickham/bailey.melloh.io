from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Fortune 

def index(request):
    l = Question.object
    i = 1


def detail(request, fortune_id):
    return HttpResponse(f'you are looking at question {fortune_id}')


