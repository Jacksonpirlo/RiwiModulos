newArray = []
def filtro(array):
    for i in array:
        if i not in newArray:
            newArray.append(i)
    return newArray

def main():
    print(filtro([1,1,1,1,1,2,3,4,5,5,5,5]))

main()