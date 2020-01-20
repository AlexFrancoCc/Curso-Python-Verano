# Funciones integradas en python Falta
# Se vio sobre Tipado Estatico y Dinamico  (Fuerte y Debil)
#----------------------------------------------------
# Clase:
# name = 'Aleexx'
# print(len(name))
# print(name, 'is', age, 'years old.')
# print('{} is {} years old.' .format(name,age))
# print(f'{name} is {age} years old.')
#-------------------------------------------------
v = 5 < 3  #  La proposicion resulta Falso
print(v)
v = 3 > 1
print(v)
print(type(v))
#------------------------------------------------
# Usando and, or
v = 5 < 10 and 3 > 5
print(v)
w = 5 < 10 or 3 > 5
print(v)
z = (not 5 < 10) or 3 > 5
print(z)

#-------------------------------------------------------------------------
# Estructuras de control de seleccion: Condicionales
name = input('What\'s your name: ')   # Ver sobre caracteres de escape \'
age = int(input(f'Hi {name}, how old are you? '))

if age < 0:
    print('Error! An age can\'t be negative. \n')
elif age < 18:
    print('You\'ll not pass \n')
else:
    print('You are allowed to pass \n')

# Ejemplo2: Sobre el area del circunferencia ******
import math
print('*** Area del circulo***')
Radio = float(input('Ingrese el radio: '))
if Radio <= 0 :
  print('Error! para una radio de circunferencia')
else:
  print('Valor de pi: ', math.pi)
  Area = float(math.pi*(Radio**2))
  print('El area del circulo es: ',Area) 
#------------------------------------------
# Funciones Integradas (siguiendo del principio)
char = input('Type a letter: ')
print(char)
print(char.lower())   # Se pone .lower para poner la letra en minuscula
print(char.upper())   # Se pone .lower para poner la letra en mayuscula
#***** Nota: Cantidad de caracteres en el horizontal debe ser 80
# Ejemplo3: Ingresar una letra   *******
char = input('Type a letter: ')
#Nc = len(char)
if len(char) == 1:     # Se utiliza == para comparar
  print('It\'s a letter: ',char)
else:
  print('It\'s not a letter!')







