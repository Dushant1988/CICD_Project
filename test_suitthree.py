import pytest


@pytest.mark.smoke
def test_suit3() :
    print("Test_suit3_method11")

def test_suit3_method2() :
    print("Test_suit3_method22")

def test_suit3_method3() :
    print("Test_suit3_method33")

@pytest.mark.smoke
def test_mytest():
    print("custom mark3")


