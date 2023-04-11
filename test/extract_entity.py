import jieba
import re
# 读取文本文件
with open('../test_data/question.txt', 'r', encoding='utf-8') as f:
    text = f.read()
# 使用jieba分词
words = jieba.cut(text)
# 定义正则表达式匹配法律实体
pattern = re.compile(r'(《[\u4e00-\u9fa5]+条例》|[\u4e00-\u9fa5]+法|[\u4e00-\u9fa5]+规定|[\u4e00-\u9fa5]+条例|[\u4e00-\u9fa5]+条|[\u4e00-\u9fa5]+案件|[\u4e00-\u9fa5]+判例|[\u4e00-\u9fa5]+裁判文书)')
# 遍历分词结果，提取法律实体
legal_entities = set()
for word in words:
    match = pattern.search(word)
    if match:
        legal_entities.add(match.group())
# 打印提取的法律实体
print(legal_entities)