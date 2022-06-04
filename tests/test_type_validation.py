import pytest
from decorators.type_validator import type_validation


class TestTypeValidation:

    def test_type_validation(self):

        @type_validation([int])
        def func(n):
            return n

        assert func(10) == 10

    def test_type_validation_multi_params(self):

        @type_validation([int, str])
        def func(n, x):
            return n

        assert func(10, 'a') == 10

    def test_type_validation_diff_types(self):

        @type_validation([int])
        def func(n):
            return n

        with pytest.raises(TypeError):
            func('a')

    def test_type_validation_multi_params_exception(self):

        @type_validation([int, int])
        def func(n, x):
            return n

        with pytest.raises(TypeError):
            func(10, 'a')
