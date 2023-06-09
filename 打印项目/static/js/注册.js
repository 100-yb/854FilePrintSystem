const form = document.querySelector('form');
const usernameInput = document.querySelector('#username');
const passwordInput = document.querySelector('#password');
const confirmPasswordInput = document.querySelector('#confirm-password');
const emailInput = document.querySelector('#email');
const registerBtn = document.querySelector('#register-btn');

function validateForm() {
  // TODO: 实现表单验证逻辑，例如检查用户名、密码、邮箱格式是否合法，确认密码是否一致等
  return true;
}

function registerUser(event) {
  event.preventDefault();

  if (!validateForm()) {
    return;
  }

  // TODO: 将用户注册信息提交到后台，例如使用Fetch API发送POST请求
  const userData = {
    username: usernameInput.value,
    password: passwordInput.value,
    email: emailInput.value,
  };
  console.log('用户注册信息：', userData);

  // 注册成功后跳转到登录页面
  alert("注册成功！");
  window.location.href = '/用户登录界面/用户登录.html';
  
}

form.addEventListener('submit', registerUser);
