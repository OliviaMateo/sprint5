class Cuenta(object):
    def __init__(self,  limite_extraccion_diario, limite_transferencia_recibida,   costo_transferencias,  saldo_descubierto_disponible,   total_tarjetas_credito,   total_chequeras):
        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.costo_transferencias = costo_transferencias
        self.saldo_descubierto_disponible =saldo_descubierto_disponible
        self.total_tarjetas_credito =total_tarjetas_credito
        self.total_chequeras =total_chequeras
