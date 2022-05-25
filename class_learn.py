#非实例化调用类方法
class A():
    var1 = 1

    @classmethod
    def fun1(cls):
        print(cls.var1)

A.fun1()

class B():
    def __init__(self):
        print("构造函数, 可以带参数")
        self.name = "B"
        # 私有
        self.__private_attrs = 1

    def __del__(self):
        print("析构函数")
    
    def funB(self):
        print("B")


class C(B):
    def funC(self):
        print("C")

test_c = C()
print(test_c.name)
test_b = B()
print(isinstance(test_c, test_b))

