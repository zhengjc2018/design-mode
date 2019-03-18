'''
    观察者模式: 定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，
               它的所以依赖着都会受到通知并自动更新

              1.定义了对象之间一对多的关系
              2.用一个共同的接口来更新观察者
              3.可从被观察者处Push或者pull, push方式更'正确'
              4.多个观察者时不可以依赖特定的通知次序

    push 方式： 主题主动向已经订阅注册的观察者推送消息
'''


class Subject1:
    def __init__(self):
        self.members = dict()
        self.data = {
            "pressure": 1,
            "humidity": 1,
            "temprature": 1,
        }

    def set_theme(self, data: dict):
        for key, value in data.items():
            self.data[key] = value
        self.push()

    def register(self, obj: object, subscribe_theme: list):
        self.members.update({obj: subscribe_theme})
        print('register succeed, subject members:%s' % self.members)

    def remove(self, obj):
        self.members.pop(obj)
        print('remove succeed, subject members:%s' % self.members)

    def push(self):
        for obj, values in self.members.items():
            data = {value: self.data.get(value) for value in values}
            obj.update(data)


class Observer1:

    def __init__(self, name):
        self.name = name
        self.context = dict()

    def update(self, data):
        self.context = data

    def display(self):
        pass


class CurrentDisplay(Observer1):

    def __init__(self, name):
        super().__init__(name)

    def update(self, data):
        super().update(data)
        self.display()

    def display(self):
        print('current display is:%s' % self.context)


if __name__ == '__main__':
    a = Subject1()
    b = CurrentDisplay('a')
    c = CurrentDisplay('b')
    a.register(b, ['pressure', 'humidity'])
    a.register(c, ['pressure', 'humidity', 'temprature'])
    a.set_theme({'pressure': 2})
    a.set_theme({'pressure': 200, 'humidity': 22})
    a.remove(b)
    # CurrentDisplay().display()