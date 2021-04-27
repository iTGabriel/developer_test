'''
    # Todas as rotas encontra-se em funcionamento e testadas via django panel e postman.
    # Fiquei com dúvida referente a 'view' solicitada na etapa 3, se era viewset's do django rest api ou template view, então acabei desenvolvendo ambos.
        - Template view só faz get da tabela survey_survey(de acordo com o migrate do django, o mesmo coloca prefixo o nome do app) 
    # Agradeço pelo desafio, me diverti e também aprendi bastante.

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

    from survey.models import *

    try:
        # Primeiro insert
        survey = Survey(name="Django é estável?", description="Empresas como Disqus, Instagram, Pinterest e Mozilla têm usado Django por muito anos. Sites desenvolvidos em Django resistem a picos de tráfego de mais de 50 mil acessos por segundo.")
        survey_question = SurveyQuestion(survey=survey, question="A descrição da pergunta, é verdadeira ou negativa ?")
        survey_question_alternative_sim = SurveyQuestionAlternative(survey=survey, survey_question=survey_question, question_alternative="Sim")
        survey_question_alternative_nao = SurveyQuestionAlternative(survey=survey, survey_question=survey_question, question_alternative="Não")
        survey_user_answer = SurveyUserAnswer(user="User 1", survey=survey, survey_question=survey_question, survey_question_alternative=survey_question_alternative_sim)
        survey.save()
        survey_question.save()
        survey_question_alternative_sim.save()
        survey_question_alternative_nao.save()
        survey_user_answer.save()
        print("Sucesso ao realizar o primeiro 1º registro no banco de dados")
    except:
        print("Falha ao realizar o primeiro 1º registro no banco de dados")

    try:
        # Segundo insert
        survey = Survey(name="Django escala ?", description="Teste de descrição.")
        survey_question = SurveyQuestion(survey=survey, question="Escolha uma das alternativas.")
        survey_question_alternative_sim = SurveyQuestionAlternative(survey=survey, survey_question=survey_question, question_alternative="Sim, o tempo de desenvolvimento em django é rápido e projetado para aproveitar o máximo de hardware quanto você pode dar a ele.")
        survey_question_alternative_nao = SurveyQuestionAlternative(survey=survey, survey_question=survey_question, question_alternative="Não, o tempo de desenvolvimento é demorado e nada benéfico ao negócio.")
        survey_user_answer = SurveyUserAnswer(user="User 2", survey=survey, survey_question=survey_question, survey_question_alternative=survey_question_alternative_sim)
        survey.save()
        survey_question.save()
        survey_question_alternative_sim.save()
        survey_question_alternative_nao.save()
        survey_user_answer.save()
        print("Sucesso ao realizar o segundo 2º registro no banco de dados")
    except:
        print("Falha ao realizar o segundo 2º registro no banco de dados")




