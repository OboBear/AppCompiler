# -*- coding: UTF-8 -*-

from random import Random
#固定长度的随机字符串
def random_str(randomlength=8):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    return random_(randomlength=randomlength,chars=chars)

def random_num(randomlength=8):
    chars = '0123456789'
    return random_(randomlength=randomlength,chars=chars)

def random_(randomlength=0,chars="000"):
    str = ''
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

# print(random_num(22))


