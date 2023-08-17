"""
    Primera forma de importar -> import ...
"""

# import operaciones

# print(operaciones.sumar(2,5))

"""
    Segunda forma de importar -> from ... import ...
"""

# from operaciones import restar as r, sumar as s

# print(s(5,4))
# print(r(5,4))


"""
    Si tengo archivos dentro de carpetas -> from ... import ...
"""
# from mi_carpeta.otras_operaciones import multiplicar
# print(multiplicar(3, 2))

"""
    Si tengo archivos dentro de carpetas -> import ...
    Para este caso si o si debe tener un ALIAS, en los casos anteriores es opcional el ALIAS
"""

import mi_carpeta.otras_operaciones as archivo # Si tenemos carpetas, debemos colocarle si o si un ALIAS
print(archivo.dividir(5, 2))