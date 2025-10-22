# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
# ... яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
import random

def get_numbers_ticket(min_num, max_num, quantity):        
  
    if (min_num < 1 or # перевіряємо вхідні дані
        max_num > 1000 or
        quantity < 1 or 
        min_num > max_num or 
        quantity > (max_num - min_num + 1)):
        return [] 
         
    lottery_numbers = random.sample(range(min_num, max_num + 1), quantity) # оскільки працюємо з ренжем, то  необхідно включити верхню границю

    sorted_lottery_numbers = sorted(lottery_numbers) # сортуюмо номери у порядку зростання

    return sorted_lottery_numbers

print(get_numbers_ticket(1,36,5))
print(get_numbers_ticket(-5,49,5))
print(get_numbers_ticket(1,49,50))



        
