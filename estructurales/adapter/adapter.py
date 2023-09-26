import json
from json_generator import JsonGenerator
from adaptador import Adaptador

def printBody(bodyGenerator: JsonGenerator):
    """
    Imprime un objeto de formato JSON en pantalla
    """

    jsonData = bodyGenerator.getJsonBody()
    data = json.loads(jsonData)
    print('\n{')
    print(f'\t"nombres": {data["nombres"]}')
    print(f'\t"apellidos": {data["apellidos"]}')
    print(f'\t"edad": {data["edad"]}')
    print(f'\t"ciudad": {data["ciudad"]}')
    print('}\n')

print('========= JSON =========')
printBody(JsonGenerator())
print('========= XML =========')
printBody(Adaptador())