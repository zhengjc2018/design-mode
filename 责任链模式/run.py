import unittest


class Handle:

    name = ""

    def successor(self, successor):
        self.successor = successor

    def handle(self, *args):
        pass

    def run(self, *args):
        try:
            print("start log")
            self.handle(*args)
        except Exception as e:
            print("error: %s" % str(e))
        finally:
            print("finish log")


class LogChain(Handle):

    def handle(self, level):
        if level == "log":
            print(f"{self.name} {level} handle success")
        else:
            self.successor.handle(level)


class ErrorChain(Handle):

    def handle(self, level):
        if level == "error":
            print(f"{self.name} {level} handle success")
        else:
            self.successor.handle(level)


class DebugChain(Handle):

    def handle(self, level):
        if level == "debug":
            print(f"{self.name} {level} handle success")
        else:
            self.successor.handle(level)


class FinallyChain(Handle):

    def handle(self, level):
        print(f"{self.name} {level} handle finish")
        raise ValueError("hhh")


class TestCase(unittest.TestCase):

    def test_result(self):
        name = ["test1", "test2", "test3", "test2", "test3"]
        log = LogChain()
        error = ErrorChain()
        debug = DebugChain()
        final = FinallyChain()

        log.successor(debug)
        debug.successor(error)
        error.successor(final)

        for i, j in enumerate(["error", "error", "log", "debug", "INFO"]):
            Handle.name = name[i]
            log.run(j)


if __name__ == '__main__':
    unittest.main()
