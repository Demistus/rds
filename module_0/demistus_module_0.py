import numpy as np

def game_core_v3(predict):
    ''' Функция принимает любое случайное число - наше первое предположение загаданного числа и возвращает число попыток
        до угадывания загаданного компьютером числа. Используется алгоритм бинарного поиска.'''
    count = 0
    lower_limit = 1
    upper_limit = 100
    number = np.random.randint(1,101) # компьютер загадал число от 1 до 100
    while predict != number:
        count += 1
        if predict < number:
            lower_limit = predict # нижний предел поиска ограничиваем предположенным числом
            predict = (upper_limit+lower_limit) // 2 
        elif predict > number:
            upper_limit = predict # верхний предел поиска ограничиваем предположенным числом
            predict = (upper_limit+lower_limit) // 2 
    return count

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
        score = int(np.mean(count_ls))
        print('Ваш алгоритм угадывает число в среднем за {} попыток'.format(score))
        return score

# Проверяем

score_game(game_core_v3)

# Вывод такой:

# Ваш алгоритм угадывает число в среднем за 6 попыток

