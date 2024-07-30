#Дополнительное практическое задание по модулю3
data_structure =  [[1, 2, 3],
          {'a': 4, 'b': 5},
          (6, {'cube': 7, 'drum': 8}),
          "Hello",
          ((), [{(2, 'Urban', ('Urban2', 35))}])]
structure_sum = 0 # сумма элементов структуры

def structure_sum_(*args):
    '''Сохраняет сумму переданных аргументов  в переменной structure_sum
       в зависимости от типа аргумента: числовой - как число,
       строковый как количество символов строки,
       для словарей передается передается два рагумента: ключ и значение'''
    global structure_sum
    for i in args:
        if type(i) == int:
            structure_sum += i
        else:
            structure_sum += len(i)

def calculate_structure_sum(structure_):
    '''Разбирает передаваемую структуру на отдельные объекты и в зависимости от
       типа объекта передает каждый элемент объекта в функцию structure_sum для
       подсчета суммы структуры, для объектов типа:
        dict - передает значения всех ключей и значений,
        list, tuple, set -  передает значения всех элементов,
        int, str - передает сам объект'''
    #обработка объектов типа словарь
    if isinstance(structure_, (dict)):
        for k, v in structure_.items():
            if isinstance(v, (dict, list, tuple, set)):
                calculate_structure_sum(v)
            else:
                structure_sum_(k, v)
    else:
        #перебирает элементы structure_ за исключением объектов типа словарь
        #если очередной элемент - словарь, список, кортеж, множество
        #осуществляется рекурсивный вызов функции calculate_structure_sum
        #с передачей в качестве аргумента данного элемента

        for i in structure_:
            #проверка принадлежности очередного элемента structure_ к типу: словарь
            if isinstance(i, dict):
                calculate_structure_sum(i)
            #проверка принадлежности очередного объекта structure_ к типу:
            #список, кортеж, множество и обработка элементов объектов данных типов
            if isinstance((i), (list, tuple, set)):
                for value_ in i:
                    if isinstance(value_, (dict, list, tuple, set)):
                        calculate_structure_sum(value_)
                    else:
                        structure_sum_(value_)
            #проверка принадлежности очередного объекта structure_ к типу:
            #число, строка
            if isinstance(i, (int, str)):
                structure_sum_(i)

calculate_structure_sum(data_structure)
print(f'Сумма элементов структуры: {structure_sum}')
