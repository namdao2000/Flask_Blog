from flask import Flask, render_template, url_for, flash, redirect
from forums import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'da8bd1a8cefcceee3476f0f10eae4697'

posts = [
    {
        'author': 'Nam Dao',
        'title': "Blog Post 1",
        'content': "First post content",
        'date_posted': "April 20, 2018"
    },
    {
        'author': 'Dianna Doe',
        'title': "Blog Post 2",
        'content': "Second post content",
        'date_posted': "April 21, 2018"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', posts=posts, title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    print("Didn't work")
    return render_template('register.html', form=form, title="Register")


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title="Login")


if __name__ == '__main__':
    app.run(debug=True)
