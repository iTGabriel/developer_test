import requests

def get_surveys():
    try:
        dados = requests.get('http://localhost:8000/api/surveys').json()
    except:
        dados = []
    return dados