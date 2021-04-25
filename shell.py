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