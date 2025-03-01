class Product:
    inventory=[]

    def __init__(self, product_id, name, category, quantity, price, supplier):
         self.product_id=product_id
         self.name=name
         self.category=category
         self.quantity= quantity
         self.price=price
         self.supplier=supplier
         

    @classmethod
    def add_product(cls, name, category, quantity, price,supplier):
        product_id=  cls.inventory[-1].product_id+1 if len(cls.inventory)>0 else 1
        new_product=cls(product_id, name, category, quantity, price, supplier)
        Product.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for item in Product.inventory:
            if item.product_id==product_id:
                if(quantity is not None):
                    item.quantity= quantity
                if(price is not None):
                    item.price= price
                if(supplier is not None):
                    item.supplier= supplier
                return "Product information updated successfully"
        return "Product not found"
        

    @classmethod
    def delete_product(cls, product_id):

       for i,item in enumerate(Product.inventory):
           if item.product_id== product_id:
              del Product.inventory[i]
              return "Product deleted successfully"
       return "Product not found"


class Order:

    def __init__(self, order_id, products, customer_info=None):
        self.order_id=order_id
        self.products=products
        self.customer_info=customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        for item in Product.inventory:
            if item.product_id== product_id and item.quantity >= quantity:
                item.quantity-=quantity
                self.customer_info=customer_info
                self.products.append((product_id ,quantity))
                return f"Order placed successfully. Order ID: {self.order_id}"
        return "product id isn't find"