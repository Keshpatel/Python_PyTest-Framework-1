import pytest


def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed "
    assert a == b, "test failed as a is not eq b"


@pytest.mark.home
def test_m2():
    name = 'Selenium'
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


@pytest.mark.home
def test_login_insta():
    assert "admin" == "admin"