class Admin():
    products = []
    udetails = {"name":"muneeb", "password":"1234"}
    # def __init__(self,uname,id,password):
    #     self.uname = uname
    #     self.id = id
    #     self.password = password
    def login(self):
<<<<<<< HEAD
        uname = input("Enter username: ")
        upass = input("Enter password: ")
        if uname == Admin.udetails["name"] and upass == Admin.udetails["password"]:
=======
        name =input("Enter your name: ")
        password = input("Enter your password: ")
        if name == Admin.udetails["name"] and password == Admin.udetails["password"]:
>>>>>>> 650bf9662765f269cd5074c7913d147290f93518
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False
    def add_product(self):
        # while True:
        #     pd = str(input("Enter product details: "))
        #     if pd == "":
        #         break
        #     Admin.products.append(pd)
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        
        new_product = Product(product_id, name, category, price, stock_quantity)
        Admin.products.append(new_product)
        print(f"Product '{name}' added successfully.")
    def view_product(self):
        if len(Admin.products) == 0:
            print("No products in inventory.")
        else:
            for product in Admin.products:
                print(f"current items in inventory are: {product}")
    def delete_product(self):
        print("Current products in inventory:")
        for product in Admin.products:
            print(product)
        try:
            del_id = input("Which product ID do you want to delete? ")
            print(product)
            for product in Admin.products:
                if product.product_id == del_id:
                    Admin.products.remove(product)
                    print(f"Product {product.name} deleted")
                    return
            print("Product not found")
        except Exception as e:
                print("Wrong input",e)

    def edit_product(self):
        product_id = input("Enter product ID to edit: ")
        for product in Admin.products:
            if product.product_id == product_id:
                product.name = input("Enter new product name: ")
                product.category = input("Enter new product category: ")
                product.price = float(input("Enter new product price: "))
                product.stock_quantity = int(input("Enter new stock quantity: "))
                print(f"Product '{product.name}' updated successfully.")
                return
        print("Product not found.")


    def check_low_stock(self, threshold=5):
        
        for product in Admin.products:
            if product.stock_quantity < threshold:
                print("Products with low stock:", product)
            else:
                print("None")

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"product ID:{self.product_id}, name: {self.name}, category:{self.category}, price:${self.price}, Stock: {self.stock_quantity}"

class User(Admin):
    udetails = {"username": "user1", "password": "userpass"} 
    # def __init__(self,uname,id, password):
    #     super().__init__(uname,id,password)
    def view_product(self):
        if len(Admin.products) == 0:
            print("No products in inventory.")
        else:
            for product in Admin.products:
                print(f"current items in inventory are: {product}")
    def login(self):
<<<<<<< HEAD
        uname = input("Enter username: ")
        upass = input("Enter password: ")
        if uname == Admin.udetails["name"] and upass == Admin.udetails["password"]:
=======
        name =input("Enter your name: ")
        password = input("Enter your password: ")
        if name == Admin.udetails["name"] and password == Admin.udetails["password"]:
>>>>>>> 650bf9662765f269cd5074c7913d147290f93518
            print("User login successful")
            return True
        else:
            print("User login failed")
            return False
class Console:
    @staticmethod
    def menu():
        print("Welcome to the Inventory Management System:\n Please select an option:\n 1. Admin\n 2. User\n 3. Exit")
        choice = input("Enter your option: ")
        return choice

<<<<<<< HEAD
admin = Admin()  
user1 = User()
=======
>>>>>>> 650bf9662765f269cd5074c7913d147290f93518

console =Console()
admin = Admin()  
user1 = User()

option =console.menu()
if option == "1":
    if admin.login():
        while True:
                print("\nInventory Management System. ")
                print("1. Add products")
                print("2. View products")
                print("3. Edit products")
                print("4. Delete products")
                print("5. Exit")

                try:
                    choice = int(input("Enter a choice: "))
                    if choice == 1 :
                        admin.add_product()
                    elif choice == 2 :
                        admin.view_product()
                    elif choice == 3 :
                        admin.edit_product()
                    elif choice == 4 :
                        admin.delete_product()
                    elif choice == 5 :
                        print("Exiting...")
                        break
                    else:
                        print("Invalid choice.Please try again")

                except ValueError as e:
                    print(f"ERROR OCCURRED: {e}")
        # admin.add_product()            # Admin can add products after login
        # admin.check_low_stock()        # Check for low stock products
        # admin.edit_product()           # Admin can edit existing products
        # admin.delete_product()         # Admin can delete products
    else:
        print("Access denied. Please check your login credentials.")
    
elif option == "2":  
    if user1.login():
        user1.view_product() 
    else:
        print("Access denied. Please check your login credentials.")     
elif option == "3":
    print("Exiting...")
else:
        print("Wrong input.")    
    