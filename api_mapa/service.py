import requests
import json
from decouple import config
import api_mapa.URLS as URLS

login_usser = config("LOGIN_USER")
login_password = config("LOGIN_PASSWORD")

token = None

def get_token():  
    global token  
    resposta = requests.post(config("URL_API_MAPA")+"login", json={"cpf":login_usser ,"password": login_usser})
    login = resposta.json()
    token = login["token"]
    print("Token: " + str(resposta.status_code))

def atualiza_foto_agente():
    if token == None:
        get_token()
    headers = { 'Authorization' : "Bearer " + token,
                'Content-Type': "Bearer " + token}

    resposta = requests.get(url=config("URL_API_MAPA")+URLS.ATUALIZA_FOTOS_AGENTES,headers=headers)
    print(resposta.status_code)
    
    if resposta.status_code == 500:
        atualiza_foto_agente()

def get_agente_logado():
    if token == None:
        get_token()
    headers = { 'Authorization' : "Bearer " + token,
                'Content-Type': "Bearer " + token}

    resposta = requests.get(url=config("URL_API_MAPA") + URLS.USER_LOGADO,headers=headers)
    print("Dados do Agente: ",resposta.status_code)


#atualiza_foto_agente()
get_agente_logado()