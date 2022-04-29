import main


def test_get_doc_shelf():
    assert main.get_doc_shelf('10006') == '2', 'Тест №1 не пройден'


def test_add_new_doc():
    num_shelf = 100
    assert main.add_new_doc('My fuhrer', 'passport', 'My brother', num_shelf) == num_shelf, 'Тест №2 не пройден'


def test_delete_doc():
    num_doc = '10006'
    assert main.delete_doc(num_doc) != main.check_document_existance(num_doc), 'Тест №3 не пройден'


