from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje proizvoda

product1 = Product("Monitor", 1000, 10)
product2 = Product("Printer", 600, 5)

# Kreiranje instance manager i dodavanje proizvoda u manager

manager = ProductManager()
manager.add_product(product1)
manager.add_product(product2)

# Prikaz proizvoda i ukupne vrednosti inventara

print(manager.show_products())
print(f"Total inventory value: ${manager.total_inventory_value()}")

# Kreiranje korpe i didavanje proizvoda u korpu

cart = Cart()
cart.add_to_cart(product1)
cart.add_to_cart(product2)

# Prikaz proizvoda u korpi i ukupne vrednosti

print(cart.show_cart())
print(f"Total cart value: ${cart.total_cart_value()}")
