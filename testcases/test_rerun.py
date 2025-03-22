# @Time: 2023/2/10 14:18
# @Author: Xiangyu Cai

import random
import pytest

# 失败重跑
class TestRerun:
    def test_rerun(self):
        num = random.randint(1, 3)
        print("num", num)

        if num != 1:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")
