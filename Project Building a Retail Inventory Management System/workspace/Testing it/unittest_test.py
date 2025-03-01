import unittest
from notebook import Product, Order  

class TestInventorySystem(unittest.TestCase):
    
    def setUp(self):
        """Reset inventory before each test."""
        Product.inventory = []
    
    def test_add_product(self):
        result = Product.add_product("Laptop", "Electronics", 10, 999.99, "TechSupplier")
        self.assertEqual(result, "Product added successfully")
        self.assertEqual(len(Product.inventory), 1)
        self.assertEqual(Product.inventory[0].name, "Laptop")
    
    def test_update_product(self):
        Product.add_product("Phone", "Electronics", 5, 599.99, "MobileSupplier")
        result = Product.update_product(1, quantity=8, price=579.99)
        self.assertEqual(result, "Product information updated successfully")
        self.assertEqual(Product.inventory[0].quantity, 8)
        self.assertEqual(Product.inventory[0].price, 579.99)
    
    def test_update_nonexistent_product(self):
        result = Product.update_product(99, quantity=5)
        self.assertEqual(result, "Product not found")
    
    def test_delete_product(self):
        Product.add_product("Tablet", "Electronics", 3, 299.99, "TabSupplier")
        result = Product.delete_product(1)
        self.assertEqual(result, "Product deleted successfully")
        self.assertEqual(len(Product.inventory), 0)
    
    def test_delete_nonexistent_product(self):
        result = Product.delete_product(99)
        self.assertEqual(result, "Product not found")
    
    def test_place_order_success(self):
        Product.add_product("Monitor", "Electronics", 15, 199.99, "ScreenSupplier")
        order = Order(order_id=1, products=[])
        result = order.place_order(1, 5, customer_info="John Doe")
        self.assertEqual(result, "Order placed successfully. Order ID: 1")
        self.assertEqual(Product.inventory[0].quantity, 10)
    
    def test_place_order_insufficient_stock(self):
        Product.add_product("Keyboard", "Electronics", 2, 49.99, "KeySupplier")
        order = Order(order_id=2, products=[])
        result = order.place_order(1, 5, customer_info="Jane Doe")
        self.assertEqual(result, "product id isn't find")
        self.assertEqual(Product.inventory[0].quantity, 2)
    
    def test_place_order_nonexistent_product(self):
        order = Order(order_id=3, products=[])
        result = order.place_order(99, 1, customer_info="Alice")
        self.assertEqual(result, "product id isn't find")

if __name__ == '__main__':
    unittest.main()
