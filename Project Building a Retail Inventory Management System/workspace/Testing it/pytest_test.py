

import pytest
from notebook import Product, Order 

@pytest.fixture(autouse=True)
def reset_inventory():
    """Fixture to reset inventory before each test."""
    Product.inventory = []

@pytest.mark.skip
def test_add_product():
    result = Product.add_product("Laptop", "Electronics", 10, 999.99, "TechSupplier")
    assert result == "Product added successfully"
    assert len(Product.inventory) == 1
    assert Product.inventory[0].name == "Laptop"

def test_update_product():
    Product.add_product("Phone", "Electronics", 5, 599.99, "MobileSupplier")
    result = Product.update_product(1, quantity=8, price=579.99)
    assert result == "Product information updated successfully"
    assert Product.inventory[0].quantity == 8
    assert Product.inventory[0].price == 579.99

def test_update_nonexistent_product():
    result = Product.update_product(99, quantity=5)
    assert result == "Product not found"

def test_delete_product():
    Product.add_product("Tablet", "Electronics", 3, 299.99, "TabSupplier")
    result = Product.delete_product(1)
    assert result == "Product deleted successfully"
    assert len(Product.inventory) == 0

def test_delete_nonexistent_product():
    result = Product.delete_product(99)
    assert result == "Product not found"

def test_place_order_success():
    Product.add_product("Monitor", "Electronics", 15, 199.99, "ScreenSupplier")
    order = Order(order_id=1, products=[])
    result = order.place_order(1, 5, customer_info="John Doe")
    assert result == "Order placed successfully. Order ID: 1"
    assert Product.inventory[0].quantity == 10

def test_place_order_insufficient_stock():
    Product.add_product("Keyboard", "Electronics", 2, 49.99, "KeySupplier")
    order = Order(order_id=2, products=[])
    result = order.place_order(1, 5, customer_info="Jane Doe")
    assert result == "product id isn't find"
    assert Product.inventory[0].quantity == 2

def test_place_order_nonexistent_product():
    order = Order(order_id=3, products=[])
    result = order.place_order(99, 1, customer_info="Alice")
    assert result == "product id isn't find"
