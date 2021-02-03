import sys
sys.path.append('.')

from back.dao.base_dao import BaseDao
from back.controllers.base_controller import BaseController
import pytest


class TestBaseDao:
    @pytest.fixture
    def create_instance(self):
        base_controller = BaseController(BaseDao)
        return base_controller

    def test_instance(self, create_instance):
        assert create_instance, "Dao creation error!"

    def test_is_istance(self, create_instance):
        assert isinstance(create_instance, BaseController)
