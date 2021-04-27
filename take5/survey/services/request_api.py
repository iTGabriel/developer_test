import requests

def get_surveys():
    try:
        dados = requests.get('http://localhost:8000/api/surveys').json()
    except:
        dados = []
    return dados

def get_surveys_questions():
    try:
        dados = requests.get('http://localhost:8000/api/surveys/questions//').json()
    except:
        dados = []
    return dados

def get_surveys_questions_alternatives():
    try:
        dados = requests.get('http://localhost:8000/api/surveys/questions/alternatives/').json()
    except:
        dados = []
    return dados

def get_surveys_user_answer():
    try:
        dados = requests.get('http://localhost:8000/api/surveys/user/answer/').json()
    except:
        dados = []
    return dados
