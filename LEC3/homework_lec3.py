import numpy as np
import pandas as pd


def task1():
    """Приведите способы создания Series(надо было 3 конкретных)"""

    # 1. Из списка Python
    s1 = pd.Series([10, 20, 30, 40])
    print("1. Из списка:\n", s1)

    # 2. Скалярное значение
    s2 = pd.Series(5, index=[1, 2, 3, 4])
    print("2. Скаляр:\n", s2)

    # 3. Из словаря
    s3 = pd.Series({'a': 100, 'b': 200, 'c': 300})
    print("3. Словарь:\n", s3)


def task2():
    """Приведите способы создания DataFrame(конкретные 5))"""

    # 1. Через объекты Series
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series(['a', 'b', 'c'])
    df1 = pd.DataFrame({'col1': s1, 'col2': s2})
    print("1. Через объекты Series:\n", df1)

    # 2. Списки словарей
    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    df2 = pd.DataFrame(data)
    print("\n2. Списки словарей:\n", df2)

    # 3. Словарь объектов Series
    s3 = pd.Series([10, 20, 30])
    s4 = pd.Series([40, 50, 60])
    df3 = pd.DataFrame({'col1': s3, 'col2': s4})
    print("\n3. Словарь объектов Series:\n", df3)

    # 4. Двумерный массив NumPy
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    df4 = pd.DataFrame(arr, columns=['A', 'B'])
    print("\n4. Двумерный массив NumPy:\n", df4)

    # 5. Структурированный массив NumPy
    dtype = [('name', 'U10'), ('age', 'i4')]
    data = np.array([('Alice', 25), ('Bob', 30)], dtype=dtype)
    df5 = pd.DataFrame(data)
    print("\n5. Структурированный массив NumPy:\n", df5)

def task3():
    """Объединение Series с заменой NaN на 1"""
    s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    s2 = pd.Series([40, 50, 60], index=['b', 'c', 'd'])

    # Объединение с заполнением NaN значением 1
    combined = s1.add(s2, fill_value=1)
    print("Результат объединения:\n", combined)


def task4():
    """Транслирование по столбцам"""
    df = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=['A', 'B', 'C'])
    print("Исходный DataFrame:\n", df)

    # Вычитание первого столбца из всех столбцов
    result = df.sub(df['A'], axis=0)
    print("\nПосле вычитания столбца 'A' из всех столбцов:\n", result)


def task5():
    """Методы ffill и bfill"""
    df = pd.DataFrame({
        'A': [1, np.nan, 3, np.nan],
        'B': [np.nan, 5, np.nan, 7],
        'C': [8, 9, np.nan, 11]
    })
    print("Исходный DataFrame:\n", df)

    # Заполнение вперед (ffill)
    filled_ffill = df.ffill()
    print("\nПосле ffill():\n", filled_ffill)

    # Заполнение назад (bfill)
    filled_bfill = df.bfill()
    print("\nПосле bfill():\n", filled_bfill)


def main():
    task1()
    task2()
    task3()
    task4()
    task5()


if __name__ == "__main__":
    main()