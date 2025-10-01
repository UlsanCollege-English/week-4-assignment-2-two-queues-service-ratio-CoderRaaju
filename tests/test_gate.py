import pytest
from src.gate import Gate

def test_basic_arrive_and_serve():
    g = Gate()
    g.arrive("fastpass", "F1")
    g.arrive("regular", "R1")
    g.arrive("regular", "R2")
    g.arrive("regular", "R3")

    # Pattern F, R, R, R
    assert g.serve() == "F1"
    assert g.serve() == "R1"
    assert g.serve() == "R2"
    assert g.serve() == "R3"

def test_serve_skips_empty_lines():
    g = Gate()
    g.arrive("fastpass", "F1")
    # Pattern F, R, R, R
    assert g.serve() == "F1"
    # Regular queue empty, pattern continues, should raise error
    with pytest.raises(IndexError):
        g.serve()

def test_peek_next_line():
    g = Gate()
    g.arrive("fastpass", "F1")
    g.arrive("regular", "R1")
    g.arrive("regular", "R2")

    # Pattern: F, R, R, R
    assert g.peek_next_line() == "fastpass"
    g.serve()  # serve F1
    assert g.peek_next_line() == "regular"
    g.serve()  # serve R1
    assert g.peek_next_line() == "regular"
    g.serve()  # serve R2
    assert g.peek_next_line() is None  # both empty

def test_invalid_line():
    g = Gate()
    with pytest.raises(ValueError):
        g.arrive("vip", "X1")
