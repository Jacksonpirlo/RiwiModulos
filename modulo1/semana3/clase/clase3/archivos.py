"""El siguiente código intenta sumar los precios de un diccionario, pero no funciona. Encuentra el error y corrígelo para que calcule correctamente el total.
python"""

"""El siguiente código intenta sumar los precios de un diccionario, pero no funciona. Encuentra el error y corrígelo para que calcule correctamente el total.
python"""

#precios = {"manzana": 1.5, "banana": 0.8, "pera": 1.2}
#total = 0
#for fruta, precio in precios:

# SOLUCION

#precios = {"manzana": 1.5, "banana": 0.8, "pera": 1.2}
#total = 0
#for precio in precios.values():
#    total = precio + total

#print(total)

#-------------------------------------------------

#usuario = {"nombre": "Ana", "edad": 30}
#print(usuario["ciudad"])

#usuario = {"nombre": "Ana", "edad": 30, "ciudad": "San cristobal"}
#print(usuario.get("ciudad"))

#-------------------------------------------------

#dic1 = {"a": 1, "b": 2}
#dic2 = {"b": 3, "c": 4}
#fusion = dic1 + dic2 
#print(fusion)

#dic1 = {"a": 1, "b": 2}
#dic2 = {"b": 3, "c": 4}
#sumaDic1 = dic1["a"] + dic1["b"]
#sumaDic2 = dic2["b"] + dic2["c"]
#fusion = sumaDic1 + sumaDic2
#print(fusion)

#-------------------------------------------------

#inventario = {"laptop": 5, "mouse": 10}
#inventario.update("laptop"=3)  
#print(inventario)

#inventario = {"laptop": 5, "mouse": 10}
#inventario["laptop"] = 6
#print(inventario)

"""Enunciado:
El siguiente código debería contar cuántas veces aparece cada palabra en una lista, pero no funciona correctamente. ¿Puedes encontrar el error y arreglarlo?
python"""

palabras = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print(contador)