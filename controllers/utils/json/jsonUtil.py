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
        backJson=json.dumps(self)
        print(backJson)
        return backJson

class BackResult(JsonBaseClass):
    errorCode=0
    errorMsg=""
    result=JsonBaseClass()

    def __init__(self,result="",errorCode=0,errorMsg=""):
        self.result=result
        self.errorCode=errorCode
        self.errorMsg=errorMsg
    def setErrorMsg(self,errorMsg=""):
        if (errorMsg != ""):
            self.errorCode=1
            self.errorMsg=errorMsg
        return self
    def setSuccessResult(self,result=""):
        self.result=result
        self.errorCode=0
        self.errorMsg=""