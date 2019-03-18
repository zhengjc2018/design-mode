'''
     工厂模式：
'''


class PizzaFactory:

    @staticmethod
    def order_pizza(type_):
        if type_ == 'cheese':
            pizza = 'cheese'
        elif type_ == 'pepperoni':
            pizza = 'pepperoni'
        elif type_ == 'clam':
            pizza = 'clam'
        else:
            pizza = 'other'
        return pizza


class OrderPizza:

    def __init__(self, type_):
        self.pizza = PizzaFactory.order_pizza(type_)

    def do_sth(self):
        self.prepare()
        self.bake()
        self.cut()
        self.box()
        return self.pizza

    def prepare(self):
        print('prepare for %s' % self.pizza)

    def bake(self):
        print('bake for %s' % self.pizza)

    def cut(self):
        print('cut for %s' % self.pizza)

    def box(self):
        print('box for %s' % self.pizza)


if __name__ == '__main__':
    a = OrderPizza('clam')
    a.do_sth()
