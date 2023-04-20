要实现这个功能，您需要对前端和后端代码进行修改。下面是一些建议：

在前端HTML代码中，添加一个下拉列表，让用户选择婚姻或交通等模块。例如：
html
Copy code
<div class="form-group">
    <label>选择模块</label>
    <select class="form-control" id="module" name="module">
        <option value="1">交通</option>
        <option value="2">婚姻</option>
    </select>
</div>
修改JavaScript代码，将用户选择的模块发送到Flask后端。您可以通过以下方式更新formData对象：
javascript
Copy code
var formData = {
    "module": $("#module").val(),
    "question": $("input[name=origin]").val()
};
在Flask后端代码中，修改ask_question()函数以接收用户选择的模块，并根据该模块读取相应的CSV文件。例如：
python
Copy code
@app.route('/function/ask_question', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        if check_cookies(request):
            data = request.get_json()
            input_question = data.get("question")
            module = data.get("module")

            # 根据用户选择的模块读取相应的CSV文件
            if module == "1":
                file_name = "between_data/question_answer/交通.csv"
            elif module == "2":
                file_name = "between_data/question_answer/婚姻.csv"
            else:
                return jsonify({"error": "Invalid module"}), 400

            df = pd.read_csv(file_name)
            answer = match_question(input_question, df['question'].tolist())
            return jsonify({"answer": answer})
        else:
            return jsonify({"error": "Not authorized"}), 401
    else:
        return jsonify({"error": "Invalid request"}), 400
对match_question()函数进行一些修改，使其适应新的需求。由于该函数不再与用户直接交互，您需要删除与用户交互有关的代码，例如input()调用。您可以修改该函数以返回匹配问题的答案，如下所示：
python
Copy code
def match_question(input_question, questions):
    match_results = {}
    for q in questions:
        score = fuzz.ratio(input_question, q)
        match_results[q] = score
    matched_questions = process.extract(input_question, questions, limit=5)
    
    # 如果匹配到至少一个问题，返回匹配度最高的问题的答案
    if matched_questions:
        best_match_question = matched_questions[0][0]
        return df.loc[df['question'] == best_match_question, 'answer'].iloc[0]
    else:
        return "未找到匹配的问题"
这些更改将使用户能够从前端选择婚姻或交通等模块，然后输入问题。Flask后端将根据所选模块读取相应的CSV文件，查找与问题匹配的答案，并将答案返回给前端。




aadiij@faker.icu
给出详细的代码
这是一个完整的示例，展示了如何实现前端和后端的修改：

前端HTML（function1.html）：

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>知识问答模块</title>
    <link rel="stylesheet" href="../static/css/demo.css">
    <link rel="stylesheet" href="../static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <script src="../static/js/jquery.min.js"></script>
</head>
<body background="../static/images/5.jpg"
      style="background-repeat:no-repeat;
            background-attachment:fixed;
            background-size:100% 100%;">
    <div class="header">
        <div class="container">
            <div class="menu">
                <a href="/function/menu">基于知识图谱的法律领域问答系统 / 知识问答模块</a>
            </div>
            <div style="clear: both"></div>
        </div>
    </div>
    <div class="container">
        <div class="shu">
            <form id="questionForm">
                <div class="form-group">
                    <label>选择模块</label>
                    <select class="form-control" id="module" name="module">
                        <option value="1">交通</option>
                        <option value="2">婚姻</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>问题</label>
                    <input type="text" class="form-control" name="origin" placeholder="问题">
                </div>
                <div class="form-group">
                    <label>专业解答</label>
                    <input type="text" class="form-control" name="destination" placeholder="专业解答" readonly>
                </div>
                <button type="submit" class="btn btn-primary">提交问题</button>
            </form>
        </div>
        <div style="clear:both;"></div>
    </div>
    <script>
        $("#questionForm").submit(function (event) {
            event.preventDefault();
            var formData = {
                "module": $("#module").val(),
                "question": $("input[name=origin]").val()
            };
            $.ajax({
                type: "POST",
                contentType: "application/json",
                url: "/function/ask_question",
                data: JSON.stringify(formData),
                dataType: "json",
                success: function (data) {
                    $("input[name=destination]").val(data.answer);
                },
                error: function (e) {
                    console.log("ERROR: ", e);
                    alert("Error!");
                }
            });
        });
    </script>
</body>
</html>
Flask后端（app.py）：

python
Copy code
# 在其他导入下方添加
import pandas as pd
from fuzzywuzzy import fuzz, process

# 在其他路由下方添加
@app.route('/function/ask_question', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        if check_cookies(request):
            data = request.get_json()
            input_question = data.get("question")
            module = data.get("module")

            # 根据用户选择的模块读取相应的CSV文件
            if module == "1":
                file_name = "between_data/question_answer/交通.csv"
            elif module == "2":
                file_name = "between_data/question_answer



aadiij@faker.icu
继续
婚姻.csv"

kotlin
Copy code
        df = pd.read_csv(file_name)

        def match_question(input_question, questions):
            match_results = {}
            for q in questions:
                score = fuzz.ratio(input_question, q)
                match_results[q] = score
            matched_questions = process.extract(input_question, questions, limit=5)

            if matched_questions:
                best_question = matched_questions[0][0]
                answer = df.loc[df['question'] == best_question, 'answer'].iloc[0]
                return answer
            else:
                return "未找到匹配的问题"

        answer = match_question(input_question, df['question'].tolist())
        response = {
            "answer": answer
        }
        return jsonify(response)
    else:
        return jsonify({"answer": "请先登录"})
else:
    return render_template('error.html')
Copy code

这个示例在前端用户界面中添加了模块选择器，用户可以选择“交通”或“婚姻”模块。当用户提交问题