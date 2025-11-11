import pytest
from profit_amount import profit_amount

def test_llm_case_1():
    assert profit_amount(1500,1200)==300

def test_llm_case_2():
    assert profit_amount(100,200)==None

def test_llm_case_3():
    assert profit_amount(2000,5000)==None

