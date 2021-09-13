from flask import Flask, render_template, flash, request
from wtforms import Form
from telephone import cmd

# App config.ini.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

#        print(form.errors)
        if request.method == 'POST':
            number = request.form['number']
            call_res = cmd(number)
            if "OK" not in call_res:
                flash(call_res)
            else:
                flash("Success " + number)

        else:
            flash('Error: telephone id  is required. ')

        return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)