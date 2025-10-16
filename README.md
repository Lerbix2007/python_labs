#Лаба 2
Задание 1
```python
def min_max(nums):
    if not nums:
        raise ValueError("Список не может быть пустым")
    
    return (min(nums), max(nums))


def unique_sorting(nums):
    unique_nums = set(nums)      
    sorted_nums = sorted(unique_nums)  
    return sorted_nums


def flatten(mat):
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Ожидается список или кортеж, получен {type(row).__name__}")
        result.extend(row)
    return result


def main():    
    
    # Тест min_max
    print("\n1. Функция min_max(nums)")
    test_cases_minmax = [
        [3, -1, 5, 5, 0],
        [42],
        [-5, -2, -9],
        [1.5, 2, 2.0, -3.1]
    ]
    
    for nums in test_cases_minmax:
        result = min_max(nums)
        print(f"  {nums} → {result}")
    
    # Тест с пустым списком
    try:
        min_max([])
    except ValueError as e:
        print(f"  [] → ValueError: {e}")
    
    # Тест unique_sorting
    print("\n2. Функция unique_sorting(nums)")
    test_cases_unique = [
        [3, 1, 2, 1, 3],
        [],
        [-1, -1, 0, 2, 2],
        [1.0, 1, 2.5, 2.5, 0]
    ]
    
    for nums in test_cases_unique:
        result = unique_sorting(nums)
        print(f"  {nums} → {result}")
    
    # Тест flatten
    print("\n3. Функция flatten(mat)")
    test_cases_flatten = [
        [[1, 2], [3, 4]],
        [[1, 2], (3, 4, 5)],
        [[1], [], [2, 3]]
    ]
    
    for mat in test_cases_flatten:
        result = flatten(mat)
        print(f"  {mat} → {result}")
    
    # Тест с некорректным типом
    try:
        flatten([[1, 2], "ab"])
    except TypeError as e:
        print(f"  [[1, 2], \"ab\"] → TypeError: {e}")
    
    
if __name__ == "__main__":
    main()
```
![alt text](images/lab02/ex01.png)

Задание 2

```python
def is_rectangular(mat):
    if not mat:
        return True
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            return False
    return True


def transpose(mat):
    if not is_rectangular(mat):
        raise ValueError("Матрица должна быть прямоугольной")
    
    result = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        result.append(new_row)
    return result


def row_sums(mat):
    if not is_rectangular(mat):
        raise ValueError("Матрица должна быть прямоугольной")
    
    sums = []
    for row in mat:
        sums.append(sum(row))
    return sums


def print_matrix(mat, title=""):
    if title:
        print(title)
    for row in mat:
        print(row)


def main():
    print("ОПЕРАЦИИ С МАТРИЦАМИ")
    
    # Тестовая матрица
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("\nИсходная матрица:")
    print_matrix(matrix)
    
    print("\nТранспонированная матрица:")
    print_matrix(transpose(matrix))
    
    print("\nСуммы строк:")
    print(row_sums(matrix))
    
    # Тест с ошибкой
    print("\nТест с рваной матрицей:")
    try:
        wrong_matrix = [[1, 2], [3]]
        transpose(wrong_matrix)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
```
![alt text](images/lab02/ex02.png)

Задание 3

```python
def format_record(rec):
    fio, group, gpa = rec
    
    # Очистка ФИО
    fio_parts = fio.strip().split()
    fio_parts = [part.capitalize() for part in fio_parts]
    
    # Форматируем фамилию и инициалы
    surname = fio_parts[0]
    initials = []
    for i in range(1, len(fio_parts)):
        if fio_parts[i]:
            initials.append(fio_parts[i][0].upper() + ".")
    
    if initials:
        formatted_fio = f"{surname} {''.join(initials)}"
    else:
        formatted_fio = surname
    
    # Форматируем строку
    formatted_str = f"{formatted_fio}, гр. {group}, GPA {gpa:.2f}"
    
    return formatted_str


def main():
    print("ФОРМАТИРОВАНИЕ ЗАПИСЕЙ СТУДЕНТОВ")
    
    test_cases = [
        ("Росинский Леонид Андреевич", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
        ("Смирнов Алексей", "БИВТ-22", 4.5),
    ]
    
    for rec in test_cases:
        result = format_record(rec)
        print(f"Вход: {rec}")
        print(f"Результат: {result}\n")


if __name__ == "__main__":
    main()
```


![alt text](images/lab02/ex03.png)

#Лаба 3
Задание 1
```python
import re

def normalize(text, casefold=True, yo2e=True):
    if not text:
        return ""
    
    result = text
    
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    
    if casefold:
        result = result.casefold()
    
    result = result.strip()
    result = re.sub(r'\s+', ' ', result)
    
    return result

def tokenize(text):
    if not text:
        return []
    
    return re.findall(r'[\w\-]+', text)

def count_freq(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq, n=5):
    if not freq:
        return []
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def test_functions():
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ")
    print("=" * 50)
    
    # Тесты для normalize
    print("\n1. normalize():")
    test_cases = [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ]
    
    for input_text, expected in test_cases:
        result = normalize(input_text)
        print(f"  '{input_text}' → '{result}'")
    
    # Тесты для tokenize
    print("\n2. tokenize():")
    test_cases = [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ]
    
    for input_text, expected in test_cases:
        result = tokenize(input_text)
        print(f"  '{input_text}' → {result}")
    
    # Тесты для count_freq + top_n
    print("\n3. count_freq() + top_n():")
    
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    freq1 = count_freq(tokens1)
    top1 = top_n(freq1, 2)
    print(f"  {tokens1} → {top1}")
    
    tokens2 = ["bb", "aa", "bb", "aa", "cc"]
    freq2 = count_freq(tokens2)
    top2 = top_n(freq2, 2)
    print(f"  {tokens2} → {top2}")
def demo_text_analysis():
    """Демонстрационный текст для анализа во 2 задании"""
    demo_text = "Привет Мир!!! Привет!.."

if __name__ == "__main__":
    test_functions()
```
![alt text](images/lab03/ex01.png)
Задание 2
```python
import sys
from scr.lib.text import normalize, tokenize, count_freq, top_n 

def main():
    demo_text = "Привет Мир!!! Привет!.."
    print("-" * 30)
    print("\nПример анализа этого текста:")
    print("-" * 30)
    # Обрабатываем текст через функции 
    normalized_text = normalize(demo_text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, 5)
    
    # Выводим результаты
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")
    
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
![alt text](images/lab03/ex02.png)