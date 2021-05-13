class PeaType(type):
    """Type of :class:`Pea`, metaclass of :class:`BasePea`."""
    _dct = {}

    def __new__(cls, name, bases, dct):
        _cls = super().__new__(cls, name, bases, dct)
        print('new')
        return _cls

    def __call__(self, *args, **kwargs) -> 'PeaType':
        return type.__call(BasePea, (Thread,), **kwargs)
        


class BasePea(metaclass=PeaType):
    def __init__(self,):
        print('basepea')


basePea = BasePea()

class A:l