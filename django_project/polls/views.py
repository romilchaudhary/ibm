from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    latest_question_list = Question.ques.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    # return HttpResponse(output)
    return render(request, 'polls/index.html', context)

@login_required
def details(request, question_id):
    try:
        question = Question.ques.get(pk=question_id)
        context = {"question":question}
    except Question.DoesNotExist:
        raise Http404("question does not exist")
    return render(request, "polls/details.html", context)

from django.core.signals import request_finished
from django.dispatch import receiver
from django_globals import globals

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
    print(globals)
