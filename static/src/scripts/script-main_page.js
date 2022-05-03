const icon_setting = document.querySelector('.admin img');
const btn_admin = document.querySelector('.admin');
const btn_user = document.querySelector('.user');
const form = document.querySelector('.admin-form-off');
const btn_back = document.querySelector('.back');

btn_admin.addEventListener('click',()=>{
    icon_setting.style.animation = 'animate-plate 2s';
    btn_admin.parentElement.className = 'col-md-8 offset-md-2';
    btn_admin.classList.add('admin-plate-on');
    btn_user.style.display = 'none';
    form.className = 'admin-form-on';
    btn_back.classList.remove('off');
    btn_back.classList.add('on');
});

btn_back.addEventListener('click',()=>{
    btn_back.classList.remove('on');
    btn_back.classList.add('off');
    icon_setting.style.animation = 'none';
    btn_admin.parentElement.className ='col-md-4';
    btn_admin.classList.remove('admin-plate-on');
    btn_user.style.display = 'flex';
    form.className = 'admin-form-off';
});