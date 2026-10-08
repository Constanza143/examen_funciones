from funciones import validador
jugador=[]
print("Bienvenido a el validador de edad y altura")
nombre=int(input("Ingrese el apellido del jugador:"))
jugador.append(nombre)
resultado=validador(jugador)
if resultado:
    print("Nacio en 2010 o más")
    print("Altura mayor o igual a 180")
else:
    print("No cumple ninguno de los parametros, intente de nuevo más adelante")
