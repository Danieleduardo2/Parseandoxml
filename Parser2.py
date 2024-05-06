import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, archivo):
        self.archivo = archivo

    def parse(self):
        try:
            tree = ET.parse(self.archivo)
            root = tree.getroot()
        
            for child in root:
                print(child.tag, child.attrib)  # (Lógica base del parser)
    
        except ET.ParseError as e:
            print("Error al parsear el archivo XML:", e)

class MyXMLParser(XMLParser):
    def parse(self):
    
        super().parse()  #(Polimorfismo: Llama al método parse de la clase base

archivo_xml = "scrpt.xml"

# Utilizando la clase base (para probar la funcionalidad básica)
xml_parser = XMLParser(archivo_xml)
xml_parser.parse()

