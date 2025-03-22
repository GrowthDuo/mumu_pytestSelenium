import pytest
from pytest_assume.plugin import assume

class TestAssert:
    def test_assert(self):
        # pytest-assert方法1：
        with assume: assert 'will' in 'will ui'

        # pytest-assert方法2：
        pytest.assume(1 == 2)  # 即使这个断言失败，后续断言仍会执行
        pytest.assume(3 == 3)  # 这个断言会成功
        pytest.assume(2 == 3)  # 这个断言会失败
        # 方法3
        assert (1+1 == 2)
        print('over')
