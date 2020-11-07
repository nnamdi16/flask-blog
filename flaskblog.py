from flask import Flask, render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'df76f403f57125a1299890ed0ad7f19d'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2018'
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('hello'))
    return render_template('register.html',title='Register',form = form)


@app.route('/login' ,methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':  
            flash(f'You have been logged in! ','success')
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html',title='Login',form = form)

if __name__ == '__main__':
    app.run(debug=True)

# To resolve python issues - https://stackoverflow.com/questions/14792605/python-flask-import-error/19470924