from hypothesis import given, strategies as st
from max_similar_indices import max_similar_indices

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1),
       st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_each_element_max(list1, list2):
    n = min(len(list1), len(list2))
    res = max_similar_indices(list1, list2)
    for i in range(n):
        a,b = list1[i], list2[i]
        assert res[i][0] >= a[0] and res[i][0] >= b[0]
        assert res[i][1] >= a[1] and res[i][1] >= b[1]
