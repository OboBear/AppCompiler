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

class BackResult(JsonBaseClass):
    errorCode=0
    errorMsg=""
    result=JsonBaseClass()

    def __init__(self,result):
        self.__init__(result=result,errorCode=0,errorMsg="")

    def __init__(self,errorCode,errorMsg):
        self.__init__(result="",errorCode=errorCode,errorMsg=errorMsg)

    def __init__(self,result,errorCode,errorMsg):
        self.result=result
        self.errorCode=errorCode
        self.errorMsg=errorMsg