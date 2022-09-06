class ClienteClassic():
    def __init__(self,cliente):
        self.nombre = cliente['nombre']
        self.apellido = cliente['apellido']
        self.numero = cliente['numero']
        self.dni = cliente['dni']
        self.direccion = cliente['direccion']
        self.limite_extraccion_diario = 10000
        self.limite_transferencia_recibida = 150000
        self.costo_transferencias = 0.1
        self.saldo_descubierto_disponible =0
        self.total_tarjetas_credito =0
        self.total_chequeras =0
    

    def puedeCrearChequera(self):
        return False

    def puedeTenerTarjetaDeCredito(self):
        return False

    def puedeComprarDolar(self):
        return False

    def tieneCuentaCorriente(self):
        return False

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return True
