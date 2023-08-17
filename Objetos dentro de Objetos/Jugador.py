class Jugador:
    #construcor 
    def __init__(self, nombre, apellido, posicion):
        # atributos privados
        self.__nombre = nombre
        self.__apellido = apellido
        self.__posicion = posicion

    # Getter
    def get_nombre(self):
        return self.__nombre
    
    # Setter
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter
    def get_apellido(self):
        return self.__apellido
    
    # Setter
    def set_apellido(self, apellido):
        self.__apellido = apellido

    # Getter
    def get_posicion(self):
        return self.__posicion
    
    # Setter
    def set_posicion(self, posicion):
        self.__posicion = posicion
    
    def dar_pase(self, jugador):
        print(self.__nombre, self.__apellido, "le dio un pase a", jugador.get_nombre(), jugador.get_apellido())

    def hizo_gol(self):
        print(self.__nombre, self.__apellido, "marco un gol")
        print("")