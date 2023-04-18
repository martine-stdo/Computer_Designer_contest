# import pandas as pd
# import difflib
#
# # 读取csv文件
# df = pd.read_csv(r'C:\Users\29241\Desktop\QASystemOnLawKG\between_data\question_answer\交通.csv')
#
# # 定义匹配函数
# def match_question(input_question):
#     # 在question列中找到匹配度最高的问题
#     match = difflib.get_close_matches(input_question, df['question'], n=1, cutoff=0.5)
#     if match:
#         # 返回匹配问题对应的答案
#         return df.loc[df['question']==match[0], 'answer'].iloc[0]
#     else:
#         return "Sorry, I couldn't find a matching question."
#
# # 测试
# input_question = "问醉驾了怎么办"
# answer = match_question(input_question)
# print(f"Question: {input_question}\nAnswer: {answer}")


# import pandas as pd
# from fuzzywuzzy import fuzz, process
#
# # 读取csv文件
# df = pd.read_csv(r'C:\Users\29241\Desktop\QASystemOnLawKG\between_data\question_answer\交通.csv')
#
#
# # 定义一个函数用于模糊匹配问题
# def match_question(input_question, questions):
#     while True:
#         # 创建一个空的字典用于存储匹配结果
#         match_results = {}
#         # 对每一个问题进行模糊匹配，并将匹配度分数存储到字典中
#         for q in questions:
#             score = fuzz.ratio(input_question, q)
#             match_results[q] = score
#         # 对匹配结果进行排序，找到匹配度最高的五个问题
#         matched_questions = process.extract(input_question, questions, limit=5)
#         # 输出匹配度前五的问题及其匹配度
#         for i, mq in enumerate(matched_questions):
#             q, s = mq
#             print(f"{i+1}. {q} ({s})")
#         # 让用户选择一个问题或退出
#         print("0. 退出")
#         choice = input("请选择一个问题(输入对应的编号): ")
#         if choice == '0':
#             return
#         choice = int(choice)
#         while choice not in range(1, 6):
#             choice = input("请输入正确的编号: ")
#             choice = int(choice)
#         selected_question = matched_questions[choice-1][0]
#         # 输出用户选择的问题的答案，并询问是否继续
#         print(f"Q: {selected_question}")
#         print(f"A: {df.loc[df['question'] == selected_question, 'answer'].iloc[0]}")
#         continue_choice = input("是否继续查找(Y/N): ")
#         if continue_choice.lower() == 'n':
#             return
#
# # 从命令行输入一个问题，并调用函数获取答案
# while True:
#     input_question = input("请输入问题(输入q退出程序): ")
#     if input_question.lower() == 'q':
#         break
#     match_question(input_question, df['question'].tolist())



import pandas as pd
from fuzzywuzzy import fuzz, process
import os



# 显示所有可选的选项
options = {
    '1': '交通',
    '2': '婚姻'
}
print("请选择一个选项:")
for key, value in options.items():
    print(f"{key}. {value}")

# 获取用户的选择
while True:
    choice = input("请输入选项(输入q退出程序): ")
    if choice.lower() == 'q':
        break
    if choice not in options.keys():
        print("请输入正确的选项")
        continue
    # 读取相应的csv文件
    file_name = 'between_data/question_answer/' + options[choice] + ".csv"
    df = pd.read_csv(file_name)

    # 定义一个函数用于模糊匹配问题
    def match_question(input_question, questions):
        while True:
            # 创建一个空的字典用于存储匹配结果
            match_results = {}
            # 对每一个问题进行模糊匹配，并将匹配度分数存储到字典中
            for q in questions:
                score = fuzz.ratio(input_question, q)
                match_results[q] = score
            # 对匹配结果进行排序，找到匹配度最高的五个问题
            matched_questions = process.extract(input_question, questions, limit=5)
            # 输出匹配度前五的问题及其匹配度
            for i, mq in enumerate(matched_questions):
                q, s = mq
                print(f"{i+1}. {q} ({s})")
            # 让用户选择一个问题或退出
            print("0. 退出")
            choice = input("请选择一个问题(输入对应的编号): ")
            if choice == '0':
                return
            choice = int(choice)
            while choice not in range(1, 6):
                choice = input("请输入正确的编号: ")
                choice = int(choice)
            selected_question = matched_questions[choice-1][0]
            # 输出用户选择的问题的答案，并询问是否继续
            print(f"Q: {selected_question}")
            print(f"A: {df.loc[df['question'] == selected_question, 'answer'].iloc[0]}")
            continue_choice = input("是否继续查找(Y/N): ")
            if continue_choice.lower() == 'n':
                return

    # 从命令行输入一个问题，并调用函数获取答案
    while True:
        input_question = input("请输入问题(输入q退出程序): ")
        if input_question.lower() == 'q':
            break
        match_question(input_question, df['question'].tolist())
