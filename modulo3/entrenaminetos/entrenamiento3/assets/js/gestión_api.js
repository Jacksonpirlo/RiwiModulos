const URL_API = 'http://localhost:3001/products';
const URL_API_ID = (id) => `http://localhost:3001/products/${id}`;

// DOM Elements
const productForm = document.getElementById('product-form');
const productList = document.getElementById('product-list');

// Get all products and render them
async function getProducts() {
  try {
    const res = await fetch(URL_API);
    const data = await res.json();

    if (res.ok) {
      renderProducts(data);
    } else {
      console.error('⚠️ Failed to fetch products');
    }
  } catch (err) {
    console.log(err);
  }
}

// Render product cards in the DOM
function renderProducts(products) {
  productList.innerHTML = '';
  products.forEach(product => {
    const card = document.createElement('div');
    card.className = 'product-card';

    card.innerHTML = `
      <span>${product.name} - $${product.price}</span>
      <div class="actions">
        <button class="update">Update</button>
        <button onclick="deleteProduct(${product.id})">Delete</button>
      </div>
    `;

    card.querySelector('.update').addEventListener('click', () => {
      updatePrompt(product.id);
    });

    productList.appendChild(card);
  });
}

// Validate product data
function validateProduct(product) {
  if (!product.name || typeof product.price !== 'number') {
    console.error('❌ Invalid product');
    return false;
  }
  return true;
}

// Auto-generate unique ID
async function generateUniqueId() {
  try {
    const res = await fetch(URL_API);
    const products = await res.json();
    const ids = products.map(p => Number(p.id));
    return Math.max(...ids, 0) + 1;
  } catch (error) {
    console.log(error);
  }
}

// Add new product
async function addProduct(product) {
  try {
    if (!validateProduct(product)) return;
    product.id = await generateUniqueId();

    const res = await fetch(URL_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(product),
    });

    if (res.ok) {
      console.log('✅ Product added');
      getProducts();
    } else {
      console.error('❌ Failed to add product');
    }
  } catch (error) {
    console.log(error);
  }
}

// Update product data
async function updateProduct(id, newData) {
  try {
    if (!validateProduct(newData)) return;

    const res = await fetch(URL_API_ID(id), {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newData),
    });

    if (res.ok) {
      console.log('✅ Product updated');
      getProducts();
    } else {
      console.error('❌ Failed to update');
    }
  } catch (error) {
    console.log(error);
  }
}

// Ask user for new data and update product
function updatePrompt(id) {
  const name = prompt('New name:');
  const price = parseFloat(prompt('New price:'));
  if (name && !isNaN(price)) {
    updateProduct(id, { name, price });
  }
}

// Delete product by ID
async function deleteProduct(id) {
  try {
    const res = await fetch(URL_API_ID(id), {
      method: 'DELETE',
    });

    if (res.ok) {
      console.log(`🗑️ Deleted product with ID ${id}`);
      getProducts();
    } else {
      console.error(`❌ Could not delete product with ID ${id}`);
    }
  } catch (error) {
    console.log(error);
  }
}

// Handle form submission
productForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const price = parseFloat(document.getElementById('price').value);

  if (name && !isNaN(price)) {
    const newProduct = { name, price };
    await addProduct(newProduct);
    productForm.reset();
  }
});

// Initial fetch of products
getProducts();
