nombre = 'Alex Ccoyllo'
#  print(nombre.title())
#  print('En Mayusculas:',nombre.upper())
#  print('En minusculas:',nombre.lower())
#  nombre = 'Alex'
#  apellido = 'Ccoyllo'
#  nombre_completo = nombre + ' ' + apellido
#  print(nombre_completo)
#  mensaje = 'Hola, ' + nombre_completo.title() + '!'
#  print(mensaje)
#  print('Lenguajes:\nPython\nJavaScript')  # \n es el salto de linea
#  lenguaje = ' python '
#  print(lenguaje.rstrip())   #-------------------------------------------
#  print(lenguaje.lstrip())   # Eliminan los espacios en blanco en lenguaje
#  print(lenguaje.strip())    #--------------------------------------------

#  edad = 23
#  mensaje = 'Feliz ' + edad + 'º aniversario3'
#  print(mensaje)       # DA ERROR!

#  edad = 23
#  mensaje = 'Feliz ' + str(edad) + 'º aniversario'
#  print(mensaje)       # DEBEN SER TIPO STRING en la variable mensaje

# Para obtener paquetes
#  import math as mt  # Cargar el paquete

#  print(mt.pi)

#  x=3
#  y=8
#  print(mt.sqrt(x*x+y*y))

#  res = mt.pi*2**3 - mt.sqrt(4)
#  print(res)

## LISTAS : Se encierran en corchetes
#===========================
bicicletas = ['trek','cannondale','redline','specialized'] # La lista comienza en cero
mensaje = 'Mi bicicleta fue una ' + bicicletas[0].title() + '.'
print(mensaje)
mensaje = 'Mi bicicleta fue una ' + bicicletas[2].title() + '.'
print(mensaje)

# Modificando lista 
motocicleta = ['honda','yamaha','suzuki']
print(motocicleta)
motocicleta[0] = 'ducati'    # Se reemplaza la posicion 0 por 'ducati'
print(motocicleta)
 
 # Agregar una entrada a una lista
motocicleta = ['honda','yamaha','suzuki']
motocicleta.append('ducati')   # Se agrega al final 'ducati' a motocicleta
print(motocicleta)

# Lista vacia : Se añade elementos con .append
motocicleta = []
motocicleta.append ('honda')
motocicleta.append('yamaha')
motocicleta.append('suzuki')
print(motocicleta)

# Insertando en una lista en una posicion con .insert
meses = ['Enero','Marzo','April']
print(meses)
meses.insert(1,'Febrero')  # Inserta Febrero en la pos 1
print(meses)

# Borrando elementos de una lista con 'del' 
meses = ['Marzo','Abril','Agosto','Diciembre']
print(meses)
del meses[1]     # SE QUITA LA POSICION 1 DE LA LISTA
print(meses)

# El comando para eliminar el ultimo elemento de la lista
cursos = ['Geomet','Algebr','Aritmet','Comunica']
print(cursos)
Ult_element = cursos.pop()  # SE ELIMNA ULTIMO ELEMENTO CON .POP
print(Ult_element)
print(cursos)
 # Para eliminar un elemento en una posicion de una lista
segundo_elemento = cursos.pop(1)  # Quita la posicion 1 de la lista
print('Segundo curso:',segundo_elemento)
print(cursos) 

# Remover un elemento de una lista (Quita de la lista)
Artefactos = ['Refrig','TV','Radio','Libros','Laptop','Platos']
muy_cara = 'Laptop'
Artefactos.remove(muy_cara)  # Remueve de la lista 'Laptop'
print(Artefactos)
print('\nUna ' + muy_cara.title() + ' es un Artefacto muy caro.') 

# ORDENANDO UNA LISTA
carros = ['BMW','AUDI','TOYOTA','SUBARU']
print(carros)
carros.sort()  # SE ORDENA LA LISTA CON .SORT 
print(carros)
#-- SE REORDENA LA LISTA DEL ULTIMO AL PRIMERO
carros.sort(reverse=True)  # SE COLOCA LA LISTA EN REVERSO
print(carros)
#-- LONGITUD DE UNA LISTA CON LEN
len(carros)
print(len(carros))
