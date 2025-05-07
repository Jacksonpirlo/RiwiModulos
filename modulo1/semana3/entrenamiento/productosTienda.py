# INITIAL PRODUCT LIST WITH ONE DEFAULT ITEM
products = [{
    "name": "Harina",
    "price": 3000,
    "quantity": 12
}]

# GLOBAL VARIABLE TO TRACK TOTAL VALUE
total: int = 0

# FUNCTION TO ADD A NEW PRODUCT TO THE LIST
def addProduct() -> None:
    productsName: str = input('Product name: ')
    productPrice: int = int(input('Product price: '))
    productQuantity: int = int(input('Product quantity: '))

    # CHECK IF THE PRODUCT ALREADY EXISTS (CASE INSENSITIVE)
    for product in products:
        if product["name"].lower() == productsName.lower():
            print(f'\n  ❌ ❌ ❌ THIS PRODUCT "{productsName.lower()}" ALREADY EXISTS ❌ ❌ ❌')
            return

    # CREATE A NEW PRODUCT DICTIONARY AND ADD IT TO THE LIST
    newProduct: dict = {
        "name": productsName,
        "price": productPrice,
        "quantity": productQuantity
    }
    products.append(newProduct)

    # ASK IF THE USER WANTS TO ADD ANOTHER PRODUCT
    doYouWant: str = input('Do you want to add another product? yes/no: ')
    if doYouWant.lower() == "yes":
        addProduct()
    elif doYouWant.lower() == "no":
        print(products)
    else:
        print(f'Data is wrong, you put "{doYouWant}". Correct options: yes / no')

# FUNCTION TO SEARCH FOR A PRODUCT BY NAME
def searchProduct() -> None:
    productName: str = input('Product name: ')
    
    for product in products:
        if product["name"].lower() == productName.lower():
            print("\n ✅ PRODUCT FOUND ✅ \n")
            name: str = product['name']
            price: int = product['price']
            quantity: int = product['quantity']

            # DISPLAY THE PRODUCT DETAILS
            print(f"Product name: {name}")
            print(f"Product price: {price}")
            print(f"Product quantity: {quantity}")
            return

    # PRODUCT WAS NOT FOUND
    print("\n ❌ PRODUCT NOT FOUND 😖")

# FUNCTION TO CHANGE THE PRICE OF AN EXISTING PRODUCT
def changePrice() -> None:
    print('Search a product by its name')
    productName: str = input('Product name: ')
    
    for product in products:
        if product["name"].lower() == productName.lower():
            print(f'Change the price of "{product["name"]}"')
            newPrice: int = int(input("New product price: "))
            product["price"] = newPrice
            print(products)

            # ASK IF THE USER WANTS TO CHANGE ANOTHER PRICE
            doYouWant: str = input('Do you want to change another product price? yes/no: ')
            if doYouWant.lower() == "yes":
                changePrice()
            elif doYouWant.lower() == "no":
                return
            else:
                print(f'Data is wrong, you put "{doYouWant}". Correct options: yes / no')
            return
    
    # PRODUCT NOT FOUND
    print("❌ Product not found")

# FUNCTION TO DELETE A PRODUCT FROM THE LIST
def deleteProduct() -> None:
    print('Search a product by its name')
    productName: str = input('Product name: ')
    
    for product in products:
        if product["name"].lower() == productName.lower():
            print(f'Deleting product "{product["name"]}"...')
            products.remove(product)
            return

    # PRODUCT NOT FOUND
    print("❌ Product not found 😖")

# FUNCTION TO CALCULATE THE TOTAL VALUE OF ALL PRODUCTS
def sumAll() -> str:
    print('Total price of products')
    total: int = sum(map(lambda p: p.get("price", 0) * p.get("quantity", 0), products))
    return f'Final total: {total} 💲'

# MAIN FUNCTION WITH THE PROGRAM MENU
def main() -> None:
    print('WELCOME TO THE VAQUITA 🐮')

    # MAIN LOOP TO KEEP SHOWING MENU UNTIL USER EXITS
    while True:
        status: int = int(input('''

      WE HAVE THESE OPTIONS FOR YOU:
                       
                PRESS:
                       1) ADD A PRODUCT ➕
                       2) SEARCH A PRODUCT 🔎
                       3) CHANGE THE PRICE OF A PRODUCT 📄
                       4) DELETE A PRODUCT ❌
                       5) VIEW YOUR TOTAL PRICE 💲
                       6) EXIT ➡️

        '''))

        # HANDLE USER SELECTION
        if status == 1:
            addProduct()
        elif status == 2:
            searchProduct()
        elif status == 3:
            changePrice()
        elif status == 4:
            deleteProduct()
        elif status == 5:
            print(sumAll())
        elif status == 6:
            print('BYE, HAVE A NICE DAY ☺️')
            break
        else:
            print("INVALID OPTION. PLEASE SELECT A NUMBER FROM 1 TO 6.")

# START THE PROGRAM
main()
