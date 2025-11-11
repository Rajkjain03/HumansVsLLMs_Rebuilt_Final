from hypothesis import given, strategies as st
from profit_amount import profit_amount

@given(st.integers(min_value=0, max_value=5000), st.integers(min_value=0, max_value=5000))
def test_profit_logic(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac > sa:
        assert res == ac - sa
    else:
        assert res is None
