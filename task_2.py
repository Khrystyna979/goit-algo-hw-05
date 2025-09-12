import re
from typing import Callable


def generator_numbers(text: str):
    """
    Функція для пошуку чисел по патерну в тексті
    Повертає генератор знайденого збігу
    """

    pattern = r'\d+.\d+' # Патерн для пошуку дійсного числа
    
    for match in re.finditer(pattern, text): # цикл який знаходить збіг в тексті та при виклику генератора видає кожен наступний збіг
        yield float(match.group()) # Дозволяє отримати збіг як дійсне число



def sum_profit(text: str, func: Callable) -> float:
    """
    Функція для отримання суми доходу через генератор
    """
    profit = sum(func(text)) # sum виступає в ролі циклу та викликає наш генератор і додає результат функції у нашу змінну 
    return profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, " \
"доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

