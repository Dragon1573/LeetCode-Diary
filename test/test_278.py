from unittest import TestCase
from src.study_plan.algorithms.intro.quiz_278.main import Solution
from src.study_plan.algorithms.intro.quiz_278.provided import initialize


s = Solution()


class Judge(TestCase):
    def test_01(self):
        initialize(4)
        self.assertEqual(4, s.firstBadVersion(5))

    def test_02(self):
        initialize(1)
        self.assertEqual(1, s.firstBadVersion(1))
