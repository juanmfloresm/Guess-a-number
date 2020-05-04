import random
import time


def RPS():
    
    while True:
        print('\n\n                                              -----PIEDRA, PAPEL O TIJERA-----\n')
        print('Para poder ganar en el famoso juego de PIEDRA, PAPEL O TIJERA, debes ganarle a tu oponente en 3 oportunidades, si lo consigues, LA VICTORIA será tuya. ¡ÉXITOS!\n')
        try:
            b = int(input('¿Qué quieres hacer?\n   1. Jugar\n   2. Salir\n     Su respuesta: '))
            if b == 1:
                return RPS1()
            if b == 2:
                return print('\n                    -----GRACIAS POR JUGAR. VUELVE PRONTO-----')
            if  b < 1 or b > 2:
                raise ValueError
            break
        except ValueError:
            print('\n------------------------------')
            print('Ingresa 1 para Jugar o 2 para Salir.')
            print('------------------------------\n')
            time.sleep(2)
def RPS1():
    global nombre
    print('\n------------------------------')
    nombre = str(input('Por favor, ingrese su nombre: '))
    RPS2()
    
def RPS2():
    c = 0           # Victorias de la computadora
    h = 0           # Victorias del humano
    while h < 3 or c < 3:
        List1 = ['Piedra', 'Papel', 'Tijera']        #Lista random que usará la computadora.
        computer = random.choice(List1)
        #print(computer)    
        while True:
            try:
                print('\n------------------------------')
                a = int(input('Escoja una de las siguientes opciones:\n   1. Piedra\n   2. Papel\n   3. Tijera\n   Su respuesta: '))
                if  a < 1 or a > 3:
                    raise ValueError
                break
            except ValueError:
                print('\n------------------------------')
                print('Para elegir debe ingresar: 1 para Piedra, 2 para Papel o 3 para Tijera')
                print('------------------------------\n')
                time.sleep(2)
        if a == 1:
            human = 'Piedra'
            # print(human)
        elif a == 2:
            human = 'Papel'
            # print(human)
        else:
            human = 'Tijera'
            # print(human)
        if human == computer:
            c = c
            h = h
            print('\n------------------------------')
            print('          -----¡EMPATE! Ambos escogieron',human,'-----\n              -----Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        elif human == 'Piedra' and computer == 'Papel':
            c = c + 1
            h = h
            print('\n------------------------------')
            print('          -----¡PERDISTE! La computadora escogió',computer,'y usted',human,'-----\n                        ----- Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        elif human == 'Piedra' and computer == 'Tijera':
            c = c 
            h = h + 1
            print('\n------------------------------')
            print('          -----¡GANASTE! La computadora escogió',computer,'y usted',human,'-----\n                        ----- Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        elif human == 'Papel' and computer == 'Tijera':
            c = c + 1
            h = h
            print('\n------------------------------')
            print('          -----¡PERDISTE! La computadora escogió ',computer,'y usted',human,'-----\n                        ----- Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        elif human == 'Papel' and computer == 'Piedra':
            c = c
            h = h + 1
            print('\n------------------------------')
            print('          -----¡GANASTE! La computadora escogió',computer,'y usted',human,'-----\n                        ----- Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        elif human == 'Tijera' and computer == 'Papel':
            c = c
            h = h + 1
            print('\n------------------------------')
            print('          -----¡GANASTE! La computadora escogió',computer,'y usted',human,'-----\n                        ----- Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        else:
            c = c + 1
            h = h
            print('\n------------------------------')
            print('          -----¡PERDISTE! La computadora escogió',computer,'y usted',human,'-----\n                        ----- Computadora',c,'vs',nombre,h,'-----')
            time.sleep(2)
        if h == 3:
            print('\n\n               -----¡GANASTE EL JUEGO, FELICITACIONES',nombre,':)!-----')
            time.sleep(2)
            break
        if c == 3:
            print('\n\n               -----¡PERDISTE EL JUEGO, LO SIENTO',nombre,';(!-----')
            time.sleep(2)
            break
    while True:
        try:
            denuevo = int(input('\n¿Quieres volver a Jugar?\n   1. Sí\n   2. No\n   3. ¿Quieres cambiar de nombre?\n   Su respuesta: '))
            if denuevo == 1:
                return RPS2()
            elif denuevo == 2:
                print('\n                    -----GRACIAS POR JUGAR. VUELVE PRONTO-----')
                return time.sleep(2)
            else:
                return RPS1()
            if denuevo < 1 or denuevo > 3:
                raise ValueError
            break
        except ValueError:
            print('\n------------------------------')
            print('Ingresa 1 para volver a jugar,  2 para salir o 3 para cambiar de nombre.')
            print('------------------------------\n')
            time.sleep(2)

            
RPS()
