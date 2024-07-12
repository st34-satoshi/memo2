def add(x, y):
    return x+y

def test_add_01():
    assert add(1, 2) == 3

def test_add_02():
    assert add(2, 3) == 5

def test_add_03():
    assert add(3, 4) == 7