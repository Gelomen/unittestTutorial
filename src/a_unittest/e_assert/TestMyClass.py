# encoding=utf-8
# 断言

import unittest
import random


# 被测试类


class MyClass(object):

    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def div(cls, a, b):
        return a / b

    @classmethod
    def return_none(cls):
        return None


# 测试类
class MyTest(unittest.TestCase):

    # 1. assertEqual() 方法实例
    def test_assert_equal(self):
        # try:
        a, b = 1, 2
        num = 4
        self.assertEqual(a + b, num, "test fail, %s + %s != %s \n" % (a, b, num))
        # except AssertionError as e:
        #     print(e)

    # 2. assertNotEqual() 方法实例
    def test_assert_not_equal(self):
        # try:
        a, b = 5, 2
        num = 3
        self.assertNotEqual(a - b, num, "test fail, %s - %s = %s \n" % (a, b, num))

    # except AssertionError as e:
    #     print(e)

    # 3. assertTrue() 方法实例
    def test_assert_true(self):
        # try:
        self.assertTrue(1 == 1, "test fail, expression is false \n")

    # except AssertionError as e:
    #     print(e)

    # 4. assertFalse() 方法实例
    def test_assert_false(self):
        # try:
        self.assertFalse(3 == 2, "test fail, expression is true \n")

    # except AssertionError as e:
    #     print(e)

    # 5. assertIs() 方法实例
    def test_assert_is(self):
        # try:
        a = 12
        b = a
        self.assertIs(a, b, "test fail, %s and %s are not the same object \n" % (a, b))

    # except AssertionError as e:
    #     print(e)

    # 6. assertIsNot() 方法实例
    def test_assert_is_not(self):
        # try:
        a = 12
        b = "test"
        self.assertIsNot(a, b, "test fail, %s and %s are the same object \n" % (a, b))

    # except AssertionError as e:
    #     print(e)

    # 7. assertIsNone() 方法实例
    def test_assert_is_none(self):
        # try:
        self.assertIsNone(MyClass.return_none(), "test fail, result is not None \n")

    # except AssertionError as e:
    #     print(e)

    # 8. assertIsNotNone 方法实例
    def test_assert_is_not_none(self):
        # try:
        result = MyClass.sum(2, 5)
        self.assertIsNotNone(result, "test fail, result is None \n")

    # except AssertionError as e:
    #     print(e)

    # 9. assertIn() 方法实例
    def test_assert_in(self):
        # try:
        str_a = "this is a test"
        str_b = "is"
        self.assertIn(str_b, str_a, "test fail, %s is not in %s \n" % (str_a, str_b))

    # except AssertionError as e:
    #     print(e)

    # 10. assertNotIn() 方法实例
    def test_assert_not_in(self):
        # try:
        str_a = "this is a test"
        str_b = "selenium"
        self.assertNotIn(str_b, str_a, "test fail, %s is in %s \n" % (str_a, str_b))

    # except AssertionError as e:
    #     print(e)

    # 11. assertIsInstance() 方法实例
    def test_is_instance(self):
        # try:
        x = MyClass
        y = object
        self.assertIsInstance(x, y, "test fail, %s is not instance of %s \n" % (x, y))

    # except AssertionError as e:
    #     print(e)

    # 12. assertNotIsInstance() 方法实例
    def test_assert_not_is_instance(self):
        # try:
        a = 123
        b = str
        self.assertNotIsInstance(a, b, "test fail, %s is instance of %s \n" % (a, b))

    # except AssertionError as e:
    #     print(e)

    # 13. assertRaises() 方法实例
    def test_assert_raises(self):
        with self.assertRaises(TypeError) as ar:
            random.sample([1, 2, 3, 4, 5], "j")
        print("test fail, ", ar.exception)

        # try:
        self.assertRaises(ZeroDivisionError, MyClass.div, 3, 0)
        # except ZeroDivisionError as e:
        #     print(e)

    # 14. assertRaisesRegex() 方法实例
    def test_assert_raises_regex(self):
        with self.assertRaisesRegex(ValueError, "literal") as ar:
            int("XYZ")

            print("test fail, ", ar.exception)

        # try:
        self.assertRaisesRegex(ValueError, "test fail, invalid literal for. *XYZ' $ \n", int, "XYZ")
        # except AssertionError as e:
        #     print(e)


if __name__ == "__main__":
    unittest.main()
