from currency_converter import CurrencyConverter
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

converter = CurrencyConverter()
cur_list = sorted(list(converter.currencies))
cur_list_name = [
    'Австралийский доллар', 'Болгарский лев', 'Бразильский реал',
    'Канадский доллар', 'Швейцарский франк', 'Китайский юань',
    'Кипрский фунт', 'Чешская крона', 'Датская крона',
    'Эстонская крона', 'Евро', 'Фунт Стерлингов',
    'Гонконгский доллар', 'Хорватская куна', 'Венгерский форинт',
    'Индонезийская рупия', 'Израильский шекель', 'Индийская рупия',
    'Исландская крона', 'Иена', 'Южнокорейская вона',
    'Литовский лит', 'Латвийский лат', 'Мальтийская лира',
    'Мексиканское песо', 'Малайзийский ринггит', 'Норвежская крона',
    'Новозеландский доллар', 'Филиппинское песо', 'Польский злотый',
    'Румынский лей (старый)', 'Румынский лей (новый)', 'Российский рубль',
    'Шведская крона', 'Сингапурский доллар', 'Словенский толар',
    'Словацкая крона', 'Тайский бат', 'Турецкая лира', 'Турецкая лира (новая)',
    'Доллар США', 'Южноафриканский рэнд'
]
new_cur = dict()
for n in range(len(cur_list)):
    new_cur[cur_list[n]] = cur_list_name[n]
str_names = [f'{key} - {item}' for key, item in new_cur.items()]


class MainForm(FlaskForm):
    select = SelectField(choices=str_names,
                         default=str_names[str_names.index('USD - Доллар США')])
    select2 = SelectField(choices=str_names,
                          default=str_names[str_names.index('RUB - '
                                                            'Российский '
                                                            'рубль')])
    data_in = StringField('Ввод', validators=[DataRequired()])
    submit = SubmitField('>>>')


class Commenting(FlaskForm):
    comment = StringField('Ваш комментарий (Your comment)', validators=[DataRequired()])
    username = StringField('Представьтесь, пожалуйста (Please introduce yourself)', validators=[DataRequired()])
    email = StringField('Ваш email (Your email address)', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Отправить комментарий (Send a comment)')
