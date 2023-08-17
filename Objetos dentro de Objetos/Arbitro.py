class Arbitro:
    def __init__(self, nombre, apellido, tipo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipo = tipo

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
    def get_tipo(self):
        return self.__tipo

    def convalido_gol(self):
        print(self)
        print("Convalido el gol")
        print("")

    def __str__(self):
        cadena = "Arbitro " + self.__tipo + "\n"
        cadena += "Nombre completo: " + self.__nombre + " " + self.__apellido

        return cadena
            