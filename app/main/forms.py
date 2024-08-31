from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegisterSubjectForm(FlaskForm):
    name = StringField('Cadastre a nova disciplina e o semestre associado', validators=[DataRequired()])
    semester = RadioField('Semestre', choices=[
        ('1', '1º semestre'),
        ('2', '2º semestre'),
        ('3', '3º semestre'),
        ('4', '4º semestre'),
        ('5', '5º semestre'),
        ('6', '6º semestre')
    ], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
