import re

def normalize_phone(phone_number):
    
    sanitized_phone = re.sub(r'[^\d\+]', '', phone_number) # очищує номер від зайвих символів крім цифр та знака плюс

  
    if sanitized_phone.startswith('380'): # працює із вже очищеними номерами, які починаються на '380'
        normalized_phone = '+' + sanitized_phone
    elif sanitized_phone.startswith('0'): # працює із вже очищеними номерами, які починаються на '0'
        normalized_phone = '+38' + sanitized_phone
    elif not sanitized_phone.startswith('+'): # працює із вже очищеними номерами, які НЕ починаються на '0'
        normalized_phone = '+38' + sanitized_phone
    else:
        normalized_phone = sanitized_phone # фіксуємо коректний номер 

    return normalized_phone

# Перевірка по 1одному номеру
print(normalize_phone("0501234567")) 
print(normalize_phone("    +38(050)123-32-34"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050 111 22 11   "))
print(normalize_phone("1234567890"))
print(normalize_phone("+1 (555) 123-4567"))

#  Перевірка списком
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "1234567890",
    "+1 (555) 123-4567" 
]

print([normalize_phone(num) for num in raw_numbers])