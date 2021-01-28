from back.models.category_model import Category


def empty_name_test():
    try:
        category_test = Category('', 'Description test')
    except Exception as e:
        assert isinstance(e, ValueError)


def type_name_test():
    try:
        category_test = Category(25.0, 'Description test')
    except Exception as e:
        assert isinstance(e, TypeError)


def len_name_test():
    try:
        category_test = Category('Name test' * 500, 'Description test')
    except Exception as e:
        assert isinstance(e, ValueError)


def type_description_test():
    try:
        category_test = Category('Name test', 25.0)
    except Exception as e:
        assert isinstance(e, TypeError)


def len_description_test():
    try:
        category_test = Category('Name test', 'Description test' * 500)
    except Exception as e:
        assert isinstance(e, ValueError)
