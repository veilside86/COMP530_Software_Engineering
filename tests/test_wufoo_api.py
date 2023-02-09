import wufoo_api as wa
import mysql.connector
from typing import Tuple

# connection detail for testing database server
test_wufoo_db = {
    'host': "db-mysql-nyc1-12016-do-user-13526185-0.b.db.ondigitalocean.com",
    'username': "doadmin",
    'password': 'AVNS_Kh4wgDoWwLrcGGjTc0o',
    'database': 'test_wufoo_db',
    'port': '25060'
}


def test_get_data():
    conn, cursor = wa.open_db()
    data = wa.get_data()
    test_data = data['Entries']
    wa.close_db(conn)
    assert len(test_data) > 10


# assign test_open_db for setup test database on the server
def test_open_db() -> Tuple[mysql.connector.MySQLConnection, mysql.connector.MySQLConnection.cursor]:
    db_connection = mysql.connector.connect(**test_wufoo_db)
    cursor = db_connection.cursor()

    return db_connection, cursor


def test_save_db():
    # call test_open_db to open the DB for testing
    conn, cursor = test_open_db()
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

    conn, cursor = test_open_db()
    cursor.execute('''SELECT Last_Name FROM wufoo''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Adams'
