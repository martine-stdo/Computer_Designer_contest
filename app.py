from flask import Flask, render_template, url_for, request, redirect,flash
from datetime import datetime
import json
import hashlib
import pandas as pd
from fuzzywuzzy import fuzz, process
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

app.secret_key = 'jfsifsihfih'

cookie = "dfjsiedhfuhuefheufhewf"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as f:
        for line in f:
            username, password = line.strip().split(',')
            credentials[username] = password
    return credentials



def check_cookies(request):
    try:
        task_cookies = request.cookies.get('my_cookie')
        return task_cookies == cookie
    except:
        return False

      
@app.route('/error_404/',methods=['GET'])
def error_404():
    return render_template('error.html')

# 登录页面，与文本核对是否一致，一致则返回cookie，空json
@app.route('/admin/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        json_data = request.data.decode('utf-8')
        data = json.loads(json_data)
        username = data.get('username')
        password = data.get('passwd')
        response = {"status": False, "cookie": ""}

        # 从数据库中查询用户凭据
        user = User.query.filter_by(username=username).first()

        # 如果用户存在且密码匹配，则返回成功响应和cookie
        if user and user.password == password:
            response = {"status": True, "cookie": cookie}

        my_json = json.dumps(response)
        return my_json
    else:
        return render_template('login.html')

    
#注册页面
@app.route('/admin/regist', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd1']

        # 检查用户名是否已存在
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is not None:
            return '用户名已存在'

        # 将用户名和密码添加到User模型并保存到数据库
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('注册成功，请登录')
        return render_template('login.html')
    else:
        return render_template('register.html')

#联系我们界面
@app.route('/contactme', methods=['GET'])
def contact():
    return render_template('reachme.html')


#退出界面   
@app.route('/admin/logout', methods=['GET'])
def logout():
    return render_template('login.html')

#返回主界面
@app.route('/admin/return_main', methods=['GET'])
def return_main():
    if check_cookies(request):
        return render_template('menu.html')
    else:
        return render_template('login.html')

#模块一

@app.route('/admin/QandA/', methods=['GET'])
def function1():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('QandA.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')



#用户输入问题，提出五个最相近的问题，用户选择
@app.route('/function/get_matched_questions', methods=['POST'])
def get_matched_questions():
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
            elif module == "3":
                file_name = "between_data/question_answer/债务.csv"
            elif module == "4":
                file_name = "between_data/question_answer/公司.csv"
            elif module == "5":
                file_name = "between_data/question_answer/刑事.csv"
            elif module == "6":
                file_name = "between_data/question_answer/劳动.csv"
            elif module == "7":
                file_name = "between_data/question_answer/合同.csv"
            elif module == "8":
                file_name = "between_data/question_answer/商标.csv"
            elif module == "9":
                file_name = "between_data/question_answer/房产.csv"
            elif module == "10":
                file_name = "between_data/question_answer/民商.csv"
            elif module == "11":
                file_name = "between_data/question_answer/民法.csv"
            elif module == "12":
                file_name = "between_data/question_answer/行政.csv"
      
            else:
                return {"status": "error", "message": "无效的模块"}

            # 读取 CSV 文件并获取问题列表
            df = pd.read_csv(file_name)
            questions = df['question'].tolist()

            # 使用 FuzzyWuzzy 计算匹配度
            match_results = {}
            for q in questions:
                score = fuzz.ratio(input_question, q)
                match_results[q] = score

            # 对匹配结果进行排序，找到匹配度最高的五个问题
            sorted_match_results = sorted(match_results.items(), key=lambda x: x[1], reverse=True)
            matched_questions = sorted_match_results[:5]

            return {"status": "success", "matched_questions": matched_questions}
        else:
            return {"status": "error", "message": "用户未登录"}

#根据用户的选择返回答案
@app.route('/function/ask_question', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        if check_cookies(request):
            data = request.get_json()
            input_question = data.get("question")
            module = data.get("module")

            if module == "1":
                file_name = "between_data/question_answer/交通.csv"
            elif module == "2":
                file_name = "between_data/question_answer/婚姻.csv"
            elif module == "3":
                file_name = "between_data/question_answer/债务.csv"
            elif module == "4":
                file_name = "between_data/question_answer/公司.csv"
            elif module == "5":
                file_name = "between_data/question_answer/刑事.csv"
            elif module == "6":
                file_name = "between_data/question_answer/劳动.csv"
            elif module == "7":
                file_name = "between_data/question_answer/合同.csv"
            elif module == "8":
                file_name = "between_data/question_answer/商标.csv"
            elif module == "9":
                file_name = "between_data/question_answer/房产.csv"
            elif module == "10":
                file_name = "between_data/question_answer/民商.csv"
            elif module == "11":
                file_name = "between_data/question_answer/民法.csv"
            elif module == "12":
                file_name = "between_data/question_answer/行政.csv"
            else:
                return {"status": "error", "message": "无效的模块"}

            df = pd.read_csv(file_name)
            questions = df['question'].tolist()

            # 在此处，我们已经知道用户选择的问题，因此无需进行模糊匹配
            # 只需根据问题查找对应的答案即可
            try:
                answer = df.loc[df['question'] == input_question, 'answer'].iloc[0]
                return {"status": "success", "answer": answer}
            except IndexError:
                return {"status": "error", "message": "未找到问题对应的答案"}

        else:
            return {"status": "error", "message": "用户未登录"}

    
#模块二
@app.route('/admin/start_graph/', methods=['GET'])
def function2():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('data_visual.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')
    
#模块三
@app.route('/adim/wordcloud/', methods=['GET'])
def function3():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('wordcloud.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')
    
#模块四
@app.route('/function/function4', methods=['GET'])
def function4():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('function5.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')

@app.route('/admin/menu/', methods=['GET'])
def main_menu():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('menu.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
            return render_template('loading.html')
    else:
        return render_template('error.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8001, debug=True)
