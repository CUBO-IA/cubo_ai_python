function addToCart(productName, productImage) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  cart.push({
    name: productName,
    image: productImage,
  });

  localStorage.setItem("cart", JSON.stringify(cart));

  alert(productName + " added to cart.");
}

function clearCart() {
  localStorage.removeItem("cart");
  displayCart();
}

function displayCart() {
  const cartElement = document.getElementById("cart");

  if (!cartElement) {
    return;
  }

  const cart = JSON.parse(localStorage.getItem("cart")) || [];

  if (cart.length === 0) {
    cartElement.innerHTML = "<p>Your cart is empty.</p>";
    return;
  }

  cartElement.innerHTML = "";

  cart.forEach(function (product) {
    const item = document.createElement("div");

    item.className = "cart-item";

    item.innerHTML = `
        <img
            src="/static/images/${product.image}"
            alt="${product.name}"
        >
        <p>${product.name}</p>
    `;

    cartElement.appendChild(item);
  });
}

document.addEventListener("DOMContentLoaded", displayCart);
