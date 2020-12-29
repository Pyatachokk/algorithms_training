import logging
import sys
import argparse

import heapq as hq
import math
from heapdict_raw import heapdict

# Определяем базовую конфигурацию логера
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logs/C2W2_Dijkstra.log',  # Основной файл, куда перенаправляются все логи, включая корневой
                    filemode='w')

# Консольный логгер. В него попадают только логи уровня INFO и выше
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Определяем форматтер консольного логгера
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# Передаём формат консольному логгеру
console.setFormatter(formatter)
# Добавляем ссылку на консольный логгер корневому логгеру
logging.getLogger('').addHandler(console)

# Определяем дополнительные логгеры там, где необходимо
logger_1 = logging.getLogger('Outer logger')
logger_1.info('Compilation started')


# При желании можно изменить этому логгеру уровень логирования и прописать отдельный файл, куда
# будут записываться только сообщения от этого логгера. Но они также будут дублироваться в основной файл

# logger_1.setLevel(logging.WARNING)
# other_file = logging.FileHandler('Outer.log', mode = 'w')
# other_file.setLevel(logging.WARNING)
# other_file.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
# logger_1.addHandler(other_file)
# logger_1.info('Done handlers')
# logger_1.warning('Warning')


def ToCommandLine():
    logger_2 = logging.getLogger('Arguments parsing')
    logger_2.info('Program started')

    #     Парсим аргументы. Два kwargs текстовых документа. Если не указаны, то стандартынй ввод-вывод.
    parser = argparse.ArgumentParser(description='Template argument parsing')
    parser.add_argument('--infile', metavar='Input', nargs=1, type=str, default=sys.stdin,
                        help='Input txt file. If not specified, stdin.')
    parser.add_argument('--outfile', metavar='Output', nargs=1, type=str, default=sys.stdout,
                        help='Output txt file. If not specified, stdout.')
    parser.add_argument('src', metavar='Source vertex', nargs=1, type=int, default=sys.stdout,
                        help='Source vertex for algorithm\'s start')
    args = parser.parse_args()
    logger_2.info('Arguments parsed')

    #     Вызов основной функции от зафиксированных аргументов
    main(args.infile, args.outfile, args.src)


def str_parse(line):

    split = line.split('\t')
    source = int(split[0])
    other = split[1:-1]

    return([list(map(int, other[i].split(','))) for i in range(len(other))])
    # print(line)


def dijkstra(G, s):
    n = len(G)
    visited = [False]*(n+1)
    weights = [math.inf]*(n+1)
    path = [None]*(n+1)
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights



def main(infile, outfile, source):
    logger_3 = logging.getLogger('Main function')
    logger_3.info('Main part started')

    file = open(infile[0], 'r', encoding='utf8')

    lines = [0] + [str_parse(line) for line in file.read().split('\n')[:-1]]

    print(lines)

    dists = dijkstra(lines, 1)[1]


    for i in (7,37,59,82,99,115,133,165,188,197):
        print(dists[i])

if __name__ == '__main__':
    ToCommandLine()

