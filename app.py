from vehiculo import Vehiculo
from escribiryleer import escribirObjeto,leerObjeto

car = Vehiculo('Ford','Fiesta','Blanco')
print(car)
escribirObjeto(car)

car2 = leerObjeto(repr(car))
print(car2)