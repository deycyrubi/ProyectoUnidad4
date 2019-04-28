import abc
from abc import ABCMeta
"""Se declara el metodo abstracto abc"""

class Juego(ABCMeta):  #Declaramos nuestra clase padre/base
    __numeroAdivinar = int(0)
    __vidas = int (0)
    __numero = int(0)
    __AdivinarNumero = int(0)
#Se identificaron los atributos

    def __init__(self,vidas): #Se declaro el metodo constructor
        self._vidas = vidas
        __metaclass__ = ABCMeta #Metaclase

    def __init__(self,numeroAdivinar,vidas):
        self.__numeroAdivinar = numeroAdivinar
        self.__vidas = vidas

    def QuitaVida(self): #Se declaro el metodo
        self._vidas=self.__vidas-1
        if self.__vidas >0:
            return True
        else:
            return False

    def Juega(self):
        return 0

    def ValidaNumero(self):
        return self._ValidaNumero

    def AdivinarNumero(self):  #Se declaro el metodo que lleva por nombre la accion a realizar
        while  self.__vidas !=0:
          numero = int(input('Introduce el numero: '))
          if  (numero ==self.__numeroAdivinar):
             print ('Felicidades, le atinaste!!!')
             break
        else:
             self.__vidas = self.__vidas-1
             print('Intentalo otra vez')


#Primer metodo decorador para clases abstractas
@abc.abstractmethod
def setName(self, name):
        self.name = name

#Segundo metodo
@abc.abstractmethod
def getname(self):
        return self.name








