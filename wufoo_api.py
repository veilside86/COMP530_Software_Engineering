from secrets import api_key
import urllib3
import json
import base64
import sqlite3
from typing import Tuple

url = "https://veilside.wufoo.com/api/v3/forms/cubes-project-proposal-submission/" \
      "entries.json?sort=EntryId&sortDirection=DESC"


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)   # connect to existing DB or create new one
    cursor = db_connection.cursor()     # get ready to read/write data

    return db_connection, cursor
    

def setup_db(cursor: sqlite3.Cursor):
    cursor.execute("DROP TABLE IF EXISTS wufoo")
    cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo(
    Entry_Id INTEGER PRIMARY KEY,
    Prefix TEXT NOT NULL,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Title TEXT NOT NULL,
    Organization_Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Organization_Website TEXT NOT NULL,
    Phone INTEGER,
    Field14 TEXT,
    Field15 TEXT,
    Field16 TEXT,
    Field17 TEXT,
    Field18 TEXT,
    Field19 TEXT,
    Field20 TEXT,
    Field114 TEXT,
    Field115 TEXT,
    Field116 TEXT,
    Field117 TEXT,
    Field118 TEXT,
    Permission TEXT
    );''')


def save_db(cursor, data):
    for wufoo_data in data:
        cursor.execute(
            """INSERT INTO wufoo(Entry_Id, Prefix, First_Name, Last_Name, Title, Organization_Name,
            Email, Organization_Website, Phone, Field14, Field15, Field16, Field17, Field18, Field19,
            Field20, Field114, Field115, Field116, Field117, Field118, Permission) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (wufoo_data['EntryId'], wufoo_data['Field2'], wufoo_data['Field4'], wufoo_data['Field5'],
             wufoo_data['Field6'], wufoo_data['Field7'], wufoo_data['Field12'], wufoo_data['Field9'],
             wufoo_data['Field10'], wufoo_data['Field14'], wufoo_data['Field15'], wufoo_data['Field16'],
             wufoo_data['Field17'], wufoo_data['Field18'], wufoo_data['Field19'], wufoo_data['Field20'],
             wufoo_data['Field114'], wufoo_data['Field115'], wufoo_data['Field116'], wufoo_data['Field117'],
             wufoo_data['Field118'], wufoo_data['Field214']))


def close_db(connection: sqlite3.Connection):
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
    conn, cursor = open_db("wufoo_db.sqlite")
    all_data = get_data()
    entry_data = all_data['Entries']
    setup_db(cursor)
    # print(entry_data)
    save_db(cursor, entry_data)
    close_db(conn)
    # save_data(all_data)


if __name__ == '__main__':
    main()
