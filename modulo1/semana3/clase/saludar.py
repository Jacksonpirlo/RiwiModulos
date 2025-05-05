def greet(name:str="Mohamed")->str:
    greeting = "Hi! " + name
    return greeting

def main():
    print(greet())

main()