'''
    命令模式：将请求封装成对象，以便使用不同的请求，
             队列或者日志来参数化其他对象，
             命令模式支持可撤销操作

    clinet -> command -> setCommand() -> Invoker -> execute() -> receiver

    女招待 : Invoker
    快餐厨师 : execute()
    orderUp() : receiver
    订单 : command
    顾客 : client
    takeOrder() : setCommand()

'''


class Light:
    def __init__(self, type):
        self.type = type
        self.func_mapping = [i for i in dir(Light) if '_' not in i]

    def on(self):
        print("%s's light is on" % self.type)

    def off(self):
        print("%s's light is off" % self.type)

    def _execute(self, command: object):
        for i in command.commands:
            if i not in self.func_mapping:
                print('invaild operation!')
                continue
            eval("self.%s()" % i)


class Command:
    def __init__(self, type):
        self.light = Light(type)
        self.commands = list()

    def add_command(self, command):
        self.commands.append(command)

    def clear(self):
        self.commands = list()

    def invoker(self):
        self.light._execute(self)


class RemoteControl:
    def __init__(self, name, control_thing='tv'):
        self.name = name
        self.action = None
        self.command = Command(control_thing)

    # work as a Invoker
    def button_press(self):
        self.command.invoker()

    # work as setCommand()
    def set_command(self, command):
        self.command.add_command(command)

    def cancle(self):
        self.command.clear()


if __name__ == '__main__':
    a = RemoteControl('zjc')
    a.set_command('on')
    a.cancle()
    a.set_command('off')
    a.set_command('on')
    a.button_press()
    a.set_command('off1')
    a.button_press()
