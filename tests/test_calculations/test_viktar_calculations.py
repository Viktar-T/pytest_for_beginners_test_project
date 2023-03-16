import pytest

from calculations import calculate_sum, \
                        calculate_product, \
                        calculate_dividend, \
                        calculate_difference


class TestCalculations:

    @pytest.mark.parametrize("a, b, sum",
                             [(2, 3, 5),
                              (5, 5, 10)])
    def test_calculate_sum(self, a, b, sum):
        assert a + b == sum

    @pytest.mark.parametrize("a, b, sum",
                             [(2, 3, 10)])
    def test_calculate_sum_erro(self, a, b, sum):
        assert a + b != sum

