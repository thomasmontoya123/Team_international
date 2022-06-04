import pytest
from decorators.positive_validation import positive_validation


class TestPositiveDecorator:

    def test_validation(self):

        @positive_validation(decorating_class=False)
        def func(n):
            return n

        assert func(10) == 10

    def test_validation_negative(self):

        @positive_validation(decorating_class=False)
        def func(n):
            return n

        with pytest.raises(ValueError):
            func(-1)
