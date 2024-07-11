from accesoDatos import accesoDatos
from entidades import tipoCambio

class logicaNegocio:
    def __init__(self):
        self.acceso_datos = accesoDatos()

    def obtener_tipo_cambio(self, fecha):
        compra_xml, venta_xml = self.acceso_datos.obtener_tipo_cambio(fecha)
        compra = self.acceso_datos.procesar_xml(compra_xml)
        venta = self.acceso_datos.procesar_xml(venta_xml)

        if compra is None or venta is None:
            raise Exception("No se encontró el tipo de cambio para la fecha solicitada, inténtelo de nuevo.")

        tipo_cambio = tipoCambio(compra=float(compra), venta=float(venta))
        return tipo_cambio
