from arithmeticFun import mult, div

def test_MulFirst():
    assert mult (10,20) == 200

def test_MulSecond():
    assert mult(10, -20) == -200

def test_DivFirst():
    assert div(10,20) == 2

def test_DivSecond():
    assert div (10,-20) == -2

def test_DivThird():
    import pytest
    with pytest.raises(ZeroDivisionError):
        assert div(100,0)

