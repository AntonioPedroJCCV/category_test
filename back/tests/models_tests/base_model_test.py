import sys
sys.path.append('.')

from back.models.base_model import BaseModel
import pytest


class TestBaseModel:
    @pytest.fixture
    def create_instance(self):
        base_model = BaseModel()
        return base_model

    def test_instance(self, create_instance):
        assert create_instance, "Dao creation error!"

    def test_is_istance(self, create_instance):
        assert isinstance(create_instance, BaseModel)
