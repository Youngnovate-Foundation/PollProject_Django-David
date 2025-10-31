from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question = Question.objects.all()
    output = ', '.join(q.question_text for q in latest_question)
    return render(request, 'polls/index.html', {'latest_questions': latest_question})