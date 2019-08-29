import random
import csv
import argparse
import sys
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='Min_cut.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
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

    logger_2 = logging.getLogger('Main part')

    count_wtf = 0
    try:
        logger_2.info('Trying read graph from file')
        text_file = open(infile[0], "r")
        lines = list(text_file.read().split('\n')[:-1])
        lines = [[item for item in line.split()] for line in lines]
        logger_2.info('Reading successful')
    except:
        logger_2.error('Attempt failed. Termination.')
        return 1

    # print(lines[0])
    logger_2.info('Graph initialization')
    graph = graph_list()

    minimum = 10000
    logger_2.info('Starting main loop')
    for i in range(10000):
        print(i)

        for line in lines:
            graph.add_node(line)
        graph.shuffle(seed=i)
        graph.merge(seed=i)
        if len(graph.edges[0]) == len(graph.edges[1]):
            if len(graph.edges[0]) < minimum:
                minimum = len(graph.edges[0])
        else:
            logger_2.critical('Code is incorrect. Impossible output.')
        graph.clear()
    logger_2.info('Main loop finished')


    print("\n" + "Minimum: " + str(minimum))

class graph_list(object):
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.num_nodes = 0
        self.log = logging.getLogger('Graph')

    def add_node(self, node):
        try:
            # print(node)
            self.nodes.append({node[0]})
            self.edges.append(node[1:])
            self.num_nodes += 1
        except ValueError:
            self.log.error('Invalid node type')
            raise(ValueError('Invalid node type'))
        except IndexError:
            self.log.error('Empty node or invalid index')
            raise IndexError('Empty node or invalid index')

    def shuffle(self, seed = 1):
        try:
            random.seed(seed)
            random.shuffle(self.nodes)
            random.seed(seed)
            random.shuffle(self.edges)
        except ValueError:
            self.log.error('Impossible shuffle')

    def merge(self, seed=None):
        if seed:
            random.seed(seed)
        while len(self.nodes) > 2:
            self.log.debug('{}'.format(self.nodes))
            self.log.debug('{}'.format(self.edges))
            first_index = random.randint(0, len(self.nodes) - 1)
            buffer = (self.nodes[first_index], self.edges[first_index])
            self.nodes[first_index], self.edges[first_index] = self.nodes[-1], self.edges[-1]
            # self.log.debug('{}'.format(self.nodes))
            # self.log.debug('{}'.format(self.edges))
            self.edges.pop()
            self.nodes.pop()
            first_nodes = buffer[0]
            first_edges = buffer[1]
            second = random.choice(first_edges)
            for i in range(len(self.nodes)):
                # self.log.info('{}'.format(self.nodes))
                if second in self.nodes[i]:
                    # self.log.debug('{}'.format(i))
                    buffer_2 = (self.nodes[i], self.edges[i])
                    self.nodes[i], self.edges[i] = self.nodes[-1], self.edges[-1]
                    self.nodes.pop()
                    self.edges.pop()
                    self.nodes.append(first_nodes.union(buffer_2[0]))
                    self.edges.append([item for item in first_edges + buffer_2[1] if (item not in first_nodes and item not in buffer_2[0])])
                    break
        self.log.debug('{}'.format(self.nodes))
        self.log.debug('{}'.format(self.edges))
        self.log.debug('Merging finished')
    def clear(self):
        self.nodes = []
        self.edges = []
        self.num_nodes = 0

if __name__ == '__main__':
    ToCommandLine()


# import random
# import csv
#
# text_file = open('graph.txt', 'r')
# lines = list(csv.reader(text_file, delimiter='\t'))
# print(lines)
#
# class graph_list(object):
#     def __init__(self):
#         self.nodes = []
#         self.edges = []
#         self.num_nodes = 0
#
#     def add_node(self, node):
#         try:
#
#             node = list(map(int, node[:-1]))
#             self.nodes.append({node[0]})
#             self.edges.append(node[1:])
#             self.num_nodes += 1
#         except ValueError:
#             raise ValueError("Invalid node type")
#
#     def shuffle(self, seed = 1):
#         try:
#             random.seed(seed)
#             random.shuffle(self.nodes)
#             random.seed(seed)
#             random.shuffle(self.edges)
#         except ValueError:
#             raise ValueError("No nodes to shuffle")
#
#     def merge(self, seed=None):
#         if seed:
#             random.seed(seed)
#         while len(self.nodes) > 2:
#             first_index = random.randint(0, len(self.nodes) - 1)
#             buffer = (self.nodes[first_index], self.edges[first_index])
#             self.nodes[first_index], self.edges[first_index] = self.nodes[-1], self.edges[-1]
#             self.edges.pop()
#             self.nodes.pop()
#             first_nodes = buffer[0]
#             first_edges = buffer[1]
#             second = random.choice(first_edges)
#             for i in range(len(self.nodes)):
#                 if second in self.nodes[i]:
#                     buffer_2 = (self.nodes[i], self.edges[i])
#                     self.nodes[i], self.edges[i] = self.nodes[-1], self.edges[-1]
#                     self.nodes.pop()
#                     self.edges.pop()
#                     self.nodes.append(first_nodes.union(buffer_2[0]))
#                     self.edges.append([item for item in first_edges + buffer_2[1] if (item not in first_nodes and item not in buffer_2[0])])
#
#     def clear(self):
#         self.nodes = []
#         self.edges = []
#         self.num_nodes = 0
#
# graph = graph_list()
#
# minimum = 10000
# for i in range(1):
#     print(i)
#     for line in lines:
#         graph.add_node(line)
#     graph.shuffle(seed = i)
#     graph.merge(seed=i)
#     if len(graph.edges[0]) + len(graph.edges[1]) < minimum:
#         minimum = len(graph.edges[0]) + len(graph.edges[1])
#     graph.clear()
#     print(minimum)
# print(minimum)
#
# #136
# #98
# #77
#
# a = dict()
# inspect(a)