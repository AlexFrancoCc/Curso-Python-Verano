#----****** USANDO While : Bucles finitos o infinitos
while True:
  num = int(input('Ingresa un numero entero para calcular su factorial: '))
  if num < 0:
      print('¡ERROR! El numero debe ser positivo o 0.')
  elif  num == 0: 
      print('0! = 1')
      break 
  else: 
    factorial = num  # Valor del factorial
    aux = num        # Variable que guarda el valor inicial del numero
    while num > 1:
      num -= 1
      factorial = factorial*num
    print(f'{aux}! = {factorial}')
    break

#****** FOR: Bucle finito
print('Primera forma de range:',end=' ')
for x in range(0,10):
  print(x, end=' ')   # POLIMORFISMOS
print()

print('Segunda forma de range:',end=' ')
for x in range(2,10,2):
  print(x,end=' ')          #  HACE CON SALTO DE LINEA
print()

print('Tercera forma de range:',end=' ')
for x in range(4,10,2):
  print(x, end=' ')   # HACE DE FORMA SEGUIDA
print()

print('Range en reversa:', end=' ')
for x in range(10,0,-1):
  print(x, end=' ')
print()

# range(x) = lista del 0 a x
# range(x,y) = lista de x (comienza en x) hasta y
# range(x,y,z) = lista de x hasta y de z en z

name = 'Aleexx'

for char in name:
    print(char, end=' ')
print()    # SALTO

#****** COLECCIONES: Sirven para guardar datos mas pequeños
#** LISTAS

lista = [1,2,True,3.0,'ALEX',[3,5,6,0]]
print(lista)

for x in lista:
  print(x,end=' ')
print()

print(lista[4])
print(lista[0:4])
print(lista[0:6:2])
print(lista[-1])  # MUESTRA EL ULTIMO DE lista
print(lista[-2:-8:-1])
lista.append('hola')  # AÑADE ELEMENTOS A LA LISTA
print(lista)
lista.pop(1)  # ELIMINA ELEMENTO
print(lista)



