from xml_generator import XmlGenerator
from json_generator import JsonGenerator
import json

class Adaptador(JsonGenerator, XmlGenerator):
    """
    Clas que funciona como adaptador entre JsonGenerator y XmlGenerator
    """

    def getJsonBody(self):
        """
        Utiliza la funcion getXmlBody y convierte la respusta a formato JSON.
        """

        xml = self.getXmlBody()
        info = xml.getroot()
        body = {
            'nombres': info.find('nombres').text,
            'apellidos': info.find('apellidos').text,
            'edad': info.find('edad').text,
            'ciudad': info.find('ciudad').text,
        }
        return json.dumps(body)