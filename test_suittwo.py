import pytest

# Second Code
@pytest.mark.smoke
def test_suit2() :
    print("Test_suit2_method11")


def test_suit2_method2() :
    print("Test_suit2_method22")


def test_suit2_method3() :
    print("Test_suit2_method33")

@pytest.mark.smoke
def test_mytest():
    print("custom mark2")


