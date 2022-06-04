import pytest
from models.DataCapture import DataCapture


def create_dc():
    datacapture = DataCapture()
    datacapture.add(3)
    datacapture.add(3)
    datacapture.add(4)
    datacapture.add(6)
    datacapture.add(9)
    return datacapture


class TestLess:

    def test_less(self):
        dc = create_dc()
        stats = dc.build_stats()
        less = stats.less(4)
        assert less == [3, 3]

    def test_less_negative(self):
        dc = create_dc()
        stats = dc.build_stats()
        less = stats.less(-4)
        assert less == []

    def test_less_exception(self):
        dc = create_dc()
        stats = dc.build_stats()
        with pytest.raises(TypeError):
            stats.less('a')


class TestGreater:

    def test_greater(self):
        dc = create_dc()
        stats = dc.build_stats()
        greater = stats.greater(4)
        assert greater == [6, 9]

    def test_greater_negative(self):
        dc = create_dc()
        stats = dc.build_stats()
        greater = stats.greater(-4)
        assert greater == dc.elements

    def test_greater_exception(self):
        dc = create_dc()
        stats = dc.build_stats()
        with pytest.raises(TypeError):
            stats.greater('a')


class TestBetween:

    def test_between(self):
        dc = create_dc()
        stats = dc.build_stats()
        between = stats.between(3, 6)
        assert between == [3, 3, 4, 6]

    def test_between_negative_start(self):
        dc = create_dc()
        stats = dc.build_stats()
        between = stats.between(-10, 4)
        assert between == [3, 3, 4]

    def test_between_negative_start(self):
        dc = create_dc()
        stats = dc.build_stats()
        between = stats.between(3, -6)
        assert between == []

    def test_between_exception_start(self):
        dc = create_dc()
        stats = dc.build_stats()
        with pytest.raises(TypeError):
            stats.between('a', 4)

    def test_between_exception_start(self):
        dc = create_dc()
        stats = dc.build_stats()
        with pytest.raises(TypeError):
            stats.between(3, 'a')
