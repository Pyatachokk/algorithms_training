import logging
import sys
import argparse

# Определяем базовую конфигурацию логера
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logs/C2W3_dynamic_median.log',  # Основной файл, куда перенаправляются все логи, включая корневой
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


class Heap:
    def __init__(self, order):
        self.heap = []
        self.order = order #True - maxheap, False - minheap

    def is_valid(self, parent, child):
        if parent < len(self.heap) and child < len(self.heap):
            if self.order:
                return self.heap[parent] >= self.heap[child]
            else:
                return self.heap[parent] <= self.heap[child]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def shift_up(self, c_i):
        p_i = (c_i - 1) // 2
        if p_i == c_i:
            return
        while (not self.is_valid(p_i, c_i)):
            self.swap(p_i, c_i)
            c_i = p_i
            if c_i == 0:
                break
            p_i = (c_i - 1) // 2


    def shift_down(self, p_i):
        c_i = self.get_swap_child_ind(p_i)
        if p_i == c_i:
            return
        while c_i and self.is_valid(p_i, c_i):
            self.swap(p_i, c_i)
            p_i = c_i
            c_i = self.get_swap_child_ind(p_i)

    def get_swap_child_ind(self, p_i):
        l_i = 2*p_i + 1
        r_i = 2*p_i + 2
        size = len(self.heap)

        if l_i >= size:
            return None
        elif r_i >= size:
            return l_i

        if self.order:
            return max(l_i, r_i, key=lambda x: self.heap[x])
        else:
            return min(l_i, r_i, key=lambda x: self.heap[x])


    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap) - 1)

    def delete(self, key):
        self.swap(key, -1)
        removed = self.heap.pop()
        p_i = (key - 1) // 2

        if self.is_valid(p_i, key):
            self.shift_down(key)
        else:
            self.shift_up(key)
        return removed

    def extract_root(self):
        if self.heap:
            self.swap(0, len(self.heap)-1)
            root = self.heap.pop()
            self.shift_down(0)
            return root

    def get_root(self):
        if self.heap:
            return self.heap[0]




def main(infile, outfile):
    logger_1.info('main-part started')
    if type(infile[0]) == str:
        try:
            text_file = open(infile[0], encoding = 'utf8')
            marker = True
        except ValueError:
            logger_1.error('invalid input filename')

    else:

        logger_1.info('reading from console')
        marker = False

    low_heap = Heap(order=True)
    high_heap = Heap(order=False)
    median = 0
    sum = 0
    while True:
        if marker:
            new_int = text_file.readline()
            try:
                new_int = int(new_int)
            except ValueError:
                break
        else:
            new_int = input()
            if new_int == ' ':
                break
            else:
                try:
                    new_int = int(new_int)
                except ValueError:
                    print("Invalig input type. Please, input integet.")
                    continue

        assert type(new_int) == int

        if len(high_heap.heap) == len(low_heap.heap):
            if new_int > median:
                high_heap.insert(new_int)
                high_min = high_heap.extract_root()
                low_heap.insert(high_min)
                sum += high_min
            else:
                low_heap.insert(new_int)
                sum += low_heap.get_root()
            median = low_heap.get_root()
        elif len(high_heap.heap) < len(low_heap.heap):
            if new_int > median:
                high_heap.insert(new_int)
                sum += low_heap.get_root()
            else:
                high_heap.insert(low_heap.extract_root())
                low_heap.insert(new_int)
                sum += low_heap.get_root()
            median = low_heap.get_root()
        logger_1.debug('low heap: {}'.format(low_heap.heap))
        logger_1.debug('high_heap: {}'.format(high_heap.heap))
    print(sum)



if __name__ == '__main__':
    ToCommandLine()