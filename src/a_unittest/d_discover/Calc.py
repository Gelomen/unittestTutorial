# encoding=utf-8


class Calc(object):

    @staticmethod
    def add(x, y, *d):
        # 加法计算
        result = x + y
        for i in d:
            result += i
        return result

    @staticmethod
    def mul(a, b):
        # 两数相乘
        return a * b
