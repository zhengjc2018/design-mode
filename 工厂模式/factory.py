'''
     工厂模式：工厂方法用来处理对象的创建，并将这样的行为封装在子类中
              定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个。
              工厂方法让类把实例化推迟到子类。
     依赖倒置原则：依赖抽象，不依赖具体类, 高层组件（由其他低层组建定义其行为的类）
                  不能依赖于低层组件
'''

from abc import ABCMeta, abstractmethod


class PizzaStore(metaclass=ABCMeta):

    @abstractmethod
    def order_pizza(self):
        pass

    def create_pizza(self):
        self._p.prepare()
        self._p.bake()
        self._p.cut()
        self._p.box()


class Pizza:
    def __init__(self, name, dough, sauce):
        self.name = name
        self.dough = dough
        self.sauce = sauce

    def prepare(self):
        print('prepare now for %s' % self.name)

    def bake(self):
        print('bake now, raw material: %s, %s' % (self.dough, self.sauce))

    def cut(self):
        print('cut now for %s' % self.name)

    def box(self):
        print('box now for %s' % self.name)


class NyPizzaStore(PizzaStore):

    def order_pizza(self, _type):
        dt = {
            "chesse": NYStyleChessePizza(),
            "pepperoni": NYStylePepperoniPizza(),
            "clam": NYStyleClamPizza(),
            "veggie": NYStyleVeggiePizza(),
        }
        self._p = dt[_type]


class ChicagoPizzaStore(PizzaStore):

    def order_pizza(_type):
        dt = {
            "chesse": ChicagoStyleChessePizza(),
            "pepperoni": ChicagoStylePepperoniPizza(),
            "clam": ChicagoStyleClamPizza(),
            "veggie": ChicagoStyleVeggiePizza(),
        }
        self._p = dt[_type]


class NYStyleChessePizza(Pizza):

    def __init__(self):
        super().__init__('NYStyle Chesse Pizza', 'dough1', 'sauce1')

    def cut(self):
        print('hhhh do not cut')


class NYStylePepperoniPizza(Pizza):

    def __init__(self):
        super().__init__('NYStyle Pepperoni Pizza', 'dough1', 'sauce1')


class NYStyleClamPizza(Pizza):

    def __init__(self):
        super().__init__('NYStyle Clam Pizza', 'dough1', 'sauce1')


class NYStyleVeggiePizza(Pizza):

    def __init__(self):
        super().__init__('NYStyle Veggie Pizza', 'dough1', 'sauce1')


class ChicagoStyleChessePizza(Pizza):

    def __init__(self):
        super().__init__('ChicagoStyle Chesse Pizza', 'dough2', 'sauce2')


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self):
        super().__init__('ChicagoStyle Pepperoni Pizza', 'dough2', 'sauce2')


class ChicagoStyleClamPizza(Pizza):

    def __init__(self):
        super().__init__('ChicagoStyle Clam Pizza', 'dough2', 'sauce2')


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self):
        super().__init__('ChicagoStyle Veggie Pizza', 'dough2', 'sauce2')


if __name__ == '__main__':
    a = NyPizzaStore()
    a.order_pizza('chesse')
    a.create_pizza()