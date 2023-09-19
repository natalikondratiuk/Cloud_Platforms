"""
Скрипт програми до ЛР № 2
"Зворотній відлік"
Кондратюк Наталії
ПІ-22-1м
"""

from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

def get_diff(date_next, date_today=datetime.now().strftime('%d/%m/%Y')) :
    """
    Зворотній відлік до обраної дати
    :param date_next: дата, до якої потрібно провести зворотній відлік
    :param date_today: дата, від якої проводиться зворотній відлік (сьогодні - параметр за замовчуванням)
    :return: наступна дата, к-ть днів, що залишилось
    """

    format_start = datetime.strptime(date_today, '%d/%m/%Y')
    date_diff = timedelta( (7+date_next-format_start.weekday()) % 7 ) # тиждень має 7 днів

    return (format_start+date_diff).strftime('%d/%m/%Y'), date_diff

@app.route("/")
def welcome() :
    return f"<h1>Зворотній відлік до обраного дня тижня</h1><br>" \
           f"<p>Використайте API /day=індекс дня тижня (0...6), аби дізнатись, скільки залишилось днів до обраного дня</p>"

@app.route("/day=<day_id>")
def get_next_day(day_id) :
    day = int(day_id)

    '''Словник повідомлень для сьогоднішнього та наступного днів'''
    message_next = {
        0 : "наступного Понеділка",
        1 : "наступного Вівторка",
        2 : "наступної Середи",
        3 : "наступного Четверга",
        4 : "наступної П'ятниці",
        5 : "наступної Суботи",
        6 : "наступної Неділі"
    }
    message_today = {
        0 : "Понеділок",
        1 : "Вівторок",
        2 : "Середа",
        3 : "Четвер",
        4 : "П'ятниця",
        5 : "Субота",
        6 : "Неділя"
    }

    date_diff = get_diff(day)
    today = datetime.now()

    return f"<h1>Зворотній відлік до {message_next.get(day)}</h1><br>" \
           f"<h2>Сьогодні - {message_today.get(today.weekday())}, {today.strftime('%d/%m/%Y')}</h2>"\
           f"<p>До {message_next.get(day)} {date_diff[0]} залишилось {date_diff[1].days} днів</p>"

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=7000, debug=True)