import pytest
from subset import subset

def test_llm_case_1():
    assert subset([1, 2, 3, 4],4) == 1

def test_llm_case_2():
    assert subset([5, 6, 9, 3, 4, 3, 4],7) == 2

def test_llm_case_3():
    assert subset([1, 2, 3 ],3) == 1

