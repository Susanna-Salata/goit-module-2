class Meta(type):
    _register = {}

    def __new__(cls, name, bases, dct):
        class_ = super(Meta, cls).__new__(cls, name, bases, dct)
        if name not in Meta._register:
            Meta._register[name] = class_
        class_.class_number = len(Meta._register) - 1
        return class_

    def __init__(*args):

        print(f'Meta __init__ called with {args}')


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    print(Cls1.class_number, Cls2.class_number)
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)