import json
class JsonBaseClass(dict):

    def __getattr__(self,name):
        if name in self:
            return self[name]
        print(name)
        n=JsonBaseClass()
        self.__setitem__(name,n)
        self.__setattr__(name,n)
        return n

    def __setattr__(self,name,value):
        print name
        self.__setitem__(name,value)

    def getJson(self):
        return json.dumps(self)