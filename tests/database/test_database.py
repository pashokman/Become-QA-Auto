""" 
Here I learned how to test databese, using methods:
JOIN, SUM, MAX, SELECT, INSERT, DELETE, UPDATE.
"""

import pytest


# Testing database connection ----------------------------------------------------------------------------------------
@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


# Testing products ---------------------------------------------------------------------------------------------------
@pytest.mark.database
def test_products_quantity_sum(database):
    sum = database.get_products_qnt_sum()
    
    assert sum[0][0] == 75, 'Products quantity sum is not equal to 75'


@pytest.mark.database
def test_max_product_quantity(database):
    max = database.get_max_product_qnt()

    assert max[0][0] == 30, 'Max product quantity is not equal to 30'


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25, 'Water product quantity after updating is not equal to 25'


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, 'печиво', 'солодке', 30)
    cookies_qnt = database.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30, 'Cookies product quantity after inserting is not equal to 30'


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0, 'Product deletion is unsuccessful'


# Testing users ------------------------------------------------------------------------------------------------------ 
@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1', 'User address is not equal'
    assert user[0][1] == 'Kyiv', 'User city is not equal'
    assert user[0][2] == '3127', 'User ZIP code is not equal'
    assert user[0][3] == 'Ukraine', 'User country is not equal'


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()
    print(f'\n{users}')


# Testing orders -----------------------------------------------------------------------------------------------------
@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення:", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1, 'Amount of orders are not equal to 1'

    # Check structure of data
    assert orders[0][0] == 1, 'Count of a product - water with sugar is not equal 1'
    assert orders[0][1] == 'Sergii', "The name of a user is not - 'Sergii'"
    assert orders[0][2] == 'солодка вода', "Thre product first part is not 'солодка вода'"
    assert orders[0][3] == 'з цукром', "Thre product name second part is not 'з цукром'"


# Testing customers --------------------------------------------------------------------------------------------------
@pytest.mark.database
def test_customer_insert(database):
    database.insert_new_customer(88, 'Pavlo', 'Shevchenka 10', 'New York', '56ZMU78', 'USA')
    customer = database.get_full_customer_data_by_id(88)
    database.delete_customer_by_id(88)
    
    assert customer[0] == (88, 'Pavlo', 'Shevchenka 10', 'New York', '56ZMU78', 'USA'), "Customer insertion error!"


@pytest.mark.database
def test_update_customer_city(database):
    database.insert_new_customer(88, 'Pavlo', 'Shevchenka 10', 'New York', '56ZMU78', 'USA')
    database.update_customer_city_by_id('LA', 88)
    city = database.get_customer_city_by_id(88)
    database.delete_customer_by_id(88)

    assert city[0][0] == 'LA', "Customer update error"
