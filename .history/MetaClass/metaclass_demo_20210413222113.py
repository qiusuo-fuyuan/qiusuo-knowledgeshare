class LxsMetaclass(type):
    def __new__(cls, cls_name, bases, attrs):
        def basketball(self):
            print('%s good at basketball' % self.name)
        attrs['basketball'] = basketball
        return super(LxsMetaclass, cls).__new__(cls, cls_name, bases, attrs)