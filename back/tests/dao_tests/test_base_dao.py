import sys
sys.path.append('.')

from back.models.base_model import BaseModel
from back.dao.base_dao import BaseDao
import pytest


class TestBaseDao:
    @pytest.fixture
    def create_instance(self):
        base_dao = BaseDao(BaseModel)
        return base_dao

    def test_instance(self, create_instance):
        assert create_instance, "Dao creation error!"

    def test_is_istance(self, create_instance):
        assert isinstance(create_instance, BaseDao)
