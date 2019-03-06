'''
    观察者模式: 定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，它的所以
               依赖着都会受到通知并自动更新
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
            obj.context = {value: self.data.get(value) for value in values}


class DisplayElement:

    def display():
        pass


class Observer1:

    def __init__(self, name):
        self.name = name
        self.context = dict()

    def update(self):
        print("observer %s context:%s" % (self.name, self.context))


class CurrentDisplay(Observer1, DisplayElement):

    def __init__(self, name):
        super().__init__(name)

    def update(self):
        super().update()
        self.display()

    def display(self):
        self.context


if __name__ == '__main__':
    a = Subject1()
    b = CurrentDisplay('a')
    c = CurrentDisplay('b')
    a.register(b, ['pressure', 'humidity'])
    a.register(c, ['pressure', 'humidity', 'temprature'])
    b.update()
    c.update()
    a.set_theme({'pressure': 2})
    b.update()
    c.update()
    a.set_theme({'pressure': 200, 'humidity': 22})
    b.update()
    c.update()
    a.remove(b)
    # CurrentDisplay().display()