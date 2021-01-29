import sys
sys.path.append('.')

import pytest
from back.models.category_model import Category


def test_type_name():
    with pytest.raises(TypeError):
        category_test = Category(25.0, 'Description test')


def test_empty_name():
    with pytest.raises(ValueError):
        category_test = Category('', 'Description test')


def test_len_name():
    with pytest.raises(ValueError):
        category_test = Category('i'*101, 'Description test')


def test_type_description():
    with pytest.raises(TypeError):
        category_test = Category('Name test', 25.0)


def test_len_description():
    with pytest.raises(ValueError):
        category_test = Category('Name test', 'Description test' * 500)
