'''
    单例模式:确保一个类只有一个实例，并提供一个全局访问点
'''
import time


class SingleInst(object):

    _instance = {}

    def __new__(cls, *args, **kw):
        print(cls._instance)
        if not cls._instance.get(cls):
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class S1(SingleInst):

    def __init__(self, name):
        self.name = name


class S2(SingleInst):

    def __init__(self, name):
        self.name = name


class S3():

    def __init__(self, name):
        self.name = name


def test_time(obj):
    t1 = time.time()
    for i in range(10):
        a = obj('test')
    t2 = time.time()
    print(t2-t1)


def test_id():
    assert id(S1('test2')) == id(S1('tets1'))
    assert id(S2('test2')) == id(S2('tets1'))
    assert id(S1('test1')) != id(S2('tets1'))


if __name__ == '__main__':
    test_time(S1)
    test_time(S3)
    test_id()
