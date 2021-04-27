from django.shortcuts import render
from .services import request_api
# Create your views here.

def home(request):
    dados_surveys = request_api.get_surveys()
    dados_questions = request_api.get_surveys_questions()
    dados_alternatives = request_api.get_surveys_questions_alternatives()
    dados_user_answer = request_api.get_surveys_user_answer()

    return render(request, 'index.html', {'dados_surveys': dados_surveys, 'dados_questions': dados_questions, 'dados_alternatives': dados_alternatives, 'dados_user_answer': dados_user_answer} )

