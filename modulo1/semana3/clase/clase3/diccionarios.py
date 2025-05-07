import math as matematica
print(matematica.sqrt(16))

team_leader1 = {
    "name": "Sebastian",
    "lastName": "puente",
    "edad": 37
}

team_leader2 = {
    "name": "Miguel",
    "lastName": "Torres",
    "edad": 25
}

coder = {
    "name": "Miguel",
    "lastName": "Torres",
    "edad": 25,
    "notas": [5,8,9,]
}


print(team_leader1["name"])
print(team_leader2.get("edad"))
print(coder["notas"][2])

for valor in coder.values():
    print(valor)

for clave in coder.keys():
    print(clave)