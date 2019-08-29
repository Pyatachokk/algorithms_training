import logging
import sys
import argparse
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
    args = parser.parse_args()
    logger_2.info('Arguments parsed')

    #     Вызов основной функции от зафиксированных аргументов
    main(args.infile, args.outfile)


def str_parse(line):
    return [tuple(map(int, item.split(","))) for item in list(line.split('\t')[1:])]

def main(infile, outfile):
    logger_3 = logging.getLogger('Main function')
    logger_3.info('Main part started')

    file = open(infile[0], 'r', encoding='utf8')

    lines = [0] + [str_parse(line) for line in file.read().split('\n')[:-1]]

    logger_3.debug('lines parsed')
    src = 1
    dist = [2**30] * 201
    visited = [False] * 201
    queue = heapdict(order=False)

    logger_3.debug('queue created')
    cum_dist = 0
    dist[src] = 0
    visited[src] = True

    for item in lines[src]:
        dist[item[0]] = item[1]
        queue[item[0]] = item[1]

    logger_3.debug('first node added to queue')
    while len(queue.heap) > 0:
        # logger_3.debug(dict(queue))

        logger_3.debug('queue: {}'.format(queue.heap))
        logger_3.debug('names: {}'.format(queue.names))
        logger_3.debug('dict: {}'.format(list(queue.into.items())))

        u, c = queue.extract_root()
        logger_3.debug('root extracted successfully')
        logger_3.debug("{}, {}".format(u, c))

        u = int(u)
        cum_dist += c
        visited[u] = True
        dist[u] = cum_dist

        logger_3.debug('queue: {}'.format(queue.heap))
        logger_3.debug('names: {}'.format(queue.names))
        logger_3.debug('dict: {}'.format(list(queue.into.items())))

        assert len(queue.names) == len(queue.heap)
        assert len(queue.names) == len(queue.into)

        if len(lines[u]) == 1:
            dist[lines[u][0][0]] = cum_dist + lines[u][0][0]
            visited[lines[u][0][0]] = True
            cum_dist -= c
        else:
            for item in lines[u]:
                if visited[item[0]] == False:
                    if str(item[0]) in queue.into:
                        print("OK")
                        queue[item[0]] = min(queue[item[0]], cum_dist + item[1])
                        dist[item[0]] = min(queue[item[0]], cum_dist + item[1])
                    else:
                        queue[item[0]] = item[1]
                        dist[item[0]] = item[1]

    for i in [7,37,59,82,99,115,133,165,188,197]:
        print(dist[i])



if __name__ == '__main__':
    ToCommandLine()