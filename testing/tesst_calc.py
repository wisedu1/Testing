#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest
from python.calc import Calc
# print(sys.path)
sys.path.append('..')


class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        self.assertEqual(3, result)


unittest.main()
