import pytest
from utils import ObjectDisplayMixin

class TestObjectDisplayMixin():

    @pytest.fixture
    def objectdisplaymixin_object(self):
        obj = ObjectDisplayMixin()
        yield obj

    def test_str_method(self):
        obj = TestObjectDisplayMixin("value1", "value2")
        self.assertEqual(str(obj), "TestRepresentation(attribute1='value1', attribute2='value2')")

    def test_repr_method(self):
        obj = TestObjectDisplayMixin("value1", "value2")
        self.assertEqual(repr(obj), "TestRepresentation(attribute1='value1', attribute2='value2')")

if __name__ == '__main__':
    unittest.main()

