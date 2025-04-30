n = int(input('What numbers do you want to compare: '))
numbers = []
for i in range(n):
    number = int(input(f'Insert number {i + 1}: '))
    numbers.append(number)
for j in numbers:
    if j > 1000:
        print(f'{j} is more than 1000')