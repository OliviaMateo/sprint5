from datos_cliente.cliente import Cliente
from evento import Evento


class RazonAltaChequera():
    def __init__(self) -> None:
        pass
    def resolver(self,cliente:Cliente,evento:Evento)-> str:
        if not cliente.puedeCrearChequera():
            return "Tipo de cliente sin acceso a chequeras"
        
        if cliente.total_chequeras<(evento.totalChequerasActualmente+1):
            return "Maximo de cheuqueras permitidas"
        
        return "No se pudo determinar la causa de rechazo"