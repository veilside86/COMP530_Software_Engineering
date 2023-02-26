import pytest
import wufoo_api as wa
from wufoo_api_gui import MainWindow
import mysql.connector
from typing import Tuple
from PySide6.QtCore import Qt


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


def test_get_checkbox_data():
    conn, cursor = wa.open_db()
    cursor.execute('''SELECT Entry_Id, Prefix, First_Name, Last_Name, Title, Organization_Name,
                Email, Organization_Website, Phone, Interested_Opt1, Interested_Opt2, Interested_Opt3,
                Interested_Opt4, Interested_Opt5, Interested_Opt6, Interested_Opt7, Collabo_Time_Opt1,
                Collabo_Time_Opt2, Collabo_Time_Opt3, Collabo_Time_Opt4, Collabo_Time_Opt5, Permission FROM wufoo''')
    results = cursor.fetchone()

    return results


@pytest.fixture
def test_app(qtbot):
    results = test_get_checkbox_data()
    test_gui = wa.display_gui(results)
    qtbot.addWidget(test_gui)

    return test_gui


def test_checkbox_checked(qtbot):
    results = test_get_checkbox_data()
    window = MainWindow(results)
    window.show()

    spy = qtbot.wait_signal(window.data_window.checkbox.stateChanged)
    qtbot.mouseClick(window.data_window.checkbox, Qt.LeftButton)
    spy.wait()

    assert window.data_window.checkbox.isChecked()
