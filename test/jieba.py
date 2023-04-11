#-*- coding: UTF-8 -*-
# @Time    : 2023/3/1 9：30
# @Author  : wrs
# @Site    :
# @File    : jieba.py
# @Software: PyCharm

import jieba
import jieba.posseg as pseg
import jieba.analyse

jieba.load_userdict("userdict.txt")   # 醉驾并发生交通事故的法律后果是什么
content = open('../test_data/question.txt', 'r', encoding='utf-8').read()
tags = jieba.analyse.extract_tags(content, topK=800, withWeight=False)
tag_words = pseg.cut(''.join(tags))
# tag_words = pseg.cut(content)
flags = []

entities_dict = {}

for word, flag in tag_words:
    print('%s %s' % (word, flag))
    entities_dict.setdefault(flag, []).append(word)
    flags.append(flag)

# flag 排序
print(flags)
flags_set = set(flags)
new_flags = sorted(flags_set, key=flags.index)
print(new_flags)

for key in entities_dict:
    print('%s %s' % (key, entities_dict[key]))

