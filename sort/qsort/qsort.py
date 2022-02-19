# -*- coding: utf-8 -*-
"""
алгоритм быстрой сортировки

"""


def qsort(x:list) -> list:
    
    if len(x) < 2:
        return x
    
    pivot = x[0]
    less = []
    greater = []
    # формируем 2 массива: больще и меньше опорного элемента 
    for val in x[1:]:
        if val < pivot:
            less.append(val)
        else:
            greater.append(val)
    # рекурсия
    return qsort(greater) + [pivot] + qsort(less)



if __name__ == '__main__':
    # самотест
    selftest = [[1,3,4,55,6,8,8,8,2,3,6,7,21],
                [2,3,4,5,6,7,8,9,34,4,2],
                [-2,3,4,2],
                [], [1], [1,2]]
    # счетчик ошибок
    cntr_err = 0
    for lst in selftest:
        mysort = qsort(lst)
        # питон сортируя список меняет исходный список
        lst.sort(reverse=True)
        if (mysort == lst):
            print(f'Ok: {mysort} == {lst}')
        else:
            cntr_err += 1
            print(f'Fail: {mysort} != {lst}')
    print('------------------------------\n'
          f'total errors: {cntr_err}' )