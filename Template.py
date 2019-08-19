import logging
import sys
import argparse

# Определяем базовую конфигурацию логера
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logs/Template.log',  # Основной файл, куда перенаправляются все логи, включая корневой
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


def main(infile, outfile):
    pass


if __name__ == '__main__':
    ToCommandLine()