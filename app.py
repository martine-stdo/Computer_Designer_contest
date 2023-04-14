from flask import Flask, render_template, url_for, request, redirect,flash
from datetime import datetime
import json
import hashlib

app = Flask(__name__)
app.secret_key = 'jfsifsihfih'

cookie = "dfjsiedhfuhuefheufhewf"

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
@app.route('/admin/login', methods=['POST','GET'])
def login():  # put application's code here
    credentials = read_credentials('user.txt')

    if request.method == 'POST':
        json_data = request.data.decode('utf-8')

        data = json.loads(json_data)
        # 从字典中获取用户名和密码
        username = data.get('username')
        password = data.get('passwd')
        response = {"status":False, "cookie": ""}
        if username in credentials:
            if password == credentials[username]:
                response = {"status":True, "cookie": cookie}
        
        my_json = json.dumps(response)
        return my_json
        
    else:
        return render_template('login.html')
    
#注册页面
@app.route('/admin/regist', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        # 从表单中获取用户名和密码
        username = request.form['username']
        password = request.form['pwd1']
        
        # 检查用户名是否已存在
        with open('user.txt', 'r') as f:
            credentials = [line.strip().split(',') for line in f.readlines()]
        if username in [user[0] for user in credentials]:
            return '用户名已存在'
        
        # 将用户名和密码写入user.txt文件中
        with open('user.txt', 'a') as f:
            f.write(username + ',' + password + '\n')
        flash('注册成功，请登录')
        return render_template('login.html')
    else:
        return render_template('register.html')
#联系我们界面
@app.route('/contactme', methods=['GET'])
def contact():
    return render_template('contactme.html')


#退出界面   
@app.route('/admin/logout', methods=['GET'])
def logout():
    return render_template('login.html')

#模块一

@app.route('/function/function1', methods=['GET'])
def function1():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('function1.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')
    
#模块二
@app.route('/function/function2', methods=['GET'])
def function2():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('function2.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')
    
#模块三
@app.route('/function/function3', methods=['GET'])
def function3():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('function3.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')
    
#模块四
@app.route('/function/function4', methods=['GET'])
def function4():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('function4.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        if check_cookies(request):
            return render_template('menu.html')
        else:
            return render_template('login.html')
    else:
        return render_template('error.html')
    



if __name__ == '__main__':
    app.run(port=8000)
