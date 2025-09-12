
def caching_fibonacci():
    """
    Повертає функцію для обрахунку чисел Фібоначчі 
    """
    cache = dict()

    def fibonacci(n: int) -> int:
        """
        Функція обраховує числа Фібоначі n та зберігає результат в кеші
        """

        if n <= 0: # Перевіряємо чи n менше 0
            return 0
        elif n == 1: # Базовий випадок
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Додаємо в кеш суму двох попередніх чисел n
        
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
print(fib(5))
