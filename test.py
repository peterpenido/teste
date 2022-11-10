from main import main
import pytest


def test_answer_1():    assert main(3,5) == 15
def test_answer_2():    assert main(1,0) == 0
def test_answer_3():    assert main(2,1) != 3

@pytest.mark.skip(reason="OK")
def test_answer_4():    assert main(3,2) == 6

def test_answer():    
    assert main(3,2) == 6
    assert main(1,1) == 1
    assert main(2,2) == 4
    assert main(3,3) == 9

