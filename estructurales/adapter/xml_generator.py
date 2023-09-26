import xml.etree.ElementTree as ET

class XmlGenerator():
    """
    Clase utilizada para generar objetos XML.
    """
    
    def getXmlBody(self):
        """
        Genera un objeto de XML:
        <info>
            <nombres>Juan Luis</nombres>
            <apellidos>García Fernandez</apellidos>
            <edad>30</edad>
            <ciudad>Cobán</ciudad>
        </info>
        """
        info = ET.Element('info')
        nombres = ET.SubElement(info, 'nombres')
        nombres.text = 'Juan Luis'
        apellidos = ET.SubElement(info, 'apellidos')
        apellidos.text = 'Garcia Fernandez'
        edad = ET.SubElement(info, 'edad')
        edad.text = 30
        ciudad = ET.SubElement(info, 'ciudad')
        ciudad.text = 'Cobán'

        output = ET.ElementTree(info)
        return output