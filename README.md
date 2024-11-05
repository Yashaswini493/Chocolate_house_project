# Chocolate_house_project
Chocolate House Application,
this is a Python-based command-line application for a fictional Chocolate House. It allows managing seasonal flavors, ingredient inventory, and customer suggestions with allergy concerns using SQLite for data storage. The application follows backend Python standards and can be set up using Docker.

Features
1. Seasonal Flavors Management:
Add, view, update, and delete seasonal chocolate flavors.
Set availability dates for each seasonal flavor.

2. Ingredient Inventory Management:
Add, view, update, and delete ingredients in stock.
Track quantity levels and update inventory stock.

3. Customer Suggestions:
Record customer suggestions for new chocolate flavors.
Track allergy concerns associated with suggested flavors.

Requirements
1. Python 3.x
2. SQLite3
3. Docker (optional for containerized setup)

Main Menu Options
1. Add Seasonal Flavor - Allows the addition of a new seasonal flavor with specified availability dates.
2. View All Seasonal Flavors - Lists all currently registered seasonal flavors.
3. Add Ingredient - Add an ingredient with a specified quantity in stock.
4. View All Ingredients - Lists all ingredients along with quantities in stock.
5. Add Customer Suggestion - Record a new customer suggestion with allergy concerns if applicable.
6. View All Customer Suggestions - Lists all customer suggestions.
7. Exit - Exits the application.

Code Structure
1. Database Initialization: Tables are created for seasonal flavors, ingredient inventory, and customer suggestions.
2. Database Operations: Functions handle basic CRUD (Create, Read, Update, Delete) operations for each table.
3. Main Menu: A loop for user input to interact with the application’s features.

Database Schema
1. seasonal_flavors: Stores seasonal flavors with unique names and availability dates.
2. ingredient_inventory: Stores ingredient details with unique names, quantities, and last-updated timestamps.
3. customer_suggestions: Stores customer flavor suggestions with optional allergy information.

Example Usage
1. To add a seasonal flavor:
  Choose option 1 in the main menu.
  Enter the flavor name and availability dates.
2. To view all customer suggestions:
  Choose option 6 in the main menu.
  All suggestions are displayed.
