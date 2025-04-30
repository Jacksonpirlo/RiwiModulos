puntos = int(input('Puntos: '))
puntoP= 0
puntoN = 0
puntoPV = 0
puntoNP = 0
for i in range(puntos):
    x = float(input(f'Ingrese x {i + 1}: '))
    y = float(input(f'Ingrese y {i + 1}: '))

    if x > 0 and y > 0:
        puntoP += 1
        print(f'X: {x} Y: {y}')
    elif x < 0 and y > 0:
        puntoN +=1
        print(f'X: {x} Y: {y}')
    elif x < 0 and y < 0:
        puntoPV += 1
        print(f'X: {x} Y: {y}')
    elif x > 0 and y < 0:
        puntoNP += 1
        print(f'X: {x} Y: {y}')
    else:
        print(f'Numeros = {x, y}. No se pueden encontrar los puntos en el cuadrante')
print(f'''

PUNTOS EN CUADRANTE 1: {puntoP}

PUNTOS EN CUADRANTE 2: {puntoN}

PUNTOS EN CUADRANTE 3: {puntoPV}

PUNTOS EN CUADRANTE 4: {puntoNP}


''')