import sys
sys.path.append('.')

from back.controllers.base_controller import BaseController
from back.controllers.category_controller import CategoryController
from back.models.category_model import Category
import pytest


class TestCategoryController:
    @pytest.fixture
    def create_controller(self):
        controller = CategoryController()
        return controller

    def test_category_controller_instance(self, create_controller):
        assert isinstance(create_controller, BaseController)
        assert isinstance(create_controller, CategoryController)

    def test_read_all_should_return_list(self, create_controller):
        result = create_controller.read_all()
        assert isinstance(result, list)

    def test_create_category(self, create_controller):
        name = 'Category name'
        description = 'Category description'
        category = Category(name, description)
        result = create_controller.create(category)
        assert result.id_ is not None
        assert result.name == name
        assert result.description == description
        create_controller.delete(result)

    def test_update_category(self, create_controller):
        name = 'Category name'
        description = 'Category description'
        category = Category(name, description)

        created = create_controller.create(category)
        created.name = 'Category name 2'
        created.description = 'Category description 2'

        result = create_controller.update(created)
        assert result.id_ is not None
        assert result.name == 'Category name 2'
        assert result.description == 'Category description 2'
        create_controller.delete(result)

    def test_delete_category(self, create_controller):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = create_controller.create(category)
        create_controller.delete(created)
        with pytest.raises(Exception) as exc:
            create_controller.read_by_id(created.id_)
            assert exc.value == 'Object not found in the database.'

    def test_read_by_id_should_return_category(self, create_controller):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = create_controller.create(category)

        result = create_controller.read_by_id(created.id_)
        assert isinstance(result, Category)
        assert result.name == name
        assert result.description == description
        create_controller.delete(created)

    def test_read_by_id_with_invalid_id_should_raise_exception(self, create_controller):
        with pytest.raises(Exception) as exc:
            create_controller.read_by_id(71289379)
            assert exc.value == 'Object not found in the database.'
