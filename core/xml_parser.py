import xml.etree.ElementTree as ET


class XMLParser:

    def __init__(self, xml_file):
        self.xml_file = xml_file

    def count_psk(self):

        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        return len(root.findall(".//PSK"))
