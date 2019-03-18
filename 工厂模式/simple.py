'''
     简单工厂模式：
'''


class Pizza:

    def __init__(self, obj):
        self.pizza = obj

    def prepare(self):
        print('prepare for %s' % self.pizza)

    def bake(self):
        print('bake for %s' % self.pizza)

    def cut(self):
        print('cut for %s' % self.pizza)

    def box(self):
        print('box for %s' % self.pizza)


class SimplePizzaFactory:

    @staticmethod
    def create_pizza(type_):
        if type_ == 'cheese':
            pizza = Pizza('cheese pizza')
        elif type_ == 'pepperoni':
            pizza = Pizza('pepperoni pizza')
        elif type_ == 'clam':
            pizza = Pizza('clam pizza')
        return pizza


class PizzaStore:

    def __init__(self, type_):
        self.pizza = SimplePizzaFactory.create_pizza(type_)

    def order_pizza(self):

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()


if __name__ == '__main__':
    a = PizzaStore('clam')
    a.order_pizza()
