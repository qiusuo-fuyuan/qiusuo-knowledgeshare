import multiprocessing
import threading

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

    def __call__(self, *args, **kwargs) -> 'PeaType':
        """
        change runtime backend

        :param args: arguments
        :param kwargs: keyword arguments
        :return: Call self as a function.
        """
        # switch to the new backend
        _cls = {
            0: threading.Thread,
            1: multiprocessing.Process,
        }.get(getattr(args[0], 'runtime_backend', 0))

        # rebuild the class according to mro
        for c in self.mro()[-2::-1]:
            arg_cls = PeaType._dct[c.__name__]['cls']
            arg_name = PeaType._dct[c.__name__]['name']
            arg_dct = PeaType._dct[c.__name__]['dct']
            _cls = super().__new__(arg_cls, arg_name, (_cls,), arg_dct)

        return type.__call__(_cls, *args, **kwargs)