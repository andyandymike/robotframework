# encoding=utf-8

class tcall(object):
    def __call__(self, *args, **kwargs):
        pass

class empty:
    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting')

    def __getattr__(self, item):
        if item == 'myget':
            print('getting attr')
            return 'world'
        return 'hello world'
    def __setattr__(self, key, value):
        print('setting attr')
        self.__dict__[key] = value

class newclass(object):
    _singletons = None
    __slots__ = ('x', '__dict__')

    @classmethod
    def foo(cls):
        print(cls.__name__)

    def __init__(self):
        print("init ...")

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(cls._singletons)
        if not cls._singletons:
            cls._singletons = super(newclass, cls).__new__(cls)
        return cls._singletons

class testiter(object):
    def __init__(self):
        self.value = 1

    def __iter__(self):
        return self

    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

def changeArray(input):
    input[0] = 999

def changeString(input):
    input = "new"

def mymeta(cls, parent, attr):
    print("test metaclass ...")
    return type(cls, parent, attr)

class testmymeta(object):
    __metaclass__ = mymeta
    test = "new"

class testattr(object):
    #def __setattr__(self, key, value):
    #    self.__dict__[key] = value
    a = 1

    #def __getattr__(self, item):
    #    if item == 'b':
    #        print('using getattr')
    #        return 2
    #        #return self.__dict__[item]

    def __getattribute__(self, item):
        return super(testattr, self).__getattribute__(item)

class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            return cls.__instance
        cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

if __name__ == '__main__':
    tttt = testattr()
    print(tttt.c)
    tttt.new = "new world"
    print(tttt.new)
    n = newclass()
    nn = newclass()
    print(id(n))
    print(id(nn))
    n.foo()
    newclass.foo()
    n.z = 1
    print(n.z)

    e = empty()
    e.myset = 'hello'
    print(e.myget)
    print(e.no)
    with empty() as e:
        pass

    print([1, 2] + [3, 4])

    e = "a"
    print(type(e))
    print(isinstance(n, newclass))

    for a in testiter():
        print(a)

    array = [1, 2, 3, 4, 5]
    changeArray(array)
    string = "string"
    changeString(string)
    print(string)
    print(array[0])
    for a in dir(array):
        print(a)
    # print(next(array))
    print(map(lambda a: a + 1, array))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
    print("abc".find(a))
    # print("abc".index("d"))
    a = "abc"
    print(a[1:2])
    if {}:
        print("aaa")
    string = "abcdefg"
    print(len(u'中文'))
    print(u'中文')
    print(u'中文'.encode('utf-8'))
    if "":
        print("empty string")
    testm = testmymeta()

    testdict = {'a': 1, 'b': 2}
    for key, value in testdict.items():
        print('{} : {}'.format(key, value))

    n = [[] for i in range(5)]
    n[0].append(9)
    print(n)
