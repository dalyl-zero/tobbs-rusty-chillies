from flask import render_template, redirect, url_for, flash, jsonify

from .form import CreateForm
from . import app, db, root
from .models import ChilliVariant


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('create'))


@app.route(f'{root}/create', methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        lastChilli = ChilliVariant.query.order_by(ChilliVariant.id.desc()).first()

        newChilli = ChilliVariant(
            name=form.name.data,
            scoville=form.scoville.data,
            days_to_germinate=form.days_to_germinate.data
        )

        if lastChilli is not None and newChilli.name == lastChilli.name:
            flash(f'Sorry, <span class="font-weight-bold">{newChilli.name}</span> exists already!', 'warning')
        else:
            db.session.add(newChilli)
            db.session.commit()

            flash(
                f'<span class="font-weight-bold">{form.name.data}</span> has been added to our HOT pepper collection '
                f'with '
                f'<span class="font-weight-bold">id = {newChilli.id}</span>',
                'success')

    return render_template('create.html', title='Create', form=form)


@app.route(f'{root}/inspect/<_id>', methods=['GET'])
def inspect(_id):
    chilliFound = ChilliVariant.query.get(_id)
    res = {}

    if chilliFound is None:
        res['error'] = 'ID does not exist'
    else:
        res['id'] = chilliFound.id
        res['name'] = chilliFound.name
        res['scoville'] = chilliFound.scoville
        res['days_to_germinate'] = chilliFound.days_to_germinate

    return jsonify(res)


if __name__ == '__main__':
    app.run()
