from unittest import TestCase
import utils


class SumTest(TestCase):
    def test_0(self):
        self.assertEquals(utils.sum(0, 0), 0)

    def test_ab(self):
        a = 5
        b = 2
        self.assertEquals(utils.sum(a,b), a+b)