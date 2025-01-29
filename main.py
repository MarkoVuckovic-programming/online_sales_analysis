from product import Product
from product_manager import ProductManager

# Kreiranje proizvoda

product1 = Product("Laptop", 1000, 15)
product2 = Product("Phone", 600, 25)

# Kreiranje instance manager i dodavanje proizvoda u manager

manager = ProductManager()
manager.add_product(product1)
manager.add_product(product2)

# Prikaz proizvoda i ukupne vrednosti inventara

print(manager.show_products())
print(f"Total inventory value: ${manager.total_inventory_value()}")
