import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(r'C:/Users/PaulKP/Documents/Projects/python/selenium/Become QA Auto' + 
                                          r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()


    # Connection to databasse method ----------------------------------------------------------------------------
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"\nConnected successfully. SQLite Database Version is: {record}")


    # Orders methods---------------------------------------------------------------------------------------------
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record
    
    
    # Products methods ---------------------------------------------------------------------------------------------
    def get_products_qnt_sum(self):
        query = "SELECT SUM(quantity) FROM products;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record

    def get_max_product_qnt(self):
        query = "SELECT MAX(quantity) FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id};"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id};"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record
    
    def insert_product(self, id, name, descript, qnt):
        query = f"INSERT OR REPLACE INTO products(id, name, description, quantity) \
            VALUES ({id}, '{name}', '{descript}', {qnt});"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, id):
        query = f"DELETE FROM products WHERE id = {id};"
        self.cursor.execute(query)
        self.connection.commit()


    # Users methods ---------------------------------------------------------------------------------------------
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}';"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record

    
    # Customers methods -----------------------------------------------------------------------------------------
    def insert_new_customer(self, id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}');"
        self.cursor.execute(query)
        self.connection.commit()

    def get_full_customer_data_by_id(self, id):
        query = f"SELECT * FROM customers WHERE id = {id};"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record
    
    def delete_customer_by_id(self, id):
        query = f"DELETE FROM customers WHERE id = {id};"
        self.cursor.execute(query)
        self.connection.commit()

    def update_customer_city_by_id(self, city, id):
        query = f"UPDATE customers SET city = '{city}' WHERE id = {id};"
        self.cursor.execute(query)
        self.connection.commit()

    def get_customer_city_by_id(self, id):
        query = f"SELECT city FROM customers WHERE id = {id};"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record
    