from unittest import TestCase
from src.study_plan.algorithms.intro.quiz_704.main import Solution


s = Solution()


class Judge(TestCase):
    def test_01(self):
        self.assertEqual(4, s.search([-1, 0, 3, 5, 9, 12], 9))

    def test_02(self):
        self.assertEqual(-1, s.search([-1, 0, 3, 5, 9, 12], 2))
