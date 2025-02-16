import numpy as np
import sys
import array as ar



# Задание 2: Напишите код, подобный приведенному выше, но с другим типом.
def array_with_different_type():
    a2 = ar.array('f', [1.5, 2.5, 3.5])
    print("\nФлоат массив(числа с плавающей точкой)")
    print(sys.getsizeof(a2))
    print(type(a2))
    print(a2)


# Задание 3: Напишите код для создания массива с 5 значениями, расположенными через равные интервалы в диапазоне от 0 до 1
def create_linspace_array():
    return np.linspace(0, 1, 5)


# Задание 4: Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1
def create_uniform_random_array():
    return np.random.uniform(0, 1, 5)


# Задание 5: Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией = 1
def create_normal_random_array():
    return np.random.normal(0, 1, 5)


# Задание 6: Напишите код для создания массива с 5 случайными целыми числами в диапазоне [0, 10)
def create_random_int_array():
    return np.random.randint(0, 10, 5)


# Задание 7: Написать код для создания срезов массива 3 на 4
# - первые две строки и три столбца: arr[:2, :3]
# - первые три строки и второй столбец: arr[:, 1]
# - все строки и столбцы в обратном порядке: arr[::-1, ::-1]
# - второй столбец: arr[:, 1]
# - третья строка: arr[2, :]
def create_slices():
    arr = np.arange(1, 13).reshape(3, 4)
    print("\nИсходный массив:")
    print(arr)

    print("\nПервые две строки и три столбца:")
    print(arr[:2, :3])

    print("\nПервые три строки и второй столбец:")
    print(arr[:, 1])

    print("\nВсе строки и столбцы в обратном порядке:")
    print(arr[::-1, ::-1])

    print("\nВторой столбец:")
    print(arr[:, 1])

    print("\nТретья строка:")
    print(arr[2, :])


# Задание 8: Продемонстрируйте, как сделать срез-копию
def create_slice_copy():
    arr = np.array([1, 2, 3, 4, 5, 6])
    # Просто применяем метод copy(если массив одномерный, иначе
    # можно было бы и deepcopy использовать)
    slice_copy = arr[:3].copy()
    slice_copy[0] = 100
    print("\nИсходный массив после изменения срез-копии:")
    print(arr)
    print("Срез-копия после изменения:")
    print(slice_copy)


# Задание 9: Написать код использования newaxis для получения вектор-столбца и вектор-строки
def use_newaxis():
    x = np.array([1, 2, 3])
    print("\nВектор-столбец:")
    print(x[:, np.newaxis])
    print("Вектор-строка:")
    print(x[np.newaxis, :])


# Задание 10: Код как работает метод dstack
# Метод dstack (depth stack) объединяет массивы по третьей оси (глубине).
# То есть если есть два 2D-массива, они будут объединены в 3D-массив.
def demonstrate_dstack():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("\nРезультат dstack:")
    print(np.dstack((a, b)))


# Задание 11: Код как работают split, vsplit, hsplit
# - split: Разделяет массив на подмассивы по указанной оси.
# - vsplit: Разделяет массив по вертикали (по строкам).
# - hsplit: Разделяет массив по горизонтали (по столбцам).
def demonstrate_splits():
    arr = np.arange(1, 13).reshape(3, 4)
    print("\nИсходный массив для split:")
    print(arr)

    print("\nРезультат split:")
    print(np.split(arr, 3))

    print("\nРезультат vsplit:")
    print(np.vsplit(arr, 3))

    print("\nРезультат hsplit:")
    print(np.hsplit(arr, 2))


# Задание 12: Привести пример использования всех универсальных функций (-, /, //, **, %)
def demonstrate_ufuncs():
    a = np.array([10, 20, 30])
    b = np.array([3, 5, 7])

    print("\nИсходные массивы:")
    print("a:", a)
    print("b:", b)

    print("\nМинус для изменения знака:")
    print("-a:", -a)

    print("\nВычитание:")
    print(a - b)

    print("\nДеление:")
    print(a / b)

    print("\nЦелочисленное деление:")
    print(a // b)

    print("\nВозведение в степень:")
    print(a ** b)

    print("\nОстаток от деления:")
    print(a % b)


# Вызов всех функций
def main():
    # Задание 1: Какие еще коды типов есть? Кроме 'i'.
    # Другие коды типов для array.array:
    # 'b' — signed char (int, 1 byte)
    # 'B' — unsigned char (int, 1 byte)
    # 'u' — Py_UNICODE (Unicode character, 2 bytes)
    # 'h' — signed short (int, 2 bytes)
    # 'H' — unsigned short (int, 2 bytes)
    # 'i' — signed int (int, 2 bytes)
    # 'I' — unsigned int (int, 2 bytes)
    # 'l' — signed long (int, 4 bytes)
    # 'L' — unsigned long (int, 4 bytes)
    # 'f' — float (float, 4 bytes)
    # 'd' — double (float, 8 bytes)
    print("Задание 2")
    array_with_different_type()

    print("\nЗадание 3")
    print(create_linspace_array())

    print("\nЗадание 4")
    print(create_uniform_random_array())

    print("\nЗадание 5")
    print(create_normal_random_array())

    print("\nЗадание 6")
    print(create_random_int_array())

    print("\nЗадание 7")
    create_slices()

    print("\nЗадание 8")
    create_slice_copy()

    print("\nЗадание 9")
    use_newaxis()

    print("\nЗадание 10")
    demonstrate_dstack()

    print("\nЗадание 11")
    demonstrate_splits()

    print("\nЗадание 12")
    demonstrate_ufuncs()

if __name__ == "__main__":
    main()