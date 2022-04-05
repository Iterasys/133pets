import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'     # endereço da API
headers = {'Content-Type': 'application/json'}  # os dados serão no formato json

def testar_incluir_usuario():
    # dados de entrada vem de user1.json
    status_code_esperado = 200  # se a comunicação teve ida e volta
    code_esperado = 200         # se fez o que pediu (inclusão do usuário)
    type_esperado = 'unknown'
    message_esperada = '918117'

    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open('C:\\Users\\corre\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'rb'),
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada

