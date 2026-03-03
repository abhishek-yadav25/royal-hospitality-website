// Highlight active navbar link based on current page
const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
const currentPage = window.location.pathname.split("/").pop(); // e.g., "menu.html"

navLinks.forEach(link => {
  const linkPage = link.getAttribute('href');
  if(linkPage === currentPage || (linkPage === "index.html" && currentPage === "")) {
    link.classList.add('active');
  } else {
    link.classList.remove('active');
  }
});


// Select all add-to-cart buttons
const addButtons = document.querySelectorAll('.add-to-cart');
const cartItemsList = document.getElementById('cart-items');
const cartCount = document.getElementById('cart-count');
const cartTotal = document.getElementById('cart-total');

let cart = [];

// Update cart display
function updateCart() {
  cartItemsList.innerHTML = '';
  let totalItems = 0;
  let totalPrice = 0;

  cart.forEach((item, index) => {
    totalItems += item.quantity;
    totalPrice += item.price * item.quantity;

    const li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between align-items-center';
    li.innerHTML = `
      <div>
        <strong>${item.name}</strong> - ₹${item.price} x ${item.quantity}
      </div>
      <div>
        <button class="btn btn-sm btn-secondary me-1" onclick="changeQuantity(${index}, -1)">-</button>
        <button class="btn btn-sm btn-secondary me-1" onclick="changeQuantity(${index}, 1)">+</button>
        <button class="btn btn-sm btn-danger" onclick="removeItem(${index})">Remove</button>
      </div>
    `;
    cartItemsList.appendChild(li);
  });

  cartCount.textContent = totalItems;
  cartTotal.textContent = totalPrice;
}

// Add item to cart
addButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const name = btn.getAttribute('data-name');
    const price = parseInt(btn.getAttribute('data-price'));

    const existingIndex = cart.findIndex(item => item.name === name);
    if (existingIndex !== -1) {
      cart[existingIndex].quantity += 1;
    } else {
      cart.push({ name, price, quantity: 1 });
    }

    updateCart();
  });
});

// Remove item completely
function removeItem(index) {
  cart.splice(index, 1);
  updateCart();
}

// Change quantity (+1 or -1)
function changeQuantity(index, delta) {
  cart[index].quantity += delta;
  if (cart[index].quantity <= 0) {
    removeItem(index);
  } else {
    updateCart();
  }
}
