from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404 ,render

from mysite.polls.models import Question


def index1(request):
    return HttpResponse("hello world you are at the polls index")
def detail(request,question_id):
    return HttpResponse("you are looking at question %s."%question_id)
def result(request,question_id):
    response="you are looking at the result of question %s"
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("you are voting on the question %s."%question_id)
def index(request):
    latest_question_list=Question.ojects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)
def detail(request,question_id):
    try:
        question=Question.objectss.get(pk=question_id)
    except Question.DoesNotExists:
        raise Http404("Question doesnot exists")
    return render(request,'polls/detail.html',{'question':question})

