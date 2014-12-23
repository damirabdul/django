from utils import fact

def test_fact0():
    assert fact(0) == 1
def test_fact_1():
    assert fact(1) == 0
def test_fact():
    n = 5
    assert fact(2) == 2