from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'路人甲'}
    posts = [
        {'name':'admin', 'score':'10000'},
        {'name':'路人甲', 'score':'8000'}
    ]
    return render_template('index.html', user=user, posts=posts, title='Zong')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    #验证表格中的数据格式是否正确
    if form.validate_on_submit():
        #闪现的信息会出现在页面，当然在页面上要设置
        flash('用户登录的名户名是:{} , 是否记住我:{}'.format(
            form.username.data,form.remember_me.data))
        #重定向至首页
        return redirect('/index')
    #首次登录/数据格式错误都会是在登录界面
    return render_template('login.html',title='登录',form=form)