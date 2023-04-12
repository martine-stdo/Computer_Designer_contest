from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import json
import hashlib

app = Flask(__name__)

cookie = "klsdfjauih[afjp'lwisdfhuiahfuwehfu"
passwd = "123456"

# 使用MD5算法对密码进行加密处理
def encrypt_password(password):
    hash_md5 = hashlib.md5()
    hash_md5.update(password.encode('utf-8'))
    return hash_md5.hexdigest()


def check_cookies(request):
    try:
        task_cookies = request.cookies.get('my_cookie')
        return task_cookies == cookie
    except:
        return False

@app.route('/authorize/', methods=['POST'])
def authorize():  # put application's code here

    if request.method == 'POST':   
        user_password = request.form['content']
        
        encrypted_password = encrypt_password(passwd)

        if encrypted_password == user_password:
            response = {"status":True, "cookie": cookie}
        else:
            response = {"status":False, "cookie": ""}
        my_json = json.dumps(response)
        return my_json
      
@app.route('/error_404/',methods=['GET'])
def error_404():
    return render_template('error.html')


@app.route('/admin/logs', methods=['POST'])
def index():  # put application's code here
    if request.method == 'POST':
        json_data = request.data.decode('utf-8')

        data = json.loads(json_data)
        # 从字典中获取用户名和密码
        username = data.get('username')
        password = data.get('passwd')

     




@app.route('/', methods=['POST','GET'])
def index():  # put application's code here
    if request.method == 'POST':
        if check_cookies(request):
            
            try:
               
                return  redirect('/')
            except:
                return 'There was an issue adding your task!'
        else :
                return redirect('/error_404/')
    else:
        if check_cookies(request):
            return render_template('menu.html')
        else:
            return render_template('login.html')

if __name__ == '__main__':
    app.run(port=8000)
