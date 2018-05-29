from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

posts = [
    {
        'author': 'redwan',
        'title': 'Post 1',
        'content': 'first post',
        'date_posted': 'May 14, 2018'
    },
    {
        'author': 'younes',
        'title': 'Post 2',
        'content': 'first post ffsad',
        'date_posted': 'May 10, 2018'
    }
]

app.config['SECRET_KEY'] = 'qVDzwrRs5EvWkOUmhenlSA=='


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Registeration', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
