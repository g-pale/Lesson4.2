class Test():
    def public_func(self):
        print('публичный метод')

    def _protect_func(self):
        print('защищенный метод')

    def __private_func(self):
        print('приватный метод')

    def test_private(self):
        self.__private_func()

test = Test()

test.public_func()
test._protect_func()
test.test_private()