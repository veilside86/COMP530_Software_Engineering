from secrets import api_key
import urllib3
import json
import base64
import mysql.connector
from typing import Tuple

url = "https://veilside.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json"

wufoo_db = {
    'host': "db-mysql-nyc1-12016-do-user-13526185-0.b.db.ondigitalocean.com",
    'username': "doadmin",
    'password': 'AVNS_Kh4wgDoWwLrcGGjTc0o',
    'database': 'wufoo_db',
    'port': '25060'
}


# open_db with mysql
def open_db() -> Tuple[mysql.connector.MySQLConnection, mysql.connector.MySQLConnection.cursor]:
    db_connection = mysql.connector.connect(**wufoo_db)
    cursor = db_connection.cursor()

    return db_connection, cursor


# setup_db with mysql
def setup_db(cursor: mysql.connector.MySQLConnection.cursor):
    cursor.execute('''DROP TABLE IF EXISTS wufoo''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo (
    Entry_Id INT PRIMARY KEY,
    Prefix VARCHAR(20) NOT NULL,
    First_Name VARCHAR(20) NOT NULL,
    Last_Name VARCHAR(20) NOT NULL,
    Title VARCHAR(30) NOT NULL,
    Organization_Name VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Organization_Website VARCHAR(100) NOT NULL,
    Phone BIGINT,
    Interested_Opt1 VARCHAR(50),
    Interested_Opt2 VARCHAR(50),
    Interested_Opt3 VARCHAR(50),
    Interested_Opt4 VARCHAR(50),
    Interested_Opt5 VARCHAR(50),
    Interested_Opt6 VARCHAR(50),
    Interested_Opt7 VARCHAR(50),
    Collabo_Time_Opt1 VARCHAR(100),
    Collabo_Time_Opt2 VARCHAR(100),
    Collabo_Time_Opt3 VARCHAR(100),
    Collabo_Time_Opt4 VARCHAR(100),
    Collabo_Time_Opt5 VARCHAR(100),
    Permission VARCHAR(100)
    );''')


def save_db(cursor, data):
    for wufoo_data in data:
        cursor.execute(
            """INSERT INTO wufoo(Entry_Id, Prefix, First_Name, Last_Name, Title, Organization_Name,
            Email, Organization_Website, Phone, Interested_Opt1, Interested_Opt2, Interested_Opt3,
            Interested_Opt4, Interested_Opt5, Interested_Opt6, Interested_Opt7, Collabo_Time_Opt1,
            Collabo_Time_Opt2, Collabo_Time_Opt3, Collabo_Time_Opt4, Collabo_Time_Opt5, Permission)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (wufoo_data['EntryId'], wufoo_data['Field2'], wufoo_data['Field4'], wufoo_data['Field5'],
             wufoo_data['Field6'], wufoo_data['Field7'], wufoo_data['Field12'], wufoo_data['Field9'],
             wufoo_data['Field10'], wufoo_data['Field14'], wufoo_data['Field15'], wufoo_data['Field16'],
             wufoo_data['Field17'], wufoo_data['Field18'], wufoo_data['Field19'], wufoo_data['Field20'],
             wufoo_data['Field114'], wufoo_data['Field115'], wufoo_data['Field116'], wufoo_data['Field117'],
             wufoo_data['Field118'], wufoo_data['Field214']))


def close_db(connection: mysql.connector.connect):
    connection.commit()
    connection.close()


def save_data(data, filename='wufoo.text'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def get_data() -> dict:
    password = 'bsu'

    http = urllib3.PoolManager()
    request = http.request(
        'GET', url,
        headers={'Authorization': 'Basic ' + base64.b64encode(f'{api_key}:{password}'.encode()).decode()}
    )
    data = json.loads(request.data.decode('utf-8'))

    return data


def main():
    conn, cursor = open_db()
    all_data = get_data()
    entry_data = all_data['Entries']
    # print(len(entry_data))
    setup_db(cursor)
    # print(entry_data)
    save_db(cursor, entry_data)
    close_db(conn)
    # save_data(entry_data)


if __name__ == '__main__':
    main()
