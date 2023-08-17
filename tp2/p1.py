class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

def __str__(self):
    return f'El nombre d la persona es {self.nombre}, el apellido es {self.apellido} y su edad es {self.edad}'

if __name__ == '__main__':
    benja = Persona('benjamin','jorge',20)
    edgardo = Persona('Edgardo','Alderete', 20)

    print(__str__(edgardo))
    print(__str__(benja))