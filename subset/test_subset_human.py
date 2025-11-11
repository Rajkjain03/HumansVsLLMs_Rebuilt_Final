from hypothesis import given, strategies as st
from subset import subset

@given(st.lists(st.integers(), min_size=1, max_size=10))
def test_non_negative(lst):
    assert subset(lst, len(lst)) >= 0
