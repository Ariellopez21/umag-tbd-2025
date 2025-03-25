# Autor: Ariel López S.

# Modulos
import random, string

# N°1
def calculadora(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return f"{a / b:.3f}"
    else:
        return 'Operación inválida'
    
print("N°1: ", calculadora(2, 3, '/'))

# N°2
def retorna_diccionario(str):
    palabras = str.split()
    dic = {}
    for i in range(len(palabras)):
        dic.update({palabras[i]: i + 1})
    return dic
print("N°2: ", retorna_diccionario('Hola mundo'))

# N°3
def palindromo(str):
    str = str.lower()
    str = str.replace(' ', '')
    for i in range(len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

print("N°3: ", palindromo('Anita lava la tina'))

#N°4
def RandPasswd(len=8, mayus=True, num=True, special=True):
    passwd = []
    select = ['minus', 'mayus', 'num', 'special']

    for i in range(len):
        if mayus == True and random.choice(select) == 'mayus':
            passwd.append(random.choice(string.ascii_uppercase))
        elif num == True and random.choice(select) == 'num':
            passwd.append(str(random.randint(0, 9)))
        elif special == True and random.choice(select) == 'special':
            passwd.append(random.choice(string.punctuation))
        else:
            passwd.append(random.choice(string.ascii_lowercase))
    return "".join(passwd)

print("N°4: ", RandPasswd())

#N°5
def ConvertCelciusToFahrenheit(C):
    return ((9 / 5) * C) + 32

print("N°5: ", ConvertCelciusToFahrenheit(0))

#N°6
def FibRecursv(n):
    if n <= 1:
        return n
    else:
        return FibRecursv(n - 1) + FibRecursv(n - 2)

def FitIter(n):
    if n <= 1:
        return n
    f0 = 0
    f1 = 1
    for i in range(2, n + 1):
        f1 = f0 + f1
        f0 = f1 - f0
    return f1

print("N°6: ", FibRecursv(7))
print("N°6: ", FitIter(7))

#N°7
def StringCountVowelAndCons(str):
    str = str.lower()
    v = "aeiou"
    c = "bcdfghjklmnpqrstvwxyz"
    count = [0,0]
    for i in str:
        if i in v:
            count[0] += 1
        elif i in c:
            count[1] += 1
    return count

print("N°7: ", StringCountVowelAndCons("HOLA mundo VaMos a Programar!"))

#N°8
def Adivinador():
    num = random.randint(1, 100)
    n = int(input("¡Adivina en qué número estoy pensando!\n Ingresa un número entre 1 y 100:"))
    while True:
        if n == num:
            print("¡Wow! Me has superado. ¡Ganaste!")
            return
        elif n > num:
            print("¡Síguelo intentando! Estás muy alto.")
        else:
            print("¡Síguelo intentando! Estás muy bajo.")
        n = int(input("Ingresa otro número:"))

print("N°8:")
Adivinador()