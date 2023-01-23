import requests
import json
from decouple import config

login_usser = config("LOGIN_USER")
login_password = config("LOGIN_PASSWORD")

token = None

def get_token():  
    global token  
    resposta = requests.post(config("URL_API_MAPA_IP")+"login", json={"cpf":login_usser ,"password": login_usser})
    login = resposta.json()
    token = login["token"]
    print("Token: " + str(resposta.status_code))

def atualiza_foto_agente():
    if token == None:
        get_token()
    headers = { 'Authorization' : "Bearer " + token,
                'Content-Type': "Bearer " + token}

    resposta = requests.get(url=config("URL_API_MAPA_IP")+"agentes/fotos",headers=headers)
    print(resposta.status_code)
    
    if resposta.status_code == 500:
        atualiza_foto_agente()



atualiza_foto_agente()