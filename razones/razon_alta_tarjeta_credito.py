from datos_cliente.cliente import Cliente
from evento import Evento
class RazonAltaTarjetaCredito():
    def resolver(self,cliente:Cliente,evento:Evento)-> str:
        if not cliente.puedeTenerTarjetaDeCredito():
            return "Este tipo de cliente no puede tener tarjeta de credito"
        
        if cliente.total_tarjetas_credito<(evento.totalTarjetasDeCreditoActualmente+1):
            return "Tiene el maximo de tarjetas de credito permitidas"
        
        return "No se pudo determinar la causa de rechazo"