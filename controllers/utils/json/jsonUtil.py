# -*- coding: UTF-8 -*-
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
        self.__setitem__(name,value)

    def getJson(self):
        backJson=json.dumps(self)
        print("backResult:"+backJson)
        return backJson

    def getDic(self):
        return self.__dict__

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
        return self.getJson()
    def setSuccessResult(self,result=""):
        self.result=result
        self.errorCode=0
        self.errorMsg=""
        return self.getJson()

def backError(error):
    return BackResult().setErrorMsg(errorMsg=error)


def backSuccess(result):
    return BackResult().setSuccessResult(result=result)

# 自定义类数组转化为单纯的字典数组
def getPureArrayFromArray(array):
    resultArray = []
    for item in array:
        resultArray.append(item.getDic())
    return resultArray

# 自定义类数组转化为jsonArray
def getJsonArrayFromArray(array):
    return json.dumps(getPureArrayFromArray(array))