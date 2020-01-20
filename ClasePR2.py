## CICLOS FOR
#----------------------------------------------------------
magos = ['alice','david','carolina']
for m in magos:
    print(m)    # MUESTRA CDA ELEMENTO
# Bloque de ejecucion
magos = ['alice','david','carolina']
i=0
for m in magos:
   print(m)            #--  SE USA IDENTACION
   i=i+1               #--
   print(i)
print('ESTO ESTA FUERA DEL CICLO')

# LISTAS NUMERICAS
for i in range(1,5):   # EL conteo comienza en i=0 y termina i=4
   print(i)
# EJEMPLOS
lista_numeros = list(range(1,6))      # SE HACE LISTA CON LIST
print(lista_numeros)
lista_pares = list(range(2,100,2)) 
print(lista_pares)

lista_cuadrados = []
for i in range(1,11):
    cuadrado = i**2
    lista_cuadrados.append(cuadrado)
print(lista_cuadrados)

digitos = list(range(1,11))  # lista de numeros de 1 a 10
minimo = min(digitos)
maximo = max(digitos)
suma = sum(digitos)
media = suma/len(digitos)
print(minimo,maximo,media)

equipos = ['BayerMunich','Liverpol','RealMadrid','Juventus','BocaJuniors','PSG']
print(equipos[0:3])
print(equipos[1:2])
print(equipos[1:4])
print(equipos[:2])
print(equipos[4:])
print(equipos[-4:])

#--- COPIANDO UNA LISTA  (DIFERENCIA DE [:] SIN [:])
comidas = ['pizza','faladel','carrot cake']
comidas2 = comidas[:]         # SE COPIA LA LISTA COMIDAS
comidas.append('cannoli')     # COMIDAS2 NO VIENE A SER LO MISMO QUE COMIDAS
comidas2.append('ice cream')
print('\nMis comidas favoritas son:')
print(comidas)
print('Mis comidas favoritas son:')
print(comidas2)

comidas = ['pizza','faladel','carrot cake']
comidas2 = comidas            #** EN ESTE CASO  SON LA MISMA VARIABLE 
comidas.append('cannoli')     #** SON EL MISMO PUNTERO
comidas2.append('ice cream')
print('\nMis comidas favoritas son:')
print(comidas)
print('Mis comidas favoritas son:')
print(comidas2)

##---- TUPLAS: LISTAs QUE NO CAMBIAN, se usa ()
datos = (200,4,'ar')
print(datos[0])
print(datos[1])
print(datos[2])
 # datos(2) = 500   ** SALE ERROR ****