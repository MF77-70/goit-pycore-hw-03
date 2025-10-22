# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
import datetime
from datetime import date, time, timedelta

def get_days_from_today(input_date) -> int : 
    
    try:   # перетворюэмо вхідні дані у формат дати та опрацьовуємо можливу помилку
        parsed_date = datetime.datetime.strptime(input_date, '%Y-%m-%d')

    except ValueError: 
        print(f'Виникала помилка: некоректний формат дати {input_date}. Правильний формат: РРРР-ММ-ДД.')
        return
              

    parsed_date_only = datetime.datetime.strptime(input_date, '%Y-%m-%d').date() # вхідні дані вже у форматі дати та часу обмежуємо датою

    today_date = datetime.datetime.today() # знаходимо сьогоднішню дату
    today_date_only = datetime.datetime.today().date() # обмежуємо сьогоднішню дату лише датою

    date_time_diff = today_date_only - parsed_date_only # знаходимо різницю між вхідною датою та сьогоднішньою
    days_diff = date_time_diff.days
    return days_diff
   

print (get_days_from_today ('2025-09-01'))           
print (get_days_from_today ('2025-12-01')) 
print (get_days_from_today ('2025-13-01')) 