import datetime

def get_upcoming_birthdays(users):

    upcoming_birthdays = [] # створюємо список

    today = datetime.datetime.today().date() # створюэмо змінну що містить актуальну дату. Одразу обрізаємо час, залишаючи лише дату

    print(f"Текущая дата: {today}\n") # Добавлено для отладки

    for info in users: # перебираємо список
        name = info ['name'] # дістаємо зі списку ім'я та дату народження
        birthday_str = info ['birthday']
        try:
            birthday = datetime.datetime.strptime(birthday_str, "%Y.%m.%d").date()
        except ValueError:
            print(f"Некоректний формат дати нарождення")
            continue
        pass
        
        birthday_this_year = birthday.replace(year=today.year) # змінюємо рік народження на теперішній рік

        if birthday_this_year < today: # якщо ДР вже був у цьому році, то розглядаємо наступний рік
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        delta_days = (birthday_this_year - today).days # розраховуэмо різницю між датами

        if 0 <= delta_days < 7: # перевіряємо чи ДР в найближчі 7 днів

            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5: # якщо ДР припадає не суботу чи неділю, то день вітання перетворюємо на найближчий понеділок
                congratulation_date += datetime.timedelta(days=2)
            elif  congratulation_date.weekday() == 6:
                congratulation_date += datetime.timedelta(days=1)
        
            upcoming_birthdays.append({ # додаємо зібрану інфу до нового списку (словника)
                "name": name, 
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })              
     
    return upcoming_birthdays

# список людей та ДР
users = [
    {"name": "John Doe", "birthday": "1992.10.22"},   # завтра
    {"name": "Emily Johnson", "birthday": "1988.10.25"},  # через кілька днів

    {"name": "Michael Brown", "birthday": "1985.10.25"},  # субота
    {"name": "Sarah Miller", "birthday": "1990.10.26"}] # неділя

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
