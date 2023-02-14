import wufoo_api as wa
from secrets import host, username, dbpassword, test_database, port
import mysql.connector
from typing import Tuple

# connection detail for testing database server
test_wufoo_db = {
    'host': host,
    'username': username,
    'password': dbpassword,
    'database': test_database,
    'port': port
}


# assign test_open_db for setup test database on the server
def test_open_db() -> Tuple[mysql.connector.MySQLConnection, mysql.connector.MySQLConnection.cursor]:
    db_connection = mysql.connector.connect(**wa.wufoo_db)
    cursor = db_connection.cursor()

    return db_connection, cursor


def test_save_db():
    # call test_open_db to open the DB for testing
    conn, cursor = wa.open_db()
    wa.setup_db(cursor)
    # fake data to test save to database method
    test_data = [{'EntryId': '36', 'Field2': 'Mr.', 'Field4': 'Samuel', 'Field5': 'Adams',
                  'Field6': 'Beer', 'Field7': 'Brewery',
                  'Field12': 'samadams@brewery.org', 'Field9': 'samadamsbostonbrewery.com',
                  'Field10': '1864596545', 'Field14': '', 'Field15': '',
                  'Field16': 'Site Visit', 'Field17': 'Job Shadow', 'Field18': '',
                  'Field19': 'Career Panel', 'Field20': 'Networking Event',
                  'Field114': '',
                  'Field115': '',
                  'Field116': 'Spring 2023 (January 2023- April 2023)',
                  'Field117': '',
                  'Field118': '', 'Field214': 'Yes'}]
    wa.save_db(cursor, test_data)
    wa.close_db(conn)

    conn, cursor = wa.open_db()
    cursor.execute('''SELECT Last_Name FROM wufoo''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Adams'


def test_get_data():
    test_data = wa.get_data()
    test_result = test_data['Entries']
    assert len(test_result) > 10
