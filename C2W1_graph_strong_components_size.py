import argparse
import sys
import logging

time = 1
num_nodes = 875714
count = 0

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logs/SCC.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)



def ToCommandLine():
    logger_1 = logging.getLogger('Arguments parsing')


    logger_1.info('Program started')
    parser = argparse.ArgumentParser(description= 'Quicksort algorythm with first entry as pivot.')
    parser.add_argument('--infile', metavar = 'Input', nargs = 1, type = str, default = sys.stdin, help = 'Input txt file. If not specified, stdin.')
    parser.add_argument('--outfile', metavar = 'Output', nargs = 1, type = str, default=sys.stdout, help = 'Output txt file. If not specified, stdout.')
    args = parser.parse_args()
    logger_1.info('Arguments parsed')

    main(args.infile, args.outfile)


def main(infile, outfile):
    global time
    global count
    logger_2 = logging.getLogger('Main part')
    file = open(infile[0], 'r', encoding='utf8')

    lines = [str_parse(line) for line in file.read().split('\n')]

    logger_2.debug('{}'.format(lines[:5]))

    nodes = range(1, num_nodes + 1)
    values = [0 for i in range(num_nodes + 1)]
    logger_2.debug('Vals before inverse:{}'.format(values[:5]))

    direct = make_graph(lines, 0, 1)
    reverse = make_graph(lines, 1, 0)

    state = ["W" for i in range(num_nodes + 1)]
    logger_2.debug('State vals before inverse: {}'.format(state[:5]))

    logger_2.info('Reversed search started')
    for node in nodes:
        if state[node] == "W":
            DFS_ITER(reverse, node, reversed=True, values = values, state = state)
    logger_2.info('Reversed search finished')

    from operator import itemgetter
    values = list(enumerate(values))
    values.sort(reverse=True, key=itemgetter(1))
    state = ["W" for i in range(num_nodes + 1)]

    logger_2.debug('Vals after inverse:{}'.format(values[:5]))
    logger_2.debug('State vals after inverse: {}'.format(state[:5]))
    print("Time: ", time)

    logger_2.info('Direct search started')
    results = []
    for pair in values:
        if pair[0] != 0:
            node = pair[0]
            if state[node] == "W":

                DFS_ITER(direct, node, reversed=False, state = state, values = values)
                results.append(count)
                count = 0

    logger_2.info('Direct search finished')
    results.sort(reverse=True)
    print(len(results))
    print(results[:5])


def str_parse(line):
    return list(map(int, line.split(' ')[:-1]))


def make_graph(lines, first, second):
    global num_nodes
    graph = [[] for i in range(num_nodes + 1)]
    for line in lines:
        if line[first] != line[second]:
            graph[line[first]].append(line[second])
    return graph


def DFS_ITER(graph:list, root:int, reversed:bool, state:list, values:list = None):
    global time
    global count
    stack = [root]
    while stack:
        v = stack.pop()
        if state[v] != "B":
            stack.append(v)
            if state[v] == "W":
                state[v] = "G"
            all_adj_dist = True

            for node in graph[v]:
                if state[node] == "W":
                    stack.append(node)
                    all_adj_dist = False

            if all_adj_dist:
                state[v] = "B"
                if reversed:
                    values[v] = time
                    time += 1
                else:
                    count += 1
                stack.pop()




if __name__ == '__main__':
    ToCommandLine()