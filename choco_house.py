import sqlite3
from datetime import datetime

conn = sqlite3.connect("chocolate_house.db")
cursor = conn.cursor()

# 1. Table for Seasonal Flavors
cursor.execute('''
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    flavor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL UNIQUE,
    availability_start DATE NOT NULL,
    availability_end DATE NOT NULL
)
''')

# 2. Table for Ingredient Inventory
cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredient_inventory (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL UNIQUE,
    quantity_in_stock INTEGER NOT NULL CHECK(quantity_in_stock >= 0),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# 3. Table for Customer Suggestions
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_suggestions (
    suggestion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    flavor_suggestion TEXT NOT NULL,
    allergy_concern TEXT
)
''')

conn.commit()
conn.close()


def insert_sample_data():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    # Sample data for seasonal_flavors
    cursor.execute("INSERT OR IGNORE INTO seasonal_flavors (flavor_name, availability_start, availability_end) VALUES (?, ?, ?)", 
                   ("Pumpkin Spice", "2024-10-01", "2024-11-30"))
    
    # Sample data for ingredient_inventory
    cursor.execute("INSERT OR IGNORE INTO ingredient_inventory (ingredient_name, quantity_in_stock) VALUES (?, ?)", 
                   ("Cocoa Powder", 50))

    # Sample data for customer_suggestions
    cursor.execute("INSERT OR IGNORE INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concern) VALUES (?, ?, ?)", 
                   ("Alice", "Hazelnut Delight", "Contains nuts"))

    conn.commit()
    conn.close()

insert_sample_data()


import sqlite3
from datetime import datetime

def connect():
    return sqlite3.connect("chocolate_house.db")

# Function to add a new seasonal flavor
def add_seasonal_flavor(flavor_name, availability_start, availability_end):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO seasonal_flavors (flavor_name, availability_start, availability_end)
            VALUES (?, ?, ?)
        ''', (flavor_name, availability_start, availability_end))
        conn.commit()
        print(f"Added seasonal flavor: {flavor_name}")
    except sqlite3.IntegrityError as e:
        print("Error: Flavor name must be unique.")
    finally:
        conn.close()

# Function to update an existing seasonal flavor
def update_seasonal_flavor(flavor_id, flavor_name=None, availability_start=None, availability_end=None):
    conn = connect()
    cursor = conn.cursor()
    # Update only provided fields
    if flavor_name:
        cursor.execute("UPDATE seasonal_flavors SET flavor_name = ? WHERE flavor_id = ?", (flavor_name, flavor_id))
    if availability_start:
        cursor.execute("UPDATE seasonal_flavors SET availability_start = ? WHERE flavor_id = ?", (availability_start, flavor_id))
    if availability_end:
        cursor.execute("UPDATE seasonal_flavors SET availability_end = ? WHERE flavor_id = ?", (availability_end, flavor_id))
    conn.commit()
    print(f"Updated seasonal flavor with ID: {flavor_id}")
    conn.close()

# Function to retrieve all seasonal flavors
def get_all_seasonal_flavors():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

# Function to delete a seasonal flavor by ID
def delete_seasonal_flavor(flavor_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM seasonal_flavors WHERE flavor_id = ?", (flavor_id,))
    conn.commit()
    print(f"Deleted seasonal flavor with ID: {flavor_id}")
    conn.close()

# Function to add a new ingredient
def add_ingredient(ingredient_name, quantity_in_stock):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO ingredient_inventory (ingredient_name, quantity_in_stock)
            VALUES (?, ?)
        ''', (ingredient_name, quantity_in_stock))
        conn.commit()
        print(f"Added ingredient: {ingredient_name}")
    except sqlite3.IntegrityError as e:
        print("Error: Ingredient name must be unique.")
    finally:
        conn.close()

# Function to update the quantity of an existing ingredient
def update_ingredient_stock(ingredient_id, new_quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE ingredient_inventory
        SET quantity_in_stock = ?, last_updated = ?
        WHERE ingredient_id = ?
    ''', (new_quantity, datetime.now(), ingredient_id))
    conn.commit()
    print(f"Updated ingredient with ID: {ingredient_id}")
    conn.close()

# Function to retrieve all ingredients
def get_all_ingredients():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredient_inventory")
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

# Function to delete an ingredient by ID
def delete_ingredient(ingredient_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ingredient_inventory WHERE ingredient_id = ?", (ingredient_id,))
    conn.commit()
    print(f"Deleted ingredient with ID: {ingredient_id}")
    conn.close()


# Function to add a new customer suggestion
def add_customer_suggestion(customer_name, flavor_suggestion, allergy_concern):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concern)
        VALUES (?, ?, ?)
    ''', (customer_name, flavor_suggestion, allergy_concern))
    conn.commit()
    print(f"Added customer suggestion from {customer_name}")
    conn.close()

# Function to retrieve all customer suggestions
def get_all_customer_suggestions():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_suggestions")
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

# Function to delete a customer suggestion by ID
def delete_customer_suggestion(suggestion_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customer_suggestions WHERE suggestion_id = ?", (suggestion_id,))
    conn.commit()
    print(f"Deleted customer suggestion with ID: {suggestion_id}")
    conn.close()

def main_menu():
    while True:
        print("\nChocolate House Application")
        print("1. Add Seasonal Flavor")
        print("2. View All Seasonal Flavors")
        print("3. Add Ingredient")
        print("4. View All Ingredients")
        print("5. Add Customer Suggestion")
        print("6. View All Customer Suggestions")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            flavor_name = input("Flavor name: ")
            start = input("Availability start (YYYY-MM-DD): ")
            end = input("Availability end (YYYY-MM-DD): ")
            add_seasonal_flavor(flavor_name, start, end)
        elif choice == "2":
            flavors = get_all_seasonal_flavors()
            for flavor in flavors:
                print(flavor)
        elif choice == "3":
            ingredient_name = input("Ingredient name: ")
            quantity = int(input("Quantity in stock: "))
            add_ingredient(ingredient_name, quantity)
        elif choice == "4":
            ingredients = get_all_ingredients()
            for ingredient in ingredients:
                print(ingredient)
        elif choice == "5":
            customer_name = input("Customer name: ")
            flavor_suggestion = input("Flavor suggestion: ")
            allergy_concern = input("Allergy concern: ")
            add_customer_suggestion(customer_name, flavor_suggestion, allergy_concern)
        elif choice == "6":
            suggestions = get_all_customer_suggestions()
            for suggestion in suggestions:
                print(suggestion)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
