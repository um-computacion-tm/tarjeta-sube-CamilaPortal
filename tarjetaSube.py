
ACTIVADO= "activado"
DESACTIVADO= "desactivado"
PRECIO_TICKET = 70
PRIMARIO= "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"

DESCUENTOS = {
    PRIMARIO: 0.5,
    SECUNDARIO: 0.4,
    UNIVERSITARIO: 0.3,
    JUBILADO: 0.25,
}

class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario != None:
            precio = PRECIO_TICKET-(PRECIO_TICKET * DESCUENTOS[self.grupo_beneficiario])
        else:
            precio = PRECIO_TICKET

        return precio
    
    def pagar_pasaje(self):

        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException()
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        
        self.saldo -= self.obtener_precio_ticket()

    def cambiar_estado(self, estado):

        if estado == ACTIVADO or estado==DESACTIVADO :
            self.estado = estado           
        else:
            raise EstadoNoExistenteException()
