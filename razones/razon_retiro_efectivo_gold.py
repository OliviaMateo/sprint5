from datos_cliente.cliente import Cliente
from evento import Evento

class RazonRetiroEfectivoGold():
    def __init__(self) -> None:
        pass
    
    def resolver(self, cliente:Cliente,evento:Evento) -> str:
        if cliente.limite_extraccion_diario<evento.monto:
            return "La extraccion supera el monto de extraccion permitido"

        if evento.monto>(evento.saldoEnCuenta):
            return "Saldo Insuficiente para retiro solicitado"
        
        if evento.monto>(evento.cupoDiarioRestante):
            return "Con esta estraccion superaria el cupo diario permitido por dia"
        
        return "No se pudo determinar la causa de rechazo"