import csv
import re
import pandas as pd
import os
# import openpyxl

"""
清洗源数据：
将获取的源数据删除空格换行等字符，并将不存的法律依据以略代替

"""


def extract_answer_to_question(folder_path):
    # 循环读取文件夹中的文件
    count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_tag = filename[:2]
            # 读取CSV文件
            df = pd.read_csv(file_path)
            # 清洗和处理数据
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            df = df.fillna("略")
            df = df.applymap(lambda x: re.sub(r'\s+', '', x) if isinstance(x, str) else x)
            df.columns = ['question', 'answer1', 'because']
            # 合并字段
            df['answer'] = df['answer1'] + "-" + df['because']
            df = df.drop(['answer1', 'because'], axis=1)
            # 插入新字段
            df.insert(1, "question_tag", "问题")
            df.insert(2, "property", "专业回答")
            df.insert(4, "answer_tag", "回答")
            output_file = "between_data/question_answer/" + file_tag + ".csv"
            # 写入Excel文件
            df.to_csv(output_file, index=False)
            count += 1
    return count


def extract_model_to_question(folder_path):
    # 循环读取文件夹中的文件
    count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_tag = filename[:2]
            # 读取CSV文件
            df = pd.read_csv(file_path)
            # 清洗和处理数据
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            df = df.fillna("略")
            df = df.applymap(lambda x: re.sub(r'\s+', '', x) if isinstance(x, str) else x)
            df.columns = ['question', 'answer1', 'because']
            # 删除字段
            df = df.drop(['answer1', 'because'], axis=1)
            # 插入新字段
            df.insert(1, "question_tag", "问题")
            df.insert(2, "property", "包含")
            df.insert(3, 'model', file_tag)
            df.insert(4, "model_tag", "模块")
            output_file = "between_data/model/" + file_tag + "_moodel" + ".csv"
            # 写入Excel文件
            df.to_csv(output_file, index=False)
            count += 1
    return count

count = extract_answer_to_question('start_data')
print(count)



# # 定义数据清洗函数
# def clean_data(start_data):
#     # 删除多余的空格和换行符
#     start_data = start_data.strip()
#     start_data = re.sub(r'\s+', ' ', start_data)
#     if not start_data:
#         start_data = '略'
#     return start_data
#
#
# # 定义要更改的字段名
# field_names = ['question', 'question_tag', 'property', 'answer', 'answer_tag', ]
# # 打开CSV文件进行读操作
# with open('交通_法律问答_法律知识问答_法律咨询在线解答-文书网.csv', mode='r') as input_file:
#     # 创建CSV读取器对象
#     reader = csv.reader(input_file)
#     # 获取CSV文件中原始的字段名
#     original_fields = next(reader)
#     # 打开CSV文件进行写操作
#     with open('output.csv', mode='w', newline='') as output_file:
#         # 创建CSV写入器对象
#         writer = csv.writer(output_file)
#         # 写入新的字段名
#         writer.writerow(field_names)
#         # 遍历每一行数据
#         for row in reader:
#             # 清洗数据
#             cleaned_row = [clean_data(start_data) for start_data in row]
#             # 在第二列和第三列之间插入新的字段
#             new_row = [cleaned_row[0], '问题', '专业回答', cleaned_row[1]+cleaned_row[2], '回答']
#             # 写入新的数据行
#             print(new_row)
#             writer.writerow(new_row)

# # 测试代码
# filename = '交通_法律问答_法律知识问答_法律咨询在线解答-文书网.csv' # CSV文件名
# new_names = {'\ufeff字段1': 'question', '字段2': 'answer', '字段3' : 'because'} # 更改后的字段名
# field_values = read_csv_all_clean_rename(filename, new_names) # 读取所有字段并清洗内容，并更改字段名
# print(field_values) # 输出结果


# ['\ufeff字段1', '字段2', '字段3']
