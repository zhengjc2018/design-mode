'''
    单例模式:确保一个类只有一个实例，并提供一个全局访问点
'''


class SingleInst(object):

    _instance = {}

    def __new__(cls, *args, **kw):
        if not cls._instance.get(cls):
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class S1(SingleInst):

    def __init__(self, name):
        self.name = name

class S2(SingleInst):

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = S1("test1")
    b = S1("test2")
    c = S2("test1")
    d = S2("test1")
    assert id(a) == id(b)
    assert id(c) == id(d)
