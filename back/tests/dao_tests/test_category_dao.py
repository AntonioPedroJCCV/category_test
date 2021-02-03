import sys
sys.path.append('.')

from sqlalchemy.orm.exc import UnmappedInstanceError
from back.dao.category_dao import CategoryDao
from back.models.category_model import Category
import pytest


class TestCategoryDao:
    @pytest.fixture
    def create_instance(self):
        category = Category('Category name', 'Category Description')
        return category

    def test_instance(self):
        category_dao = CategoryDao()
        assert isinstance(category_dao, CategoryDao)

    def test_save(self, create_instance):
        category_saved = CategoryDao().save(create_instance)
        assert category_saved.id_ is not None
        CategoryDao().delete(category_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            category_saved = CategoryDao().save('category')

    def test_read_by_id(self, create_instance):
        category_saved = CategoryDao().save(create_instance)
        category_read = CategoryDao().read_by_id(category_saved.id_)
        assert isinstance(category_read, Category)
        CategoryDao().delete(category_saved)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            category_read = CategoryDao().read_by_id('category_saved.id_')

    def test_read_all(self):
        category_read = CategoryDao().read_all()
        assert isinstance(category_read, list)

    def test_delete(self, create_instance):
        category_saved = CategoryDao().save(create_instance)
        category_read = CategoryDao().read_by_id(category_saved.id_)
        CategoryDao().delete(category_read)
        category_read = CategoryDao().read_by_id(category_saved.id_)
        assert category_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().delete('category_read')
