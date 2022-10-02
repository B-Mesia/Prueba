def numero(literal, inferior, superior):
   while True:
      valor=input(literal)
      while(not valor.isnumeric()):
         print("Solo se adminten números entre {0} y {1}".format(inferior,superior))
         valor=input(literal)
      coor=int(valor)
      if(coor>=inferior and coor<=superior):
         return coor

      else:
         print("El valor indicado es incorrecto, introduzca un número entre {0} y {1}".format(inferior,superior))

jugadores=[2]
numeroJugadores=numero("Numero de jugadores: ",0,2)
for i in range(numeroJugadores):
   jugadores.append({"nombre":input("Nombre del jugador "+str(i+1)+": "),"tipo":"H"})
for i in range(numeroJugadores):
   jugadores.append({"nombre":"Maquina "+str(i+1),"tipo":"M"})
   
   player =input("Ingrese rol Jugador 1:\n ==>")
if player == 'Camarada':
    print("El jugador A posee el rol Camarada, por lo que el jugador B poseerá el de Ondulado")
elif player == 'Ondulado':
    print('El jugador A posee el rol Ondulado, por lo que el jugador B poseerá el de Camarada')
import random

comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador A')
else:
    print('Comienza el jugador B')

import random

fixed_digits = 6
num = random.randrange(111111, 999999, fixed_digits) 
def isUndulating(num):
    if num <= 2:
        return False

    for i in range(2, len(num)):
        if (num[i - 2] != num[i]):
            return False

    return True
 

    
if (isUndulating(num)):
    print("Yes")
else:
    print("No")
 

 
 

    