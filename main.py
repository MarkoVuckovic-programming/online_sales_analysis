from product import Product
from product_manager import ProductManager

# Kreiranje proizvoda

product1 = Product("Monitor", 1000, 10)
product2 = Product("Printer", 600, 5)

# Kreiranje instance manager i dodavanje proizvoda u manager

manager = ProductManager()
manager.add_product(product1)
manager.add_product(product2)
