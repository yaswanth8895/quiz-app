from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, QuizSession
import random

def start_quiz(request):
    session_id = request.session.get('quiz_session_id')
    if session_id:
        QuizSession.objects.filter(id=session_id).delete()
    
    session = QuizSession.objects.create()
    request.session['quiz_session_id'] = session.id
    return redirect('get_questions')

def get_questions(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return HttpResponse("No active quiz session found.")
    
    try:
        session = QuizSession.objects.get(id=session_id)
    except QuizSession.DoesNotExist:
        return HttpResponse("Invalid quiz session.")
    remaining_questions = Question.objects.all()
    
    if remaining_questions.count() < 3:
        return HttpResponse("Not enough questions available to start the quiz.")
    
    questions = random.sample(list(remaining_questions), 3)
    for question in questions:
        session.asked_questions.add(question)
    return render(request, 'quiz/questions.html', {'questions': questions})

def submit_answers(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return HttpResponse("No active quiz session found.")
    
    session = QuizSession.objects.get(id=session_id)
    for question_id in request.POST.getlist('question_id'):
        question = Question.objects.get(id=question_id)
        selected_option = request.POST.get(f'option_{question_id}')
        session.total_questions += 1
        if selected_option == question.correct_option:
            session.correct_answers += 1
        else:
            session.incorrect_answers += 1
    session.save()
    return redirect('get_results')

def get_results(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return HttpResponse("No active quiz session found.")
    
    session = QuizSession.objects.get(id=session_id)
    return render(request, 'quiz/results.html', {'session': session})