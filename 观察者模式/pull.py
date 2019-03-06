'''
    观察者模式: 定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，
               它的所以依赖着都会受到通知并自动更新
    pull 模式： 观察者可以自主选择获取的信息
'''


class Subject1:
    def __init__(self):
        _theme = ['pressure', 'humidity', 'temprature']
        _len = len(_theme)
        self.data = dict(zip(_theme, [1]*_len))
        self.change = dict(zip(_theme, [False]*_len))

    def set_theme(self, data: dict):
        for key, value in data.items():
            if self.data.get(key) == value:
                self.change[key] = False
                continue
            self.data[key] = value
            self.change[key] = True

    def pull(self, theme: list):
        value = {i: self.data[i] for i in theme if self.change.get(i)}
        return value

    def reset(self):
        value = {i: False for i in self.change}
        self.change = value


class Observer1:

    def __init__(self, name):
        self.name = name
        self.context = dict()

    def update(self, obj, theme: list):
        data = obj.pull(theme)
        if data:
            self.context = data
            print("%s's context has changed" % self.name)
        else:
            print('already up to date')

    def reset(self, obj):
        obj.reset()

    def display(self):
        pass


class CurrentDisplay(Observer1):

    def __init__(self, name):
        super().__init__(name)

    def update(self, obj, theme):
        super().update(obj, theme)
        self.display()

    def display(self):
        print('current display is:%s' % self.context)


if __name__ == '__main__':
    a = Subject1()
    b = CurrentDisplay('a')
    c = CurrentDisplay('b')
    b.update(a, ['pressure', 'temprature'])
    c.update(a, ['humidity', 'temprature'])
    a.set_theme({'pressure': 200, 'humidity': 22, 'temprature': 100})
    b.update(a, ['humidity', 'temprature'])
    c.update(a, ['pressure', 'temprature'])
    a.set_theme({'pressure': 200, 'humidity': 22, 'temprature': 100})
    b.update(a, ['pressure', 'humidity', 'temprature'])
    c.update(a, ['pressure', 'humidity', 'temprature'])
    b.reset(a)
    a.set_theme({'pressure': 2100, 'humidity': 222, 'temprature': 110})
    b.update(a, ['pressure', 'humidity', 'temprature'])
