from tarjetadeCreditoTarea import TarjetaCredito
class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = TarjetaCredito(0, 30000, .02)

    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)
        return self

    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self #Encadenacion de métodos
    
    def mostrar_saldo_usuario(self):
        print(f"Usuario:{self.nombre} {self.apellido}")
        self.tarjeta.mostrar_info_tarjeta()
