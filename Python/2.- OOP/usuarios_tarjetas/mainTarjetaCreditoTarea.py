from tarjetadeCreditoTarea import TarjetaCredito


tarjetaVisa = TarjetaCredito(0,3000,0.02)
tarjetaMaestro = TarjetaCredito(0,3000,0.02)
tarjetaPlatinum = TarjetaCredito(0,5000,0.02)

#----- Acciones Tarjeta 1------
print("INICIO TARJETA VISA")
tarjetaVisa.compra(400),tarjetaVisa.compra(200),tarjetaVisa.pago(100),tarjetaVisa.cobrar_interes(),tarjetaVisa.mostrar_info_tarjeta()

#----- Acciones Tarjeta 2------
print("INICIO TARJETA MAESTRO")
tarjetaMaestro.compra(1000),tarjetaMaestro.compra(200),tarjetaMaestro.compra(200),tarjetaMaestro.pago(500),tarjetaMaestro.pago(500),tarjetaMaestro.cobrar_interes(),tarjetaMaestro.mostrar_info_tarjeta()

#----- Acciones Tarjeta 3------
print("INICIO TARJETA PLATINUM")
tarjetaPlatinum.compra(1000),tarjetaPlatinum.compra(500),tarjetaPlatinum.compra(500),tarjetaPlatinum.compra(1000),tarjetaPlatinum.compra(6500),tarjetaPlatinum.mostrar_info_tarjeta()


