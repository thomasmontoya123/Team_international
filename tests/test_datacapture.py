import pytest
from models.DataCapture import DataCapture


class TestAdd:
    def test_add(self):
        datacapture = DataCapture()
        num = 10
        datacapture.add(num)
        assert datacapture.elements == [10]

    def test_add_negative(self):
        datacapture = DataCapture()
        num = -10
        with pytest.raises(ValueError):
            datacapture.add(num)

    def test_add_excpetion(self):
        datacapture = DataCapture()
        num = 'a'
        with pytest.raises(TypeError):
            datacapture.add(num)
