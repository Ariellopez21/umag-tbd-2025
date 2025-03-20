print("Hola mundo!")

x = 0

# LISTAS
mi_lista = [1,2,4,6,5]

for i in mi_lista:
    print(i, end=" ")

print()

mi_lista.extend([7,8,9])

print(mi_lista)

print(mi_lista[3:-3])

# TUPLAS: Son fijas.

mi_tupla = (1,2,3,4,5)

for e in mi_tupla:
    print(e, end=" ")

# CONJUNTOS: No se pueden repetir elementos. No se puede agregar listas ni tuplas.
# Usa Union, Intersection, etc...

mi_conjunto = {1,2,3,4,5,6,7,8,9,10}

# DICCIONARIOS: Son como los JSON. Son clave-valor.
print()
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
# print(mi_diccionario)
# print("Nombre = ", mi_diccionario["nombre"])
# print("GET = ", mi_diccionario.get("nombre"))
# print(mi_diccionario.keys())
# print(mi_diccionario.values())

#for k in mi_diccionario.keys():
    # print(k, end=" ")
#print()

#for k in mi_diccionario.keys():
    # print(k, mi_diccionario[k], end=" ")
#print()

#for k, v in mi_diccionario.items():
    # print(k, v, end=" ")
#print()

#for i, e in enumerate(mi_lista):
    #print(i, e)

# LISTA POR CONTENCION

mis_numeros = [1, 2, 3, 4, 5]

mis_cuadrados = [n*n for n in mis_numeros if n % 2 == 0]
#print(mis_cuadrados)

mis_letras = ["a", "b", "c", "d", "e"]
mis_letras_mayusculas = [l.upper() for l in mis_letras]
#print(mis_letras_mayusculas)

# STRINGS

mi_texto = "Hola mundo!"

#print(mi_texto.split())
mi_texto = mi_texto.split()
#print("*".join(mi_texto))

# FSTRINGS: Formateo de strings, soportan interpolaciones.

nombre = "Juan"
mi_fstring = f"Hola {nombre}. \n{2**8} \t {"Mi texto"}"
#print(mi_fstring)
mi_fstring_debugger = f"{nombre=}."
#print(mi_fstring_debugger)

# FUNCIONES

def sum(a, b):
    '''
    Esta es la documentacion de la funcion.
    :param: a: Primer Argumento
    '''
    return a + b

def aplica_fn(valores, fn):
    return [fn(valores)]
print()
print(aplica_fn([1,2,3,4,5], lambda x: x+x))

# Un * es para listas y dos ** para diccionarios.
def test(a, b, **kwargs):
    print(a, b, kwargs)

mi_a = {"A": 1, "B": 2, "C": 3, "D": 4}
test(**mi_a)