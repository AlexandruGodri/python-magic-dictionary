import json
import copy

class md:
    def __init__(self):
        pass

    def get_one(self, k):
        if k not in self.__dict__:
            self.__dict__[k] = md()
        return self.__dict__[k]

    def set_one(self, k, v):
        self.__dict__[k] = v

    def __setitem__(self, k, v):
        self.set_one(k, v)

    def __getitem__(self, k):
        return self.get_one(k)

    def __setattr__(self, k, v):
        self.set_one(k, v)

    def __getattr__(self, k):
        return self.get_one(k)

    def __coerce__(self, v):
        return (v, 0)

    def __string_conversion(self, dest, items):
        for key in items:
            value = items[key]
            if isinstance(value, md):
                dest[key] = {}
                self.__string_conversion(dest[key], value.__dict__)
            else:
                dest[key] = value

    def importDict(self, **entries):
        self.__dict__.update(entries)
        for key in self.__dict__:
            if type(self.__dict__[key]) is dict:
                item = md()
                item.importDict(**self.__dict__[key])
                self.__dict__[key] = item

    @staticmethod
    def createFromDict(**entries):
        m = md()
        m.importDict(**entries)
        return m

    def exportDict(self):
        dest = {}
        self.__string_conversion(dest, self.__dict__)
        return dest

    def __str__(self):
        dest = {}
        self.__string_conversion(dest, self.__dict__)
        return json.dumps(dest)