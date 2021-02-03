import sys
sys.path.append('.')

import pytest
from back.models.category_model import Category


class TestCategoryModel:
    @pytest.mark.parametrize("name, description", 
        [(1, 'Description test'),
        (1.9, 'Description test'),
        (True, 'Description test'),
        (None, 'Description test')]
    )
    def test_type_name(self, name, description):
        with pytest.raises(TypeError):
            category_test = Category(name, description)

    def test_empty_name(self):
        with pytest.raises(ValueError):
            category_test = Category('', 'Description test')

    def test_len_name(self):
        with pytest.raises(ValueError):
            category_test = Category('i'*101, 'Description test')


    @pytest.mark.parametrize("name, description", 
        [('Name test', 1),
        ('Name test', 1.9),
        ('Name test', True),
        ('Name test', None)]
    )
    def test_type_description(self, name, description):
        with pytest.raises(TypeError):
            category_test = Category(name, description)

    def test_len_description(self):
        with pytest.raises(ValueError):
            category_test = Category('Name test', 'Description test' * 500)
