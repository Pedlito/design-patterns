import json

class JsonGenerator():
    """
    Clase utilizada para generar objetos JSON.
    """

    def getJsonBody(self):
        """
        Genera un objeto JSON:
        {
            "nombres": "Pedro Andrés",
            "apellidos": "Veta Stalling",
            "edad": 29,
            "ciudad": "Guatemala"
        }
        """
        body = {
            'nombres': 'Pedro Andrés',
            'apellidos': 'Vega Stalling',
            'edad': 29,
            'ciudad': 'Guatemala'
        }
        return json.dumps(body)