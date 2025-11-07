from contextlib import nullcontext as does_not_raise

import pytest

from src.bin_search import bin_search


class TestBin:
    @pytest.mark.parametrize(
        "array, digit, expected_index, expectation",
        [
            ([1, 2, 3, 4, 5], 3, 2, does_not_raise()),
            ([1, 2, 3, 4], 2, 1, does_not_raise()),
            ([1, 2, 3, 4], 3, 2, does_not_raise()),
            ([1], 1, 0, does_not_raise()),
            ([1, 2], 1, 0, does_not_raise()),
            ([1, 2], 2, 1, does_not_raise()),
        ],
    )
    def test_middle(self, array, digit, expected_index, expectation):
        with expectation:
            assert bin_search(array, digit) == expected_index

    def test_start(self):
        assert bin_search([1, 2, 3, 4], 2) == 1

    def test_empty_list(self):
        assert bin_search([], 1) == -1

    def test_incorrect_index(self):
        assert bin_search([1, 2], 3) == -1
        assert bin_search([1, 2, 3, 4], 5) == -1
