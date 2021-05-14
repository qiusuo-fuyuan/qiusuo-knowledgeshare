class PeaType(type):
    """Type of :class:`Pea`, metaclass of :class:`BasePea`."""
    _dct = {}

    def __new__(cls, name, bases, dct):
        _cls = super().__new__(cls, name, bases, dct)
        print('new')
        return _cls

    def __call__(cls, *args, **kwargs) -> 'PeaType':
        print('call')

        return type.__call__(_cls, *args, **kwargs)
