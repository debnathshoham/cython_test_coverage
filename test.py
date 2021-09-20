import pytest
from cython_test_coverage.basic_cython import add_test_cython
from python_test import py_diff

@pytest.mark.parametrize("a,b,sum",[(2,5,7), (3,0,3),(-1,5,4), (-1,-3,-4)])
def test_add_cython(a,b,sum):
     assert add_test_cython(a,b)==sum

@pytest.mark.parametrize("a,b,diff", [(4,3,1),(3,4,-1)])
def test_diff_python(a,b,diff):
     assert py_diff(a,b)==diff
