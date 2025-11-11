import pytest
from nCr_mod_p import nCr_mod_p

def test_llm_case_1():
    assert nCr_mod_p(10, 2, 13) == 6

def test_llm_case_2():
    assert nCr_mod_p(11, 3, 14) == 11

def test_llm_case_3():
    assert nCr_mod_p(18, 14, 19) == 1

