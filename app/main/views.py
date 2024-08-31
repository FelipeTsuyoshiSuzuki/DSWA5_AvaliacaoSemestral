from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Discipline
from ..email import send_email, send_simple_message
from . import main
from .forms import RegisterSubjectForm
from datetime import datetime


@main.route('/', methods=['GET', 'POST'])
def index():
    current_time = datetime.utcnow()
    return render_template('index.html',
                           name=session.get('name'),
                           current_time = current_time)



@main.route('/disciplinas', methods=['GET', 'POST'])
def register_subjects():
    form = RegisterSubjectForm()
    if form.validate_on_submit():
        discipline = Discipline(name=form.name.data, semester=form.semester.data)
        db.session.add(discipline)
        db.session.commit()
        return redirect(url_for('.register_subjects'))
    disciplines = Discipline.query.all()
    return render_template('register_subject.html',
                            form=form,
                            disciplines=disciplines)



@main.route('/professores', methods=['GET', 'POST'])
def register_teachers():
    return render_template('unavailable.html')



@main.route('/alunos', methods=['GET', 'POST'])
def register_students():
    return render_template('unavailable.html')

