# -*- coding: utf-8 -*-
"""
算法模块单元测试

作者：张谨洋（@pingjingdenaiwa）
分支：test/pingjingdenaiwa-qa
职责：把设计文档 6.1 节那张表变成可执行的测试用例。

当前状态：全部标记为 skip，因为两位算法同学还没实现。
         他们实现完成后，把 @unittest.skip(...) 这一行删掉，
         测试就会真正跑起来。

运行方式：
    python -m unittest tests.test_algorithms -v
    或直接：python tests/test_algorithms.py
"""

from __future__ import annotations

import os
import sys
import unittest

# 让测试能 import 到 src/ 下的模块
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from algo_binary import binary_search_steps   # noqa: E402
from algo_hash import hash_search_steps       # noqa: E402

ARR = [3, 8, 12, 19, 25, 31, 40, 47, 52, 60]
KEYS = [34, 46, 25, 61, 72, 7, 18, 53]
SIZE = 11


class TestBinarySearch(unittest.TestCase):
    """二分查找：对应设计文档 6.1 节前四条。"""

    @unittest.skip("待 algo_binary.binary_search_steps 实现后删除本行")
    def test_found_normal(self):
        r = binary_search_steps(ARR, 40)
        self.assertTrue(r["found"])
        self.assertEqual(r["index"], 6)
        self.assertLessEqual(r["comparisons"], 4)

    @unittest.skip("待实现")
    def test_not_found(self):
        r = binary_search_steps(ARR, 41)
        self.assertFalse(r["found"])
        self.assertIsNone(r["index"])

    @unittest.skip("待实现")
    def test_single_element(self):
        r = binary_search_steps([5], 5)
        self.assertTrue(r["found"])
        self.assertEqual(r["comparisons"], 1)

    @unittest.skip("待实现")
    def test_empty_array_does_not_crash(self):
        r = binary_search_steps([], 5)
        self.assertFalse(r["found"])
        self.assertEqual(r["comparisons"], 0)


class TestHashSearch(unittest.TestCase):
    """哈希查找：对应设计文档 6.1 节后四条。"""

    @unittest.skip("待 algo_hash.hash_search_steps 实现后删除本行")
    def test_found_normal(self):
        r = hash_search_steps(KEYS, 72, SIZE)
        self.assertTrue(r["found"])
        self.assertEqual(r["slot"], 6)

    @unittest.skip("待实现")
    def test_not_found(self):
        r = hash_search_steps(KEYS, 99, SIZE)
        self.assertFalse(r["found"])
        self.assertIsNone(r["slot"])

    @unittest.skip("待实现")
    def test_all_collision(self):
        keys = [5, 10, 15, 20]          # 全部落在桶 0
        r = hash_search_steps(keys, 20, 5)
        self.assertTrue(r["found"])
        self.assertEqual(r["comparisons"], 4)

    @unittest.skip("待实现")
    def test_empty_table_does_not_crash(self):
        r = hash_search_steps([], 5, SIZE)
        self.assertFalse(r["found"])
        self.assertEqual(r["comparisons"], 0)


class TestStepContract(unittest.TestCase):
    """Step 结构契约：两个模块产出的字段必须一致。"""

    @unittest.skip("待两个算法模块都实现后启用")
    def test_binary_step_fields(self):
        r = binary_search_steps(ARR, 40)
        self.assertGreater(len(r["steps"]), 0)
        s = r["steps"][0]
        for key in ("type", "lo", "hi", "mid", "slot", "chain_pos", "message"):
            self.assertIn(key, s, f"Step 缺少字段 {key}")

    @unittest.skip("待两个算法模块都实现后启用")
    def test_hash_step_fields(self):
        r = hash_search_steps(KEYS, 72, SIZE)
        self.assertGreater(len(r["steps"]), 0)
        s = r["steps"][0]
        for key in ("type", "lo", "hi", "mid", "slot", "chain_pos", "message"):
            self.assertIn(key, s, f"Step 缺少字段 {key}")


if __name__ == "__main__":
    unittest.main(verbosity=2)