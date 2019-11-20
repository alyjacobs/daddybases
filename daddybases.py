from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

    @app.route("/signup", methods=['GET', 'POST'])
    def signup():
        form = ReusableForm(request.form)

        print form.errors
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print name, " ", email, " ", password

        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('signup.html', form=form)



if __name__ == "__main__":
    app.run()
