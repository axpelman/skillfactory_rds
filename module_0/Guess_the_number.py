import numpy as np # import the numpy library

def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    
def game_core_v3(number):
    '''First, we set the value to 50 (half of the specified range) in the range of values from 0 to 100, and then decrease or increase it depending on whether it is more or less than the desired one using the binary search algorithm. The function takes the desired value and returns the number of attempts.'''
    count = 0 # attempt counter
    predict = 50
    first_number = 0 # first value of a given range
    last_number = 100 # last value of a given range
    while number != predict: # the cycle runs until the selected value becomes equal to the desired
        count += 1 # with each iteration of the loop, the counter of the number of attempts increases by 1
        predict = (first_number + last_number)//2 # reduce the search area of the desired value
        if number > predict: # if the desired value is greater than the selected, 
            first_number = predict + 1 # the first value of the specified range is taken as the selected increased by 1
        else: last_number = predict - 1 # if the desired value is less than the selected, the first value of the specified range is taken as the selected reduced by 1

    return(count) # exit from the cycle, with the number of attempts if the number is guessed
