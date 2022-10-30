from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Instructions


def index(request):
    insrtructions = Instructions.objects.order_by('-topic')
    return render(request, "instruction/list.html", {'all_insrtructions': insrtructions})


def detail(request, instruction_id):
    try:
        instruction = Instructions.objects.get(id=instruction_id)
    except Exception:
        return Http404('Инструкция не найдена')
    return render(request, "instruction/instruction.html", {'instruction': instruction})
