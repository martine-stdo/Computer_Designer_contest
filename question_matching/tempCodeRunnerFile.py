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
