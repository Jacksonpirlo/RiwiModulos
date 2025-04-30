triangulos = int(input('Triangulos: '))
temp = 0
for i in range(triangulos):
    base = float(input(f'Ingrese base {i + 1}: '))
    altura = float(input(f'Ingrese base {i + 1}: '))
    area = (base * altura) / 2
    print(area)

    if area > 12:
        temp += 1
        print(temp)
        
print(temp)