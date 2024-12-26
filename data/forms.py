from flask_wtf import FlaskForm
import wtforms



class SignUpForm(FlaskForm):
    username = wtforms.StringField("Введіть логін", validators=[wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Введіть пошту", validators=[wtforms.validators.DataRequired(),wtforms.validators.Email()])
    password = wtforms.PasswordField("Введіть пароль", validators=[wtforms.validators.DataRequired(), wtforms.validators.Length(8)])
    submit = wtforms.SubmitField("Зарееструватися")

class LoginForm(FlaskForm):
    username = wtforms.StringField("Введіть вас логін", validators=[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Введіть свій пароль", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Зайти 52")




