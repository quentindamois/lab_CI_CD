from app import add # or app instance, depending on your project structure

def test_add():
    res = add(1, 2)
    assert res == 3

