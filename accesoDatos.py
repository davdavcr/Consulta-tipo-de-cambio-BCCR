from zeep import Client
from zeep.transports import Transport
from datetime import datetime
import xml.etree.ElementTree as ET

class accesoDatos:
    def __init__(self):
        wsdl_url = 'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx?WSDL'
        self.client = Client(wsdl=wsdl_url, transport=Transport(timeout=10))

    def obtener_tipo_cambio(self, fecha):
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        elif not isinstance(fecha, datetime):
            raise ValueError("La fecha debe ser una cadena en formato 'YYYY-MM-DD' o un objeto datetime")
        fecha_str = fecha.strftime('%d/%m/%Y')

        parametros_compra = {
            'Indicador': 317,
            'FechaInicio': fecha_str,
            'FechaFinal': fecha_str,
            'Nombre': 'David',
            'SubNiveles': 'N',
            'CorreoElectronico': 'dbrenes2005@gmail.com',
            'Token': 'RANORBIATV'
        }

        parametros_venta = {
            'Indicador': 318,
            'FechaInicio': fecha_str,
            'FechaFinal': fecha_str,
            'Nombre': 'David',
            'SubNiveles': 'N',
            'CorreoElectronico': 'dbrenes2005@gmail.com',
            'Token': 'RANORBIATV'
        }

        try:
            compra = self.client.service.ObtenerIndicadoresEconomicosXML(**parametros_compra)
            venta = self.client.service.ObtenerIndicadoresEconomicosXML(**parametros_venta)
        except Exception as ex:
            print(f"Sucedió un error al obtener el tipo de cambio para la fecha {fecha_str}: {ex}")
            return None, None

        return compra, venta

    def procesar_xml(self, xml_response):
        try:
            root = ET.fromstring(xml_response)
            tipo_de_cambio_tag = root.find('.//NUM_VALOR')

            if tipo_de_cambio_tag is not None:
                tipo_cambio = tipo_de_cambio_tag.text
                return tipo_cambio
            else:
                return None  # Devolver None si no se encuentra el tipo de cambio

        except ET.ParseError as parse_error:
            print(f"Sucedió un error al parsear el XML: {parse_error}")
            return None

        except Exception as ex:
            print(f"Error al procesar respuesta XML: {ex} el XML recibido: {xml_response}")
            return None
