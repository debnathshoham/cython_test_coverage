import pytest
from cython_test_coverage.basic_cython import add_test_cython

@pytest.mark.parametrize("a,b,sum",[(2,5,7), (3,0,3),(-1,5,4)])
def test_add_cython(a,b,sum):
     assert add_test_cython(a,b)==sum