#include <iostream>

/*! @brief print array
 *
 *  @param beg адресс первого элемента массива
 *  @param beg адресс последнего элемента массива
 *  @return Void.
 */
void print(int *beg, int * end)
{
    std::cout << " {";
    while(beg < end)
    {
        std::cout << *beg << ", ";
        beg++;
    }
    std::cout << *end << " }" << std::endl;
}

/*! @brief деление массива на две части
 *
 * Вспомогательная функция быстрой сортировки
 * Функция переставляет элеметны массива таки образом, 
 * что изначально последний элемент оказывается на позиции, 
 * когда все элементы до его позиции больше, а после - меньше
 *
 * Пример:
 * { 0,  2, 32, 11,  3,  7,  6, 10}->
 * {11, 32, 10,  0,  3,  7,  6,  2}
 * Т.е. произошло несколько перестановок и в результате, все что левее "10" - больше 10, 
 * а всё что правее - меньше
 *
 *  @param beg адресс первого элемента массива
 *  @param beg адресс последнего элемента массива
 *  @return адрес "среднего" элемента. По адресам ниже элементы большие "среднего" эелемента, по адресам выще - элементы массива меньшие "среднего" эелемента.
 */
int* partition(int *beg, int* end)
{
    int tmp;
    int *pivot = end;
    while(beg < end)
    {
        while (*pivot >= *end &&  beg < end)
            end--;
        
        while (*pivot < *beg)
            beg++;
        
        if (beg < end)
        {
            tmp = *end;
            *end = *beg;
            *beg = tmp;
        }
    }
    tmp = *pivot;
    *pivot = *beg;
    *beg = tmp;
    return beg;
}

/*! @brief быстрая сортировка целочисленного массива
 *
 *  В функции используется рекурсия. Внутри массива элементы несколько раз меняются местами.
 *  В результате сортировки элементы распалагаются от большего к меньшему
 *
 *  @param beg адресс первого элемента массива
 *  @param beg адресс последнего элемента массива
 *  @return Void
 */
void qsort(int *beg, int* end)
{
    std::cout << "-----------------------" << std::endl;
    print(beg, end);
    if (end - beg < 1)
        return;
    int *p = partition(beg, end);
    
    
    std::cout << p - beg << "  -> "<< *p << std::endl;
    print(beg, p-1);
    std::cout << *p << std::endl;
    print(p+1, end);
    std::cout << "-----------------------" << std::endl;
    qsort(beg, p-1);
    qsort(p+1, end);
    return;
}



int main()
{
    // поленился написать нормальный цикл для тестирования....
//    {
//    int arr[] = {1,3,2,77,4,13,-2,3,12,43,5};
//    int *end = (int *)(&arr + 1) - 1;
//    print(arr, end);
//    qsort(arr, end);
//    print(arr, end);
//    }
    std::cout << "----------------" << std::endl;
    {
    int arr[] = { 0,  2, 32, 11,  3,  7,  6, 10};
    int *end = (int *)(&arr + 1) - 1;
    print(arr, end);
    qsort(arr, end);
    print(arr, end);
    }
    return 0;
}