class ClienteBlack():
    def __init__(self,cliente):
        self.nombre = cliente['nombre']
        self.apellido = cliente['apellido']
        self.numero = cliente['numero']
        self.dni = cliente['dni']
        self.direccion = cliente['direccion']
        self.limite_extraccion_diario = 100000
        self.limite_transferencia_recibida = 900000**100
        self.costo_transferencias =0
        self.saldo_descubierto_disponible =0
        self.total_tarjetas_credito =5
        self.total_chequeras =2

    def puedeCrearChequera(self):
        return True

    def puedeTenerTarjetaDeCredito(self):
        return True

    def puedeComprarDolar(self):
        return True

    def tieneCuentaCorriente(self):
        return True

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return False