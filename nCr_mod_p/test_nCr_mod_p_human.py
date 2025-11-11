from hypothesis import given, strategies as st
from nCr_mod_p import nCr_mod_p

@given(st.integers(min_value=1, max_value=20), st.integers(min_value=0, max_value=10), st.integers(min_value=2, max_value=30))
def test_mod_range(n, r, p):
    if r > n: return
    val = nCr_mod_p(n, r, p)
    assert 0 <= val < p
