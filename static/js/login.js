function submitForm() {
  // 获取表单中的用户名和密码
  var username = document.getElementsByName('username')[0].value;
  var passwd = document.getElementsByName('passwd')[0].value;
  
  // 发送 POST 请求到后端
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/admin/login');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    var result = JSON.parse(xhr.responseText);
    if (result.cookies) {
      // 如果后端返回的 JSON 对象中包含 cookies 字段，表示登录成功
      // 在前端设置 cookies，有效期为 7 天
      var date = new Date();
      date.setTime(date.getTime() + (7 * 24 * 60 * 60 * 1000));
      document.cookie = 'cookies=' + result.cookies + ';expires=' + date.toUTCString() + ';path=/';
      
      // 跳转到主页
      window.location.href = '/';
    } else {
      // 如果后端返回的 JSON 对象中不包含 cookies 字段，表示登录失败
      // 在页面中显示错误信息
      var backSpan = document.getElementsByClassName('back')[0];
      backSpan.innerHTML = '用户名或密码错误，请重试！';
    }
  };
  xhr.send(JSON.stringify({username: username, passwd: passwd}));
}
