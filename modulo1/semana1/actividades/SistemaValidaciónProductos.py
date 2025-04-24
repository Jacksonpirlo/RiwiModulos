# CREATING INITIAL VARIABLES TO START THE PROGRAM
productName = input('Product name: ')
unitPrice = int(input('Unit Price: '))
QuantityOfProducts = int(input('Quantity of products: '))
offer = int(input('Offer: '))

# CREATING CONDITIONALS TO VALIDATE IF UNIT PRICE AND QUANTITY OF PRODUCTS ARE GREATER THAN 0
if unitPrice > 0 and QuantityOfProducts > 0:
    
    # VALIDATING IF THERE IS A VALID OFFER
    if offer >= 1 and offer <= 100:
        PriceDone = unitPrice * QuantityOfProducts
        discount = unitPrice * (offer / 100)  # Calculating the discount per unit
        finalPrice = unitPrice - discount  # Final price per unit after discount
        totalWithDiscount = finalPrice * QuantityOfProducts  # Total price with discount applied
        
        # PRINTING ALL INFORMATION ABOUT THE PRODUCT WITH OFFER
        print(f'''
        Hi User,
        Your Product: {productName}
        Unit Price: {unitPrice}
        Offer: {offer}%
        Discount per Unit: {discount}
        Total with Offer: {totalWithDiscount}
        ''')

    else:
        PriceDone = unitPrice * QuantityOfProducts
        # PRINTING ALL INFORMATION WITHOUT OFFER
        print(f'''
        Hi User,
        Your Product: {productName}
        Unit Price: {unitPrice}
        Total: {PriceDone}
        ''')

else:
    print('Factura Invalida: Selecciona un producto')
