import random


def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    k = low - 1
    g = high + 1
    while True:
        k += 1
        while nums[k] < pivot:
            k += 1
        g -= 1
        while nums[g] > pivot:
            g -= 1
        if k >= g:
            return g

        # Если элемент с индексом k (слева от опорного) больше, чем
        # элемент с индексом g (справа от опорного), меняем их местами
        nums[k], nums[g] = nums[g], nums[k]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


with open('ORDER.txt', 'r') as file:
    inner_list = [line.strip().split() for line in file.readlines()]
column_names = 'Расчетный счет плательщика, Расчетный счет получателя, Перечисляемая сумма в руб.'
print(column_names)
for strInner_list in inner_list:
    print(strInner_list)


random_index = random.randint(0, len(inner_list)-1)
print('\nНомер операции:', str(random_index + 1) + '.\nРасчетный счет плательщика, соответсвующий номеру операции:',
      inner_list[random_index][0] + '.')


string_rand_ind_0 = inner_list[random_index][0]
string_rand_ind_1 = inner_list[random_index][1]
string = inner_list[random_index][0], inner_list[random_index][1]
zero_counter = string_rand_ind_0.count('0') + string_rand_ind_1.count('0')
print('Расчетный счет получателя, соответсвующий номеру операции:', string_rand_ind_1 + '.')
print('Количество нулей, встречающихся в расчетном счете плательщиа и расчетном счете получателя вместе:',
      str(zero_counter) + '.')


for i in range(len(inner_list)):
    if zero_counter <= 5:
        if inner_list[random_index][0] == inner_list[i][0]:
            with open('ORDER_out_part_a.txt', 'a') as file:
                file.writelines(' '.join(map(str, inner_list[i])))
                file.writelines('\n')
                print('\nФайл ORDER_out_part_a.txt успешно загружен.')
    else:
        print('\nФайл ORDER_out_part_a.txt не загружен, так как количество нулей (' + str(zero_counter) + ') > 5.')
        break


inner_list_cost = [inner_list[0][2]]
for i in range(1, len(inner_list)):
    inner_list_cost += [inner_list[i][2]]
sort_list_cost = inner_list_cost
quick_sort(sort_list_cost)


sort_inner_list = []
for i in range(len(inner_list)):
    j = 0
    while inner_list[j][2] != sort_list_cost[i]:
        j += 1
    if inner_list[j][2] == sort_list_cost[i]:
        with open('ORDER_out_part_b.txt', 'a') as file:
            file.writelines(' '.join(map(str, inner_list[j])))
            file.writelines('\n')
print('\nФайл ORDER_out_part_b.txt успешно загружен.')


sorted_inner_list = sorted(inner_list, key=lambda x: x[2])
print('\n\nОтсортированный список по перечисляемой сумме:\n')
print(column_names)
for strSorted_inner_list in sorted_inner_list:
    print(strSorted_inner_list)