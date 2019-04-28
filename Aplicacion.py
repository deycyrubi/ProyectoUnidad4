from JuegoAdivinaNumero import *

def main():
    juego = JuegoAdivinaNumero()
    juego.Juega()
    juego.JuegoAdivinaPar

    while True:
        reiniciar = input("¿Deseas volver a jugar (S/N?) ")
        if reiniciar == "S":
            juego.reiniciaPartida()
        else:
            break

if __name__ == '__main__':
    main()
