class PeaType(type):
    """Type of :class:`Pea`, metaclass of :class:`BasePea`."""
    _dct = {}

    def __new__(cls, name, bases, dct):
        """
        Create and register a new class with this meta class.

        :param name: name of the :class:`Pea`
        :param bases: bases of :class:`Pea`
        :param dct: arguments dictionary
        :return: registered class
        """
        _cls = super().__new__(cls, name, bases, dct)
        PeaType._dct.update({name: {'cls': cls,
                                    'name': name,
                                    'bases': bases,
                                    'dct': dct}})
        return _cls

    def __call__(cls, *args, **kwargs) -> 'PeaType':
        print()

        return type.__call__(_cls, *args, **kwargs)
