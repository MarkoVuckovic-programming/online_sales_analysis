# online_sales_analysis

# Opis projekta

Online Sales Analysis je Python aplikacija koja omogucava upravljanje prodajnim podacima u online prodavnici.

Aplikacija podrzava:

- Rad sa proizvodima (dodavanje, prikaz, azuriranje i uklanjanje proizvoda)

- Upravljanje korpom kupaca (dodavanje proizvoda,prikaz sadrzaja i izracunavanje ukupne vrednosti korpe)

- Sigurnost podataka koriscenjem .gitignore

- Dokumentaciju projekta kroz README.md

# Klase i funkcionalnosti

1. Klasa Product

Predstavlja jedan proizvod u prodavnici.

Atributi:

- name - naziv proizvoda

- price - cena proizvoda

- quantity - kolicina proizvoda na stanju

Metode:

- show_info() - prikazuje informacije o proizvodu

- update_quantity(new_quantity) - azurira kolicinu proizvoda

2. Klasa ProductManager

Upravlja listom proizvoda dostupnih u prodavnici.

Atributi:

- products - lista proizvoda u prodavnici

Metode:

- add_product(product) - dodaje novi proizvod

- show_products() - prikazuje sve proizvode

- total_inventory_value() - racuna ukupnu vrednost svih proizvoda

- remove_product(product_name) -uklanja proizvod prema imenu

3. Klasa Cart

Predstavlja korpu kupaca i omogucava dodavanje proizvoda.

Atributi:

- cart_items - lista proizvoda u korpi

Metode:

- add_to_cart(product) - dodaje proizvod u korpu

- total_cart_value() - racuna ukupnu vrednost korpe

- show_cart() - prikazuje sve proizvode u korpi
