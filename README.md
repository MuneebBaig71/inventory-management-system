# Inventory Management System

## Description
The Inventory Management System is a console-based application that allows users to manage product inventory through an admin or user interface. Admin users can add, edit, delete, and view product details, while regular users can only view the products. The application uses a simple login system for both roles and provides error handling for invalid inputs.

## Features
1. **Admin Functionalities**:
   - **Add Product**: Add new products to the inventory with details like ID, name, category, price, and stock quantity.
   - **View Product**: View all products currently in the inventory.
   - **Edit Product**: Modify the details of existing products.
   - **Delete Product**: Remove products from the inventory based on product ID.
   - **Check Low Stock**: Identify products that have low stock levels based on a defined threshold.
  
2. **User Functionalities**:
   - **View Products**: Users can view all products in the inventory without modification privileges.

3. **Console Interface**:
   - Provides a user-friendly menu interface that guides both admin and regular users through available options.
   - Error handling for invalid inputs to improve user experience.

## Classes and Methods

- **Class: `Admin`**
  - **Methods**:
    - `login()`: Authenticates admin credentials.
    - `add_product()`: Adds a product to the inventory.
    - `view_product()`: Lists all products in the inventory.
    - `delete_product()`: Deletes a product by its ID.
    - `edit_product()`: Updates details of an existing product.
    - `check_low_stock()`: Checks and displays products with stock below a specified threshold.

- **Class: `Product`**
  - **Attributes**:
    - `product_id`, `name`, `category`, `price`, `stock_quantity`.
  - **Method**:
    - `__str__()`: Provides a formatted string representation of a product.

- **Class: `User`**
  - **Methods**:
    - `login()`: Authenticates user credentials.
    - `view_product()`: Lists all products in the inventory.
  
- **Class: `Console`**
  - **Methods**:
    - `menu()`: Displays the main menu options for the system and takes user input.

## Usage

1. **Start the Application**:
   - Run the main script. You will see a welcome menu with options to select either Admin or User mode.

2. **Admin Mode**:
   - Choose "1" for Admin and enter the correct admin credentials.
   - If login is successful, an additional menu will appear, allowing you to:
     - Add new products.
     - View the current inventory.
     - Edit or delete existing products.
     - Check for low-stock items.
     - Exit the admin menu.

3. **User Mode**:
   - Choose "2" for User and enter the correct user credentials.
   - If login is successful, the user can view the list of products in the inventory.

4. **Exit**:
   - Choose "3" from the main menu to exit the application.

## Example Workflow

```plaintext
Welcome to the Inventory Management System:
 Please select an option:
 1. Admin
 2. User
 3. Exit

# Selecting "1" for Admin and entering credentials
Enter your name: muneeb
Enter your password: 1234
Login successful

# Admin-specific menu is displayed
Inventory Management System.
1. Add products
2. View products
3. Edit products
4. Delete products
5. Exit

Enter a choice: 1
Enter product ID: 101
Enter product name: Apple
Enter product category: Fruit
Enter product price: 1.99
Enter stock quantity: 50
Product 'Apple' added successfully.

# Additional options to manage products follow.
