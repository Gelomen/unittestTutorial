# encoding=utf-8
# 按顺序执行测试用例


class Calc(object):

    @staticmethod
    def add(x, y, *d):
        # 加法计算
        result = x + y
        for i in d:
            result += i
        return result

    @staticmethod
    def sub(x, y, *d):
        # 减法计算
        result = x - y
        for i in d:
            result -= i
        return result

    @classmethod  # 标注了@classmethod，MyTest类直接调用Calc类才不会报错
    def mul(cls, x, y, *d):
        # 乘法计算
        result = x * y
        for i in d:
            result *= i
        return result

    @staticmethod  # 标注了@staticmethod，所以函数不需要 self
    def div(x, y, *d):
        # 除法计算
        if y != 0:
            result = x / y
        else:
            return -1
        for i in d:
            if i != 0:
                result /= i
            else:
                return -1
        return result
