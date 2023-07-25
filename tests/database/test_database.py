from sqlite3 import IntegrityError
import sqlite3
import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


# @pytest.mark.database
# def test_check_all_users():
#     db = Database()
#     users = db.get_all_users()

#     print(users)

# @pytest.mark.database
# def test_check_user_sergii():
#     db = Database()
#     user = db.get_user_address_by_name('Sergii')

#     assert user[0][0] == 'Maydan Nezalezhnosti 1'
#     assert user[0][1] == 'Kyiv'
#     assert user[0][2] == '3127'
#     assert user[0][3] == 'Ukraine'

# @pytest.mark.database
# def test_product_qnt_update():
#     db = Database()
#     db.update_product_qnt_by_id(1, 25)
#     water_qnt = db.select_product_qnt_by_id(1)
    
#     assert water_qnt[0][0] == 25
    
# @pytest.mark.database
# def test_product_insert():
#     db = Database()
#     db.insert_products(4, 'печиво', 'солодке', 30)
#     water_qnt = db.select_product_qnt_by_id(4)

#     assert water_qnt[0][0] == 30

# @pytest.mark.database
# def test_product_delete():
#     db = Database()
#     db.insert_products(99, 'тестові', 'дані', 999)
#     db.delete_product_by_id(99)
#     qnt = db.select_product_qnt_by_id(99)

#     assert len(qnt) == 0

# @pytest.mark.database
# def test_detailed_orders():
#     db = Database()
#     orders = db.get_detailed_orders()
#     print("Замовлення", orders)
#     # Check quantity of orders equal to 1
#     assert len(orders) == 1

#     # Check struture of data
#     assert orders[0][0] == 1
#     assert orders[0][1] == 'Sergii'
#     assert orders[0][2] == 'солодка вода'
#     assert orders[0][3] == 'з цукром'


# Individual tests
@pytest.mark.database
def test_check_column_types():
    db = Database()
    table = db.get_column_types('products')

    assert table[0][3] == 1
    assert table[0][5] == 1

@pytest.mark.database
def test_check_customers_required_field():
    db = Database()
    # тимчасова зміна для перевірки обов'язкового поля Name
    insert_error = False
    # Перехоплення виключення
    try:
        db.insert_customer_without_name(3, 'Heroiv Ukraine', 'New York')
    except sqlite3.IntegrityError as e:
        # Перехопили помилку
        insert_error = True

    assert insert_error is True

@pytest.mark.database
def test_long_int_id():
    db = Database()
    insert_error = True
    # Перехоплення виключення
    try:
        db.insert_products(123456789012345678901, 'цукерка', 'Джек', 0.5)
    except sqlite3.IntegrityError as e:
        # Перехопили помилку
        insert_error = False

    assert insert_error is True
