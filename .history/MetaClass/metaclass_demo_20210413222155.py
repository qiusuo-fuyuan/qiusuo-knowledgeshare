class LxsMetaclass(type):
    def __new__(cls, cls_name, bases, attrs):
        def basketball(self):
            print('%s good at basketball' % self.name)
        attrs['basketball'] = basketball
        return super(LxsMetaclass, cls).__new__(cls, cls_name, bases, attrs)
        
        
class Cxk(object, metaclass=LxsMetaclass):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        print('%s practiced %s years' % (self.name, self.duration))
    
    def sing(self):
        print('%s good at singing' % self.name)
    
    def dance(self):
        print('%s good at  dancing' % self.name)
    
    def rap(self):
        print('%s good at  rap' % self.name)

    
cxk = Cxk('cxk',2.5)
cxk.basketball()

cxk.__init__
cxk.__new__