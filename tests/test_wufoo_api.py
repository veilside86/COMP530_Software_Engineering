import pytest
import wufoo_api as wa
import wufoo_api_gui
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


def test_checkbox_checked(qtbot):
    window = wufoo_api_gui.MainWindow()
    window.show()

    qtbot.addWidget(window)
    row = 0
    target_item = window.list_control.item(row)
    rect = window.list_control.visualItemRect(target_item)
    click_point = rect.center()
    qtbot.mouseClick(window.list_control.viewport(), Qt.LeftButton, pos=click_point)
    assert window.course_project.isChecked() is True
    assert window.networking_event.isChecked() is False
