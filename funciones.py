def validador(Jugador):
    naci=int(input("Ingrese en que año nació el jugador:"))
    alt=int(input("Ingrese la altura del jugador en centimetros (ej:180,170):"))
    if naci >= 2010:
        return True
    if alt>= 180:
        return True
    return False

   


    

        