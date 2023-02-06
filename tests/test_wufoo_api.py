import wufoo_api as wa
# import pytest


def test_save_db():
    conn, cursor = wa.open_db('testdb.sqlite')
    wa.setup_db(cursor)
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

    conn, cursor = wa.open_db('testdb.sqlite')
    cursor.execute('''SELECT Last_Name FROM wufoo''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Adams'


# def test_get_data():
#     data = wa.get_data()
#     test_data = data['Entries']
#     assert len(test_data) > 10
