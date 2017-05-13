# Мурованый Андрей.КНИТ16-А
# Условие: имеется n городов, система дорог между которыми представлена
# матрицей a[i][j].Найти кратчайший маршрут, начинающийся в первом городе
# и проходящий через все остальные города.
from os import chdir, getcwd
from numpy import ones
from pickle import dump, load


def distance(countries, start, distance_matrix):
    """
    Алгоритм Дейкстры.
    
    Алгоритм дейкстры для определения кратчайшего пути.
    :param countries: Количество городов
    :param start: начальный город
    :param distance_matrix: матрица достижимости
    :return: оптимальный путь
    """
    valid = [True] * countries
    weight = [1000000] * countries
    weight[start] = 0
    for i in range(countries):
        min_weight = 1000001
        min_w = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                min_w = i
        for i in range(countries):
            if weight[min_w] + distance_matrix[min_w][i] < weight[i]:
                weight[i] = weight[min_w] + distance_matrix[min_w][i]
        valid[min_w] = False
    return weight


while True:
    chdir('D:/NewFold/MyFold')
    print('Мы находимся в следующуей директории:', getcwd())
    countries = int(input('Введите кол-во городов: \n'
                          '>>> '))
    country_name = []
    distance_matrix = ones((countries, countries), dtype=int)
    i = 0
    while len(country_name) < countries:
        i += 1
        country_name.append(input('Название {} города: '.format(str(i)) + '\n'
                            '>>> '))
    for j in range(countries):
        for k in range(countries):
            if j != k:
                if distance_matrix[j][k] == 1 and distance_matrix[j][k] == 1:
                    distance_matrix[k][j] = distance_matrix[j][k] = \
                        int(input('Расстояние между {} и {} '.
                                  format(country_name[j], country_name[k])))
            else:
                distance_matrix[j][k] = 0

    print('Список городов: ', country_name)
    print('Короткий путь: ', distance(countries, 0, distance_matrix))
    if input('Press Enter to continue...') != '':
        flag = False
        break
