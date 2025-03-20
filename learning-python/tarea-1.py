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