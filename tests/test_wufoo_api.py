import wufoo_api as wa


def test_get_data():
    data = wa.get_data()
    assert len(data) == 1
