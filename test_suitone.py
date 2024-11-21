import pytest

# First Code
@pytest.mark.smoke
def test_suit1() :
    print("Test_suit1_method11")


def test_suit1_method2() :
    print("Test_suit1_method22")


def test_suit1_method3() :
    print("Test_suit1_method33")


@pytest.mark.smoke
def test_mytest():
    print("custom mark1")

#Code End


