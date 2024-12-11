
'''
main.py: koden till hela programmet

__author__  = "Oscar Haij"
__version__ = "1.0.0"
__email__   = "oscar.haij@elev.ga.ntig.se"
'''
import csv
import uuid

def load_data(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": row['id'],
                "name": row['name'],
                "desc": row['desc'],
                "price": float(row['price']),
                "quantity": int(row['quantity'])
            })
    return products

def save_data(filename, products):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def display_products(products):
    for product in products:
        print(f"{product['id']}: {product['name']} - {product['desc']} - ${product['price']} - Qty: {product['quantity']}")

def add_product(products):
    new_product = {
        "id": str(uuid.uuid4()),  # Generera ID
        "name": input("Ange produktnamn: "),
        "desc": input("Ange produktbeskrivning: "),
        "price": float(input("Ange pris: ")),
        "quantity": int(input("Ange antal i lager: "))
    }
    products.append(new_product)
    print("Produkt tillagd.")

def edit_product(product_id, products):
    for product in products:
        if product['id'] == product_id:
            product['name'] = input(f"Ny produktnamn ({product['name']}): ") or product['name']
            product['desc'] = input(f"Ny beskrivning ({product['desc']}): ") or product['desc']
            product['price'] = float(input(f"Nytt pris ({product['price']}): ") or product['price'])
            product['quantity'] = int(input(f"Nytt antal ({product['quantity']}): ") or product['quantity'])
            print("Produkt uppdaterad.")
            return
    print("Produkt ej funnen.")

def delete_product(product_id, products):
    for i, product in enumerate(products):
        if product['id'] == product_id:
            del products[i]
            print("Produkt borttagen.")
            return
    print("produkt ej funnen")

# Ladda produkter
filename = 'db_inventory.csv'
products = load_data(filename)

display_products(products)
add_product(products)
edit_product('id_du_vill_redigera', products)
delete_product('id_du_vill_ta_bort', products)
save_data(filename, products)
