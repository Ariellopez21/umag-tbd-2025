try:
    pass
    #a = 10 / 0
# Soporta múltiples excepciones
except (KeyError, ZeroDivisionError):
    print('Error')

else: 
    print('Todo bien')

#raise Exception('Mi Error')