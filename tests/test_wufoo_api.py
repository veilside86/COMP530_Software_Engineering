import wufoo_api as wa
import mysql.connector
from typing import Tuple


# assign test_open_db for setup test database on the server
def test_open_db() -> Tuple[mysql.connector.MySQLConnection, mysql.connector.MySQLConnection.cursor]:
    db_connection = mysql.connector.connect(**wa.wufoo_db)
    cursor = db_connection.cursor()

    return db_connection, cursor


def test_save_db():
    conn, cursor = wa.open_db()

    cursor.execute('''SELECT First_Name FROM wufoo''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Junseok'
    cursor.execute('''SELECT Last_Name FROM wufoo''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Hur'
    cursor.execute('''SELECT Email FROM wufoo''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'gjwnstjr100@gmail.com'


def test_get_data():
    test_data = wa.get_data()
    test_result = test_data['Entries']
    assert len(test_result) > 10


# Test to make there is data in database table
def test_database_has_data():
    conn, cursor = wa.open_db()
    cursor.execute('''SELECT count(*) FROM wufoo''')
    count = cursor.fetchone()[0]
    assert count > 0


# class TestCheckBox:
#     def test_checkbox_checked(self):
#         wa.display_gui(data)

