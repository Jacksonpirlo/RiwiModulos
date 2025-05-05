def es_par(num:int=2)->bool:
    if num % 2 == 0:
        return True
    else:
        return False
    
def main():
    print(es_par())

main()