'''
    # Todas as rotas encontra-se em funcionamento e testadas via django panel e postman.
    # Fiquei com dúvida referente a 'view' solicitada na etapa 3, se era viewset's do django rest api ou template view, então acabei desenvolvendo ambos.
        - Template view só faz get da tabela survey_survey(de acordo com o migrate do django, o mesmo coloca prefixo o nome do app) 
    # Agradeço pelo desafio, me diverti e também aprendi bastante.

    # O script logo abaixo só atende até a etapa 2, ambas opções foram feitas, tanto pelo panel do django quanto via script abaixo.
    # Deixei disponível em requirements.txt tudo que foi utilizado no projeto
'''
if __name__ == '__main__':

    import os, sys
    import django
    from take5.take5 import *

    diretorio_atual = f"{os.getcwd()}\\take5"
    # Adicionando o projeto como 'modulo' aos modulos gerênciado por python
    sys.path.append(diretorio_atual)
    # Definindo o arquivo de configuracao para o django se basear
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'take5.take5.settings')
    django.setup()

    import sqlite3
    from survey.models import Survey
    
    connection = sqlite3.connect(f"{diretorio_atual}\\db.sqlite3")
    cursor = connection.cursor()

    pesquisa = cursor.execute("SELECT * FROM survey_survey")
    pesquisa_contagem = len(pesquisa.fetchall()) + 1

    sql = f"INSERT INTO survey_survey VALUES ('{pesquisa_contagem}','Pesquisa teste {pesquisa_contagem}', 'Teste {pesquisa_contagem}')"
    cursor.execute(sql)
    connection.commit()
    connection.close()