import wufoo_api_gui
from secrets import api_key, host, username, dbpassword, port, database
# import urllib3
import json
# import base64
import requests
from requests.auth import HTTPBasicAuth
import sys
import mysql.connector
from typing import Tuple
from PySide6.QtWidgets import QApplication, QLineEdit

url = "https://veilside.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json"

wufoo_db = {
    'host': host,
    'username': username,
    'password': dbpassword,
    'database': database,
    'port': port
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
    # The original method work with window os
    # password = 'bsu'
    #
    # http = urllib3.PoolManager()
    # request = http.request(
    #     'GET', url,
    #     headers={'Authorization': 'Basic ' + base64.b64encode(f'{api_key}:{password}'.encode()).decode()}
    # )
    # data = json.loads(request.data.decode('utf-8'))
    #
    # return data

    # The original method was not working with macos
    response = requests.get(url, auth=HTTPBasicAuth(api_key, "pass"))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(
            f"Failed to get data, response code:{response.status_code} and error message: {response.reason} "
        )
        sys.exit(-1)
    gresponse = response.json()
    return gresponse


def display_gui(data: list):
    qt_app = QApplication(sys.argv)
    mainwindow = wufoo_api_gui.MainWindow(data)
    sys.exit(qt_app.exec())


def main():
    # while True:
    conn, cursor = open_db()
    all_data = get_data()
    entry_data = all_data['Entries']
    setup_db(cursor)
    save_db(cursor, entry_data)
    close_db(conn)
    display_gui(entry_data)

    # test_data = [{'EntryId': '1', 'Field2': 'Mr.', 'Field4': 'Samuel', 'Field5': 'Adams',
    #               'Field6': 'Beer', 'Field7': 'Brewery',
    #               'Field12': 'samadams@brewery.org', 'Field9': 'samadamsbostonbrewery.com',
    #               'Field10': '1864596545', 'Field14': '', 'Field15': '',
    #               'Field16': 'Site Visit', 'Field17': 'Job Shadow', 'Field18': '',
    #               'Field19': 'Career Panel', 'Field20': 'Networking Event',
    #               'Field114': '',
    #               'Field115': '',
    #               'Field116': 'Spring 2023 (January 2023- April 2023)',
    #               'Field117': '',
    #               'Field118': '', 'Field214': 'Yes'},
    #              {'EntryId': '2', 'Field2': 'Ms.', 'Field4': 'Lisa', 'Field5': 'Wufoo',
    #               'Field6': 'Teacher', 'Field7': 'BSU',
    #               'Field12': 'l1wufoo@bridgew.edu', 'Field9': 'bridgew.edu',
    #               'Field10': '1234567890', 'Field14': '', 'Field15': '',
    #               'Field16': '', 'Field17': 'Job Shadow', 'Field18': '',
    #               'Field19': 'Career Panel', 'Field20': 'Networking Event',
    #               'Field114': '',
    #               'Field115': '',
    #               'Field116': '',
    #               'Field117': '',
    #               'Field118': 'Other', 'Field214': 'No'}
    #              ]
    # display_gui(test_data)
    # save_data(entry_data)
    # time.sleep()


# uvicorn
if __name__ == '__main__':
    main()
