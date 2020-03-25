from flask import Flask, render_template, redirect, url_for, flash
from form import ChilliForm

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xe8\xaf\xa8\x00\x94^\x1e\x84\\)\xfc\x8d1\xbfN\x8c\x94D&\xdf\x1e\x0f\x1bg\xf0\x98L}2\xb03~'


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('create'))


@app.route('/chilli/variants/create', methods=['GET', 'POST'])
def create():
    form = ChilliForm()
    if form.validate_on_submit():
        flash(f'{form.name.data}', 'success')
    return render_template('create.html', title='Create', form=form)


if __name__ == '__main__':
    app.run()
