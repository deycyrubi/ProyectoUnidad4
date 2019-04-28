from Juego import* #Se importo la clase padre Juego
from random import*
"""Se importo la palabra reservada random, el cual permite crear una secuencia de números aleatorios """

class JuegoAdivinaNumero(Juego):
#Creamos la clase hija/subclase
    __NumeroAdivinar = int(0)
    __intentos = int(0)
#Se declaro los atributos del problema

    def __init__(self):
        super().__init__(3)
        """Se declaro la palabra reservada super la cual llamara
    al constructor de la clase padre"""
        self.__numeroAdivinar = randrange(10)

    def mostrarNumeroAdivinar(self): #Se declaro el método
        return self.__numeroAdivinar

    def mostrarRecord(self): #Se declaro el metodo
        return self.__intentos

    def ActualizaRecord(self): #Se declaro el metodo
        self.__intentos = self.__intentos + 1

    def reiniciaPartida(self):
    #Se declaro el metodo reinicia partida
        self.reiniciaRecord()
        self.__numeroAdivinar = randrange(10)
        self.__setVidas(3)
        self.Juega()

    def Juego(self): #Se implemento el metodo de la clase base
        while True:
            try:
                numero = int(input("Escribe el numero a adivinar: ")) #Muestra un mensaje
                if numero == self._numeroAdivinar:
                        print("¡Acertaste!")
                        self.ActualizaRecord()
                        break
                else:
                        if self.QuitaVida():
                            if numero > self._numeroAdivinar:
                               print ("Intentalo de nuevo. El múmero a adivinar es menor")
                            else:
                               print ("Intentalo de nuevo. El numero a adivinar es mayor")
                            self.ActualizaRecord()
                        else:
                         self.ActualizaRecord()
                        break
            except ValueError:
                print ("Escribe un numero")
            print("Tu record fue de: ", self.mostrarRecord())
            print ("El numero a adivinar era: ", self.mostrarNumeroAdivinar())







