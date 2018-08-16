from collections import OrderedDict
dic = OrderedDict()

dic[1] = 1
dic[2] = 2
dic[3] = 3
dic[1] = 41

print dic.popitem()