from evento import Evento
from procesador_html import ProcesadorHtml
import json
from datos_cliente.cliente_black import ClienteBlack
from datos_cliente.cliente_classic import ClienteClassic
from datos_cliente.cliente_gold import ClienteGold
from razones.razon_alta_chequera import RazonAltaChequera
from razones.razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from razones.razon_compra_dolar import RazonCompraDolar
from razones.razon_retiro_efectivo_black import RazonRetiroEfectivoBlack
from razones.razon_retiro_efectivo_classic import RazonRetiroEfectivoClassic
from razones.razon_retiro_efectivo_gold import RazonRetiroEfectivoGold
from razones.razon_transferencia_enviada import RazonTransferenciaEnviada
from razones.razon_transferencia_recibida import RazonTransferenciaRecibida


def cargar_datos(ruta):
    with open(ruta) as archivo:
        persona=json.load(archivo)
    return persona
def buscar_problema(transaccion,cliente,evento,tipo):
    if transaccion["tipo"]=="RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
        if tipo=='CLASSIC':RAZON=RazonRetiroEfectivoClassic()
        elif tipo=='GOLD':RAZON=RazonRetiroEfectivoGold()
        elif tipo=='BLACK':RAZON=RazonRetiroEfectivoBlack()
        
    elif transaccion["tipo"]=="ALTA_TARJETA_CREDITO":
        RAZON=RazonAltaTarjetaCredito()
    elif transaccion["tipo"]=="ALTA_CHEQUERA":
        RAZON=RazonAltaChequera()
    elif transaccion["tipo"]=="COMPRA_DOLAR":
        RAZON=RazonCompraDolar()
    elif transaccion["tipo"]=="TRANSFERENCIA_ENVIADA":
        RAZON=RazonTransferenciaEnviada()
    elif transaccion["tipo"]=="TRANSFERENCIA_RECIBIDA":
        RAZON=RazonTransferenciaRecibida()
    return RAZON.resolver(cliente,evento)


if __name__ == '__main__':
    ruta = 'eventos\eventos_black.json'
    cliente_json=cargar_datos(ruta)
    tipo = cliente_json['tipo']
    
    
    if tipo == 'CLASSIC':
        cliente = ClienteClassic(cliente_json)
    elif tipo == 'GOLD':
        cliente = ClienteGold(cliente_json)
    elif tipo=='BLACK':
        cliente = ClienteBlack(cliente_json)
    
    
    
    HTML=ProcesadorHtml(cliente_json)
    for transaccion in cliente_json['transacciones']:
        transaccion['cantidadExtraccionesHechas']=None
        evento=evento(transaccion)
        
        if transaccion["estado"]=='RECHAZADA':
            razon=buscar_problema(transaccion,cliente,evento,tipo)
            HTML.escribir_html_rechazo(transaccion,razon)
            print(buscar_problema(transaccion,cliente,evento,tipo))
        else:
            print("transaccion aceptada")
            HTML.escribir_html_aceptacion(transaccion)    
    HTML.cerrar_html()
    archivo = open("index.html", "w")
    archivo.write(HTML.texto_html)
    archivo.close()    

