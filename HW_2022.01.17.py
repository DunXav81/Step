# ШАГ, Python 111, Дунько В. А.

'''
Задание
Выдано: 17.01.2022
Тема: Git

1. Установить себе домой Git
2. Сконфигурировать (добавить имя пользователя, пароль, ssh-ключ)
3. Инициализировать пустой репозиторий для выполнения следующего dz
4. Все задачи выполнять, записывая изменения в git (git commit -m "what I did")
5. Само задание: 
Получить с клавиатуры 6 чисел.
Вывести на экран их в возрастающем порядке
'''

number_of_element = 1
print ('\nВведите шесть любых целых чисел\n')
set_of_numbers = []

while number_of_element <= 6:
    element = int(input('Введите новое число: '))
    set_of_numbers.append(element)
    print ('Вы ввели элемент № ', number_of_element)
    number_of_element += 1

print ('\nВы ввели все шесть чисел:\n', set_of_numbers)

set_of_numbers.sort()
print('\nРасположим числа по возрастанию:\n', set_of_numbers)

