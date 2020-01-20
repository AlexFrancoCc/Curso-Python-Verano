# while 6 > 5:
#    print('hello world')
# Lo anterior hace sin detenerse

# Factorial de un numero de forma
# descendente

num = int(input('Ingresa un numero entero para calcular su factorial'))
factorial = num    # Valor del factorial
auxiliar = num   # Variable que guarda el valor inicial del numero

while num > 1:
    num -= 1
    factorial = factorial + num
    
