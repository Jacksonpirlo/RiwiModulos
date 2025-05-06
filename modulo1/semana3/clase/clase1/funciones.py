def demo_meth(name:str="world" )->str:
    resutl:str= "hello " + name
    return resutl

def demo_meth_2(world_var:str="world", number_var:int=0)->int:

    result_var :int = number_var + len(world_var)
    return result_var

def main():
    print('Hello world')
    print(demo_meth())
    print(demo_meth("python"))
    print(demo_meth_2("Wilson", 5))

main()