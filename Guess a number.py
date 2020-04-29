# El siguiente código tiene como función adivinar el número, entre 0 y 20, que el usuario introduzca.

from random import randint

num1 = randint(0,20)        #Número randóm entre 0 y 20 
loop = False                #Variable para el while

def AdivinaElNumero():
    print('\n            -----------------ADIVINA UN NÚMERO-----------------\nEl siguiente juego tiene por objetivo adivinar un número entero al azar entre 0 y 20. Sin embargo, solo posees 5 intentos para completar el juego.\n')
    print('¿Qué quieres hacer? Escribe el número que corresponda con tu opción.')
    while True:
        try:
            a = int(input('1) Adivinar un número\n2) Salir\nColoca tu respuesta aquí: '))
            if a == 2:
                return print('\n                -----------------GRACIAS POR JUGAR-----------------')
            if a < 1 or a > 2:
                raise ValueError
            break
        except ValueError:
            print('----------------------------\n')
            print('Debes ingresar la opción 1, o la opción 2')
            return AdivinaElNumero()
    guess = 0
    while  guess < 5:
        while True:
            try:
                num2 = int(input('Ingrese un número entero entre 0 y 20: '))
                if type(num2) != int: 
                    raise ValueError
                break
            except ValueError:
                print('----------------------------\n')
                print('¡ATENCIÓN, DEBES INGRESAR UN NÚMERO ENTERO ENTRE 0 Y 20!\n')
        if num2 > 20:
            print('----------------------------\n')
            print('¡ATENCIÓN, NO PUEDES INGRESAR UN NÚMERO MAYOR A 20!\n')
            guess = guess - 1
        elif 0 > num2:
            print('----------------------------\n')
            print('¡ATENCIÓN, NO PUEDES INGRESAR UN NÚMERO MENOR A 0!')
            guess = guess -1
        elif num1 < num2:
            print('----------------------------\n')
            print('Tu número está por encima del objetivo')
        elif num1 > num2:
            print('----------------------------\n')
            print('Tu número está por debajo del objetivo')
        elif num1 == num2:
            print('----------------------------\n')
            print('     ----------¡FELICIDADES,',num2,'es el número correcto!----------')
            break
        guess = guess + 1
        if guess == 5:
            return print('\n    -----------------GAME OVER: Utilizaste tus 5 intentos-----------------')
    while True:    
        try:
            b = int(input('Escribe 0 para salir, o 1 para jugar de nuevo: '))
            if b == 0:
                return print('\n            -----------------GRACIAS POR JUGAR-----------------')
            elif b == 1:
                return AdivinaElNumero()
            if b < 0 or b > 1:
                raise ValueError
            break
        except ValueError:
            print('----------------------------')
        
AdivinaElNumero()           

