import os
import jieba
import pandas as pd
from wordcloud import WordCloud
#
# # 读取CSV文件
# df = pd.read_csv('../between_data/model/交通_moodel.csv')
#
# # 选择某一列并将其转换为字符串
# text = ' '.join(df['question'].astype(str))
# print(text)
# # 生成词云
# wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
#
# # 显示词云
# import matplotlib.pyplot as plt
# plt.figure(figsize=(8, 8), facecolor=None)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.tight_layout(pad=0)
# plt.show()
#
# # 保存词云图
# wordcloud.to_file("../between_data/wordcloud_image/your_file_path.png")


def extract_wordcloud(folder_path):
    # 循环读取文件夹中的文件
    count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_tag = filename[:2]
            # 读取CSV文件
            df = pd.read_csv(file_path)
            # 选择某一列并将其转换为字符串
            text = ' '.join(df['question'].astype(str))
            text = text.replace('问', '')
            print(text)
            # 生成词云
            seg_list = jieba.cut(text, cut_all=False)
            seg_str = ' '.join(seg_list)

            # 生成词云图
            wc = WordCloud(font_path='simsun.ttc', width=1000, height=800, background_color='white').generate(seg_str)

            # 保存词云图
            filename = "between_data/wordcloud_image/" + file_tag + ".png"
            wc.to_file(filename)
            count += 1
    return count
count = extract_wordcloud('between_data/model')
print(count)