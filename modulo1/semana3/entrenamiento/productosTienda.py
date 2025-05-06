products = [{
    "name": "Harina",
    "price": 3000,
    "quantity": 12
}]
total:int=0

def addProduct():
    productsName = str(input('Product name: '))
    Productprice = int(input('Product price: '))
    Productquantity = int(input('Product quantity: '))

    products.append({

        "name": productsName,
        "price": Productprice,
        "quantity": Productquantity
    })

    doYouWant:str=input('Do you want to add another product? yes/no: ')

    if doYouWant.lower() == "yes":
        return changePrice()
    elif doYouWant.lower() == "no":
        print(products)
        return main()
    else:
        print(f'Data be wrong, you put {doYouWant}. Correct data: yes/ no')
    return products

def searchProduct():
    productName = input('Product name: ')
    
    for product in products:
        if product["name"].lower() == productName.lower():
            print("Product found \n")
            print(f"Product name: {product["name"]}")
            print(f"Product price: {product["price"]}")
            print(f"Product quantity: {product["quantity"]}")
            return

    print("Product not found")


def changePrice():
    print('Search a product by its name')
    productName = input('Product name: ')
    
    for product in products:
        if product["name"].lower() == productName.lower():
            print(f'Change the price of {product["name"]}')
            newPrice = str(input("New product price: "))
            product["price"] = newPrice
            print(products)
            doYouWant:str=input('Do you want to change another price of product: ')

            if doYouWant.lower() == "yes":
                return changePrice()
            elif doYouWant.lower() == "no":
                print(products)
                return main()
            else:
                print(f'Data be wrong, you put {doYouWant}. Correct data: yes/ no')

def deleteProduct():
    print('Search a product by its name')
    productName = input('Product name:')
    
    for product in products:
        if product["name"].lower() == productName.lower():
            print(f'delete the price of {product["name"]}...')
            products.remove(product)
            return products

    print("Product not found")
    return main()

def sumAll():
    print('Total price of products')
    
    for product in products:
        total += product["price"] * total
        return total
    print("Product not found")


print('WELCOME TO THE VAQUITA 🐮')
def main():
    status = int(input(f'''

      We have this options for you:
                       
                Press:
                       
                       1) Add a product ➕
                       2) Search a product 🔎
                       3) Change the price of product 📄
                       4) Delete a product ❌
                       5) View your total price 💲
                       6) Exit ➡️

'''))
    
    if status == 1:
        print("Add a product")
        print(addProduct())
    elif status == 2:
        print("Search a product by Its name")
        print(searchProduct())
    elif status == 3:
        print("Change the price of product")
        print(changePrice())
    elif status == 4:
        print("Delete a product")
        print(deleteProduct())
    elif status == 5:
        print("View your total price")
        print(sumAll())
    elif status == 6:
        return print('Bye, have a nice day ☺️')

main()