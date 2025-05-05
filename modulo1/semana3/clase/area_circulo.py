def circle_area(radio:int=23)->int:
    pi:int=3.1416
    area:int= pi * (radio * 2)
    return area

def main():
    print(circle_area())

main()