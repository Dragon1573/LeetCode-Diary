from unittest import TestCase
from src.study_plan.algorithms.intro.quiz_35.main import Solution

s = Solution()


class Judge(TestCase):
    def test_01(self):
        self.assertEqual(2, s.searchInsert([1, 3, 5, 6], 5))

    def test_02(self):
        self.assertEqual(1, s.searchInsert([1, 3, 5, 6], 2))

    def test_03(self):
        self.assertEqual(4, s.searchInsert([1, 3, 5, 6], 7))

    def test_04(self):
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6], 0))

    def test_05(self):
        self.assertEqual(0, s.searchInsert([1], 0))
