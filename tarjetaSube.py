
ACTIVADO= "activado"
DESACTIVADO= "desactivado"
PRECIO_TICKET = 70
PRIMARIO= "primario"

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

        if self.grupo_beneficiario == None:
            precio = PRECIO_TICKET
        
        if self.grupo_beneficiario == PRIMARIO:
            precio = (PRECIO_TICKET*0.5)

        return precio
    
    def pagar_pasaje(self):

        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()

        if self.grupo_beneficiario == None:
            if self.saldo < PRECIO_TICKET:
                raise NoHaySaldoException()
            else:
                self.saldo -= PRECIO_TICKET

        if self.grupo_beneficiario == PRIMARIO:
            if self.saldo < (PRECIO_TICKET*0.5):
                raise NoHaySaldoException()
            else:
                self.saldo -= (PRECIO_TICKET*0.5)

    def cambiar_estado(self, estado):

        if estado == ACTIVADO or estado==DESACTIVADO :
            self.estado = estado           
        else:
            raise EstadoNoExistenteException()
