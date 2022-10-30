from django.http import HttpResponse, Http404


from .models import Question
from django.shortcuts import render



def index(request):
    question = Question.objects.order_by('topic_answer')
    return render(request, "question/list.html", {'all_question' : question})


def detail(request, question_id):
    try: 
        question = Question.objects.get(id = question_id )
    except Exception:
        raise Http404("«Ой, кажется, такой страницы нет».")
    return render(request, "question/question.html", {'question': question})


