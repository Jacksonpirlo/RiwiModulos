
texto1:str =""
texto2:str ="" 
texto3:str="" 
numero1:float=0.0 
numero2:float=0.0
promedioFinal = 0
sumList = 0
promedio = []
sumar:float =0 
texto1= str(input('Insert ratings: ')) + ","
if texto1 != " ":
    for i in texto1: 
        if i != ",":
            texto3 = texto3.__add__(i)
        else:
            numero:float = float(texto3)
            if numero > 0 and numero <= 100:
                texto3=""
                sumar = sumar + numero
                promedio.append(numero)            
            else:
                print('Numeros fuera de rango')
    for j in promedio:
            sumList += j
            promedioFinal = sumList / len(promedio)
if 

print(sumList)
print(promedioFinal)