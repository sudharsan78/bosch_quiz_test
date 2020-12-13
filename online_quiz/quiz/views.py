from django.shortcuts import render

from .models import Quiz, Questions


def quiz_list(request):
    queryset = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', context={'quiz_list': queryset})


def quiz(request, quiz_id):
    question_set = Questions.objects.filter(quiz_id=quiz_id).prefetch_related('choice_set')

    context = {'question_set': question_set}
    return render(request, 'quiz/quiz.html', context)
