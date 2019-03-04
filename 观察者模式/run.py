'''
    观察者模式: 定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，它的所以
               依赖着都会受到通知并自动更新
'''


class Observer:
    def __init__(self):
        self.members = {
            "观察者id": ["订阅内容", 'theme1', 'theme2'],
        }

    def theme1(self):
        pass

    def theme2(self):
        pass

    def register(self, id_or_name, subscribe_theme: list):
        self.members.update({id_or_name: subscribe_theme})
