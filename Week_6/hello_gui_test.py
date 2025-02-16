import pytest

from hello_gui import calculate_area


def test_calculate_area():

    assert calculate_area(3, 5) == 15
    assert calculate_area(4, 6) == 24


pytest.main(["-v", "--tb=line", "-rN", __file__])
# if __name__ == "__main__":
#     test_calculate_area()
#     print("calculate_area PASSED")