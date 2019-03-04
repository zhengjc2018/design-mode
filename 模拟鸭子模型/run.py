'''
    策略模式：定义了算法族，分别封装起来，让他们之间可以互相替换，此模式让算法的变化
             独立于使用算法的客户

    设计原则:
    1.找出应用中可能需要变化之处，把他们独立出来，不要和那些不需要
      变化的代码混在一起

    2.多用组合，少用继承
'''


class Duck:

    def quack(self):
        print('i can quack')

    def swim(self):
        print('i can swim')

    def display(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):

    def display(self):
        print('green head')


class RedHeadDuck(Duck):

    def display(self):
        print('red head')


def test():
    obj = MallardDuck()
    obj.display()
    obj.swim()
