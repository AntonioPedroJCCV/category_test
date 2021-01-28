import sys
sys.path.append('.')


from back.models.category_model import Category


def test_empty_name():
    try:
        category_test = Category('', 'Description test')
    except Exception as e:
        assert isinstance(e, ValueError)


def test_type_name():
    try:
        category_test = Category(25.0, 'Description test')
    except Exception as e:
        assert isinstance(e, TypeError)


def test_len_name():
    try:
        category_test = Category('Name test' * 500, 'Description test')
    except Exception as e:
        assert isinstance(e, ValueError)


def test_type_description():
    try:
        category_test = Category('Name test', 25.0)
    except Exception as e:
        assert isinstance(e, TypeError)


def test_len_description():
    try:
        category_test = Category('Name test', 'Description test' * 500)
    except Exception as e:
        assert isinstance(e, ValueError)
