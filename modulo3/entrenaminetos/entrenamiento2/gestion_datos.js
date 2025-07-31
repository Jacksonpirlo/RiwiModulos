console.log('Data manage with Objects, Sets and Maps! ');

const products = {
    1: {id: 1, name: "Harina", price: 6000},
    2: {id: 2, name: "TV", price: 16000},
    3: {id: 3, name: "Table", price: 12500}
}

console.log(products[1])
console.log(Object.values(products))

// We use this "for in" to traverse the object and get the product ID with de const id and show the detaills placing id in products

for (const id in products) {
    console.log(`Product ID: ${id}, Detaills: ${products[id]}`)
}

// Here we create a Set because we don't want to have repeated elements, then we pick up the product items to access at it's values

const setProducts = new Set(Object.values(products).map(products => products.name));
console.log(setProducts)

// We use to get the product values

for (const products_item in setProducts) {
    console.log('unique product', products_item)
}


// Use Map to associate categories with products

const mapProducts = new Map([

    ["Food", "Harina"],
    ["Electronics", "TV"],
    ["House", "Table"],

])

// Finally, we use this "for each" to get the category and it's product

mapProducts.forEach((product, category) => {
    console.log(`Category: ${category}. Product ${product}`)
})

console.log('Complete user management tests');
console.log('Object', products)
console.log('Set', setProducts)
console.log('Map', mapProducts)
