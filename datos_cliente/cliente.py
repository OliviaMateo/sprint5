from datos_cliente.direccion import Direccion
from datos_cliente.cuenta import Cuenta
class Cliente(object):
    def __init__(self,cuenta):
        self.cuenta = cuenta(cuenta)
    
    def gestionarDatos(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['dni']
        self.direccion = Direccion(**datos['direccion'])
    
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

