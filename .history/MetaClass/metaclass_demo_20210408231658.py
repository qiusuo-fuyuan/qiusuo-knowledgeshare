class PeaType(type):
    """Type of :class:`Pea`, metaclass of :class:`BasePea`."""
    _dct = {}

    def __new__(cls, name, bases, dct):
        _cls = super().__new__(cls, name, bases, dct)
        print('new')
        return _cls

    def __call__(self, *args, **kwargs) -> 'PeaType':
        print('call')


class BasePea(metaclass=PeaType):
    print('basepea')


type.__call__(BasePea, (), {})
basePea = BasePea()
