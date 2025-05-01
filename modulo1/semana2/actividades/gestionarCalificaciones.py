texto1: str = ""
texto2: str = ""
numero1: float = 0.0
numero2: float = 0.0
promedioFinal = 0
pasarOno: float = 65.00
numRepetido = 0
sumList = 0
promedio = []
conteo = {}

texto1 = str(input('Insert ratings: ')) + ","

if texto1 != " ":
    for i in texto1:
        if i != ",":
            texto2 = texto2.__add__(i)
        else:
            numero: float = float(texto2)
            if numero > 0 and numero <= 100:
                texto2 = ""
                promedio.append(numero)
            else:
                print('Numeros fuera de rango')

    for j in promedio:
        sumList += j
        promedioFinal = sumList / len(promedio)

    valorEspesifico = float(input('Ingrese un valor espesifico: '))
    if valorEspesifico > 0 and valorEspesifico <= 100:
        for k in promedio:
            if k > valorEspesifico:
                print(f'''{k} es mayor que {valorEspesifico}
''')

for x in promedio:
    if x in conteo:
        conteo[x] += 1
    else:
        conteo[x] = 1

for numero, veces in conteo.items():
    print(f'''La nota {numero} aparece {veces} veces.''')

if promedioFinal >= pasarOno:
    print(f'''

          BOLETIN DE NOTAS

Felicidades! pasaste. Aqui tienes mas informacion sobre tus notas:

           Tus notas: {promedio}
           
           Lo que necesitabas para pasar: {pasarOno}
           Lo que sacaste: {promedioFinal}

''')
else:
    print(f'''
          
          BOLETIN DE NOTAS
     
     Lo sentimos, no tuviste el desempeno sufuciente para pasar:

           Tus notas: {promedio}

           Lo que necesitabas para pasar: {pasarOno}
           Lo que sacaste: {promedioFinal}
     
''')
