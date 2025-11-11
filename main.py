import random

# Создаем список из 10 случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Исходный список: {numbers}")

# 1. Находим сумму всех элементов
total_sum = sum(numbers)
print(f"Сумма всех элементов: {total_sum}")

# 2. Находим максимальный и минимальный элемент
max_element = max(numbers)
min_element = min(numbers)
print(f"Максимальный элемент: {max_element}")
print(f"Минимальный элемент: {min_element}")

# 3. Сортируем список по возрастанию и убыванию
ascending_sorted = sorted(numbers)
descending_sorted = sorted(numbers, reverse=True)
print(f"Сортировка по возрастанию: {ascending_sorted}")
print(f"Сортировка по убыванию: {descending_sorted}")

# 4. Удаляем все четные числа из списка
numbers_without_even = [x for x in numbers if x % 2 != 0]
print(f"Список без четных чисел: {numbers_without_even}")
# Создаем кортеж из 5 различных элементов разных типов
my_tuple = (42, "Hello", 3.14, [1, 2, 3], {"name": "John"})
print(f"Исходный кортеж: {my_tuple}")
#1.2  задание
# 1. Пытаемся изменить один из элементов (должна возникнуть ошибка)
try:
    my_tuple[0] = 100  # Эта строка вызовет ошибку
except TypeError as e:
    print(f"Ошибка при попытке изменить кортеж: {e}")

# 2. Преобразуем кортеж в список
my_list = list(my_tuple)
print(f"Преобразованный список: {my_list}")

# 3. Добавляем новый элемент в преобразованный список
my_list.append("Новый элемент")
print(f"Список после добавления элемента: {my_list}")

# 4. Преобразуем список обратно в кортеж
new_tuple = tuple(my_list)
print(f"Новый кортеж: {new_tuple}")
#1.3 задание 
# Создаем список списков, представляющий таблицу 3x3
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Вывод таблицы в читаемом виде
print("Таблица 3x3:")
for row in table:
    print(row)

# Альтернативный красивый вывод
print("\nКрасивый вывод таблицы:")
for i, row in enumerate(table):
    print(f"Строка {i+1}: {row}")

# 2. Поиск суммы всех элементов таблицы
total_sum = 0
for row in table:
    total_sum += sum(row)
print(f"\nСумма всех элементов таблицы: {total_sum}")

# Более короткий способ
total_sum_short = sum(sum(row) for row in table)
print(f"Сумма всех элементов (короткий способ): {total_sum_short}")

# 3. Поиск суммы элементов каждой строки
print("\nСуммы по строкам:")
for i, row in enumerate(table):
    row_sum = sum(row)
    print(f"Строка {i+1}: {row} -> Сумма: {row_sum}")
