class Admin():
    products = []
    udetails = {"name":"muneeb", "password":"1234"}
    # def __init__(self,uname,id,password):
    #     self.uname = uname
    #     self.id = id
    #     self.password = password
    def login(self):
        uname = input("Enter username: ")
        upass = input("Enter password: ")
        if uname == Admin.udetails["name"] and upass == Admin.udetails["password"]:
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

    def delete_product(self):
        print("current products:")
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
        print("Products with low stock:")
        for product in Admin.products:
            if product.stock_quantity < threshold:
                print(product)
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
        return f"{self.product_id}: {self.name}, {self.category}, ${self.price}, Stock: {self.stock_quantity}"

class User(Admin):
    udetails = {"username": "user1", "password": "userpass"} 
    # def __init__(self,uname,id, password):
    #     super().__init__(uname,id,password)
    def view_product(self):
        print(f"current items in inventory are: {Admin.products}")
    def login(self):
        uname = input("Enter username: ")
        upass = input("Enter password: ")
        if uname == Admin.udetails["name"] and upass == Admin.udetails["password"]:
            print("User login successful")
            return True
        else:
            print("User login failed")
            return False

admin = Admin()  
user1 = User()

if admin.login():
    admin.add_product()             # Admin can add products after login
    admin.check_low_stock()        # Check for low stock products
    admin.edit_product()           # Admin can edit existing products
    admin.delete_product()         # Admin can delete products
else:
    print("Access denied. Please check your login credentials.")

if user1.login():  
    user1.view_product()           
else:
    print("Access denied for User. Please check your login credentials.")