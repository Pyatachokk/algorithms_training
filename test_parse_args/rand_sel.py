import random
import argparse
import sys

def ToCommandLine():

    parser = argparse.ArgumentParser(description= 'Quicksort algorythm with first entry as pivot.')
    parser.add_argument('--infile', metavar = 'Input', nargs = 1, type = str, default = sys.stdin, help = 'Input txt file. If not specified, stdin.')
    parser.add_argument('--outfile', metavar = 'Output', nargs = 1, type = str, default=sys.stdout, help = 'Output txt file. If not specified, stdout.')
    parser.add_argument('target', metavar = 'Target', nargs = 1, type = int, help = 'Target ordinal statistics')
    args = parser.parse_args()

    sorting_fun(args.infile, args.outfile, args.target)

def sorting_fun(infile, outfile, target):
    try:
        text_file = open(infile[0], "r")
        lines = list(map(int, text_file.read().split('\n')[:-1]))
    except:
        lines = list(map(int, input().split()))

    found = rand_sel(lines, target[0], 0, len(lines) - 1)

    try:
        writing_file = open(outfile[0], "w")
        writing_file.write('found\n')
    except:
        print(str(target[0]) + '`th order statistic: ' + str(found))


def rand_sel(a, target, low, high):
    if low == high:
        return a[low]

    pivot = random.randint(low, high)
    buffer = None
    buffer = a[pivot]
    a[pivot] = a[low]
    a[low] = buffer
    pivot = low

    marker = False
    i = low + 1
    j = low + 1

    while j <= high:
        if a[j] < a[pivot]:
            buffer = a[i]
            a[i] = a[j]
            a[j] = buffer
            i += 1
            j += 1
            marker = True
        else:
            j += 1

    if marker:
        # print(pivot)
        # print(i)
        # print(low, high)
        # print(a)
        buffer = a[pivot]
        a[pivot] = a[i-1]
        a[i-1] = buffer

        if i-1 == target:
            return a[i-1]
        elif i - 1  < target:
            return rand_sel(a, target, i, high)
        else:
            return rand_sel(a, target, low, i-2)
    else:
        if pivot == target:
            return a[pivot]
        else:
            return rand_sel(a, target, i, high)

if __name__ == '__main__':
    ToCommandLine()