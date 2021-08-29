import unittest
from unittest.case import TestCase


class Solution:

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for ball in range(lowLimit, highLimit + 1):
            box = self.sumNumber(ball)
            if box not in boxes:
                boxes[box] = 0
            boxes[box] += 1 
        return max(boxes.values())

    def sumNumber(self, number):
        ret = 0
        while number > 0:
            ret += number % 10
            number //= 10
        return ret



class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()


    def test_first_case(self):
        self.assertEqual(
            self.solution.countBalls(lowLimit = 1, highLimit = 10),
            2
        )

    def test_second_case(self):
        self.assertEqual(
            self.solution.countBalls(lowLimit = 5, highLimit = 15),
            2
        )

    def test_third_case(self):
        self.assertEqual(
            self.solution.countBalls(lowLimit = 19, highLimit = 28),
            2
        )

    def test_five_case(self):
        self.assertEqual(
            self.solution.countBalls(lowLimit = 4, highLimit = 7),
            1
        )

    def test_sum_number(self):
        self.assertEqual(
            self.solution.sumNumber(1234),
            10
        )


if __name__ == "__main__":
    unittest.main()