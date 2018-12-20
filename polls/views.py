from django.shortcuts import render
from django.http import  HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_test for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("you're looking at question %s." % question_id)

def results(request,question_id):
    response = "you're looking at the results of question %s."
    return  HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on question %s." % question_id)

# Create your views here.
