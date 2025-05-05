productPosition = 0
product = [{
       
        "name": "",
        "price": "",
        "quantity": ""
        
    }]
def Viewproducts(name = " ", price = " ", quantity = " "):
    return product

def addProducts(name = " ", price = " ", quantity = " "):
    name = str(input('Inser name: '))
    price = str(input('Inser price: '))
    quantity = str(input('Inser quantity: '))

    product["price"] = name
    product["price"] = price
    product["quantity"] = quantity
    return product


def main():
    print(Viewproducts())
    print(addProducts())
    print(addProducts())

main()
