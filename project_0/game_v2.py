import numpy as np

def game_core_v3(number:int=1) -> int:
    """Угадываем число на минимальное возомжное количество итераций

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    predict = 50

    if predict != number:
        while predict != number:
            count +=1  
            if predict < number:                        #Проверяем условия совпадение числа предсказания с загаданным
                predict += round(predict / 2)           #И каждый раз, пока не найдем само число
            elif predict > number:                      #снижаем область поиска в два раза
                predict -= round(predict / 2)
    else:
        count += 1
        
    return(count)

print(f'Количество попыток: {game_core_v3()}')

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] 
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(game_core_v3)