from abc import ABCMeta, abstractmethod
'''
    设计原则： 类应该对扩展开放，对修改关闭
    装饰者模式: 动态地奖责任附加到对象上。
               1.装饰者和被装饰对象有相同的超类型（任何需要原始对象的场合，
                 可以用装饰过的对象代替它）
               2.可以用一个或多个装饰者包装一个对象

'''


class Beverage(metaclass=ABCMeta):

    def __init__(self):
        pass

    def get_description(self, data):
        return "description is %s" % data

    @abstractmethod
    def cost(self):
        pass


class Condiment(Beverage):
    # 调料
    def __init__(self, obj: object):
        pass

    def get_description(self, data):
        super().get_description(data)

    def cost(self, price):
        return price


class Mocha(Condiment):
    def __init__(self, obj):
        self.obj = obj

    def get_description(self):
        return self.obj.get_description() + 'Mocha'

    def cost(self):
        return 0.2+self.obj.cost()


class Espresso(Beverage):
    def get_description(self):
        return super().get_description('Espresso')

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    # 具体组件
    def get_description(self):
        return super().get_description('HouseBlend')

    def cost(self):
        return 0.89
