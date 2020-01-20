# Variables
var = 'Antes De Todo'
print(var.upper())
print(var.lower())
print(var.swapcase())    # CAMBIAN: MAYUS --> MINUS y MINUS --> MAYUS
print(var.capitalize())   # PONE LA 1RA LETRA MAYUSCULA, LOS DEMAS MINUSCULA
print(var.replace('Antes','Sobre'))  # CAMBIA Antes --> Sobre
print(var.replace('Todo','Algo').upper()) # CAMBIA Todo -> Algo y hace MAYUSCULA
print(var.count('o'))   # CUENTA LA LETRA 'o' EN var
# print(var.count(' ')) 
print(var.startswith('antes')) # PARA VER SI EMPIEZA CON 'antes'
# print(var.startswith('a'))  # PARA VER SI EMPIEZA CON 'a'
print(var.endswith('do'))  # PARA VER SI TERMINA CON 'Todo

print(var.split('e')) # DIVIDE var SEGUN APAREZCA 'e', 
                      # Y MUESTRA UNA LISTA DE STRINGS

print(var.find('o'))  # DEVUELVE LA POSICION DE 'o'
print(len(var))  # LONGITUD DEL STRING
print(var.index('e')) # VALOR DE LA POSICION DE 'e'

print(var[7])  # MUESTRA LA POSICION 7 de var
print(var[3])
print(var[10])
print(var[-4])

nomb = 'Alex'  
# LO SIGUIENTE MUESTRA LO MISMO
print('My name is ' + nomb) 
print(f'My names is {nomb}')
print('My name is {0}'.format(nomb))