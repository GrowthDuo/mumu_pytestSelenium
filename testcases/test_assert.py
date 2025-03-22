import pytest
from selenium.webdriver.common.by import By


class TestAssert:
    def test_assert(self):
        assert 'wall' == 'wall'
        assert 'wall_a' != 'wall_b'
        assert 5 < 6
        assert 5 > (1 + 3)
        assert 5 >= (2 + 3)
        assert 5 <= (2 + 3)
        # 包含和不包含
        assert 'wall' in 'waller'
        assert 'wall' not in 'wa'
        # true 和 false   一般适用于判断元素是否存在
        assert 1
        assert (9 < 10) is True
        assert not False

        # alert_element = driver.find_elements(By.ID, 'alert-box')
        # assert bool(alert_element)  # 如果元素存在，alert_element 列表长度大于 0，转换为布尔值为 True
