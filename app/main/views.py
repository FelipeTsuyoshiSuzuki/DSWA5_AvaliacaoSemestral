from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User, Role
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
    return render_template('register_subject.html',
                            form=form)



@main.route('/professores', methods=['GET', 'POST'])
def register_teachers():
    return render_template('unavailable.html')



@main.route('/alunos', methods=['GET', 'POST'])
def register_students():
    return render_template('unavailable.html')

