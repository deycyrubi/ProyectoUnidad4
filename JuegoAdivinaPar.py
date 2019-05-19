from JuegoAdivinaNumero import*
from random import*

class JuegoAdivinaPar:
#Se identifico el nombre de la clase
#Creamos la clase de nuestro nuevo juego que consiste en adivinar si el numero es par o impar
    __NumeroPar = int(0)
    __NumeroImpar = int(0)
    __ValidaNumero =int(0)
    __a = int(0)
    """Hemos declarado nuestros atributos"""

    def __init__(self): #Se identifico el metodo constructor
        self.__NumeroPar
        self.__NumeroImpar

    def validaNumero(self):
        self.__ValidaNumero
        return 0

    a = 0
    a = int(input("Introduzca un número: ")) #Se declaro la acción a realizar

    if a%2 == 0: #Usamos el Modulo(%2) para saber si el numero es par o impar
      print("El numero: es par ")
    else:
      print("El numero:  es impar")



