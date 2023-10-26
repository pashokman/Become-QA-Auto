import pytest

@pytest.mark.database
def test_database_connection(database):
    database.test_connection()

@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()
    print(f'\n{users}')

@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, 'печиво', 'солодке', 30)
    cookies_qnt = database.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення:", orders)
    # Check quantity of orders equal to 2
    assert len(orders) == 2

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

# Additional tests
@pytest.mark.database
def test_customer_insert(database):
    database.insert_new_customer(88, 'Pavlo', 'Shevchenka 10', 'New York', '56ZMU78', 'USA')
    customer = database.get_full_customer_data_by_id(88)
    database.delete_customer_by_id(88)
    
    assert customer[0] == (88, 'Pavlo', 'Shevchenka 10', 'New York', '56ZMU78', 'USA')


@pytest.mark.database
def test_update_customer_city(database):
    database.insert_new_customer(88, 'Pavlo', 'Shevchenka 10', 'New York', '56ZMU78', 'USA')
    database.update_customer_city_by_id('LA', 88)
    city = database.get_customer_city_by_id(88)
    database.delete_customer_by_id(88)

    assert city[0][0] == 'LA'

@pytest.mark.database
def test_get_sum_of_quantity_products(database):
    sum = database.get_products_qnt_sum()
    
    assert sum[0][0] == 75

@pytest.mark.database
def test_get_max_product_quantity(database):
    max = database.get_max_product_qnt()

    assert max[0][0] == 30
    

