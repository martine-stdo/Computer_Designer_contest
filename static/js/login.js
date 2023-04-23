function setCookie(name, value, expiryDays) {
  var d = new Date();
  d.setTime(d.getTime() + (expiryDays * 24 * 60 * 60 * 1000));
  var expires = "expires=" + d.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}


function submitForm(event) {
  event.preventDefault(); // 阻止表单的默认提交行为

  // 获取表单中的用户名和密码
  var username = document.getElementsByName('username')[0].value;
  var passwd = document.getElementsByName('passwd')[0].value;
  
  // 发送 POST 请求到后端
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/admin/login');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    var result = JSON.parse(xhr.responseText);
    if (result.status == true) {
      // 如果后端返回的 JSON 对象中包含 cookies 字段，表示登录成功
      // 在前端设置 cookies，有效期为 7 天
        setCookie('my_cookie', result.cookie, 7);

      // 跳转到主页
      window.location.href = '/admin/menu/';
    } else {
      // 显示错误信息
      alert("用户不存在或密码错误");
    }
  };
  xhr.send(JSON.stringify({username: username, passwd: passwd}));
}

var loginBtn = document.querySelector('.btn');
loginBtn.addEventListener('click', submitForm);
