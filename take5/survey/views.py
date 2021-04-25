from django.shortcuts import render
from .services import request_api
# Create your views here.

def home(request):
    dados = request_api.get_surveys()
    return render(request, 'index.html', {'dados': dados} )

