class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugadores = [] # Una lista de objetos de la clase Jugador

    def get_nombre(self):
        return self.__nombre

    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)

    def __str__(self):
        cadena = self.__nombre
        
        return cadena