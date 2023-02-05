import requests
import json
import model
from types import SimpleNamespace
from decouple import config
import time, sys



login_usser = config("LOGIN_USER")
login_password = config("LOGIN_PASSWORD")

token = None
user:model.UserLogado = None
n = 0
def get_token():  
    global token  
    resposta = requests.post(config("URL_API_MAPA")+"login", json={"cpf":login_usser ,"password": login_usser})
    login = resposta.json()
    token = login["token"]
    user = model.UserLogado(login["user"]["original"][0])

    

    #atualizar_agente(agente_logado)

    print(user)
    print("Token: " + str(resposta.status_code))
    return user

def atualiza_foto_agente():
    global n
    if token == None:
        get_token()
    headers = { 'Authorization' : "Bearer " + token,
                'Content-Type': "Bearer " + token}

    try:
        resposta = requests.get(url=config("URL_API_MAPA")+"agentes/fotos",headers=headers)

        n = n+1
        print(resposta.status_code, "Atualizado: ",n)
        
        if resposta.status_code > 299:
            time.sleep(1) # Aguarda 1 segundo
            atualiza_foto_agente()
    except:
        n = n+1
        print("Atualizado: ",n)
        time.sleep(1) # Aguarda 1 segundo
        atualiza_foto_agente()


def atualizar_agente(agente:dict):   
    if token == None:
        get_token()
    headers = { 'Authorization' : "Bearer " + token,
                'Content-Type': "Bearer " + token}

    agente_json = json.dumps(agente)

    resposta = requests.put(url=config("URL_API_MAPA")+"agentes/"+str(agente["id"]),headers=headers, json=agente_json)
    print(resposta.status_code)


get_token()
    
#atualiza_foto_agente()