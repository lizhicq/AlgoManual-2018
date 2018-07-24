# -*- coding: utf-8 -*-

from collections import Counter
with open("daode.txt", 'rb') as f:
    file = f.read().decode("utf-8")
    count = Counter(file)
    ignore = ["。", '\r', '\n', ' ', '，',
              '“', '：', '”', '！', '、', '？']
    for word in ignore:
        if word in count:
            del count[word]
    print(count.most_common(100))
