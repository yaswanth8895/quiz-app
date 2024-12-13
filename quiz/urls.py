from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('questions/', views.get_questions, name='get_questions'),
    path('submit/', views.submit_answers, name='submit_answers'),
    path('results/', views.get_results, name='get_results'),
]