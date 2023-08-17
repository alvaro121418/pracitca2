class Persona:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    # Getter
    @property
    def nombre(self):
        return self.__nombre
    
    # Setter
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def mostrar(self):
        print("Nombre: ", self.nombre)

    # Sirve para mostrar los datos del objeto sin llamar a una funcion aparte
    def __str__(self):
        cadena = "Nombre: "

        cadena += self.nombre

        return cadena

if __name__ == "__main__":
    pers1 = Persona("Pablo")
    print(pers1) # Aqui se usa el __str__
    pers1.mostrar() # Aqui se usa un metodo que muestra los datos 