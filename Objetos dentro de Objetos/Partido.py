class Partido:
    def __init__(self, equipo_local, equipo_visitante, arbitro):
        self.__equipo_local = equipo_local # Un objeto de la clase Equipo
        self.__equipo_visitante = equipo_visitante # Un objeto de la clase Equipo
        self.__arbitro = arbitro # Un objeto de la clase Arbitro
        self.__marcador_local = 0
        self.__marcador_visitante = 0

    # Getter
    def get_equipo_local(self):
        return self.__equipo_local
    
    # Getter
    def get_equipo_visitante(self):
        return self.__equipo_visitante

    # Getter
    def get_marcador_local(self):
        return self.__marcador_local
    
    # Getter
    def get_marcador_visitante(self):
        return self.__marcador_visitante

    # Getter
    def get_arbitro(self):
        return self.__arbitro

    def incrementar_marcador_local(self):
        self.__marcador_local += 1

    def incrementar_marcador_visitante(self):
        self.__marcador_visitante += 1

    def iniciar_partido(self):
        print("Inicio la final del mundo")

    def finalizar_partido(self):
        print("Finalizo la final del mundo")

    def __str__(self):
        cadena = str(self.get_equipo_local()) + ": " + str(self.get_marcador_local())
        cadena +=  " - "
        cadena += str(self.get_equipo_visitante()) + ": " + str(self.get_marcador_visitante())
        cadena += "\n"

        return cadena