import wufoo_api_gui
from secrets import api_key, host, username, dbpassword, port, database, gmail_user, gmail_password
# import urllib3
import json
# import base64
import requests
from requests.auth import HTTPBasicAuth
import sys
import mysql.connector
from typing import Tuple
from PySide6.QtWidgets import QApplication
import smtplib

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
            Email, Organization_Website, Interested_Opt1, Interested_Opt2, Interested_Opt3,
            Interested_Opt4, Interested_Opt5, Interested_Opt6, Interested_Opt7, Collabo_Time_Opt1,
            Collabo_Time_Opt2, Collabo_Time_Opt3, Collabo_Time_Opt4, Collabo_Time_Opt5, Permission)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (wufoo_data['EntryId'], wufoo_data['Field2'], wufoo_data['Field4'], wufoo_data['Field5'],
             wufoo_data['Field6'], wufoo_data['Field7'], wufoo_data['Field12'], wufoo_data['Field9'],
             wufoo_data['Field14'], wufoo_data['Field15'], wufoo_data['Field16'], wufoo_data['Field17'],
             wufoo_data['Field18'], wufoo_data['Field19'], wufoo_data['Field20'], wufoo_data['Field114'],
             wufoo_data['Field115'], wufoo_data['Field116'], wufoo_data['Field117'],
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
    json_response = response.json()
    return json_response


def display_gui():
    qt_app = QApplication(sys.argv)
    my_window = wufoo_api_gui.MainWindow()
    my_window.show()
    sys.exit(qt_app.exec())


def claim_by_email():
    sent_from = gmail_user
    receive_to = ['person_a@gmail.com', 'person_b@gmail.com']
    subject = 'Testing for smtp email'
    body = 'aaaa'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(receive_to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, receive_to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


def choose_menu():
    while True:
        print("======= Select the menu =======")
        print("Update data from wufoo form [U]")
        print("Data visualization [D]")
        print("Exit program [E]")
        print("===============================")

        # menu = input("Enter: ").lower()
        menu = 'd'

        if menu == 'u':
            conn, cursor = open_db()
            all_data = get_data()
            all_data = all_data['Entries']
            setup_db(cursor)
            save_db(cursor, all_data)
            close_db(conn)
            print("Updated Data")
            print("")
        elif menu == 'd':
            display_gui()
        elif menu == 'e':
            sys.exit(0)
        else:
            print("Invalid menu")


def main():
    choose_menu()


if __name__ == '__main__':
    main()
